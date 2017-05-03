# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: trace.py
"""program/module to trace Python program or function execution

Sample use, command line:
  trace.py -c -f counts --ignore-dir '$prefix' spam.py eggs
  trace.py -t --ignore-dir '$prefix' spam.py eggs
  trace.py --trackcalls spam.py eggs

Sample use, programmatically
  import sys

  # create a Trace object, telling it what to ignore, and whether to
  # do tracing or line-counting or both.
  tracer = trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix,], trace=0,
                    count=1)
  # run the new command using the given tracer
  tracer.run('main()')
  # make a report, placing output in /tmp
  r = tracer.results()
  r.write_results(show_missing=True, coverdir="/tmp")
"""
import linecache
import os
import re
import sys
import time
import token
import tokenize
import inspect
import gc
import dis
try:
    import cPickle
    pickle = cPickle
except ImportError:
    import pickle

try:
    import threading
except ImportError:
    _settrace = sys.settrace

    def _unsettrace():
        sys.settrace(None)
        return


else:

    def _settrace(func):
        threading.settrace(func)
        sys.settrace(func)


    def _unsettrace():
        sys.settrace(None)
        threading.settrace(None)
        return


def usage(outfile):
    outfile.write("Usage: %s [OPTIONS] <file> [ARGS]\n\nMeta-options:\n--help                Display this help then exit.\n--version             Output version information then exit.\n\nOtherwise, exactly one of the following three options must be given:\n-t, --trace           Print each line to sys.stdout before it is executed.\n-c, --count           Count the number of times each line is executed\n                      and write the counts to <module>.cover for each\n                      module executed, in the module's directory.\n                      See also `--coverdir', `--file', `--no-report' below.\n-l, --listfuncs       Keep track of which functions are executed at least\n                      once and write the results to sys.stdout after the\n                      program exits.\n-T, --trackcalls      Keep track of caller/called pairs and write the\n                      results to sys.stdout after the program exits.\n-r, --report          Generate a report from a counts file; do not execute\n                      any code.  `--file' must specify the results file to\n                      read, which must have been created in a previous run\n                      with `--count --file=FILE'.\n\nModifiers:\n-f, --file=<file>     File to accumulate counts over several runs.\n-R, --no-report       Do not generate the coverage report files.\n                      Useful if you want to accumulate over several runs.\n-C, --coverdir=<dir>  Directory where the report files.  The coverage\n                      report for <package>.<module> is written to file\n                      <dir>/<package>/<module>.cover.\n-m, --missing         Annotate executable lines that were not executed\n                      with '>>>>>> '.\n-s, --summary         Write a brief summary on stdout for each file.\n                      (Can only be used with --count or --report.)\n-g, --timing          Prefix each line with the time since the program started.\n                      Only used while tracing.\n\nFilters, may be repeated multiple times:\n--ignore-module=<mod> Ignore the given module(s) and its submodules\n                      (if it is a package).  Accepts comma separated\n                      list of module names\n--ignore-dir=<dir>    Ignore files in the given directory (multiple\n                      directories can be joined by os.pathsep).\n" % sys.argv[0])


PRAGMA_NOCOVER = '#pragma NO COVER'
rx_blank = re.compile('^\\s*(#.*)?$')

class Ignore:

    def __init__(self, modules=None, dirs=None):
        self._mods = modules or []
        self._dirs = dirs or []
        self._dirs = map(os.path.normpath, self._dirs)
        self._ignore = {'<string>': 1}

    def names(self, filename, modulename):
        if modulename in self._ignore:
            return self._ignore[modulename]
        else:
            for mod in self._mods:
                if mod == modulename:
                    self._ignore[modulename] = 1
                    return 1
                n = len(mod)
                if mod == modulename[:n] and modulename[n] == '.':
                    self._ignore[modulename] = 1
                    return 1

            if filename is None:
                self._ignore[modulename] = 1
                return 1
            for d in self._dirs:
                if filename.startswith(d + os.sep):
                    self._ignore[modulename] = 1
                    return 1

            self._ignore[modulename] = 0
            return 0


def modname(path):
    """Return a plausible module name for the patch."""
    base = os.path.basename(path)
    filename, ext = os.path.splitext(base)
    return filename


def fullmodname(path):
    """Return a plausible module name for the path."""
    comparepath = os.path.normcase(path)
    longest = ''
    for dir in sys.path:
        dir = os.path.normcase(dir)
        if comparepath.startswith(dir) and comparepath[len(dir)] == os.sep:
            if len(dir) > len(longest):
                longest = dir

    if longest:
        base = path[len(longest) + 1:]
    else:
        base = path
    drive, base = os.path.splitdrive(base)
    base = base.replace(os.sep, '.')
    if os.altsep:
        base = base.replace(os.altsep, '.')
    filename, ext = os.path.splitext(base)
    return filename.lstrip('.')


class CoverageResults:

    def __init__(self, counts=None, calledfuncs=None, infile=None, callers=None, outfile=None):
        self.counts = counts
        if self.counts is None:
            self.counts = {}
        self.counter = self.counts.copy()
        self.calledfuncs = calledfuncs
        if self.calledfuncs is None:
            self.calledfuncs = {}
        self.calledfuncs = self.calledfuncs.copy()
        self.callers = callers
        if self.callers is None:
            self.callers = {}
        self.callers = self.callers.copy()
        self.infile = infile
        self.outfile = outfile
        if self.infile:
            try:
                counts, calledfuncs, callers = pickle.load(open(self.infile, 'rb'))
                self.update(self.__class__(counts, calledfuncs, callers))
            except (IOError, EOFError, ValueError) as err:
                print >> sys.stderr, 'Skipping counts file %r: %s' % (
                 self.infile, err)

        return

    def update(self, other):
        """Merge in the data from another CoverageResults"""
        counts = self.counts
        calledfuncs = self.calledfuncs
        callers = self.callers
        other_counts = other.counts
        other_calledfuncs = other.calledfuncs
        other_callers = other.callers
        for key in other_counts.keys():
            counts[key] = counts.get(key, 0) + other_counts[key]

        for key in other_calledfuncs.keys():
            calledfuncs[key] = 1

        for key in other_callers.keys():
            callers[key] = 1

    def write_results(self, show_missing=True, summary=False, coverdir=None):
        """
        @param coverdir
        """
        if self.calledfuncs:
            print
            print 'functions called:'
            calls = self.calledfuncs.keys()
            calls.sort()
            for filename, modulename, funcname in calls:
                print 'filename: %s, modulename: %s, funcname: %s' % (
                 filename, modulename, funcname)

        if self.callers:
            print
            print 'calling relationships:'
            calls = self.callers.keys()
            calls.sort()
            lastfile = lastcfile = ''
            for (pfile, pmod, pfunc), (cfile, cmod, cfunc) in calls:
                if pfile != lastfile:
                    print
                    print '***', pfile, '***'
                    lastfile = pfile
                    lastcfile = ''
                if cfile != pfile and lastcfile != cfile:
                    print '  -->', cfile
                    lastcfile = cfile
                print '    %s.%s -> %s.%s' % (pmod, pfunc, cmod, cfunc)

        per_file = {}
        for filename, lineno in self.counts.keys():
            lines_hit = per_file[filename] = per_file.get(filename, {})
            lines_hit[lineno] = self.counts[filename, lineno]

        sums = {}
        for filename, count in per_file.iteritems():
            if filename == '<string>':
                continue
            if filename.startswith('<doctest '):
                continue
            if filename.endswith(('.pyc', '.pyo')):
                filename = filename[:-1]
            if coverdir is None:
                dir = os.path.dirname(os.path.abspath(filename))
                modulename = modname(filename)
            else:
                dir = coverdir
                if not os.path.exists(dir):
                    os.makedirs(dir)
                modulename = fullmodname(filename)
            if show_missing:
                lnotab = find_executable_linenos(filename)
            else:
                lnotab = {}
            source = linecache.getlines(filename)
            coverpath = os.path.join(dir, modulename + '.cover')
            n_hits, n_lines = self.write_results_file(coverpath, source, lnotab, count)
            if summary and n_lines:
                percent = 100 * n_hits // n_lines
                sums[modulename] = (n_lines, percent, modulename, filename)

        if summary and sums:
            mods = sums.keys()
            mods.sort()
            print 'lines   cov%   module   (path)'
            for m in mods:
                n_lines, percent, modulename, filename = sums[m]
                print '%5d   %3d%%   %s   (%s)' % sums[m]

        if self.outfile:
            try:
                pickle.dump((self.counts, self.calledfuncs, self.callers), open(self.outfile, 'wb'), 1)
            except IOError as err:
                print >> sys.stderr, "Can't save counts files because %s" % err

        return

    def write_results_file(self, path, lines, lnotab, lines_hit):
        """Return a coverage results file in path."""
        try:
            outfile = open(path, 'w')
        except IOError as err:
            print >> sys.stderr, 'trace: Could not open %r for writing: %s- skipping' % (
             path, err)
            return (0, 0)

        n_lines = 0
        n_hits = 0
        for i, line in enumerate(lines):
            lineno = i + 1
            if lineno in lines_hit:
                outfile.write('%5d: ' % lines_hit[lineno])
                n_hits += 1
                n_lines += 1
            elif rx_blank.match(line):
                outfile.write('       ')
            elif lineno in lnotab and PRAGMA_NOCOVER not in lines[i]:
                outfile.write('>>>>>> ')
                n_lines += 1
            else:
                outfile.write('       ')
            outfile.write(lines[i].expandtabs(8))

        outfile.close()
        return (
         n_hits, n_lines)


def find_lines_from_code(code, strs):
    """Return dict where keys are lines in the line number table."""
    linenos = {}
    for _, lineno in dis.findlinestarts(code):
        if lineno not in strs:
            linenos[lineno] = 1

    return linenos


def find_lines(code, strs):
    """Return lineno dict for all code objects reachable from code."""
    linenos = find_lines_from_code(code, strs)
    for c in code.co_consts:
        if inspect.iscode(c):
            linenos.update(find_lines(c, strs))

    return linenos


def find_strings(filename):
    """Return a dict of possible docstring positions.
    
    The dict maps line numbers to strings.  There is an entry for
    line that contains only a string or a part of a triple-quoted
    string.
    """
    d = {}
    prev_ttype = token.INDENT
    f = open(filename)
    for ttype, tstr, start, end, line in tokenize.generate_tokens(f.readline):
        if ttype == token.STRING:
            if prev_ttype == token.INDENT:
                sline, scol = start
                eline, ecol = end
                for i in range(sline, eline + 1):
                    d[i] = 1

        prev_ttype = ttype

    f.close()
    return d


def find_executable_linenos(filename):
    """Return dict where keys are line numbers in the line number table."""
    try:
        prog = open(filename, 'rU').read()
    except IOError as err:
        print >> sys.stderr, 'Not printing coverage data for %r: %s' % (
         filename, err)
        return {}

    code = compile(prog, filename, 'exec')
    strs = find_strings(filename)
    return find_lines(code, strs)


class Trace:

    def __init__(self, count=1, trace=1, countfuncs=0, countcallers=0, ignoremods=(), ignoredirs=(), infile=None, outfile=None, timing=False):
        """
        @param count true iff it should count number of times each
                     line is executed
        @param trace true iff it should print out each line that is
                     being counted
        @param countfuncs true iff it should just output a list of
                     (filename, modulename, funcname,) for functions
                     that were called at least once;  This overrides
                     `count' and `trace'
        @param ignoremods a list of the names of modules to ignore
        @param ignoredirs a list of the names of directories to ignore
                     all of the (recursive) contents of
        @param infile file from which to read stored counts to be
                     added into the results
        @param outfile file in which to write the results
        @param timing true iff timing information be displayed
        """
        self.infile = infile
        self.outfile = outfile
        self.ignore = Ignore(ignoremods, ignoredirs)
        self.counts = {}
        self.blabbed = {}
        self.pathtobasename = {}
        self.donothing = 0
        self.trace = trace
        self._calledfuncs = {}
        self._callers = {}
        self._caller_cache = {}
        self.start_time = None
        if timing:
            self.start_time = time.time()
        if countcallers:
            self.globaltrace = self.globaltrace_trackcallers
        elif countfuncs:
            self.globaltrace = self.globaltrace_countfuncs
        elif trace and count:
            self.globaltrace = self.globaltrace_lt
            self.localtrace = self.localtrace_trace_and_count
        elif trace:
            self.globaltrace = self.globaltrace_lt
            self.localtrace = self.localtrace_trace
        elif count:
            self.globaltrace = self.globaltrace_lt
            self.localtrace = self.localtrace_count
        else:
            self.donothing = 1
        return

    def run(self, cmd):
        import __main__
        dict = __main__.__dict__
        if not self.donothing:
            threading.settrace(self.globaltrace)
            sys.settrace(self.globaltrace)
        try:
            exec cmd in dict, dict
        finally:
            if not self.donothing:
                sys.settrace(None)
                threading.settrace(None)

        return

    def runctx(self, cmd, globals=None, locals=None):
        if globals is None:
            globals = {}
        if locals is None:
            locals = {}
        if not self.donothing:
            _settrace(self.globaltrace)
        try:
            exec cmd in globals, locals
        finally:
            if not self.donothing:
                _unsettrace()

        return

    def runfunc(self, func, *args, **kw):
        result = None
        if not self.donothing:
            sys.settrace(self.globaltrace)
        try:
            result = func(*args, **kw)
        finally:
            if not self.donothing:
                sys.settrace(None)

        return result

    def file_module_function_of(self, frame):
        code = frame.f_code
        filename = code.co_filename
        if filename:
            modulename = modname(filename)
        else:
            modulename = None
        funcname = code.co_name
        clsname = None
        if code in self._caller_cache:
            if self._caller_cache[code] is not None:
                clsname = self._caller_cache[code]
        else:
            self._caller_cache[code] = None
            funcs = [ f for f in gc.get_referrers(code) if inspect.isfunction(f)
                    ]
            if len(funcs) == 1:
                dicts = [ d for d in gc.get_referrers(funcs[0]) if isinstance(d, dict) ]
                if len(dicts) == 1:
                    classes = [ c for c in gc.get_referrers(dicts[0]) if hasattr(c, '__bases__') ]
                    if len(classes) == 1:
                        clsname = classes[0].__name__
                        self._caller_cache[code] = clsname
        if clsname is not None:
            funcname = '%s.%s' % (clsname, funcname)
        return (
         filename, modulename, funcname)

    def globaltrace_trackcallers(self, frame, why, arg):
        """Handler for call events.
        
        Adds information about who called who to the self._callers dict.
        """
        if why == 'call':
            this_func = self.file_module_function_of(frame)
            parent_func = self.file_module_function_of(frame.f_back)
            self._callers[parent_func, this_func] = 1

    def globaltrace_countfuncs(self, frame, why, arg):
        """Handler for call events.
        
        Adds (filename, modulename, funcname) to the self._calledfuncs dict.
        """
        if why == 'call':
            this_func = self.file_module_function_of(frame)
            self._calledfuncs[this_func] = 1

    def globaltrace_lt(self, frame, why, arg):
        """Handler for call events.
        
        If the code block being entered is to be ignored, returns `None',
        else returns self.localtrace.
        """
        if why == 'call':
            code = frame.f_code
            filename = frame.f_globals.get('__file__', None)
            if filename:
                modulename = modname(filename)
                if modulename is not None:
                    ignore_it = self.ignore.names(filename, modulename)
                    if not ignore_it:
                        if self.trace:
                            print ' --- modulename: %s, funcname: %s' % (
                             modulename, code.co_name)
                        return self.localtrace
            else:
                return
        return

    def localtrace_trace_and_count(self, frame, why, arg):
        if why == 'line':
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            key = (filename, lineno)
            self.counts[key] = self.counts.get(key, 0) + 1
            if self.start_time:
                print '%.2f' % (time.time() - self.start_time),
            bname = os.path.basename(filename)
            print '%s(%d): %s' % (bname, lineno,
             linecache.getline(filename, lineno)),
        return self.localtrace

    def localtrace_trace(self, frame, why, arg):
        if why == 'line':
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            if self.start_time:
                print '%.2f' % (time.time() - self.start_time),
            bname = os.path.basename(filename)
            print '%s(%d): %s' % (bname, lineno,
             linecache.getline(filename, lineno)),
        return self.localtrace

    def localtrace_count(self, frame, why, arg):
        if why == 'line':
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            key = (filename, lineno)
            self.counts[key] = self.counts.get(key, 0) + 1
        return self.localtrace

    def results(self):
        return CoverageResults(self.counts, infile=self.infile, outfile=self.outfile, calledfuncs=self._calledfuncs, callers=self._callers)


def _err_exit(msg):
    sys.stderr.write('%s: %s\n' % (sys.argv[0], msg))
    sys.exit(1)


def main(argv=None):
    import getopt
    if argv is None:
        argv = sys.argv
    try:
        opts, prog_argv = getopt.getopt(argv[1:], 'tcrRf:d:msC:lTg', [
         'help', 'version', 'trace', 'count',
         'report', 'no-report', 'summary',
         'file=', 'missing',
         'ignore-module=', 'ignore-dir=',
         'coverdir=', 'listfuncs',
         'trackcalls', 'timing'])
    except getopt.error as msg:
        sys.stderr.write('%s: %s\n' % (sys.argv[0], msg))
        sys.stderr.write("Try `%s --help' for more information\n" % sys.argv[0])
        sys.exit(1)

    trace = 0
    count = 0
    report = 0
    no_report = 0
    counts_file = None
    missing = 0
    ignore_modules = []
    ignore_dirs = []
    coverdir = None
    summary = 0
    listfuncs = False
    countcallers = False
    timing = False
    for opt, val in opts:
        if opt == '--help':
            usage(sys.stdout)
            sys.exit(0)
        if opt == '--version':
            sys.stdout.write('trace 2.0\n')
            sys.exit(0)
        if opt == '-T' or opt == '--trackcalls':
            countcallers = True
            continue
        if opt == '-l' or opt == '--listfuncs':
            listfuncs = True
            continue
        if opt == '-g' or opt == '--timing':
            timing = True
            continue
        if opt == '-t' or opt == '--trace':
            trace = 1
            continue
        if opt == '-c' or opt == '--count':
            count = 1
            continue
        if opt == '-r' or opt == '--report':
            report = 1
            continue
        if opt == '-R' or opt == '--no-report':
            no_report = 1
            continue
        if opt == '-f' or opt == '--file':
            counts_file = val
            continue
        if opt == '-m' or opt == '--missing':
            missing = 1
            continue
        if opt == '-C' or opt == '--coverdir':
            coverdir = val
            continue
        if opt == '-s' or opt == '--summary':
            summary = 1
            continue
        if opt == '--ignore-module':
            for mod in val.split(','):
                ignore_modules.append(mod.strip())

            continue
        if opt == '--ignore-dir':
            for s in val.split(os.pathsep):
                s = os.path.expandvars(s)
                s = s.replace('$prefix', os.path.join(sys.prefix, 'lib', 'python' + sys.version[:3]))
                s = s.replace('$exec_prefix', os.path.join(sys.exec_prefix, 'lib', 'python' + sys.version[:3]))
                s = os.path.normpath(s)
                ignore_dirs.append(s)

            continue

    if listfuncs and (count or trace):
        _err_exit('cannot specify both --listfuncs and (--trace or --count)')
    if not (count or trace or report or listfuncs or countcallers):
        _err_exit('must specify one of --trace, --count, --report, --listfuncs, or --trackcalls')
    if report and no_report:
        _err_exit('cannot specify both --report and --no-report')
    if report and not counts_file:
        _err_exit('--report requires a --file')
    if no_report and len(prog_argv) == 0:
        _err_exit('missing name of file to run')
    if report:
        results = CoverageResults(infile=counts_file, outfile=counts_file)
        results.write_results(missing, summary=summary, coverdir=coverdir)
    else:
        sys.argv = prog_argv
        progname = prog_argv[0]
        sys.path[0] = os.path.split(progname)[0]
        t = Trace(count, trace, countfuncs=listfuncs, countcallers=countcallers, ignoremods=ignore_modules, ignoredirs=ignore_dirs, infile=counts_file, outfile=counts_file, timing=timing)
        try:
            with open(progname) as fp:
                code = compile(fp.read(), progname, 'exec')
            globs = {'__file__': progname,
               '__name__': '__main__',
               '__package__': None,
               '__cached__': None
               }
            t.runctx(code, globs, globs)
        except IOError as err:
            _err_exit('Cannot run file %r because: %s' % (sys.argv[0], err))
        except SystemExit:
            pass

        results = t.results()
        if not no_report:
            results.write_results(missing, summary=summary, coverdir=coverdir)
    return


if __name__ == '__main__':
    main()