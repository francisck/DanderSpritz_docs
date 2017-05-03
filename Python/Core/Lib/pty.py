# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: pty.py
"""Pseudo terminal utilities."""
from select import select
import os
import tty
__all__ = [
 'openpty', 'fork', 'spawn']
STDIN_FILENO = 0
STDOUT_FILENO = 1
STDERR_FILENO = 2
CHILD = 0

def openpty():
    """openpty() -> (master_fd, slave_fd)
    Open a pty master/slave pair, using os.openpty() if possible."""
    try:
        return os.openpty()
    except (AttributeError, OSError):
        pass

    master_fd, slave_name = _open_terminal()
    slave_fd = slave_open(slave_name)
    return (
     master_fd, slave_fd)


def master_open():
    """master_open() -> (master_fd, slave_name)
    Open a pty master and return the fd, and the filename of the slave end.
    Deprecated, use openpty() instead."""
    try:
        master_fd, slave_fd = os.openpty()
    except (AttributeError, OSError):
        pass
    else:
        slave_name = os.ttyname(slave_fd)
        os.close(slave_fd)
        return (
         master_fd, slave_name)

    return _open_terminal()


def _open_terminal():
    """Open pty master and return (master_fd, tty_name).
    SGI and generic BSD version, for when openpty() fails."""
    try:
        import sgi
    except ImportError:
        pass
    else:
        try:
            tty_name, master_fd = sgi._getpty(os.O_RDWR, 438, 0)
        except IOError as msg:
            raise os.error, msg

        return (master_fd, tty_name)

    for x in 'pqrstuvwxyzPQRST':
        for y in '0123456789abcdef':
            pty_name = '/dev/pty' + x + y
            try:
                fd = os.open(pty_name, os.O_RDWR)
            except os.error:
                continue

            return (
             fd, '/dev/tty' + x + y)

    raise os.error, 'out of pty devices'


def slave_open(tty_name):
    """slave_open(tty_name) -> slave_fd
    Open the pty slave and acquire the controlling terminal, returning
    opened filedescriptor.
    Deprecated, use openpty() instead."""
    result = os.open(tty_name, os.O_RDWR)
    try:
        from fcntl import ioctl, I_PUSH
    except ImportError:
        return result

    try:
        ioctl(result, I_PUSH, 'ptem')
        ioctl(result, I_PUSH, 'ldterm')
    except IOError:
        pass

    return result


def fork():
    """fork() -> (pid, master_fd)
    Fork and make the child a session leader with a controlling terminal."""
    try:
        pid, fd = os.forkpty()
    except (AttributeError, OSError):
        pass
    else:
        if pid == CHILD:
            try:
                os.setsid()
            except OSError:
                pass

        return (pid, fd)

    master_fd, slave_fd = openpty()
    pid = os.fork()
    if pid == CHILD:
        os.setsid()
        os.close(master_fd)
        os.dup2(slave_fd, STDIN_FILENO)
        os.dup2(slave_fd, STDOUT_FILENO)
        os.dup2(slave_fd, STDERR_FILENO)
        if slave_fd > STDERR_FILENO:
            os.close(slave_fd)
        tmp_fd = os.open(os.ttyname(STDOUT_FILENO), os.O_RDWR)
        os.close(tmp_fd)
    else:
        os.close(slave_fd)
    return (
     pid, master_fd)


def _writen(fd, data):
    """Write all the data to a descriptor."""
    while data != '':
        n = os.write(fd, data)
        data = data[n:]


def _read(fd):
    """Default read function."""
    return os.read(fd, 1024)


def _copy(master_fd, master_read=_read, stdin_read=_read):
    """Parent copy loop.
    Copies
            pty master -> standard output   (master_read)
            standard input -> pty master    (stdin_read)"""
    while 1:
        rfds, wfds, xfds = select([
         master_fd, STDIN_FILENO], [], [])
        if master_fd in rfds:
            data = master_read(master_fd)
            os.write(STDOUT_FILENO, data)
        if STDIN_FILENO in rfds:
            data = stdin_read(STDIN_FILENO)
            _writen(master_fd, data)


def spawn(argv, master_read=_read, stdin_read=_read):
    """Create a spawned process."""
    if type(argv) == type(''):
        argv = (
         argv,)
    pid, master_fd = fork()
    if pid == CHILD:
        os.execlp(argv[0], *argv)
    try:
        mode = tty.tcgetattr(STDIN_FILENO)
        tty.setraw(STDIN_FILENO)
        restore = 1
    except tty.error:
        restore = 0

    try:
        _copy(master_fd, master_read, stdin_read)
    except (IOError, OSError):
        if restore:
            tty.tcsetattr(STDIN_FILENO, tty.TCSAFLUSH, mode)

    os.close(master_fd)