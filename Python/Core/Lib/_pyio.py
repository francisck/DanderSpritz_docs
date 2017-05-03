# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _pyio.py
u"""
Python implementation of the io module.
"""
from __future__ import print_function, unicode_literals
import os
import abc
import codecs
import warnings
try:
    from thread import allocate_lock as Lock
except ImportError:
    from dummy_thread import allocate_lock as Lock

import io
from io import __all__, SEEK_SET, SEEK_CUR, SEEK_END
from errno import EINTR
__metaclass__ = type
DEFAULT_BUFFER_SIZE = 8 * 1024

class BlockingIOError(IOError):
    u"""Exception raised when I/O would block on a non-blocking I/O stream."""

    def __init__(self, errno, strerror, characters_written=0):
        super(IOError, self).__init__(errno, strerror)
        if not isinstance(characters_written, (int, long)):
            raise TypeError(u'characters_written must be a integer')
        self.characters_written = characters_written


def open(file, mode=u'r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True):
    ur"""Open file and return a stream.  Raise IOError upon failure.
    
    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)
    
    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), and 'a' for appending (which on some Unix systems,
    means that all writes append to the end of the file regardless of the
    current seek position). In text mode, if encoding is not specified the
    encoding used is platform dependent. (For reading and writing raw
    bytes use binary mode and leave encoding unspecified.) The available
    modes are:
    
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (for backwards compatibility; unneeded
              for new code)
    ========= ===============================================================
    
    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation.
    
    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.
    
    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:
    
    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.
    
    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.
    
    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.
    
    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register for a list of the permitted
    encoding error strings.
    
    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:
    
    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.
    
    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '', no translation takes place. If newline is any of the
      other legal values, any '\n' characters written are translated to
      the given string.
    
    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.
    
    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.
    
    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.
    """
    if not isinstance(file, (basestring, int, long)):
        raise TypeError(u'invalid file: %r' % file)
    if not isinstance(mode, basestring):
        raise TypeError(u'invalid mode: %r' % mode)
    if not isinstance(buffering, (int, long)):
        raise TypeError(u'invalid buffering: %r' % buffering)
    if encoding is not None and not isinstance(encoding, basestring):
        raise TypeError(u'invalid encoding: %r' % encoding)
    if errors is not None and not isinstance(errors, basestring):
        raise TypeError(u'invalid errors: %r' % errors)
    modes = set(mode)
    if modes - set(u'arwb+tU') or len(mode) > len(modes):
        raise ValueError(u'invalid mode: %r' % mode)
    reading = u'r' in modes
    writing = u'w' in modes
    appending = u'a' in modes
    updating = u'+' in modes
    text = u't' in modes
    binary = u'b' in modes
    if u'U' in modes:
        if writing or appending:
            raise ValueError(u"can't use U and writing mode at once")
        reading = True
    if text and binary:
        raise ValueError(u"can't have text and binary mode at once")
    if reading + writing + appending > 1:
        raise ValueError(u"can't have read/write/append mode at once")
    if not (reading or writing or appending):
        raise ValueError(u'must have exactly one of read/write/append mode')
    if binary and encoding is not None:
        raise ValueError(u"binary mode doesn't take an encoding argument")
    if binary and errors is not None:
        raise ValueError(u"binary mode doesn't take an errors argument")
    if binary and newline is not None:
        raise ValueError(u"binary mode doesn't take a newline argument")
    raw = FileIO(file, (reading and u'r' or u'') + (writing and u'w' or u'') + (appending and u'a' or u'') + (updating and u'+' or u''), closefd)
    line_buffering = False
    if buffering == 1 or buffering < 0 and raw.isatty():
        buffering = -1
        line_buffering = True
    if buffering < 0:
        buffering = DEFAULT_BUFFER_SIZE
        try:
            bs = os.fstat(raw.fileno()).st_blksize
        except (os.error, AttributeError):
            pass
        else:
            if bs > 1:
                buffering = bs
    if buffering < 0:
        raise ValueError(u'invalid buffering size')
    if buffering == 0:
        if binary:
            return raw
        raise ValueError(u"can't have unbuffered text I/O")
    if updating:
        buffer = BufferedRandom(raw, buffering)
    elif writing or appending:
        buffer = BufferedWriter(raw, buffering)
    elif reading:
        buffer = BufferedReader(raw, buffering)
    else:
        raise ValueError(u'unknown mode: %r' % mode)
    if binary:
        return buffer
    else:
        text = TextIOWrapper(buffer, encoding, errors, newline, line_buffering)
        text.mode = mode
        return text


class DocDescriptor():
    u"""Helper for builtins.open.__doc__
    """

    def __get__(self, obj, typ):
        return u"open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True)\n\n" + open.__doc__


class OpenWrapper():
    u"""Wrapper for builtins.open
    
    Trick so that open won't become a bound method when stored
    as a class variable (as dbm.dumb does).
    
    See initstdio() in Python/pythonrun.c.
    """
    __doc__ = DocDescriptor()

    def __new__(cls, *args, **kwargs):
        return open(*args, **kwargs)


class UnsupportedOperation(ValueError, IOError):
    pass


class IOBase():
    __metaclass__ = abc.ABCMeta

    def _unsupported(self, name):
        u"""Internal: raise an exception for unsupported operations."""
        raise UnsupportedOperation(u'%s.%s() not supported' % (
         self.__class__.__name__, name))

    def seek(self, pos, whence=0):
        u"""Change stream position.
        
        Change the stream position to byte offset offset. offset is
        interpreted relative to the position indicated by whence.  Values
        for whence are:
        
        * 0 -- start of stream (the default); offset should be zero or positive
        * 1 -- current stream position; offset may be negative
        * 2 -- end of stream; offset is usually negative
        
        Return the new absolute position.
        """
        self._unsupported(u'seek')

    def tell(self):
        u"""Return current stream position."""
        return self.seek(0, 1)

    def truncate(self, pos=None):
        u"""Truncate file to size bytes.
        
        Size defaults to the current IO position as reported by tell().  Return
        the new size.
        """
        self._unsupported(u'truncate')

    def flush(self):
        u"""Flush write buffers, if applicable.
        
        This is not implemented for read-only and non-blocking streams.
        """
        self._checkClosed()

    __closed = False

    def close(self):
        u"""Flush and close the IO object.
        
        This method has no effect if the file is already closed.
        """
        if not self.__closed:
            self.flush()
            self.__closed = True

    def __del__(self):
        u"""Destructor.  Calls close()."""
        try:
            self.close()
        except:
            pass

    def seekable(self):
        u"""Return whether object supports random access.
        
        If False, seek(), tell() and truncate() will raise IOError.
        This method may need to do a test seek().
        """
        return False

    def _checkSeekable(self, msg=None):
        u"""Internal: raise an IOError if file is not seekable
        """
        if not self.seekable():
            raise IOError(u'File or stream is not seekable.' if msg is None else msg)
        return

    def readable(self):
        u"""Return whether object was opened for reading.
        
        If False, read() will raise IOError.
        """
        return False

    def _checkReadable(self, msg=None):
        u"""Internal: raise an IOError if file is not readable
        """
        if not self.readable():
            raise IOError(u'File or stream is not readable.' if msg is None else msg)
        return

    def writable(self):
        u"""Return whether object was opened for writing.
        
        If False, write() and truncate() will raise IOError.
        """
        return False

    def _checkWritable(self, msg=None):
        u"""Internal: raise an IOError if file is not writable
        """
        if not self.writable():
            raise IOError(u'File or stream is not writable.' if msg is None else msg)
        return

    @property
    def closed(self):
        u"""closed: bool.  True iff the file has been closed.
        
        For backwards compatibility, this is a property, not a predicate.
        """
        return self.__closed

    def _checkClosed(self, msg=None):
        u"""Internal: raise an ValueError if file is closed
        """
        if self.closed:
            raise ValueError(u'I/O operation on closed file.' if msg is None else msg)
        return

    def __enter__(self):
        u"""Context management protocol.  Returns self."""
        self._checkClosed()
        return self

    def __exit__(self, *args):
        u"""Context management protocol.  Calls close()"""
        self.close()

    def fileno(self):
        u"""Returns underlying file descriptor if one exists.
        
        An IOError is raised if the IO object does not use a file descriptor.
        """
        self._unsupported(u'fileno')

    def isatty(self):
        u"""Return whether this is an 'interactive' stream.
        
        Return False if it can't be determined.
        """
        self._checkClosed()
        return False

    def readline(self, limit=-1):
        ur"""Read and return a line from the stream.
        
        If limit is specified, at most limit bytes will be read.
        
        The line terminator is always b'\n' for binary files; for text
        files, the newlines argument to open can be used to select the line
        terminator(s) recognized.
        """
        if hasattr(self, u'peek'):

            def nreadahead():
                readahead = self.peek(1)
                if not readahead:
                    return 1
                n = readahead.find('\n') + 1 or len(readahead)
                if limit >= 0:
                    n = min(n, limit)
                return n

        else:

            def nreadahead():
                return 1

        if limit is None:
            limit = -1
        else:
            if not isinstance(limit, (int, long)):
                raise TypeError(u'limit must be an integer')
            res = bytearray()
            while limit < 0 or len(res) < limit:
                b = self.read(nreadahead())
                if not b:
                    break
                res += b
                if res.endswith('\n'):
                    break

        return bytes(res)

    def __iter__(self):
        self._checkClosed()
        return self

    def next(self):
        line = self.readline()
        if not line:
            raise StopIteration
        return line

    def readlines(self, hint=None):
        u"""Return a list of lines from the stream.
        
        hint can be specified to control the number of lines read: no more
        lines will be read if the total size (in bytes/characters) of all
        lines so far exceeds hint.
        """
        if hint is not None and not isinstance(hint, (int, long)):
            raise TypeError(u'integer or None expected')
        if hint is None or hint <= 0:
            return list(self)
        else:
            n = 0
            lines = []
            for line in self:
                lines.append(line)
                n += len(line)
                if n >= hint:
                    break

            return lines

    def writelines(self, lines):
        self._checkClosed()
        for line in lines:
            self.write(line)


io.IOBase.register(IOBase)

class RawIOBase(IOBase):
    u"""Base class for raw binary I/O."""

    def read(self, n=-1):
        u"""Read and return up to n bytes.
        
        Returns an empty bytes object on EOF, or None if the object is
        set not to block and has no data to read.
        """
        if n is None:
            n = -1
        if n < 0:
            return self.readall()
        else:
            b = bytearray(n.__index__())
            n = self.readinto(b)
            if n is None:
                return
            del b[n:]
            return bytes(b)

    def readall(self):
        u"""Read until EOF, using multiple read() call."""
        res = bytearray()
        while True:
            data = self.read(DEFAULT_BUFFER_SIZE)
            if not data:
                break
            res += data

        if res:
            return bytes(res)
        else:
            return data

    def readinto(self, b):
        u"""Read up to len(b) bytes into b.
        
        Returns number of bytes read (0 for EOF), or None if the object
        is set not to block and has no data to read.
        """
        self._unsupported(u'readinto')

    def write(self, b):
        u"""Write the given buffer to the IO stream.
        
        Returns the number of bytes written, which may be less than len(b).
        """
        self._unsupported(u'write')


io.RawIOBase.register(RawIOBase)
from _io import FileIO
RawIOBase.register(FileIO)

class BufferedIOBase(IOBase):
    u"""Base class for buffered IO objects.
    
    The main difference with RawIOBase is that the read() method
    supports omitting the size argument, and does not have a default
    implementation that defers to readinto().
    
    In addition, read(), readinto() and write() may raise
    BlockingIOError if the underlying raw stream is in non-blocking
    mode and not ready; unlike their raw counterparts, they will never
    return None.
    
    A typical implementation should not inherit from a RawIOBase
    implementation, but wrap one.
    """

    def read(self, n=None):
        u"""Read and return up to n bytes.
        
        If the argument is omitted, None, or negative, reads and
        returns all data until EOF.
        
        If the argument is positive, and the underlying raw stream is
        not 'interactive', multiple raw reads may be issued to satisfy
        the byte count (unless EOF is reached first).  But for
        interactive raw streams (XXX and for pipes?), at most one raw
        read will be issued, and a short result does not imply that
        EOF is imminent.
        
        Returns an empty bytes array on EOF.
        
        Raises BlockingIOError if the underlying raw stream has no
        data at the moment.
        """
        self._unsupported(u'read')

    def read1(self, n=None):
        u"""Read up to n bytes with at most one read() system call."""
        self._unsupported(u'read1')

    def readinto(self, b):
        u"""Read up to len(b) bytes into b.
        
        Like read(), this may issue multiple reads to the underlying raw
        stream, unless the latter is 'interactive'.
        
        Returns the number of bytes read (0 for EOF).
        
        Raises BlockingIOError if the underlying raw stream has no
        data at the moment.
        """
        data = self.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)

        return n

    def write(self, b):
        u"""Write the given buffer to the IO stream.
        
        Return the number of bytes written, which is never less than
        len(b).
        
        Raises BlockingIOError if the buffer is full and the
        underlying raw stream cannot accept more data at the moment.
        """
        self._unsupported(u'write')

    def detach(self):
        u"""
        Separate the underlying raw stream from the buffer and return it.
        
        After the raw stream has been detached, the buffer is in an unusable
        state.
        """
        self._unsupported(u'detach')


io.BufferedIOBase.register(BufferedIOBase)

class _BufferedIOMixin(BufferedIOBase):
    u"""A mixin implementation of BufferedIOBase with an underlying raw stream.
    
    This passes most requests on to the underlying raw stream.  It
    does *not* provide implementations of read(), readinto() or
    write().
    """

    def __init__(self, raw):
        self._raw = raw

    def seek(self, pos, whence=0):
        new_position = self.raw.seek(pos, whence)
        if new_position < 0:
            raise IOError(u'seek() returned an invalid position')
        return new_position

    def tell(self):
        pos = self.raw.tell()
        if pos < 0:
            raise IOError(u'tell() returned an invalid position')
        return pos

    def truncate(self, pos=None):
        self.flush()
        if pos is None:
            pos = self.tell()
        return self.raw.truncate(pos)

    def flush(self):
        if self.closed:
            raise ValueError(u'flush of closed file')
        self.raw.flush()

    def close(self):
        if self.raw is not None and not self.closed:
            self.flush()
            self.raw.close()
        return

    def detach(self):
        if self.raw is None:
            raise ValueError(u'raw stream already detached')
        self.flush()
        raw = self._raw
        self._raw = None
        return raw

    def seekable(self):
        return self.raw.seekable()

    def readable(self):
        return self.raw.readable()

    def writable(self):
        return self.raw.writable()

    @property
    def raw(self):
        return self._raw

    @property
    def closed(self):
        return self.raw.closed

    @property
    def name(self):
        return self.raw.name

    @property
    def mode(self):
        return self.raw.mode

    def __repr__(self):
        clsname = self.__class__.__name__
        try:
            name = self.name
        except AttributeError:
            return u'<_pyio.{0}>'.format(clsname)

        return u'<_pyio.{0} name={1!r}>'.format(clsname, name)

    def fileno(self):
        return self.raw.fileno()

    def isatty(self):
        return self.raw.isatty()


class BytesIO(BufferedIOBase):
    u"""Buffered I/O implementation using an in-memory bytes buffer."""

    def __init__(self, initial_bytes=None):
        buf = bytearray()
        if initial_bytes is not None:
            buf.extend(initial_bytes)
        self._buffer = buf
        self._pos = 0
        return

    def __getstate__(self):
        if self.closed:
            raise ValueError(u'__getstate__ on closed file')
        return self.__dict__.copy()

    def getvalue(self):
        u"""Return the bytes value (contents) of the buffer
        """
        if self.closed:
            raise ValueError(u'getvalue on closed file')
        return bytes(self._buffer)

    def read(self, n=None):
        if self.closed:
            raise ValueError(u'read from closed file')
        if n is None:
            n = -1
        if not isinstance(n, (int, long)):
            raise TypeError(u'integer argument expected, got {0!r}'.format(type(n)))
        if n < 0:
            n = len(self._buffer)
        if len(self._buffer) <= self._pos:
            return ''
        else:
            newpos = min(len(self._buffer), self._pos + n)
            b = self._buffer[self._pos:newpos]
            self._pos = newpos
            return bytes(b)

    def read1(self, n):
        u"""This is the same as read.
        """
        return self.read(n)

    def write(self, b):
        if self.closed:
            raise ValueError(u'write to closed file')
        if isinstance(b, unicode):
            raise TypeError(u"can't write unicode to binary stream")
        n = len(b)
        if n == 0:
            return 0
        pos = self._pos
        if pos > len(self._buffer):
            padding = '\x00' * (pos - len(self._buffer))
            self._buffer += padding
        self._buffer[pos:pos + n] = b
        self._pos += n
        return n

    def seek(self, pos, whence=0):
        if self.closed:
            raise ValueError(u'seek on closed file')
        try:
            pos.__index__
        except AttributeError:
            raise TypeError(u'an integer is required')

        if whence == 0:
            if pos < 0:
                raise ValueError(u'negative seek position %r' % (pos,))
            self._pos = pos
        elif whence == 1:
            self._pos = max(0, self._pos + pos)
        elif whence == 2:
            self._pos = max(0, len(self._buffer) + pos)
        else:
            raise ValueError(u'invalid whence value')
        return self._pos

    def tell(self):
        if self.closed:
            raise ValueError(u'tell on closed file')
        return self._pos

    def truncate(self, pos=None):
        if self.closed:
            raise ValueError(u'truncate on closed file')
        if pos is None:
            pos = self._pos
        else:
            try:
                pos.__index__
            except AttributeError:
                raise TypeError(u'an integer is required')

            if pos < 0:
                raise ValueError(u'negative truncate position %r' % (pos,))
        del self._buffer[pos:]
        return pos

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True


class BufferedReader(_BufferedIOMixin):
    u"""BufferedReader(raw[, buffer_size])
    
    A buffer for a readable, sequential BaseRawIO object.
    
    The constructor creates a BufferedReader for the given readable raw
    stream and buffer_size. If buffer_size is omitted, DEFAULT_BUFFER_SIZE
    is used.
    """

    def __init__(self, raw, buffer_size=DEFAULT_BUFFER_SIZE):
        u"""Create a new buffered reader using the given readable raw IO object.
        """
        if not raw.readable():
            raise IOError(u'"raw" argument must be readable.')
        _BufferedIOMixin.__init__(self, raw)
        if buffer_size <= 0:
            raise ValueError(u'invalid buffer size')
        self.buffer_size = buffer_size
        self._reset_read_buf()
        self._read_lock = Lock()

    def _reset_read_buf(self):
        self._read_buf = ''
        self._read_pos = 0

    def read(self, n=None):
        u"""Read n bytes.
        
        Returns exactly n bytes of data unless the underlying raw IO
        stream reaches EOF or if the call would block in non-blocking
        mode. If n is negative, read until EOF or until read() would
        block.
        """
        if n is not None and n < -1:
            raise ValueError(u'invalid number of bytes to read')
        with self._read_lock:
            return self._read_unlocked(n)
        return

    def _read_unlocked(self, n=None):
        nodata_val = ''
        empty_values = ('', None)
        buf = self._read_buf
        pos = self._read_pos
        if n is None or n == -1:
            self._reset_read_buf()
            chunks = [buf[pos:]]
            current_size = 0
            while True:
                try:
                    chunk = self.raw.read()
                except IOError as e:
                    if e.errno != EINTR:
                        raise
                    continue

                if chunk in empty_values:
                    nodata_val = chunk
                    break
                current_size += len(chunk)
                chunks.append(chunk)

            return ''.join(chunks) or nodata_val
        else:
            avail = len(buf) - pos
            if n <= avail:
                self._read_pos += n
                return buf[pos:pos + n]
            chunks = [
             buf[pos:]]
            wanted = max(self.buffer_size, n)
            while avail < n:
                try:
                    chunk = self.raw.read(wanted)
                except IOError as e:
                    if e.errno != EINTR:
                        raise
                    continue

                if chunk in empty_values:
                    nodata_val = chunk
                    break
                avail += len(chunk)
                chunks.append(chunk)

            n = min(n, avail)
            out = ''.join(chunks)
            self._read_buf = out[n:]
            self._read_pos = 0
            if out:
                return out[:n]
            return nodata_val

    def peek(self, n=0):
        u"""Returns buffered bytes without advancing the position.
        
        The argument indicates a desired minimal number of bytes; we
        do at most one raw read to satisfy it.  We never return more
        than self.buffer_size.
        """
        with self._read_lock:
            return self._peek_unlocked(n)

    def _peek_unlocked(self, n=0):
        want = min(n, self.buffer_size)
        have = len(self._read_buf) - self._read_pos
        if have < want or have <= 0:
            to_read = self.buffer_size - have
            while True:
                try:
                    current = self.raw.read(to_read)
                except IOError as e:
                    if e.errno != EINTR:
                        raise
                    continue

                break

            if current:
                self._read_buf = self._read_buf[self._read_pos:] + current
                self._read_pos = 0
        return self._read_buf[self._read_pos:]

    def read1(self, n):
        u"""Reads up to n bytes, with at most one read() system call."""
        if n < 0:
            raise ValueError(u'number of bytes to read must be positive')
        if n == 0:
            return ''
        with self._read_lock:
            self._peek_unlocked(1)
            return self._read_unlocked(min(n, len(self._read_buf) - self._read_pos))

    def tell(self):
        return _BufferedIOMixin.tell(self) - len(self._read_buf) + self._read_pos

    def seek(self, pos, whence=0):
        if not 0 <= whence <= 2:
            raise ValueError(u'invalid whence value')
        with self._read_lock:
            if whence == 1:
                pos -= len(self._read_buf) - self._read_pos
            pos = _BufferedIOMixin.seek(self, pos, whence)
            self._reset_read_buf()
            return pos


class BufferedWriter(_BufferedIOMixin):
    u"""A buffer for a writeable sequential RawIO object.
    
    The constructor creates a BufferedWriter for the given writeable raw
    stream. If the buffer_size is not given, it defaults to
    DEFAULT_BUFFER_SIZE.
    """
    _warning_stack_offset = 2

    def __init__(self, raw, buffer_size=DEFAULT_BUFFER_SIZE, max_buffer_size=None):
        if not raw.writable():
            raise IOError(u'"raw" argument must be writable.')
        _BufferedIOMixin.__init__(self, raw)
        if buffer_size <= 0:
            raise ValueError(u'invalid buffer size')
        if max_buffer_size is not None:
            warnings.warn(u'max_buffer_size is deprecated', DeprecationWarning, self._warning_stack_offset)
        self.buffer_size = buffer_size
        self._write_buf = bytearray()
        self._write_lock = Lock()
        return

    def write(self, b):
        if self.closed:
            raise ValueError(u'write to closed file')
        if isinstance(b, unicode):
            raise TypeError(u"can't write unicode to binary stream")
        with self._write_lock:
            if len(self._write_buf) > self.buffer_size:
                try:
                    self._flush_unlocked()
                except BlockingIOError as e:
                    raise BlockingIOError(e.errno, e.strerror, 0)

            before = len(self._write_buf)
            self._write_buf.extend(b)
            written = len(self._write_buf) - before
            if len(self._write_buf) > self.buffer_size:
                try:
                    self._flush_unlocked()
                except BlockingIOError as e:
                    if len(self._write_buf) > self.buffer_size:
                        overage = len(self._write_buf) - self.buffer_size
                        written -= overage
                        self._write_buf = self._write_buf[:self.buffer_size]
                        raise BlockingIOError(e.errno, e.strerror, written)

            return written

    def truncate(self, pos=None):
        with self._write_lock:
            self._flush_unlocked()
            if pos is None:
                pos = self.raw.tell()
            return self.raw.truncate(pos)
        return

    def flush(self):
        with self._write_lock:
            self._flush_unlocked()

    def _flush_unlocked(self):
        if self.closed:
            raise ValueError(u'flush of closed file')
        written = 0
        try:
            while self._write_buf:
                try:
                    n = self.raw.write(self._write_buf)
                except IOError as e:
                    if e.errno != EINTR:
                        raise
                    continue

                if n > len(self._write_buf) or n < 0:
                    raise IOError(u'write() returned incorrect number of bytes')
                del self._write_buf[:n]
                written += n

        except BlockingIOError as e:
            n = e.characters_written
            del self._write_buf[:n]
            written += n
            raise BlockingIOError(e.errno, e.strerror, written)

    def tell(self):
        return _BufferedIOMixin.tell(self) + len(self._write_buf)

    def seek(self, pos, whence=0):
        if not 0 <= whence <= 2:
            raise ValueError(u'invalid whence')
        with self._write_lock:
            self._flush_unlocked()
            return _BufferedIOMixin.seek(self, pos, whence)


class BufferedRWPair(BufferedIOBase):
    u"""A buffered reader and writer object together.
    
    A buffered reader object and buffered writer object put together to
    form a sequential IO object that can read and write. This is typically
    used with a socket or two-way pipe.
    
    reader and writer are RawIOBase objects that are readable and
    writeable respectively. If the buffer_size is omitted it defaults to
    DEFAULT_BUFFER_SIZE.
    """

    def __init__(self, reader, writer, buffer_size=DEFAULT_BUFFER_SIZE, max_buffer_size=None):
        u"""Constructor.
        
        The arguments are two RawIO instances.
        """
        if max_buffer_size is not None:
            warnings.warn(u'max_buffer_size is deprecated', DeprecationWarning, 2)
        if not reader.readable():
            raise IOError(u'"reader" argument must be readable.')
        if not writer.writable():
            raise IOError(u'"writer" argument must be writable.')
        self.reader = BufferedReader(reader, buffer_size)
        self.writer = BufferedWriter(writer, buffer_size)
        return

    def read(self, n=None):
        if n is None:
            n = -1
        return self.reader.read(n)

    def readinto(self, b):
        return self.reader.readinto(b)

    def write(self, b):
        return self.writer.write(b)

    def peek(self, n=0):
        return self.reader.peek(n)

    def read1(self, n):
        return self.reader.read1(n)

    def readable(self):
        return self.reader.readable()

    def writable(self):
        return self.writer.writable()

    def flush(self):
        return self.writer.flush()

    def close(self):
        self.writer.close()
        self.reader.close()

    def isatty(self):
        return self.reader.isatty() or self.writer.isatty()

    @property
    def closed(self):
        return self.writer.closed


class BufferedRandom(BufferedWriter, BufferedReader):
    u"""A buffered interface to random access streams.
    
    The constructor creates a reader and writer for a seekable stream,
    raw, given in the first argument. If the buffer_size is omitted it
    defaults to DEFAULT_BUFFER_SIZE.
    """
    _warning_stack_offset = 3

    def __init__(self, raw, buffer_size=DEFAULT_BUFFER_SIZE, max_buffer_size=None):
        raw._checkSeekable()
        BufferedReader.__init__(self, raw, buffer_size)
        BufferedWriter.__init__(self, raw, buffer_size, max_buffer_size)

    def seek(self, pos, whence=0):
        if not 0 <= whence <= 2:
            raise ValueError(u'invalid whence')
        self.flush()
        if self._read_buf:
            with self._read_lock:
                self.raw.seek(self._read_pos - len(self._read_buf), 1)
        pos = self.raw.seek(pos, whence)
        with self._read_lock:
            self._reset_read_buf()
        if pos < 0:
            raise IOError(u'seek() returned invalid position')
        return pos

    def tell(self):
        if self._write_buf:
            return BufferedWriter.tell(self)
        else:
            return BufferedReader.tell(self)

    def truncate(self, pos=None):
        if pos is None:
            pos = self.tell()
        return BufferedWriter.truncate(self, pos)

    def read(self, n=None):
        if n is None:
            n = -1
        self.flush()
        return BufferedReader.read(self, n)

    def readinto(self, b):
        self.flush()
        return BufferedReader.readinto(self, b)

    def peek(self, n=0):
        self.flush()
        return BufferedReader.peek(self, n)

    def read1(self, n):
        self.flush()
        return BufferedReader.read1(self, n)

    def write(self, b):
        if self._read_buf:
            with self._read_lock:
                self.raw.seek(self._read_pos - len(self._read_buf), 1)
                self._reset_read_buf()
        return BufferedWriter.write(self, b)


class TextIOBase(IOBase):
    u"""Base class for text I/O.
    
    This class provides a character and line based interface to stream
    I/O. There is no readinto method because Python's character strings
    are immutable. There is no public constructor.
    """

    def read(self, n=-1):
        u"""Read at most n characters from stream.
        
        Read from underlying buffer until we have n characters or we hit EOF.
        If n is negative or omitted, read until EOF.
        """
        self._unsupported(u'read')

    def write(self, s):
        u"""Write string s to stream."""
        self._unsupported(u'write')

    def truncate(self, pos=None):
        u"""Truncate size to pos."""
        self._unsupported(u'truncate')

    def readline(self):
        u"""Read until newline or EOF.
        
        Returns an empty string if EOF is hit immediately.
        """
        self._unsupported(u'readline')

    def detach(self):
        u"""
        Separate the underlying buffer from the TextIOBase and return it.
        
        After the underlying buffer has been detached, the TextIO is in an
        unusable state.
        """
        self._unsupported(u'detach')

    @property
    def encoding(self):
        u"""Subclasses should override."""
        return None

    @property
    def newlines(self):
        u"""Line endings translated so far.
        
        Only line endings translated during reading are considered.
        
        Subclasses should override.
        """
        return None

    @property
    def errors(self):
        u"""Error setting of the decoder or encoder.
        
        Subclasses should override."""
        return None


io.TextIOBase.register(TextIOBase)

class IncrementalNewlineDecoder(codecs.IncrementalDecoder):
    ur"""Codec used when reading a file in universal newlines mode.  It wraps
    another incremental decoder, translating \r\n and \r into \n.  It also
    records the types of newlines encountered.  When used with
    translate=False, it ensures that the newline sequence is returned in
    one piece.
    """

    def __init__(self, decoder, translate, errors=u'strict'):
        codecs.IncrementalDecoder.__init__(self, errors=errors)
        self.translate = translate
        self.decoder = decoder
        self.seennl = 0
        self.pendingcr = False

    def decode(self, input, final=False):
        if self.decoder is None:
            output = input
        else:
            output = self.decoder.decode(input, final=final)
        if self.pendingcr and (output or final):
            output = u'\r' + output
            self.pendingcr = False
        if output.endswith(u'\r') and not final:
            output = output[:-1]
            self.pendingcr = True
        crlf = output.count(u'\r\n')
        cr = output.count(u'\r') - crlf
        lf = output.count(u'\n') - crlf
        self.seennl |= (lf and self._LF) | (cr and self._CR) | (crlf and self._CRLF)
        if self.translate:
            if crlf:
                output = output.replace(u'\r\n', u'\n')
            if cr:
                output = output.replace(u'\r', u'\n')
        return output

    def getstate(self):
        if self.decoder is None:
            buf = ''
            flag = 0
        else:
            buf, flag = self.decoder.getstate()
        flag <<= 1
        if self.pendingcr:
            flag |= 1
        return (buf, flag)

    def setstate(self, state):
        buf, flag = state
        self.pendingcr = bool(flag & 1)
        if self.decoder is not None:
            self.decoder.setstate((buf, flag >> 1))
        return

    def reset(self):
        self.seennl = 0
        self.pendingcr = False
        if self.decoder is not None:
            self.decoder.reset()
        return

    _LF = 1
    _CR = 2
    _CRLF = 4

    @property
    def newlines(self):
        return (
         None,
         u'\n',
         u'\r',
         (u'\r', u'\n'),
         u'\r\n',
         (u'\n', u'\r\n'),
         (u'\r', u'\r\n'),
         (u'\r', u'\n', u'\r\n'))[self.seennl]


class TextIOWrapper(TextIOBase):
    ur"""Character and line based layer over a BufferedIOBase object, buffer.
    
    encoding gives the name of the encoding that the stream will be
    decoded or encoded with. It defaults to locale.getpreferredencoding.
    
    errors determines the strictness of encoding and decoding (see the
    codecs.register) and defaults to "strict".
    
    newline can be None, '', '\n', '\r', or '\r\n'.  It controls the
    handling of line endings. If it is None, universal newlines is
    enabled.  With this enabled, on input, the lines endings '\n', '\r',
    or '\r\n' are translated to '\n' before being returned to the
    caller. Conversely, on output, '\n' is translated to the system
    default line seperator, os.linesep. If newline is any other of its
    legal values, that newline becomes the newline when the file is read
    and it is returned untranslated. On output, '\n' is converted to the
    newline.
    
    If line_buffering is True, a call to flush is implied when a call to
    write contains a newline character.
    """
    _CHUNK_SIZE = 2048

    def __init__(self, buffer, encoding=None, errors=None, newline=None, line_buffering=False):
        if newline is not None and not isinstance(newline, basestring):
            raise TypeError(u'illegal newline type: %r' % (type(newline),))
        if newline not in (None, u'', u'\n', u'\r', u'\r\n'):
            raise ValueError(u'illegal newline value: %r' % (newline,))
        if encoding is None:
            try:
                import locale
            except ImportError:
                encoding = u'ascii'
            else:
                encoding = locale.getpreferredencoding()

        if not isinstance(encoding, basestring):
            raise ValueError(u'invalid encoding: %r' % encoding)
        if errors is None:
            errors = u'strict'
        elif not isinstance(errors, basestring):
            raise ValueError(u'invalid errors: %r' % errors)
        self._buffer = buffer
        self._line_buffering = line_buffering
        self._encoding = encoding
        self._errors = errors
        self._readuniversal = not newline
        self._readtranslate = newline is None
        self._readnl = newline
        self._writetranslate = newline != u''
        self._writenl = newline or os.linesep
        self._encoder = None
        self._decoder = None
        self._decoded_chars = u''
        self._decoded_chars_used = 0
        self._snapshot = None
        self._seekable = self._telling = self.buffer.seekable()
        if self._seekable and self.writable():
            position = self.buffer.tell()
            if position != 0:
                try:
                    self._get_encoder().setstate(0)
                except LookupError:
                    pass

        return

    def __repr__(self):
        try:
            name = self.name
        except AttributeError:
            return u"<_pyio.TextIOWrapper encoding='{0}'>".format(self.encoding)

        return u"<_pyio.TextIOWrapper name={0!r} encoding='{1}'>".format(name, self.encoding)

    @property
    def encoding(self):
        return self._encoding

    @property
    def errors(self):
        return self._errors

    @property
    def line_buffering(self):
        return self._line_buffering

    @property
    def buffer(self):
        return self._buffer

    def seekable(self):
        return self._seekable

    def readable(self):
        return self.buffer.readable()

    def writable(self):
        return self.buffer.writable()

    def flush(self):
        self.buffer.flush()
        self._telling = self._seekable

    def close(self):
        if self.buffer is not None and not self.closed:
            self.flush()
            self.buffer.close()
        return

    @property
    def closed(self):
        return self.buffer.closed

    @property
    def name(self):
        return self.buffer.name

    def fileno(self):
        return self.buffer.fileno()

    def isatty(self):
        return self.buffer.isatty()

    def write(self, s):
        if self.closed:
            raise ValueError(u'write to closed file')
        if not isinstance(s, unicode):
            raise TypeError(u"can't write %s to text stream" % s.__class__.__name__)
        length = len(s)
        haslf = (self._writetranslate or self._line_buffering) and u'\n' in s
        if haslf and self._writetranslate and self._writenl != u'\n':
            s = s.replace(u'\n', self._writenl)
        encoder = self._encoder or self._get_encoder()
        b = encoder.encode(s)
        self.buffer.write(b)
        if self._line_buffering and (haslf or u'\r' in s):
            self.flush()
        self._snapshot = None
        if self._decoder:
            self._decoder.reset()
        return length

    def _get_encoder(self):
        make_encoder = codecs.getincrementalencoder(self._encoding)
        self._encoder = make_encoder(self._errors)
        return self._encoder

    def _get_decoder(self):
        make_decoder = codecs.getincrementaldecoder(self._encoding)
        decoder = make_decoder(self._errors)
        if self._readuniversal:
            decoder = IncrementalNewlineDecoder(decoder, self._readtranslate)
        self._decoder = decoder
        return decoder

    def _set_decoded_chars(self, chars):
        u"""Set the _decoded_chars buffer."""
        self._decoded_chars = chars
        self._decoded_chars_used = 0

    def _get_decoded_chars(self, n=None):
        u"""Advance into the _decoded_chars buffer."""
        offset = self._decoded_chars_used
        if n is None:
            chars = self._decoded_chars[offset:]
        else:
            chars = self._decoded_chars[offset:offset + n]
        self._decoded_chars_used += len(chars)
        return chars

    def _rewind_decoded_chars(self, n):
        u"""Rewind the _decoded_chars buffer."""
        if self._decoded_chars_used < n:
            raise AssertionError(u'rewind decoded_chars out of bounds')
        self._decoded_chars_used -= n

    def _read_chunk(self):
        u"""
        Read and decode the next chunk of data from the BufferedReader.
        """
        if self._decoder is None:
            raise ValueError(u'no decoder')
        if self._telling:
            dec_buffer, dec_flags = self._decoder.getstate()
        input_chunk = self.buffer.read1(self._CHUNK_SIZE)
        eof = not input_chunk
        self._set_decoded_chars(self._decoder.decode(input_chunk, eof))
        if self._telling:
            self._snapshot = (
             dec_flags, dec_buffer + input_chunk)
        return not eof

    def _pack_cookie(self, position, dec_flags=0, bytes_to_feed=0, need_eof=0, chars_to_skip=0):
        return position | dec_flags << 64 | bytes_to_feed << 128 | chars_to_skip << 192 | bool(need_eof) << 256

    def _unpack_cookie(self, bigint):
        rest, position = divmod(bigint, 18446744073709551616L)
        rest, dec_flags = divmod(rest, 18446744073709551616L)
        rest, bytes_to_feed = divmod(rest, 18446744073709551616L)
        need_eof, chars_to_skip = divmod(rest, 18446744073709551616L)
        return (
         position, dec_flags, bytes_to_feed, need_eof, chars_to_skip)

    def tell(self):
        if not self._seekable:
            raise IOError(u'underlying stream is not seekable')
        if not self._telling:
            raise IOError(u'telling position disabled by next() call')
        self.flush()
        position = self.buffer.tell()
        decoder = self._decoder
        if decoder is None or self._snapshot is None:
            if self._decoded_chars:
                raise AssertionError(u'pending decoded text')
            return position
        else:
            dec_flags, next_input = self._snapshot
            position -= len(next_input)
            chars_to_skip = self._decoded_chars_used
            if chars_to_skip == 0:
                return self._pack_cookie(position, dec_flags)
            saved_state = decoder.getstate()
            try:
                decoder.setstate(('', dec_flags))
                start_pos = position
                start_flags, bytes_fed, chars_decoded = dec_flags, 0, 0
                need_eof = 0
                for next_byte in next_input:
                    bytes_fed += 1
                    chars_decoded += len(decoder.decode(next_byte))
                    dec_buffer, dec_flags = decoder.getstate()
                    if not dec_buffer and chars_decoded <= chars_to_skip:
                        start_pos += bytes_fed
                        chars_to_skip -= chars_decoded
                        start_flags, bytes_fed, chars_decoded = dec_flags, 0, 0
                    if chars_decoded >= chars_to_skip:
                        break
                else:
                    chars_decoded += len(decoder.decode('', final=True))
                    need_eof = 1
                    if chars_decoded < chars_to_skip:
                        raise IOError(u"can't reconstruct logical file position")
                    return self._pack_cookie(start_pos, start_flags, bytes_fed, need_eof, chars_to_skip)

            finally:
                decoder.setstate(saved_state)

            return

    def truncate(self, pos=None):
        self.flush()
        if pos is None:
            pos = self.tell()
        return self.buffer.truncate(pos)

    def detach(self):
        if self.buffer is None:
            raise ValueError(u'buffer is already detached')
        self.flush()
        buffer = self._buffer
        self._buffer = None
        return buffer

    def seek(self, cookie, whence=0):
        if self.closed:
            raise ValueError(u'tell on closed file')
        if not self._seekable:
            raise IOError(u'underlying stream is not seekable')
        if whence == 1:
            if cookie != 0:
                raise IOError(u"can't do nonzero cur-relative seeks")
            whence = 0
            cookie = self.tell()
        if whence == 2:
            if cookie != 0:
                raise IOError(u"can't do nonzero end-relative seeks")
            self.flush()
            position = self.buffer.seek(0, 2)
            self._set_decoded_chars(u'')
            self._snapshot = None
            if self._decoder:
                self._decoder.reset()
            return position
        else:
            if whence != 0:
                raise ValueError(u'invalid whence (%r, should be 0, 1 or 2)' % (
                 whence,))
            if cookie < 0:
                raise ValueError(u'negative seek position %r' % (cookie,))
            self.flush()
            start_pos, dec_flags, bytes_to_feed, need_eof, chars_to_skip = self._unpack_cookie(cookie)
            self.buffer.seek(start_pos)
            self._set_decoded_chars(u'')
            self._snapshot = None
            if cookie == 0 and self._decoder:
                self._decoder.reset()
            elif self._decoder or dec_flags or chars_to_skip:
                self._decoder = self._decoder or self._get_decoder()
                self._decoder.setstate(('', dec_flags))
                self._snapshot = (dec_flags, '')
            if chars_to_skip:
                input_chunk = self.buffer.read(bytes_to_feed)
                self._set_decoded_chars(self._decoder.decode(input_chunk, need_eof))
                self._snapshot = (dec_flags, input_chunk)
                if len(self._decoded_chars) < chars_to_skip:
                    raise IOError(u"can't restore logical file position")
                self._decoded_chars_used = chars_to_skip
            try:
                encoder = self._encoder or self._get_encoder()
            except LookupError:
                pass
            else:
                if cookie != 0:
                    encoder.setstate(0)
                else:
                    encoder.reset()

            return cookie

    def read(self, n=None):
        self._checkReadable()
        if n is None:
            n = -1
        decoder = self._decoder or self._get_decoder()
        try:
            n.__index__
        except AttributeError:
            raise TypeError(u'an integer is required')

        if n < 0:
            result = self._get_decoded_chars() + decoder.decode(self.buffer.read(), final=True)
            self._set_decoded_chars(u'')
            self._snapshot = None
            return result
        else:
            eof = False
            result = self._get_decoded_chars(n)
            while len(result) < n and not eof:
                eof = not self._read_chunk()
                result += self._get_decoded_chars(n - len(result))

            return result
            return

    def next(self):
        self._telling = False
        line = self.readline()
        if not line:
            self._snapshot = None
            self._telling = self._seekable
            raise StopIteration
        return line

    def readline(self, limit=None):
        if self.closed:
            raise ValueError(u'read from closed file')
        if limit is None:
            limit = -1
        else:
            if not isinstance(limit, (int, long)):
                raise TypeError(u'limit must be an integer')
            line = self._get_decoded_chars()
            start = 0
            if not self._decoder:
                self._get_decoder()
            pos = endpos = None
            while True:
                if self._readtranslate:
                    pos = line.find(u'\n', start)
                    if pos >= 0:
                        endpos = pos + 1
                        break
                    else:
                        start = len(line)
                else:
                    if self._readuniversal:
                        nlpos = line.find(u'\n', start)
                        crpos = line.find(u'\r', start)
                        if crpos == -1:
                            if nlpos == -1:
                                start = len(line)
                            else:
                                endpos = nlpos + 1
                                break
                        elif nlpos == -1:
                            endpos = crpos + 1
                            break
                        elif nlpos < crpos:
                            endpos = nlpos + 1
                            break
                        elif nlpos == crpos + 1:
                            endpos = crpos + 2
                            break
                        else:
                            endpos = crpos + 1
                            break
                    else:
                        pos = line.find(self._readnl)
                        if pos >= 0:
                            endpos = pos + len(self._readnl)
                            break
                    if limit >= 0 and len(line) >= limit:
                        endpos = limit
                        break
                    while self._read_chunk():
                        if self._decoded_chars:
                            break

                if self._decoded_chars:
                    line += self._get_decoded_chars()
                else:
                    self._set_decoded_chars(u'')
                    self._snapshot = None
                    return line

        if limit >= 0 and endpos > limit:
            endpos = limit
        self._rewind_decoded_chars(len(line) - endpos)
        return line[:endpos]

    @property
    def newlines(self):
        if self._decoder:
            return self._decoder.newlines
        else:
            return None


class StringIO(TextIOWrapper):
    u"""Text I/O implementation using an in-memory buffer.
    
    The initial_value argument sets the value of object.  The newline
    argument is like the one of TextIOWrapper's constructor.
    """

    def __init__(self, initial_value=u'', newline=u'\n'):
        super(StringIO, self).__init__(BytesIO(), encoding=u'utf-8', errors=u'strict', newline=newline)
        if newline is None:
            self._writetranslate = False
        if initial_value:
            if not isinstance(initial_value, unicode):
                initial_value = unicode(initial_value)
            self.write(initial_value)
            self.seek(0)
        return

    def getvalue(self):
        self.flush()
        return self.buffer.getvalue().decode(self._encoding, self._errors)

    def __repr__(self):
        return object.__repr__(self)

    @property
    def errors(self):
        return None

    @property
    def encoding(self):
        return None

    def detach(self):
        self._unsupported(u'detach')