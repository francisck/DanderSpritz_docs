# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: bdb.py
"""Debugger basics"""
import fnmatch
import sys
import os
import types
__all__ = [
 'BdbQuit', 'Bdb', 'Breakpoint']

class BdbQuit(Exception):
    """Exception to give up completely"""
    pass


class Bdb():
    """Generic Python debugger base class.
    
    This class takes care of details of the trace facility;
    a derived class should implement user interaction.
    The standard debugger class (pdb.Pdb) is an example.
    """

    def __init__(self, skip=None):
        self.skip = set(skip) if skip else None
        self.breaks = {}
        self.fncache = {}
        return

    def canonic(self, filename):
        if filename == '<' + filename[1:-1] + '>':
            return filename
        canonic = self.fncache.get(filename)
        if not canonic:
            canonic = os.path.abspath(filename)
            canonic = os.path.normcase(canonic)
            self.fncache[filename] = canonic
        return canonic

    def reset(self):
        import linecache
        linecache.checkcache()
        self.botframe = None
        self._set_stopinfo(None, None)
        return

    def trace_dispatch(self, frame, event, arg):
        if self.quitting:
            return
        if event == 'line':
            return self.dispatch_line(frame)
        if event == 'call':
            return self.dispatch_call(frame, arg)
        if event == 'return':
            return self.dispatch_return(frame, arg)
        if event == 'exception':
            return self.dispatch_exception(frame, arg)
        if event == 'c_call':
            return self.trace_dispatch
        if event == 'c_exception':
            return self.trace_dispatch
        if event == 'c_return':
            return self.trace_dispatch
        print 'bdb.Bdb.dispatch: unknown debugging event:', repr(event)
        return self.trace_dispatch

    def dispatch_line(self, frame):
        if self.stop_here(frame) or self.break_here(frame):
            self.user_line(frame)
            if self.quitting:
                raise BdbQuit
        return self.trace_dispatch

    def dispatch_call(self, frame, arg):
        if self.botframe is None:
            self.botframe = frame.f_back
            return self.trace_dispatch
        else:
            if not (self.stop_here(frame) or self.break_anywhere(frame)):
                return
            self.user_call(frame, arg)
            if self.quitting:
                raise BdbQuit
            return self.trace_dispatch

    def dispatch_return(self, frame, arg):
        if self.stop_here(frame) or frame == self.returnframe:
            self.user_return(frame, arg)
            if self.quitting:
                raise BdbQuit
        return self.trace_dispatch

    def dispatch_exception(self, frame, arg):
        if self.stop_here(frame):
            self.user_exception(frame, arg)
            if self.quitting:
                raise BdbQuit
        return self.trace_dispatch

    def is_skipped_module(self, module_name):
        for pattern in self.skip:
            if fnmatch.fnmatch(module_name, pattern):
                return True

        return False

    def stop_here(self, frame):
        if self.skip and self.is_skipped_module(frame.f_globals.get('__name__')):
            return False
        else:
            if frame is self.stopframe:
                if self.stoplineno == -1:
                    return False
                return frame.f_lineno >= self.stoplineno
            while frame is not None and frame is not self.stopframe:
                if frame is self.botframe:
                    return True
                frame = frame.f_back

            return False

    def break_here(self, frame):
        filename = self.canonic(frame.f_code.co_filename)
        if filename not in self.breaks:
            return False
        else:
            lineno = frame.f_lineno
            if lineno not in self.breaks[filename]:
                lineno = frame.f_code.co_firstlineno
                if lineno not in self.breaks[filename]:
                    return False
            bp, flag = effective(filename, lineno, frame)
            if bp:
                self.currentbp = bp.number
                if flag and bp.temporary:
                    self.do_clear(str(bp.number))
                return True
            return False

    def do_clear(self, arg):
        raise NotImplementedError, 'subclass of bdb must implement do_clear()'

    def break_anywhere(self, frame):
        return self.canonic(frame.f_code.co_filename) in self.breaks

    def user_call(self, frame, argument_list):
        """This method is called when there is the remote possibility
        that we ever need to stop in this function."""
        pass

    def user_line(self, frame):
        """This method is called when we stop or break at this line."""
        pass

    def user_return(self, frame, return_value):
        """This method is called when a return trap is set here."""
        pass

    def user_exception(self, frame, exc_info):
        exc_type, exc_value, exc_traceback = exc_info

    def _set_stopinfo(self, stopframe, returnframe, stoplineno=0):
        self.stopframe = stopframe
        self.returnframe = returnframe
        self.quitting = 0
        self.stoplineno = stoplineno

    def set_until(self, frame):
        """Stop when the line with the line no greater than the current one is
        reached or when returning from current frame"""
        self._set_stopinfo(frame, frame, frame.f_lineno + 1)

    def set_step(self):
        """Stop after one line of code."""
        self._set_stopinfo(None, None)
        return

    def set_next(self, frame):
        """Stop on the next line in or below the given frame."""
        self._set_stopinfo(frame, None)
        return

    def set_return(self, frame):
        """Stop when returning from the given frame."""
        self._set_stopinfo(frame.f_back, frame)

    def set_trace(self, frame=None):
        """Start debugging from `frame`.
        
        If frame is not specified, debugging starts from caller's frame.
        """
        if frame is None:
            frame = sys._getframe().f_back
        self.reset()
        while frame:
            frame.f_trace = self.trace_dispatch
            self.botframe = frame
            frame = frame.f_back

        self.set_step()
        sys.settrace(self.trace_dispatch)
        return

    def set_continue(self):
        self._set_stopinfo(self.botframe, None, -1)
        if not self.breaks:
            sys.settrace(None)
            frame = sys._getframe().f_back
            while frame and frame is not self.botframe:
                del frame.f_trace
                frame = frame.f_back

        return

    def set_quit(self):
        self.stopframe = self.botframe
        self.returnframe = None
        self.quitting = 1
        sys.settrace(None)
        return

    def set_break(self, filename, lineno, temporary=0, cond=None, funcname=None):
        filename = self.canonic(filename)
        import linecache
        line = linecache.getline(filename, lineno)
        if not line:
            return 'Line %s:%d does not exist' % (filename,
             lineno)
        if filename not in self.breaks:
            self.breaks[filename] = []
        list = self.breaks[filename]
        if lineno not in list:
            list.append(lineno)
        bp = Breakpoint(filename, lineno, temporary, cond, funcname)

    def _prune_breaks(self, filename, lineno):
        if (
         filename, lineno) not in Breakpoint.bplist:
            self.breaks[filename].remove(lineno)
        if not self.breaks[filename]:
            del self.breaks[filename]

    def clear_break(self, filename, lineno):
        filename = self.canonic(filename)
        if filename not in self.breaks:
            return 'There are no breakpoints in %s' % filename
        if lineno not in self.breaks[filename]:
            return 'There is no breakpoint at %s:%d' % (filename,
             lineno)
        for bp in Breakpoint.bplist[filename, lineno][:]:
            bp.deleteMe()

        self._prune_breaks(filename, lineno)

    def clear_bpbynumber(self, arg):
        try:
            number = int(arg)
        except:
            return 'Non-numeric breakpoint number (%s)' % arg

        try:
            bp = Breakpoint.bpbynumber[number]
        except IndexError:
            return 'Breakpoint number (%d) out of range' % number

        if not bp:
            return 'Breakpoint (%d) already deleted' % number
        bp.deleteMe()
        self._prune_breaks(bp.file, bp.line)

    def clear_all_file_breaks(self, filename):
        filename = self.canonic(filename)
        if filename not in self.breaks:
            return 'There are no breakpoints in %s' % filename
        for line in self.breaks[filename]:
            blist = Breakpoint.bplist[filename, line]
            for bp in blist:
                bp.deleteMe()

        del self.breaks[filename]

    def clear_all_breaks(self):
        if not self.breaks:
            return 'There are no breakpoints'
        for bp in Breakpoint.bpbynumber:
            if bp:
                bp.deleteMe()

        self.breaks = {}

    def get_break(self, filename, lineno):
        filename = self.canonic(filename)
        return filename in self.breaks and lineno in self.breaks[filename]

    def get_breaks(self, filename, lineno):
        filename = self.canonic(filename)
        return filename in self.breaks and lineno in self.breaks[filename] and Breakpoint.bplist[filename, lineno] or []

    def get_file_breaks(self, filename):
        filename = self.canonic(filename)
        if filename in self.breaks:
            return self.breaks[filename]
        else:
            return []

    def get_all_breaks(self):
        return self.breaks

    def get_stack(self, f, t):
        stack = []
        if t and t.tb_frame is f:
            t = t.tb_next
        while f is not None:
            stack.append((f, f.f_lineno))
            if f is self.botframe:
                break
            f = f.f_back

        stack.reverse()
        i = max(0, len(stack) - 1)
        while t is not None:
            stack.append((t.tb_frame, t.tb_lineno))
            t = t.tb_next

        if f is None:
            i = max(0, len(stack) - 1)
        return (stack, i)

    def format_stack_entry(self, frame_lineno, lprefix=': '):
        import linecache
        import repr
        frame, lineno = frame_lineno
        filename = self.canonic(frame.f_code.co_filename)
        s = '%s(%r)' % (filename, lineno)
        if frame.f_code.co_name:
            s = s + frame.f_code.co_name
        else:
            s = s + '<lambda>'
        if '__args__' in frame.f_locals:
            args = frame.f_locals['__args__']
        else:
            args = None
        if args:
            s = s + repr.repr(args)
        else:
            s = s + '()'
        if '__return__' in frame.f_locals:
            rv = frame.f_locals['__return__']
            s = s + '->'
            s = s + repr.repr(rv)
        line = linecache.getline(filename, lineno, frame.f_globals)
        if line:
            s = s + lprefix + line.strip()
        return s

    def run(self, cmd, globals=None, locals=None):
        if globals is None:
            import __main__
            globals = __main__.__dict__
        if locals is None:
            locals = globals
        self.reset()
        sys.settrace(self.trace_dispatch)
        if not isinstance(cmd, types.CodeType):
            cmd = cmd + '\n'
        try:
            try:
                exec cmd in globals, locals
            except BdbQuit:
                pass

        finally:
            self.quitting = 1
            sys.settrace(None)

        return

    def runeval(self, expr, globals=None, locals=None):
        if globals is None:
            import __main__
            globals = __main__.__dict__
        if locals is None:
            locals = globals
        self.reset()
        sys.settrace(self.trace_dispatch)
        if not isinstance(expr, types.CodeType):
            expr = expr + '\n'
        try:
            try:
                return eval(expr, globals, locals)
            except BdbQuit:
                pass

        finally:
            self.quitting = 1
            sys.settrace(None)

        return

    def runctx(self, cmd, globals, locals):
        self.run(cmd, globals, locals)

    def runcall(self, func, *args, **kwds):
        self.reset()
        sys.settrace(self.trace_dispatch)
        res = None
        try:
            try:
                res = func(*args, **kwds)
            except BdbQuit:
                pass

        finally:
            self.quitting = 1
            sys.settrace(None)

        return res


def set_trace():
    Bdb().set_trace()


class Breakpoint():
    """Breakpoint class
    
    Implements temporary breakpoints, ignore counts, disabling and
    (re)-enabling, and conditionals.
    
    Breakpoints are indexed by number through bpbynumber and by
    the file,line tuple using bplist.  The former points to a
    single instance of class Breakpoint.  The latter points to a
    list of such instances since there may be more than one
    breakpoint per line.
    
    """
    next = 1
    bplist = {}
    bpbynumber = [None]

    def __init__(self, file, line, temporary=0, cond=None, funcname=None):
        self.funcname = funcname
        self.func_first_executable_line = None
        self.file = file
        self.line = line
        self.temporary = temporary
        self.cond = cond
        self.enabled = 1
        self.ignore = 0
        self.hits = 0
        self.number = Breakpoint.next
        Breakpoint.next = Breakpoint.next + 1
        self.bpbynumber.append(self)
        if (file, line) in self.bplist:
            self.bplist[file, line].append(self)
        else:
            self.bplist[file, line] = [
             self]
        return

    def deleteMe(self):
        index = (
         self.file, self.line)
        self.bpbynumber[self.number] = None
        self.bplist[index].remove(self)
        if not self.bplist[index]:
            del self.bplist[index]
        return

    def enable(self):
        self.enabled = 1

    def disable(self):
        self.enabled = 0

    def bpprint(self, out=None):
        if out is None:
            out = sys.stdout
        if self.temporary:
            disp = 'del  '
        else:
            disp = 'keep '
        if self.enabled:
            disp = disp + 'yes  '
        else:
            disp = disp + 'no   '
        print >> out, '%-4dbreakpoint   %s at %s:%d' % (self.number, disp,
         self.file, self.line)
        if self.cond:
            print >> out, '\tstop only if %s' % (self.cond,)
        if self.ignore:
            print >> out, '\tignore next %d hits' % self.ignore
        if self.hits:
            if self.hits > 1:
                ss = 's'
            else:
                ss = ''
            print >> out, '\tbreakpoint already hit %d time%s' % (
             self.hits, ss)
        return


def checkfuncname(b, frame):
    """Check whether we should break here because of `b.funcname`."""
    if not b.funcname:
        if b.line != frame.f_lineno:
            return False
        return True
    if frame.f_code.co_name != b.funcname:
        return False
    if not b.func_first_executable_line:
        b.func_first_executable_line = frame.f_lineno
    if b.func_first_executable_line != frame.f_lineno:
        return False
    return True


def effective(file, line, frame):
    """Determine which breakpoint for this file:line is to be acted upon.
    
    Called only if we know there is a bpt at this
    location.  Returns breakpoint that was triggered and a flag
    that indicates if it is ok to delete a temporary bp.
    
    """
    possibles = Breakpoint.bplist[file, line]
    for i in range(0, len(possibles)):
        b = possibles[i]
        if b.enabled == 0:
            continue
        if not checkfuncname(b, frame):
            continue
        b.hits = b.hits + 1
        if not b.cond:
            if b.ignore > 0:
                b.ignore = b.ignore - 1
                continue
            else:
                return (
                 b, 1)
        else:
            try:
                val = eval(b.cond, frame.f_globals, frame.f_locals)
                if val:
                    if b.ignore > 0:
                        b.ignore = b.ignore - 1
                    else:
                        return (b, 1)
            except:
                return (
                 b, 0)

    return (None, None)


class Tdb(Bdb):

    def user_call(self, frame, args):
        name = frame.f_code.co_name
        if not name:
            name = '???'
        print '+++ call', name, args

    def user_line(self, frame):
        import linecache
        name = frame.f_code.co_name
        if not name:
            name = '???'
        fn = self.canonic(frame.f_code.co_filename)
        line = linecache.getline(fn, frame.f_lineno, frame.f_globals)
        print '+++', fn, frame.f_lineno, name, ':', line.strip()

    def user_return(self, frame, retval):
        print '+++ return', retval

    def user_exception(self, frame, exc_stuff):
        print '+++ exception', exc_stuff
        self.set_continue()


def foo(n):
    print 'foo(', n, ')'
    x = bar(n * 10)
    print 'bar returned', x


def bar(a):
    print 'bar(', a, ')'
    return a / 2


def test():
    t = Tdb()
    t.run('import bdb; bdb.foo(10)')