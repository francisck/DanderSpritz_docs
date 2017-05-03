# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: sched.py
"""A generally useful event scheduler class.

Each instance of this class manages its own queue.
No multi-threading is implied; you are supposed to hack that
yourself, or use a single instance per application.

Each instance is parametrized with two functions, one that is
supposed to return the current time, one that is supposed to
implement a delay.  You can implement real-time scheduling by
substituting time and sleep from built-in module time, or you can
implement simulated time by writing your own functions.  This can
also be used to integrate scheduling with STDWIN events; the delay
function is allowed to modify the queue.  Time can be expressed as
integers or floating point numbers, as long as it is consistent.

Events are specified by tuples (time, priority, action, argument).
As in UNIX, lower priority numbers mean higher priority; in this
way the queue can be maintained as a priority queue.  Execution of the
event means calling the action function, passing it the argument
sequence in "argument" (remember that in Python, multiple function
arguments are be packed in a sequence).
The action function may be an instance method so it
has another way to reference private data (besides global variables).
"""
import heapq
from collections import namedtuple
__all__ = [
 'scheduler']
Event = namedtuple('Event', 'time, priority, action, argument')

class scheduler:

    def __init__(self, timefunc, delayfunc):
        """Initialize a new instance, passing the time and delay
        functions"""
        self._queue = []
        self.timefunc = timefunc
        self.delayfunc = delayfunc

    def enterabs(self, time, priority, action, argument):
        """Enter a new event in the queue at an absolute time.
        
        Returns an ID for the event which can be used to remove it,
        if necessary.
        
        """
        event = Event(time, priority, action, argument)
        heapq.heappush(self._queue, event)
        return event

    def enter(self, delay, priority, action, argument):
        """A variant that specifies the time as a relative time.
        
        This is actually the more commonly used interface.
        
        """
        time = self.timefunc() + delay
        return self.enterabs(time, priority, action, argument)

    def cancel(self, event):
        """Remove an event from the queue.
        
        This must be presented the ID as returned by enter().
        If the event is not in the queue, this raises ValueError.
        
        """
        self._queue.remove(event)
        heapq.heapify(self._queue)

    def empty(self):
        """Check whether the queue is empty."""
        return not self._queue

    def run(self):
        """Execute events until the queue is empty.
        
        When there is a positive delay until the first event, the
        delay function is called and the event is left in the queue;
        otherwise, the event is removed from the queue and executed
        (its action function is called, passing it the argument).  If
        the delay function returns prematurely, it is simply
        restarted.
        
        It is legal for both the delay function and the action
        function to to modify the queue or to raise an exception;
        exceptions are not caught but the scheduler's state remains
        well-defined so run() may be called again.
        
        A questionable hack is added to allow other threads to run:
        just after an event is executed, a delay of 0 is executed, to
        avoid monopolizing the CPU when other threads are also
        runnable.
        
        """
        q = self._queue
        delayfunc = self.delayfunc
        timefunc = self.timefunc
        pop = heapq.heappop
        while q:
            time, priority, action, argument = checked_event = q[0]
            now = timefunc()
            if now < time:
                delayfunc(time - now)
            else:
                event = pop(q)
                if event is checked_event:
                    action(*argument)
                    delayfunc(0)
                else:
                    heapq.heappush(q, event)

    @property
    def queue(self):
        """An ordered list of upcoming events.
        
        Events are named tuples with fields for:
            time, priority, action, arguments
        
        """
        events = self._queue[:]
        return map(heapq.heappop, [events] * len(events))