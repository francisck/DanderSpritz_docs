# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: util.py
import itertools
import weakref
import atexit
import threading
from multiprocessing.process import current_process, active_children
__all__ = [
 'sub_debug', 'debug', 'info', 'sub_warning', 'get_logger',
 'log_to_stderr', 'get_temp_dir', 'register_after_fork',
 'is_exiting', 'Finalize', 'ForkAwareThreadLock', 'ForkAwareLocal',
 'SUBDEBUG', 'SUBWARNING']
NOTSET = 0
SUBDEBUG = 5
DEBUG = 10
INFO = 20
SUBWARNING = 25
LOGGER_NAME = 'multiprocessing'
DEFAULT_LOGGING_FORMAT = '[%(levelname)s/%(processName)s] %(message)s'
_logger = None
_log_to_stderr = False

def sub_debug(msg, *args):
    global _logger
    if _logger:
        _logger.log(SUBDEBUG, msg, *args)


def debug(msg, *args):
    if _logger:
        _logger.log(DEBUG, msg, *args)


def info(msg, *args):
    if _logger:
        _logger.log(INFO, msg, *args)


def sub_warning(msg, *args):
    if _logger:
        _logger.log(SUBWARNING, msg, *args)


def get_logger():
    """
    Returns logger used by multiprocessing
    """
    global _logger
    import logging
    import atexit
    logging._acquireLock()
    try:
        if not _logger:
            _logger = logging.getLogger(LOGGER_NAME)
            _logger.propagate = 0
            logging.addLevelName(SUBDEBUG, 'SUBDEBUG')
            logging.addLevelName(SUBWARNING, 'SUBWARNING')
            if hasattr(atexit, 'unregister'):
                atexit.unregister(_exit_function)
                atexit.register(_exit_function)
            else:
                atexit._exithandlers.remove((_exit_function, (), {}))
                atexit._exithandlers.append((_exit_function, (), {}))
    finally:
        logging._releaseLock()

    return _logger


def log_to_stderr(level=None):
    """
    Turn on logging and add a handler which prints to stderr
    """
    global _log_to_stderr
    import logging
    logger = get_logger()
    formatter = logging.Formatter(DEFAULT_LOGGING_FORMAT)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if level:
        logger.setLevel(level)
    _log_to_stderr = True
    return _logger


def get_temp_dir():
    if current_process()._tempdir is None:
        import shutil
        import tempfile
        tempdir = tempfile.mkdtemp(prefix='pymp-')
        info('created temp directory %s', tempdir)
        Finalize(None, shutil.rmtree, args=[tempdir], exitpriority=-100)
        current_process()._tempdir = tempdir
    return current_process()._tempdir


_afterfork_registry = weakref.WeakValueDictionary()
_afterfork_counter = itertools.count()

def _run_after_forkers():
    items = list(_afterfork_registry.items())
    items.sort()
    for (index, ident, func), obj in items:
        try:
            func(obj)
        except Exception as e:
            info('after forker raised exception %s', e)


def register_after_fork(obj, func):
    _afterfork_registry[_afterfork_counter.next(), id(obj), func] = obj


_finalizer_registry = {}
_finalizer_counter = itertools.count()

class Finalize(object):
    """
    Class which supports object finalization using weakrefs
    """

    def __init__(self, obj, callback, args=(), kwargs=None, exitpriority=None):
        if obj is not None:
            self._weakref = weakref.ref(obj, self)
        self._callback = callback
        self._args = args
        self._kwargs = kwargs or {}
        self._key = (exitpriority, _finalizer_counter.next())
        _finalizer_registry[self._key] = self
        return

    def __call__(self, wr=None):
        """
        Run the callback unless it has already been called or cancelled
        """
        try:
            del _finalizer_registry[self._key]
        except KeyError:
            sub_debug('finalizer no longer registered')
        else:
            sub_debug('finalizer calling %s with args %s and kwargs %s', self._callback, self._args, self._kwargs)
            res = self._callback(*self._args, **self._kwargs)
            self._weakref = self._callback = self._args = self._kwargs = self._key = None
            return res

        return

    def cancel(self):
        """
        Cancel finalization of the object
        """
        try:
            del _finalizer_registry[self._key]
        except KeyError:
            pass
        else:
            self._weakref = self._callback = self._args = self._kwargs = self._key = None

        return

    def still_active(self):
        """
        Return whether this finalizer is still waiting to invoke callback
        """
        return self._key in _finalizer_registry

    def __repr__(self):
        try:
            obj = self._weakref()
        except (AttributeError, TypeError):
            obj = None

        if obj is None:
            return '<Finalize object, dead>'
        else:
            x = '<Finalize object, callback=%s' % getattr(self._callback, '__name__', self._callback)
            if self._args:
                x += ', args=' + str(self._args)
            if self._kwargs:
                x += ', kwargs=' + str(self._kwargs)
            if self._key[0] is not None:
                x += ', exitprority=' + str(self._key[0])
            return x + '>'


def _run_finalizers(minpriority=None):
    """
    Run all finalizers whose exit priority is not None and at least minpriority
    
    Finalizers with highest priority are called first; finalizers with
    the same priority will be called in reverse order of creation.
    """
    if minpriority is None:
        f = lambda p: p[0][0] is not None
    else:
        f = lambda p: p[0][0] is not None and p[0][0] >= minpriority
    items = [ x for x in _finalizer_registry.items() if f(x) ]
    items.sort(reverse=True)
    for key, finalizer in items:
        sub_debug('calling %s', finalizer)
        try:
            finalizer()
        except Exception:
            import traceback
            traceback.print_exc()

    if minpriority is None:
        _finalizer_registry.clear()
    return


def is_exiting():
    """
    Returns true if the process is shutting down
    """
    global _exiting
    return _exiting or _exiting is None


_exiting = False

def _exit_function():
    info('process shutting down')
    debug('running all "atexit" finalizers with priority >= 0')
    _run_finalizers(0)
    for p in active_children():
        if p._daemonic:
            info('calling terminate() for daemon %s', p.name)
            p._popen.terminate()

    for p in active_children():
        info('calling join() for process %s', p.name)
        p.join()

    debug('running the remaining "atexit" finalizers')
    _run_finalizers()


atexit.register(_exit_function)

class ForkAwareThreadLock(object):

    def __init__(self):
        self._lock = threading.Lock()
        self.acquire = self._lock.acquire
        self.release = self._lock.release
        register_after_fork(self, ForkAwareThreadLock.__init__)


class ForkAwareLocal(threading.local):

    def __init__(self):
        register_after_fork(self, lambda obj: obj.__dict__.clear())

    def __reduce__(self):
        return (
         type(self), ())