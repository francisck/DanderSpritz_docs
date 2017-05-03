# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: profile.py
"""Class for profiling Python code."""
import sys
import os
import time
import marshal
from optparse import OptionParser
__all__ = [
 'run', 'runctx', 'help', 'Profile']

def run(statement, filename=None, sort=-1):
    """Run statement under profiler optionally saving results in filename
    
    This function takes a single argument that can be passed to the
    "exec" statement, and an optional file name.  In all cases this
    routine attempts to "exec" its first argument and gather profiling
    statistics from the execution. If no file name is present, then this
    function automatically prints a simple profiling report, sorted by the
    standard name string (file/line/function-name) that is presented in
    each line.
    """
    prof = Profile()
    try:
        prof = prof.run(statement)
    except SystemExit:
        pass

    if filename is not None:
        prof.dump_stats(filename)
    else:
        return prof.print_stats(sort)
    return


def runctx(statement, globals, locals, filename=None, sort=-1):
    """Run statement under profiler, supplying your own globals and locals,
    optionally saving results in filename.
    
    statement and filename have the same semantics as profile.run
    """
    prof = Profile()
    try:
        prof = prof.runctx(statement, globals, locals)
    except SystemExit:
        pass

    if filename is not None:
        prof.dump_stats(filename)
    else:
        return prof.print_stats(sort)
    return


def help():
    print 'Documentation for the profile module can be found '
    print "in the Python Library Reference, section 'The Python Profiler'."


if hasattr(os, 'times'):

    def _get_time_times(timer=os.times):
        t = timer()
        return t[0] + t[1]


_has_res = 0
try:
    import resource
    resgetrusage = lambda : resource.getrusage(resource.RUSAGE_SELF)

    def _get_time_resource(timer=resgetrusage):
        t = timer()
        return t[0] + t[1]


    _has_res = 1
except ImportError:
    pass

class Profile():
    """Profiler class.
    
    self.cur is always a tuple.  Each such tuple corresponds to a stack
    frame that is currently active (self.cur[-2]).  The following are the
    definitions of its members.  We use this external "parallel stack" to
    avoid contaminating the program that we are profiling. (old profiler
    used to write into the frames local dictionary!!) Derived classes
    can change the definition of some entries, as long as they leave
    [-2:] intact (frame and previous tuple).  In case an internal error is
    detected, the -3 element is used as the function name.
    
    [ 0] = Time that needs to be charged to the parent frame's function.
           It is used so that a function call will not have to access the
           timing data for the parent frame.
    [ 1] = Total time spent in this frame's function, excluding time in
           subfunctions (this latter is tallied in cur[2]).
    [ 2] = Total time spent in subfunctions, excluding time executing the
           frame's function (this latter is tallied in cur[1]).
    [-3] = Name of the function that corresponds to this frame.
    [-2] = Actual frame that we correspond to (used to sync exception handling).
    [-1] = Our parent 6-tuple (corresponds to frame.f_back).
    
    Timing data for each function is stored as a 5-tuple in the dictionary
    self.timings[].  The index is always the name stored in self.cur[-3].
    The following are the definitions of the members:
    
    [0] = The number of times this function was called, not counting direct
          or indirect recursion,
    [1] = Number of times this function appears on the stack, minus one
    [2] = Total time spent internal to this function
    [3] = Cumulative time that this function was present on the stack.  In
          non-recursive functions, this is the total execution time from start
          to finish of each invocation of a function, including time spent in
          all subfunctions.
    [4] = A dictionary indicating for each function name, the number of times
          it was called by us.
    """
    bias = 0

    def __init__(self, timer=None, bias=None):
        self.timings = {}
        self.cur = None
        self.cmd = ''
        self.c_func_name = ''
        if bias is None:
            bias = self.bias
        self.bias = bias
        if not timer:
            if _has_res:
                self.timer = resgetrusage
                self.dispatcher = self.trace_dispatch
                self.get_time = _get_time_resource
            elif hasattr(time, 'clock'):
                self.timer = self.get_time = time.clock
                self.dispatcher = self.trace_dispatch_i
            elif hasattr(os, 'times'):
                self.timer = os.times
                self.dispatcher = self.trace_dispatch
                self.get_time = _get_time_times
            else:
                self.timer = self.get_time = time.time
                self.dispatcher = self.trace_dispatch_i
        else:
            self.timer = timer
            t = self.timer()
            try:
                length = len(t)
            except TypeError:
                self.get_time = timer
                self.dispatcher = self.trace_dispatch_i
            else:
                if length == 2:
                    self.dispatcher = self.trace_dispatch
                else:
                    self.dispatcher = self.trace_dispatch_l

                def get_time_timer(timer=timer, sum=sum):
                    return sum(timer())

                self.get_time = get_time_timer

        self.t = self.get_time()
        self.simulate_call('profiler')
        return

    def trace_dispatch(self, frame, event, arg):
        timer = self.timer
        t = timer()
        t = t[0] + t[1] - self.t - self.bias
        if event == 'c_call':
            self.c_func_name = arg.__name__
        if self.dispatch[event](self, frame, t):
            t = timer()
            self.t = t[0] + t[1]
        else:
            r = timer()
            self.t = r[0] + r[1] - t

    def trace_dispatch_i(self, frame, event, arg):
        timer = self.timer
        t = timer() - self.t - self.bias
        if event == 'c_call':
            self.c_func_name = arg.__name__
        if self.dispatch[event](self, frame, t):
            self.t = timer()
        else:
            self.t = timer() - t

    def trace_dispatch_mac(self, frame, event, arg):
        timer = self.timer
        t = timer() / 60.0 - self.t - self.bias
        if event == 'c_call':
            self.c_func_name = arg.__name__
        if self.dispatch[event](self, frame, t):
            self.t = timer() / 60.0
        else:
            self.t = timer() / 60.0 - t

    def trace_dispatch_l(self, frame, event, arg):
        get_time = self.get_time
        t = get_time() - self.t - self.bias
        if event == 'c_call':
            self.c_func_name = arg.__name__
        if self.dispatch[event](self, frame, t):
            self.t = get_time()
        else:
            self.t = get_time() - t

    def trace_dispatch_exception(self, frame, t):
        rpt, rit, ret, rfn, rframe, rcur = self.cur
        if rframe is not frame and rcur:
            return self.trace_dispatch_return(rframe, t)
        self.cur = (
         rpt, rit + t, ret, rfn, rframe, rcur)
        return 1

    def trace_dispatch_call(self, frame, t):
        if self.cur and frame.f_back is not self.cur[-2]:
            rpt, rit, ret, rfn, rframe, rcur = self.cur
            if not isinstance(rframe, Profile.fake_frame):
                self.trace_dispatch_return(rframe, 0)
        fcode = frame.f_code
        fn = (fcode.co_filename, fcode.co_firstlineno, fcode.co_name)
        self.cur = (t, 0, 0, fn, frame, self.cur)
        timings = self.timings
        if fn in timings:
            cc, ns, tt, ct, callers = timings[fn]
            timings[fn] = (cc, ns + 1, tt, ct, callers)
        else:
            timings[fn] = (
             0, 0, 0, 0, {})
        return 1

    def trace_dispatch_c_call(self, frame, t):
        fn = (
         '', 0, self.c_func_name)
        self.cur = (t, 0, 0, fn, frame, self.cur)
        timings = self.timings
        if fn in timings:
            cc, ns, tt, ct, callers = timings[fn]
            timings[fn] = (cc, ns + 1, tt, ct, callers)
        else:
            timings[fn] = (
             0, 0, 0, 0, {})
        return 1

    def trace_dispatch_return(self, frame, t):
        if frame is not self.cur[-2]:
            self.trace_dispatch_return(self.cur[-2], 0)
        rpt, rit, ret, rfn, frame, rcur = self.cur
        rit = rit + t
        frame_total = rit + ret
        ppt, pit, pet, pfn, pframe, pcur = rcur
        self.cur = (ppt, pit + rpt, pet + frame_total, pfn, pframe, pcur)
        timings = self.timings
        cc, ns, tt, ct, callers = timings[rfn]
        if not ns:
            ct = ct + frame_total
            cc = cc + 1
        if pfn in callers:
            callers[pfn] = callers[pfn] + 1
        else:
            callers[pfn] = 1
        timings[rfn] = (cc, ns - 1, tt + rit, ct, callers)
        return 1

    dispatch = {'call': trace_dispatch_call,
       'exception': trace_dispatch_exception,
       'return': trace_dispatch_return,
       'c_call': trace_dispatch_c_call,
       'c_exception': trace_dispatch_return,
       'c_return': trace_dispatch_return
       }

    def set_cmd(self, cmd):
        if self.cur[-1]:
            return
        self.cmd = cmd
        self.simulate_call(cmd)

    class fake_code:

        def __init__(self, filename, line, name):
            self.co_filename = filename
            self.co_line = line
            self.co_name = name
            self.co_firstlineno = 0

        def __repr__(self):
            return repr((self.co_filename, self.co_line, self.co_name))

    class fake_frame:

        def __init__(self, code, prior):
            self.f_code = code
            self.f_back = prior

    def simulate_call(self, name):
        code = self.fake_code('profile', 0, name)
        if self.cur:
            pframe = self.cur[-2]
        else:
            pframe = None
        frame = self.fake_frame(code, pframe)
        self.dispatch['call'](self, frame, 0)
        return

    def simulate_cmd_complete(self):
        get_time = self.get_time
        t = get_time() - self.t
        while self.cur[-1]:
            self.dispatch['return'](self, self.cur[-2], t)
            t = 0

        self.t = get_time() - t

    def print_stats(self, sort=-1):
        import pstats
        pstats.Stats(self).strip_dirs().sort_stats(sort).print_stats()

    def dump_stats(self, file):
        f = open(file, 'wb')
        self.create_stats()
        marshal.dump(self.stats, f)
        f.close()

    def create_stats(self):
        self.simulate_cmd_complete()
        self.snapshot_stats()

    def snapshot_stats(self):
        self.stats = {}
        for func, (cc, ns, tt, ct, callers) in self.timings.iteritems():
            callers = callers.copy()
            nc = 0
            for callcnt in callers.itervalues():
                nc += callcnt

            self.stats[func] = (
             cc, nc, tt, ct, callers)

    def run(self, cmd):
        import __main__
        dict = __main__.__dict__
        return self.runctx(cmd, dict, dict)

    def runctx(self, cmd, globals, locals):
        self.set_cmd(cmd)
        sys.setprofile(self.dispatcher)
        try:
            exec cmd in globals, locals
        finally:
            sys.setprofile(None)

        return self

    def runcall(self, func, *args, **kw):
        self.set_cmd(repr(func))
        sys.setprofile(self.dispatcher)
        try:
            return func(*args, **kw)
        finally:
            sys.setprofile(None)

        return

    def calibrate(self, m, verbose=0):
        if self.__class__ is not Profile:
            raise TypeError('Subclasses must override .calibrate().')
        saved_bias = self.bias
        self.bias = 0
        try:
            return self._calibrate_inner(m, verbose)
        finally:
            self.bias = saved_bias

    def _calibrate_inner(self, m, verbose):
        get_time = self.get_time

        def f1(n):
            for i in range(n):
                x = 1

        def f(m, f1=f1):
            for i in range(m):
                f1(100)

        f(m)
        t0 = get_time()
        f(m)
        t1 = get_time()
        elapsed_noprofile = t1 - t0
        if verbose:
            print 'elapsed time without profiling =', elapsed_noprofile
        p = Profile()
        t0 = get_time()
        p.runctx('f(m)', globals(), locals())
        t1 = get_time()
        elapsed_profile = t1 - t0
        if verbose:
            print 'elapsed time with profiling =', elapsed_profile
        total_calls = 0.0
        reported_time = 0.0
        for (filename, line, funcname), (cc, ns, tt, ct, callers) in p.timings.items():
            if funcname in ('f', 'f1'):
                total_calls += cc
                reported_time += tt

        if verbose:
            print "'CPU seconds' profiler reported =", reported_time
            print 'total # calls =', total_calls
        if total_calls != m + 1:
            raise ValueError('internal error: total calls = %d' % total_calls)
        mean = (reported_time - elapsed_noprofile) / 2.0 / total_calls
        if verbose:
            print 'mean stopwatch overhead per profile event =', mean
        return mean


def Stats(*args):
    print 'Report generating functions are in the "pstats" module\x07'


def main():
    usage = 'profile.py [-o output_file_path] [-s sort] scriptfile [arg] ...'
    parser = OptionParser(usage=usage)
    parser.allow_interspersed_args = False
    parser.add_option('-o', '--outfile', dest='outfile', help='Save stats to <outfile>', default=None)
    parser.add_option('-s', '--sort', dest='sort', help='Sort order when printing to stdout, based on pstats.Stats class', default=-1)
    if not sys.argv[1:]:
        parser.print_usage()
        sys.exit(2)
    options, args = parser.parse_args()
    sys.argv[:] = args
    if len(args) > 0:
        progname = args[0]
        sys.path.insert(0, os.path.dirname(progname))
        with open(progname, 'rb') as fp:
            code = compile(fp.read(), progname, 'exec')
        globs = {'__file__': progname,'__name__': '__main__',
           '__package__': None
           }
        runctx(code, globs, None, options.outfile, options.sort)
    else:
        parser.print_usage()
    return parser


if __name__ == '__main__':
    main()