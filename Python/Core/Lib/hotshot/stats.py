# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: stats.py
"""Statistics analyzer for HotShot."""
import profile
import pstats
import hotshot.log
from hotshot.log import ENTER, EXIT

def load(filename):
    return StatsLoader(filename).load()


class StatsLoader:

    def __init__(self, logfn):
        self._logfn = logfn
        self._code = {}
        self._stack = []
        self.pop_frame = self._stack.pop

    def load(self):
        p = Profile()
        p.get_time = _brokentimer
        log = hotshot.log.LogReader(self._logfn)
        taccum = 0
        for event in log:
            what, (filename, lineno, funcname), tdelta = event
            if tdelta > 0:
                taccum += tdelta
            if what == ENTER:
                frame = self.new_frame(filename, lineno, funcname)
                p.trace_dispatch_call(frame, taccum * 1e-06)
                taccum = 0
            elif what == EXIT:
                frame = self.pop_frame()
                p.trace_dispatch_return(frame, taccum * 1e-06)
                taccum = 0

        return pstats.Stats(p)

    def new_frame(self, *args):
        try:
            code = self._code[args]
        except KeyError:
            code = FakeCode(*args)
            self._code[args] = code

        if self._stack:
            back = self._stack[-1]
        else:
            back = None
        frame = FakeFrame(code, back)
        self._stack.append(frame)
        return frame


class Profile(profile.Profile):

    def simulate_cmd_complete(self):
        pass


class FakeCode:

    def __init__(self, filename, firstlineno, funcname):
        self.co_filename = filename
        self.co_firstlineno = firstlineno
        self.co_name = self.__name__ = funcname


class FakeFrame:

    def __init__(self, code, back):
        self.f_back = back
        self.f_code = code


def _brokentimer():
    raise RuntimeError, 'this timer should not be called'