# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: heap.py
import bisect
import mmap
import tempfile
import os
import sys
import threading
import itertools
import _multiprocessing
from multiprocessing.util import Finalize, info
from multiprocessing.forking import assert_spawning
__all__ = [
 'BufferWrapper']
if sys.platform == 'win32':
    from _multiprocessing import win32

    class Arena(object):
        _counter = itertools.count()

        def __init__(self, size):
            self.size = size
            self.name = 'pym-%d-%d' % (os.getpid(), Arena._counter.next())
            self.buffer = mmap.mmap(-1, self.size, tagname=self.name)
            self._state = (
             self.size, self.name)

        def __getstate__(self):
            assert_spawning(self)
            return self._state

        def __setstate__(self, state):
            self.size, self.name = self._state = state
            self.buffer = mmap.mmap(-1, self.size, tagname=self.name)


else:

    class Arena(object):

        def __init__(self, size):
            self.buffer = mmap.mmap(-1, size)
            self.size = size
            self.name = None
            return


class Heap(object):
    _alignment = 8

    def __init__(self, size=mmap.PAGESIZE):
        self._lastpid = os.getpid()
        self._lock = threading.Lock()
        self._size = size
        self._lengths = []
        self._len_to_seq = {}
        self._start_to_block = {}
        self._stop_to_block = {}
        self._allocated_blocks = set()
        self._arenas = []

    @staticmethod
    def _roundup(n, alignment):
        mask = alignment - 1
        return n + mask & ~mask

    def _malloc(self, size):
        i = bisect.bisect_left(self._lengths, size)
        if i == len(self._lengths):
            length = self._roundup(max(self._size, size), mmap.PAGESIZE)
            self._size *= 2
            info('allocating a new mmap of length %d', length)
            arena = Arena(length)
            self._arenas.append(arena)
            return (
             arena, 0, length)
        length = self._lengths[i]
        seq = self._len_to_seq[length]
        block = seq.pop()
        if not seq:
            del self._len_to_seq[length]
            del self._lengths[i]
        arena, start, stop = block
        del self._start_to_block[arena, start]
        del self._stop_to_block[arena, stop]
        return block

    def _free(self, block):
        arena, start, stop = block
        try:
            prev_block = self._stop_to_block[arena, start]
        except KeyError:
            pass
        else:
            start, _ = self._absorb(prev_block)

        try:
            next_block = self._start_to_block[arena, stop]
        except KeyError:
            pass
        else:
            _, stop = self._absorb(next_block)

        block = (arena, start, stop)
        length = stop - start
        try:
            self._len_to_seq[length].append(block)
        except KeyError:
            self._len_to_seq[length] = [
             block]
            bisect.insort(self._lengths, length)

        self._start_to_block[arena, start] = block
        self._stop_to_block[arena, stop] = block

    def _absorb(self, block):
        arena, start, stop = block
        del self._start_to_block[arena, start]
        del self._stop_to_block[arena, stop]
        length = stop - start
        seq = self._len_to_seq[length]
        seq.remove(block)
        if not seq:
            del self._len_to_seq[length]
            self._lengths.remove(length)
        return (
         start, stop)

    def free(self, block):
        self._lock.acquire()
        try:
            self._allocated_blocks.remove(block)
            self._free(block)
        finally:
            self._lock.release()

    def malloc(self, size):
        if os.getpid() != self._lastpid:
            self.__init__()
        self._lock.acquire()
        try:
            size = self._roundup(max(size, 1), self._alignment)
            arena, start, stop = self._malloc(size)
            new_stop = start + size
            if new_stop < stop:
                self._free((arena, new_stop, stop))
            block = (
             arena, start, new_stop)
            self._allocated_blocks.add(block)
            return block
        finally:
            self._lock.release()


class BufferWrapper(object):
    _heap = Heap()

    def __init__(self, size):
        block = BufferWrapper._heap.malloc(size)
        self._state = (block, size)
        Finalize(self, BufferWrapper._heap.free, args=(block,))

    def get_address(self):
        (arena, start, stop), size = self._state
        address, length = _multiprocessing.address_of_buffer(arena.buffer)
        return address + start

    def get_size(self):
        return self._state[1]