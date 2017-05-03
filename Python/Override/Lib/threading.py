# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: threading.py
import dsz.script
_threadsAllowed = False
try:
    if dsz.script.Env['script_threading'] == 'YES':
        _threadsAllowed = True
except:
    pass

if _threadsAllowed:
    from _threading import *
else:
    import _threading
    active_count = _threading.active_count
    activeCount = _threading.activeCount
    Condition = _threading.Condition
    current_thread = _threading.current_thread
    currentThread = _threading.currentThread
    enumerate = _threading.enumerate
    Event = _threading.Event
    local = _threading.local
    Lock = _threading.Lock
    RLock = _threading.RLock
    Semaphore = _threading.Semaphore
    BoundedSemaphore = _threading.BoundedSemaphore
    settrace = _threading.settrace
    setprofile = _threading.setprofile
    stack_size = _threading.stack_size

    class Timer:

        def __init__(self, interval, function, args=[], kwargs={}):
            raise RuntimeError('Threads are not supported in embedded DSZ Python scripts')


    class Thread:

        def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
            raise RuntimeError('Threads are not supported in embedded DSZ Python scripts')

        def run(self):
            raise RuntimeError('Threads are not supported in embedded DSZ Python scripts')