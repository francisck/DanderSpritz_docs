# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _threading.py
"""Thread module emulating a subset of Java's threading model."""
import sys as _sys
try:
    import thread
except ImportError:
    del _sys.modules[__name__]
    raise

import warnings
from time import time as _time, sleep as _sleep
from traceback import format_exc as _format_exc
from collections import deque
__all__ = [
 'activeCount', 'active_count', 'Condition', 'currentThread',
 'current_thread', 'enumerate', 'Event',
 'Lock', 'RLock', 'Semaphore', 'BoundedSemaphore', 'Thread',
 'Timer', 'setprofile', 'settrace', 'local', 'stack_size']
_start_new_thread = thread.start_new_thread
_allocate_lock = thread.allocate_lock
_get_ident = thread.get_ident
ThreadError = thread.error
del thread
warnings.filterwarnings('ignore', category=DeprecationWarning, module='threading', message='sys.exc_clear')
_VERBOSE = False

class _Verbose(object):

    def __init__(self, verbose=None):
        pass

    def _note(self, *args):
        pass


_profile_hook = None
_trace_hook = None

def setprofile(func):
    global _profile_hook
    _profile_hook = func


def settrace(func):
    global _trace_hook
    _trace_hook = func


Lock = _allocate_lock

def RLock(*args, **kwargs):
    return _RLock(*args, **kwargs)


class _RLock(_Verbose):

    def __init__(self, verbose=None):
        _Verbose.__init__(self, verbose)
        self.__block = _allocate_lock()
        self.__owner = None
        self.__count = 0
        return

    def __repr__(self):
        owner = self.__owner
        try:
            owner = _active[owner].name
        except KeyError:
            pass

        return '<%s owner=%r count=%d>' % (
         self.__class__.__name__, owner, self.__count)

    def acquire(self, blocking=1):
        me = _get_ident()
        if self.__owner == me:
            self.__count = self.__count + 1
            return 1
        rc = self.__block.acquire(blocking)
        if rc:
            self.__owner = me
            self.__count = 1
        return rc

    __enter__ = acquire

    def release(self):
        if self.__owner != _get_ident():
            raise RuntimeError('cannot release un-acquired lock')
        self.__count = count = self.__count - 1
        if not count:
            self.__owner = None
            self.__block.release()
        return

    def __exit__(self, t, v, tb):
        self.release()

    def _acquire_restore(self, count_owner):
        count, owner = count_owner
        self.__block.acquire()
        self.__count = count
        self.__owner = owner

    def _release_save(self):
        count = self.__count
        self.__count = 0
        owner = self.__owner
        self.__owner = None
        self.__block.release()
        return (
         count, owner)

    def _is_owned(self):
        return self.__owner == _get_ident()


def Condition(*args, **kwargs):
    return _Condition(*args, **kwargs)


class _Condition(_Verbose):

    def __init__(self, lock=None, verbose=None):
        _Verbose.__init__(self, verbose)
        if lock is None:
            lock = RLock()
        self.__lock = lock
        self.acquire = lock.acquire
        self.release = lock.release
        try:
            self._release_save = lock._release_save
        except AttributeError:
            pass

        try:
            self._acquire_restore = lock._acquire_restore
        except AttributeError:
            pass

        try:
            self._is_owned = lock._is_owned
        except AttributeError:
            pass

        self.__waiters = []
        return

    def __enter__(self):
        return self.__lock.__enter__()

    def __exit__(self, *args):
        return self.__lock.__exit__(*args)

    def __repr__(self):
        return '<Condition(%s, %d)>' % (self.__lock, len(self.__waiters))

    def _release_save(self):
        self.__lock.release()

    def _acquire_restore(self, x):
        self.__lock.acquire()

    def _is_owned(self):
        if self.__lock.acquire(0):
            self.__lock.release()
            return False
        else:
            return True

    def wait(self, timeout=None):
        if not self._is_owned():
            raise RuntimeError('cannot wait on un-acquired lock')
        waiter = _allocate_lock()
        waiter.acquire()
        self.__waiters.append(waiter)
        saved_state = self._release_save()
        try:
            if timeout is None:
                waiter.acquire()
            else:
                endtime = _time() + timeout
                delay = 0.0005
                while True:
                    gotit = waiter.acquire(0)
                    if gotit:
                        break
                    remaining = endtime - _time()
                    if remaining <= 0:
                        break
                    delay = min(delay * 2, remaining, 0.05)
                    _sleep(delay)

            if not gotit:
                try:
                    self.__waiters.remove(waiter)
                except ValueError:
                    pass

        finally:
            self._acquire_restore(saved_state)

        return

    def notify(self, n=1):
        if not self._is_owned():
            raise RuntimeError('cannot notify on un-acquired lock')
        __waiters = self.__waiters
        waiters = __waiters[:n]
        if not waiters:
            return
        self._note('%s.notify(): notifying %d waiter%s', self, n, n != 1 and 's' or '')
        for waiter in waiters:
            waiter.release()
            try:
                __waiters.remove(waiter)
            except ValueError:
                pass

    def notifyAll(self):
        self.notify(len(self.__waiters))

    notify_all = notifyAll


def Semaphore(*args, **kwargs):
    return _Semaphore(*args, **kwargs)


class _Semaphore(_Verbose):

    def __init__(self, value=1, verbose=None):
        if value < 0:
            raise ValueError('semaphore initial value must be >= 0')
        _Verbose.__init__(self, verbose)
        self.__cond = Condition(Lock())
        self.__value = value

    def acquire(self, blocking=1):
        rc = False
        self.__cond.acquire()
        while self.__value == 0:
            if not blocking:
                break
            self.__cond.wait()
        else:
            self.__value = self.__value - 1
            rc = True

        self.__cond.release()
        return rc

    __enter__ = acquire

    def release(self):
        self.__cond.acquire()
        self.__value = self.__value + 1
        self.__cond.notify()
        self.__cond.release()

    def __exit__(self, t, v, tb):
        self.release()


def BoundedSemaphore(*args, **kwargs):
    return _BoundedSemaphore(*args, **kwargs)


class _BoundedSemaphore(_Semaphore):
    """Semaphore that checks that # releases is <= # acquires"""

    def __init__(self, value=1, verbose=None):
        _Semaphore.__init__(self, value, verbose)
        self._initial_value = value

    def release(self):
        if self._Semaphore__value >= self._initial_value:
            raise ValueError, 'Semaphore released too many times'
        return _Semaphore.release(self)


def Event(*args, **kwargs):
    return _Event(*args, **kwargs)


class _Event(_Verbose):

    def __init__(self, verbose=None):
        _Verbose.__init__(self, verbose)
        self.__cond = Condition(Lock())
        self.__flag = False

    def _reset_internal_locks(self):
        self.__cond.__init__()

    def isSet(self):
        return self.__flag

    is_set = isSet

    def set(self):
        self.__cond.acquire()
        try:
            self.__flag = True
            self.__cond.notify_all()
        finally:
            self.__cond.release()

    def clear(self):
        self.__cond.acquire()
        try:
            self.__flag = False
        finally:
            self.__cond.release()

    def wait(self, timeout=None):
        self.__cond.acquire()
        try:
            if not self.__flag:
                self.__cond.wait(timeout)
            return self.__flag
        finally:
            self.__cond.release()


_counter = 0

def _newname(template='Thread-%d'):
    global _counter
    _counter = _counter + 1
    return template % _counter


_active_limbo_lock = _allocate_lock()
_active = {}
_limbo = {}

class Thread(_Verbose):
    __initialized = False
    __exc_info = _sys.exc_info
    __exc_clear = _sys.exc_clear

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        _Verbose.__init__(self, verbose)
        if kwargs is None:
            kwargs = {}
        self.__target = target
        self.__name = str(name or _newname())
        self.__args = args
        self.__kwargs = kwargs
        self.__daemonic = self._set_daemon()
        self.__ident = None
        self.__started = Event()
        self.__stopped = False
        self.__block = Condition(Lock())
        self.__initialized = True
        self.__stderr = _sys.stderr
        return

    def _reset_internal_locks(self):
        if hasattr(self, '_Thread__block'):
            self.__block.__init__()
        self.__started._reset_internal_locks()

    @property
    def _block(self):
        return self.__block

    def _set_daemon(self):
        return current_thread().daemon

    def __repr__(self):
        status = 'initial'
        if self.__started.is_set():
            status = 'started'
        if self.__stopped:
            status = 'stopped'
        if self.__daemonic:
            status += ' daemon'
        if self.__ident is not None:
            status += ' %s' % self.__ident
        return '<%s(%s, %s)>' % (self.__class__.__name__, self.__name, status)

    def start(self):
        global _active_limbo_lock
        if not self.__initialized:
            raise RuntimeError('thread.__init__() not called')
        if self.__started.is_set():
            raise RuntimeError('threads can only be started once')
        with _active_limbo_lock:
            _limbo[self] = self
        try:
            _start_new_thread(self.__bootstrap, ())
        except Exception:
            with _active_limbo_lock:
                del _limbo[self]
            raise

        self.__started.wait()

    def run(self):
        try:
            if self.__target:
                self.__target(*self.__args, **self.__kwargs)
        finally:
            del self.__target
            del self.__args
            del self.__kwargs

    def __bootstrap(self):
        try:
            self.__bootstrap_inner()
        except:
            if self.__daemonic and _sys is None:
                return
            raise

        return

    def _set_ident(self):
        self.__ident = _get_ident()

    def __bootstrap_inner(self):
        try:
            self._set_ident()
            self.__started.set()
            with _active_limbo_lock:
                _active[self.__ident] = self
                del _limbo[self]
            if _trace_hook:
                self._note('%s.__bootstrap(): registering trace hook', self)
                _sys.settrace(_trace_hook)
            if _profile_hook:
                self._note('%s.__bootstrap(): registering profile hook', self)
                _sys.setprofile(_profile_hook)
            try:
                try:
                    self.run()
                except SystemExit:
                    pass
                except:
                    if _sys:
                        _sys.stderr.write('Exception in thread %s:\n%s\n' % (
                         self.name, _format_exc()))
                    else:
                        exc_type, exc_value, exc_tb = self.__exc_info()
                        try:
                            print >> self.__stderr, 'Exception in thread ' + self.name + ' (most likely raised during interpreter shutdown):'
                            print >> self.__stderr, 'Traceback (most recent call last):'
                            while exc_tb:
                                print >> self.__stderr, '  File "%s", line %s, in %s' % (
                                 exc_tb.tb_frame.f_code.co_filename,
                                 exc_tb.tb_lineno,
                                 exc_tb.tb_frame.f_code.co_name)
                                exc_tb = exc_tb.tb_next

                            print >> self.__stderr, '%s: %s' % (exc_type, exc_value)
                        finally:
                            del exc_type
                            del exc_value
                            del exc_tb

            finally:
                self.__exc_clear()

        finally:
            with _active_limbo_lock:
                self.__stop()
                try:
                    del _active[_get_ident()]
                except:
                    pass

    def __stop(self):
        self.__block.acquire()
        self.__stopped = True
        self.__block.notify_all()
        self.__block.release()

    def __delete(self):
        """Remove current thread from the dict of currently running threads."""
        try:
            with _active_limbo_lock:
                del _active[_get_ident()]
        except KeyError:
            if 'dummy_threading' not in _sys.modules:
                raise

    def join(self, timeout=None):
        if not self.__initialized:
            raise RuntimeError('Thread.__init__() not called')
        if not self.__started.is_set():
            raise RuntimeError('cannot join thread before it is started')
        if self is current_thread():
            raise RuntimeError('cannot join current thread')
        self.__block.acquire()
        try:
            if timeout is None:
                while not self.__stopped:
                    self.__block.wait()

            else:
                deadline = _time() + timeout
                while not self.__stopped:
                    delay = deadline - _time()
                    if delay <= 0:
                        break
                    self.__block.wait(delay)

        finally:
            self.__block.release()

        return

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = str(name)

    @property
    def ident(self):
        return self.__ident

    def isAlive(self):
        return self.__started.is_set() and not self.__stopped

    is_alive = isAlive

    @property
    def daemon(self):
        return self.__daemonic

    @daemon.setter
    def daemon(self, daemonic):
        if not self.__initialized:
            raise RuntimeError('Thread.__init__() not called')
        if self.__started.is_set():
            raise RuntimeError('cannot set daemon status of active thread')
        self.__daemonic = daemonic

    def isDaemon(self):
        return self.daemon

    def setDaemon(self, daemonic):
        self.daemon = daemonic

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name


def Timer(*args, **kwargs):
    return _Timer(*args, **kwargs)


class _Timer(Thread):
    """Call a function after a specified number of seconds:
    
    t = Timer(30.0, f, args=[], kwargs={})
    t.start()
    t.cancel() # stop the timer's action if it's still waiting
    """

    def __init__(self, interval, function, args=[], kwargs={}):
        Thread.__init__(self)
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.finished = Event()

    def cancel(self):
        """Stop the timer if it hasn't finished yet"""
        self.finished.set()

    def run(self):
        self.finished.wait(self.interval)
        if not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
        self.finished.set()


class _MainThread(Thread):

    def __init__(self):
        Thread.__init__(self, name='MainThread')
        self._Thread__started.set()
        self._set_ident()
        with _active_limbo_lock:
            _active[_get_ident()] = self

    def _set_daemon(self):
        return False

    def _exitfunc(self):
        self._Thread__stop()
        t = _pickSomeNonDaemonThread()
        if t:
            pass
        while t:
            t.join()
            t = _pickSomeNonDaemonThread()

        self._Thread__delete()


def _pickSomeNonDaemonThread():
    for t in enumerate():
        if not t.daemon and t.is_alive():
            return t

    return None


class _DummyThread(Thread):

    def __init__(self):
        Thread.__init__(self, name=_newname('Dummy-%d'))
        del self._Thread__block
        self._Thread__started.set()
        self._set_ident()
        with _active_limbo_lock:
            _active[_get_ident()] = self

    def _set_daemon(self):
        return True

    def join(self, timeout=None):
        pass


def currentThread():
    try:
        return _active[_get_ident()]
    except KeyError:
        return _DummyThread()


current_thread = currentThread

def activeCount():
    with _active_limbo_lock:
        return len(_active) + len(_limbo)


active_count = activeCount

def _enumerate():
    return _active.values() + _limbo.values()


def enumerate():
    with _active_limbo_lock:
        return _active.values() + _limbo.values()


from thread import stack_size
_shutdown = _MainThread()._exitfunc
try:
    from thread import _local as local
except ImportError:
    from _threading_local import local

def _after_fork():
    global _active_limbo_lock
    _active_limbo_lock = _allocate_lock()
    new_active = {}
    current = current_thread()
    with _active_limbo_lock:
        for thread in _active.itervalues():
            if thread is current:
                ident = _get_ident()
                thread._Thread__ident = ident
                if hasattr(thread, '_reset_internal_locks'):
                    thread._reset_internal_locks()
                new_active[ident] = thread
            else:
                thread._Thread__stopped = True

        _limbo.clear()
        _active.clear()
        _active.update(new_active)


def _test():

    class BoundedQueue(_Verbose):

        def __init__(self, limit):
            _Verbose.__init__(self)
            self.mon = RLock()
            self.rc = Condition(self.mon)
            self.wc = Condition(self.mon)
            self.limit = limit
            self.queue = deque()

        def put(self, item):
            self.mon.acquire()
            while len(self.queue) >= self.limit:
                self._note('put(%s): queue full', item)
                self.wc.wait()

            self.queue.append(item)
            self._note('put(%s): appended, length now %d', item, len(self.queue))
            self.rc.notify()
            self.mon.release()

        def get(self):
            self.mon.acquire()
            while not self.queue:
                self._note('get(): queue empty')
                self.rc.wait()

            item = self.queue.popleft()
            self._note('get(): got %s, %d left', item, len(self.queue))
            self.wc.notify()
            self.mon.release()
            return item

    class ProducerThread(Thread):

        def __init__(self, queue, quota):
            Thread.__init__(self, name='Producer')
            self.queue = queue
            self.quota = quota

        def run(self):
            from random import random
            counter = 0
            while counter < self.quota:
                counter = counter + 1
                self.queue.put('%s.%d' % (self.name, counter))
                _sleep(random() * 1e-05)

    class ConsumerThread(Thread):

        def __init__(self, queue, count):
            Thread.__init__(self, name='Consumer')
            self.queue = queue
            self.count = count

        def run(self):
            while self.count > 0:
                item = self.queue.get()
                print item
                self.count = self.count - 1

    NP = 3
    QL = 4
    NI = 5
    Q = BoundedQueue(QL)
    P = []
    for i in range(NP):
        t = ProducerThread(Q, NI)
        t.name = 'Producer-%d' % (i + 1)
        P.append(t)

    C = ConsumerThread(Q, NI * NP)
    for t in P:
        t.start()
        _sleep(1e-06)

    C.start()
    for t in P:
        t.join()

    C.join()


if __name__ == '__main__':
    _test()