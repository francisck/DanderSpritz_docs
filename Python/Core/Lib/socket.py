# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: socket.py
"""This module provides socket operations and some related functions.
On Unix, it supports IP (Internet Protocol) and Unix domain sockets.
On other systems, it only supports IP. Functions specific for a
socket are available as methods of the socket object.

Functions:

socket() -- create a new socket object
socketpair() -- create a pair of new socket objects [*]
fromfd() -- create a socket object from an open file descriptor [*]
gethostname() -- return the current hostname
gethostbyname() -- map a hostname to its IP number
gethostbyaddr() -- map an IP number or hostname to DNS info
getservbyname() -- map a service name and a protocol name to a port number
getprotobyname() -- map a protocol name (e.g. 'tcp') to a number
ntohs(), ntohl() -- convert 16, 32 bit int from network to host byte order
htons(), htonl() -- convert 16, 32 bit int from host to network byte order
inet_aton() -- convert IP addr string (123.45.67.89) to 32-bit packed format
inet_ntoa() -- convert 32-bit packed format IP to string (123.45.67.89)
ssl() -- secure socket layer support (only available if configured)
socket.getdefaulttimeout() -- get the default timeout value
socket.setdefaulttimeout() -- set the default timeout value
create_connection() -- connects to an address, with an optional timeout and
                       optional source address.

 [*] not available on all platforms!

Special objects:

SocketType -- type object for socket objects
error -- exception raised for I/O errors
has_ipv6 -- boolean value indicating if IPv6 is supported

Integer constants:

AF_INET, AF_UNIX -- socket domains (first argument to socket() call)
SOCK_STREAM, SOCK_DGRAM, SOCK_RAW -- socket types (second argument)

Many other constants may be defined; these may be used in calls to
the setsockopt() and getsockopt() methods.
"""
import _socket
from _socket import *
from functools import partial
from types import MethodType
try:
    import _ssl
except ImportError:
    pass
else:

    def ssl(sock, keyfile=None, certfile=None):
        import ssl as _realssl
        warnings.warn('socket.ssl() is deprecated.  Use ssl.wrap_socket() instead.', DeprecationWarning, stacklevel=2)
        return _realssl.sslwrap_simple(sock, keyfile, certfile)


    from _ssl import SSLError as sslerror
    from _ssl import RAND_add, RAND_egd, RAND_status, SSL_ERROR_ZERO_RETURN, SSL_ERROR_WANT_READ, SSL_ERROR_WANT_WRITE, SSL_ERROR_WANT_X509_LOOKUP, SSL_ERROR_SYSCALL, SSL_ERROR_SSL, SSL_ERROR_WANT_CONNECT, SSL_ERROR_EOF, SSL_ERROR_INVALID_ERROR_CODE

import os
import sys
import warnings
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

try:
    import errno
except ImportError:
    errno = None

EBADF = getattr(errno, 'EBADF', 9)
EINTR = getattr(errno, 'EINTR', 4)
__all__ = [
 'getfqdn', 'create_connection']
__all__.extend(os._get_exports_list(_socket))
_realsocket = socket
if sys.platform.lower().startswith('win'):
    errorTab = {}
    errorTab[10004] = 'The operation was interrupted.'
    errorTab[10009] = 'A bad file handle was passed.'
    errorTab[10013] = 'Permission denied.'
    errorTab[10014] = 'A fault occurred on the network??'
    errorTab[10022] = 'An invalid operation was attempted.'
    errorTab[10035] = 'The socket operation would block'
    errorTab[10036] = 'A blocking operation is already in progress.'
    errorTab[10048] = 'The network address is in use.'
    errorTab[10054] = 'The connection has been reset.'
    errorTab[10058] = 'The network has been shut down.'
    errorTab[10060] = 'The operation timed out.'
    errorTab[10061] = 'Connection refused.'
    errorTab[10063] = 'The name is too long.'
    errorTab[10064] = 'The host is down.'
    errorTab[10065] = 'The host is unreachable.'
    __all__.append('errorTab')

def getfqdn(name=''):
    """Get fully qualified domain name from name.
    
    An empty argument is interpreted as meaning the local host.
    
    First the hostname returned by gethostbyaddr() is checked, then
    possibly existing aliases. In case no FQDN is available, hostname
    from gethostname() is returned.
    """
    name = name.strip()
    if not name or name == '0.0.0.0':
        name = gethostname()
    try:
        hostname, aliases, ipaddrs = gethostbyaddr(name)
    except error:
        pass
    else:
        aliases.insert(0, hostname)
        for name in aliases:
            if '.' in name:
                break
        else:
            name = hostname

    return name


_socketmethods = (
 'bind', 'connect', 'connect_ex', 'fileno', 'listen',
 'getpeername', 'getsockname', 'getsockopt', 'setsockopt',
 'sendall', 'setblocking',
 'settimeout', 'gettimeout', 'shutdown')
if os.name == 'nt':
    _socketmethods = _socketmethods + ('ioctl',)
if sys.platform == 'riscos':
    _socketmethods = _socketmethods + ('sleeptaskw',)
_delegate_methods = (
 'recv', 'recvfrom', 'recv_into', 'recvfrom_into',
 'send', 'sendto')

class _closedsocket(object):
    __slots__ = []

    def _dummy(*args):
        raise error(EBADF, 'Bad file descriptor')

    send = recv = recv_into = sendto = recvfrom = recvfrom_into = _dummy
    __getattr__ = _dummy


class _socketobject(object):
    """_sock"""
    __slots__ = [
     '_sock', '__weakref__'] + list(_delegate_methods)

    def __init__(self, family=AF_INET, type=SOCK_STREAM, proto=0, _sock=None):
        if _sock is None:
            _sock = _realsocket(family, type, proto)
        self._sock = _sock
        for method in _delegate_methods:
            setattr(self, method, getattr(_sock, method))

        return

    def close(self, _closedsocket=_closedsocket, _delegate_methods=_delegate_methods, setattr=setattr):
        self._sock = _closedsocket()
        dummy = self._sock._dummy
        for method in _delegate_methods:
            setattr(self, method, dummy)

    close.__doc__ = _realsocket.close.__doc__

    def accept(self):
        sock, addr = self._sock.accept()
        return (
         _socketobject(_sock=sock), addr)

    accept.__doc__ = _realsocket.accept.__doc__

    def dup(self):
        """dup() -> socket object
        
        Return a new socket object connected to the same system resource."""
        return _socketobject(_sock=self._sock)

    def makefile(self, mode='r', bufsize=-1):
        """makefile([mode[, bufsize]]) -> file object
        
        Return a regular file object corresponding to the socket.  The mode
        and bufsize arguments are as for the built-in open() function."""
        return _fileobject(self._sock, mode, bufsize)

    family = property(lambda self: self._sock.family, doc='the socket family')
    type = property(lambda self: self._sock.type, doc='the socket type')
    proto = property(lambda self: self._sock.proto, doc='the socket protocol')


def meth(name, self, *args):
    return getattr(self._sock, name)(*args)


for _m in _socketmethods:
    p = partial(meth, _m)
    p.__name__ = _m
    p.__doc__ = getattr(_realsocket, _m).__doc__
    m = MethodType(p, None, _socketobject)
    setattr(_socketobject, _m, m)

socket = SocketType = _socketobject

class _fileobject(object):
    """Faux file object attached to a socket object."""
    default_bufsize = 8192
    name = '<socket>'
    __slots__ = [
     'mode', 'bufsize', 'softspace',
     '_sock', '_rbufsize', '_wbufsize', '_rbuf', '_wbuf', '_wbuf_len',
     '_close']

    def __init__(self, sock, mode='rb', bufsize=-1, close=False):
        self._sock = sock
        self.mode = mode
        if bufsize < 0:
            bufsize = self.default_bufsize
        self.bufsize = bufsize
        self.softspace = False
        if bufsize == 0:
            self._rbufsize = 1
        elif bufsize == 1:
            self._rbufsize = self.default_bufsize
        else:
            self._rbufsize = bufsize
        self._wbufsize = bufsize
        self._rbuf = StringIO()
        self._wbuf = []
        self._wbuf_len = 0
        self._close = close

    def _getclosed(self):
        return self._sock is None

    closed = property(_getclosed, doc='True if the file is closed')

    def close(self):
        try:
            if self._sock:
                self.flush()
        finally:
            if self._close:
                self._sock.close()
            self._sock = None

        return

    def __del__(self):
        try:
            self.close()
        except:
            pass

    def flush(self):
        if self._wbuf:
            data = ''.join(self._wbuf)
            self._wbuf = []
            self._wbuf_len = 0
            buffer_size = max(self._rbufsize, self.default_bufsize)
            data_size = len(data)
            write_offset = 0
            view = memoryview(data)
            try:
                while write_offset < data_size:
                    self._sock.sendall(view[write_offset:write_offset + buffer_size])
                    write_offset += buffer_size

            finally:
                if write_offset < data_size:
                    remainder = data[write_offset:]
                    del view
                    del data
                    self._wbuf.append(remainder)
                    self._wbuf_len = len(remainder)

    def fileno(self):
        return self._sock.fileno()

    def write(self, data):
        data = str(data)
        if not data:
            return
        self._wbuf.append(data)
        self._wbuf_len += len(data)
        if self._wbufsize == 0 or self._wbufsize == 1 and '\n' in data or self._wbuf_len >= self._wbufsize:
            self.flush()

    def writelines(self, list):
        lines = filter(None, map(str, list))
        self._wbuf_len += sum(map(len, lines))
        self._wbuf.extend(lines)
        if self._wbufsize <= 1 or self._wbuf_len >= self._wbufsize:
            self.flush()
        return

    def read(self, size=-1):
        rbufsize = max(self._rbufsize, self.default_bufsize)
        buf = self._rbuf
        buf.seek(0, 2)
        if size < 0:
            self._rbuf = StringIO()
            while True:
                try:
                    data = self._sock.recv(rbufsize)
                except error as e:
                    if e.args[0] == EINTR:
                        continue
                    raise

                if not data:
                    break
                buf.write(data)

            return buf.getvalue()
        else:
            buf_len = buf.tell()
            if buf_len >= size:
                buf.seek(0)
                rv = buf.read(size)
                self._rbuf = StringIO()
                self._rbuf.write(buf.read())
                return rv
            self._rbuf = StringIO()
            while True:
                left = size - buf_len
                try:
                    data = self._sock.recv(left)
                except error as e:
                    if e.args[0] == EINTR:
                        continue
                    raise

                if not data:
                    break
                n = len(data)
                if n == size and not buf_len:
                    return data
                if n == left:
                    buf.write(data)
                    del data
                    break
                buf.write(data)
                buf_len += n
                del data

            return buf.getvalue()

    def readline(self, size=-1):
        buf = self._rbuf
        buf.seek(0, 2)
        if buf.tell() > 0:
            buf.seek(0)
            bline = buf.readline(size)
            if bline.endswith('\n') or len(bline) == size:
                self._rbuf = StringIO()
                self._rbuf.write(buf.read())
                return bline
            del bline
        if size < 0:
            if self._rbufsize <= 1:
                buf.seek(0)
                buffers = [buf.read()]
                self._rbuf = StringIO()
                data = None
                recv = self._sock.recv
                while True:
                    try:
                        while data != '\n':
                            data = recv(1)
                            if not data:
                                break
                            buffers.append(data)

                    except error as e:
                        if e.args[0] == EINTR:
                            continue
                        raise

                    break

                return ''.join(buffers)
            buf.seek(0, 2)
            self._rbuf = StringIO()
            while True:
                try:
                    data = self._sock.recv(self._rbufsize)
                except error as e:
                    if e.args[0] == EINTR:
                        continue
                    raise

                if not data:
                    break
                nl = data.find('\n')
                if nl >= 0:
                    nl += 1
                    buf.write(data[:nl])
                    self._rbuf.write(data[nl:])
                    del data
                    break
                buf.write(data)

            return buf.getvalue()
        else:
            buf.seek(0, 2)
            buf_len = buf.tell()
            if buf_len >= size:
                buf.seek(0)
                rv = buf.read(size)
                self._rbuf = StringIO()
                self._rbuf.write(buf.read())
                return rv
            self._rbuf = StringIO()
            while True:
                try:
                    data = self._sock.recv(self._rbufsize)
                except error as e:
                    if e.args[0] == EINTR:
                        continue
                    raise

                if not data:
                    break
                left = size - buf_len
                nl = data.find('\n', 0, left)
                if nl >= 0:
                    nl += 1
                    self._rbuf.write(data[nl:])
                    if buf_len:
                        buf.write(data[:nl])
                        break
                    else:
                        return data[:nl]
                n = len(data)
                if n == size and not buf_len:
                    return data
                if n >= left:
                    buf.write(data[:left])
                    self._rbuf.write(data[left:])
                    break
                buf.write(data)
                buf_len += n

            return buf.getvalue()
            return

    def readlines(self, sizehint=0):
        total = 0
        list = []
        while True:
            line = self.readline()
            if not line:
                break
            list.append(line)
            total += len(line)
            if sizehint and total >= sizehint:
                break

        return list

    def __iter__(self):
        return self

    def next(self):
        line = self.readline()
        if not line:
            raise StopIteration
        return line


_GLOBAL_DEFAULT_TIMEOUT = object()

def create_connection(address, timeout=_GLOBAL_DEFAULT_TIMEOUT, source_address=None):
    """Connect to *address* and return the socket object.
    
    Convenience function.  Connect to *address* (a 2-tuple ``(host,
    port)``) and return the socket object.  Passing the optional
    *timeout* parameter will set the timeout on the socket instance
    before attempting to connect.  If no *timeout* is supplied, the
    global default timeout setting returned by :func:`getdefaulttimeout`
    is used.  If *source_address* is set it must be a tuple of (host, port)
    for the socket to bind as a source address before making the connection.
    An host of '' or port 0 tells the OS to use the default.
    """
    host, port = address
    err = None
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        sock = None
        try:
            sock = socket(af, socktype, proto)
            if timeout is not _GLOBAL_DEFAULT_TIMEOUT:
                sock.settimeout(timeout)
            if source_address:
                sock.bind(source_address)
            sock.connect(sa)
            return sock
        except error as _:
            err = _
            if sock is not None:
                sock.close()

    if err is not None:
        raise err
    else:
        raise error('getaddrinfo returns an empty list')
    return