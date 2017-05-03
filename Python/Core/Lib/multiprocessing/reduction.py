# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: reduction.py
__all__ = []
import os
import sys
import socket
import threading
import _multiprocessing
from multiprocessing import current_process
from multiprocessing.forking import Popen, duplicate, close, ForkingPickler
from multiprocessing.util import register_after_fork, debug, sub_debug
from multiprocessing.connection import Client, Listener
if not (sys.platform == 'win32' or hasattr(_multiprocessing, 'recvfd')):
    raise ImportError('pickling of connections not supported')
if sys.platform == 'win32':
    import _subprocess
    from _multiprocessing import win32

    def send_handle(conn, handle, destination_pid):
        process_handle = win32.OpenProcess(win32.PROCESS_ALL_ACCESS, False, destination_pid)
        try:
            new_handle = duplicate(handle, process_handle)
            conn.send(new_handle)
        finally:
            close(process_handle)


    def recv_handle(conn):
        return conn.recv()


else:

    def send_handle(conn, handle, destination_pid):
        _multiprocessing.sendfd(conn.fileno(), handle)


    def recv_handle(conn):
        return _multiprocessing.recvfd(conn.fileno())


_cache = set()

def _reset(obj):
    global _cache
    global _listener
    global _lock
    for h in _cache:
        close(h)

    _cache.clear()
    _lock = threading.Lock()
    _listener = None
    return


_reset(None)
register_after_fork(_reset, _reset)

def _get_listener():
    global _listener
    if _listener is None:
        _lock.acquire()
        try:
            if _listener is None:
                debug('starting listener and thread for sending handles')
                _listener = Listener(authkey=current_process().authkey)
                t = threading.Thread(target=_serve)
                t.daemon = True
                t.start()
        finally:
            _lock.release()

    return _listener


def _serve():
    from .util import is_exiting, sub_warning
    while 1:
        try:
            conn = _listener.accept()
            handle_wanted, destination_pid = conn.recv()
            _cache.remove(handle_wanted)
            send_handle(conn, handle_wanted, destination_pid)
            close(handle_wanted)
            conn.close()
        except:
            if not is_exiting():
                import traceback
                sub_warning('thread for sharing handles raised exception :\n' + '-' * 79 + '\n' + traceback.format_exc() + '-' * 79)


def reduce_handle(handle):
    if Popen.thread_is_spawning():
        return (None, Popen.duplicate_for_child(handle), True)
    else:
        dup_handle = duplicate(handle)
        _cache.add(dup_handle)
        sub_debug('reducing handle %d', handle)
        return (
         _get_listener().address, dup_handle, False)


def rebuild_handle(pickled_data):
    address, handle, inherited = pickled_data
    if inherited:
        return handle
    sub_debug('rebuilding handle %d', handle)
    conn = Client(address, authkey=current_process().authkey)
    conn.send((handle, os.getpid()))
    new_handle = recv_handle(conn)
    conn.close()
    return new_handle


def reduce_connection(conn):
    rh = reduce_handle(conn.fileno())
    return (
     rebuild_connection, (rh, conn.readable, conn.writable))


def rebuild_connection(reduced_handle, readable, writable):
    handle = rebuild_handle(reduced_handle)
    return _multiprocessing.Connection(handle, readable=readable, writable=writable)


ForkingPickler.register(_multiprocessing.Connection, reduce_connection)

def fromfd(fd, family, type_, proto=0):
    s = socket.fromfd(fd, family, type_, proto)
    if s.__class__ is not socket.socket:
        s = socket.socket(_sock=s)
    return s


def reduce_socket(s):
    reduced_handle = reduce_handle(s.fileno())
    return (
     rebuild_socket, (reduced_handle, s.family, s.type, s.proto))


def rebuild_socket(reduced_handle, family, type_, proto):
    fd = rebuild_handle(reduced_handle)
    _sock = fromfd(fd, family, type_, proto)
    close(fd)
    return _sock


ForkingPickler.register(socket.socket, reduce_socket)
if sys.platform == 'win32':

    def reduce_pipe_connection(conn):
        rh = reduce_handle(conn.fileno())
        return (
         rebuild_pipe_connection, (rh, conn.readable, conn.writable))


    def rebuild_pipe_connection(reduced_handle, readable, writable):
        handle = rebuild_handle(reduced_handle)
        return _multiprocessing.PipeConnection(handle, readable=readable, writable=writable)


    ForkingPickler.register(_multiprocessing.PipeConnection, reduce_pipe_connection)