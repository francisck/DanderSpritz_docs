# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: signals.py
import signal
import weakref
from functools import wraps
__unittest = True

class _InterruptHandler(object):

    def __init__(self, default_handler):
        self.called = False
        self.default_handler = default_handler

    def __call__(self, signum, frame):
        installed_handler = signal.getsignal(signal.SIGINT)
        if installed_handler is not self:
            self.default_handler(signum, frame)
        if self.called:
            self.default_handler(signum, frame)
        self.called = True
        for result in _results.keys():
            result.stop()


_results = weakref.WeakKeyDictionary()

def registerResult(result):
    _results[result] = 1


def removeResult(result):
    return bool(_results.pop(result, None))


_interrupt_handler = None

def installHandler():
    global _interrupt_handler
    if _interrupt_handler is None:
        default_handler = signal.getsignal(signal.SIGINT)
        _interrupt_handler = _InterruptHandler(default_handler)
        signal.signal(signal.SIGINT, _interrupt_handler)
    return


def removeHandler(method=None):
    if method is not None:

        @wraps(method)
        def inner(*args, **kwargs):
            initial = signal.getsignal(signal.SIGINT)
            removeHandler()
            try:
                return method(*args, **kwargs)
            finally:
                signal.signal(signal.SIGINT, initial)

        return inner
    else:
        if _interrupt_handler is not None:
            signal.signal(signal.SIGINT, _interrupt_handler.default_handler)
        return