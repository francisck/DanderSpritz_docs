# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: gzip.py
"""Functions that read and write gzipped files.

The user of the file doesn't have to worry about the compression,
but random access is not allowed."""
import struct
import sys
import time
import os
import zlib
import io
import __builtin__
__all__ = [
 'GzipFile', 'open']
FTEXT, FHCRC, FEXTRA, FNAME, FCOMMENT = (
 1, 2, 4, 8, 16)
READ, WRITE = (
 1, 2)

def write32u(output, value):
    output.write(struct.pack('<L', value))


def read32(input):
    return struct.unpack('<I', input.read(4))[0]


def open(filename, mode='rb', compresslevel=9):
    """Shorthand for GzipFile(filename, mode, compresslevel).
    
    The filename argument is required; mode defaults to 'rb'
    and compresslevel defaults to 9.
    
    """
    return GzipFile(filename, mode, compresslevel)


class GzipFile(io.BufferedIOBase):
    """The GzipFile class simulates most of the methods of a file object with
    the exception of the readinto() and truncate() methods.
    
    """
    myfileobj = None
    max_read_chunk = 10485760

    def __init__(self, filename=None, mode=None, compresslevel=9, fileobj=None, mtime=None):
        """Constructor for the GzipFile class.
        
        At least one of fileobj and filename must be given a
        non-trivial value.
        
        The new class instance is based on fileobj, which can be a regular
        file, a StringIO object, or any other object which simulates a file.
        It defaults to None, in which case filename is opened to provide
        a file object.
        
        When fileobj is not None, the filename argument is only used to be
        included in the gzip file header, which may includes the original
        filename of the uncompressed file.  It defaults to the filename of
        fileobj, if discernible; otherwise, it defaults to the empty string,
        and in this case the original filename is not included in the header.
        
        The mode argument can be any of 'r', 'rb', 'a', 'ab', 'w', or 'wb',
        depending on whether the file will be read or written.  The default
        is the mode of fileobj if discernible; otherwise, the default is 'rb'.
        Be aware that only the 'rb', 'ab', and 'wb' values should be used
        for cross-platform portability.
        
        The compresslevel argument is an integer from 1 to 9 controlling the
        level of compression; 1 is fastest and produces the least compression,
        and 9 is slowest and produces the most compression.  The default is 9.
        
        The mtime argument is an optional numeric timestamp to be written
        to the stream when compressing.  All gzip compressed streams
        are required to contain a timestamp.  If omitted or None, the
        current time is used.  This module ignores the timestamp when
        decompressing; however, some programs, such as gunzip, make use
        of it.  The format of the timestamp is the same as that of the
        return value of time.time() and of the st_mtime member of the
        object returned by os.stat().
        
        """
        if mode and 'b' not in mode:
            mode += 'b'
        if fileobj is None:
            fileobj = self.myfileobj = __builtin__.open(filename, mode or 'rb')
        if filename is None:
            if hasattr(fileobj, 'name'):
                filename = fileobj.name
            else:
                filename = ''
        if mode is None:
            if hasattr(fileobj, 'mode'):
                mode = fileobj.mode
            else:
                mode = 'rb'
        if mode[0:1] == 'r':
            self.mode = READ
            self._new_member = True
            self.extrabuf = ''
            self.extrasize = 0
            self.extrastart = 0
            self.name = filename
            self.min_readsize = 100
        elif mode[0:1] == 'w' or mode[0:1] == 'a':
            self.mode = WRITE
            self._init_write(filename)
            self.compress = zlib.compressobj(compresslevel, zlib.DEFLATED, -zlib.MAX_WBITS, zlib.DEF_MEM_LEVEL, 0)
        else:
            raise IOError, 'Mode ' + mode + ' not supported'
        self.fileobj = fileobj
        self.offset = 0
        self.mtime = mtime
        if self.mode == WRITE:
            self._write_gzip_header()
        return

    @property
    def filename(self):
        import warnings
        warnings.warn('use the name attribute', DeprecationWarning, 2)
        if self.mode == WRITE and self.name[-3:] != '.gz':
            return self.name + '.gz'
        return self.name

    def __repr__(self):
        s = repr(self.fileobj)
        return '<gzip ' + s[1:-1] + ' ' + hex(id(self)) + '>'

    def _check_closed(self):
        """Raises a ValueError if the underlying file object has been closed.
        
        """
        if self.closed:
            raise ValueError('I/O operation on closed file.')

    def _init_write(self, filename):
        self.name = filename
        self.crc = zlib.crc32('') & 4294967295L
        self.size = 0
        self.writebuf = []
        self.bufsize = 0

    def _write_gzip_header(self):
        self.fileobj.write('\x1f\x8b')
        self.fileobj.write('\x08')
        fname = os.path.basename(self.name)
        if fname.endswith('.gz'):
            fname = fname[:-3]
        flags = 0
        if fname:
            flags = FNAME
        self.fileobj.write(chr(flags))
        mtime = self.mtime
        if mtime is None:
            mtime = time.time()
        write32u(self.fileobj, long(mtime))
        self.fileobj.write('\x02')
        self.fileobj.write('\xff')
        if fname:
            self.fileobj.write(fname + '\x00')
        return

    def _init_read(self):
        self.crc = zlib.crc32('') & 4294967295L
        self.size = 0

    def _read_gzip_header(self):
        magic = self.fileobj.read(2)
        if magic != '\x1f\x8b':
            raise IOError, 'Not a gzipped file'
        method = ord(self.fileobj.read(1))
        if method != 8:
            raise IOError, 'Unknown compression method'
        flag = ord(self.fileobj.read(1))
        self.mtime = read32(self.fileobj)
        self.fileobj.read(2)
        if flag & FEXTRA:
            xlen = ord(self.fileobj.read(1))
            xlen = xlen + 256 * ord(self.fileobj.read(1))
            self.fileobj.read(xlen)
        if flag & FNAME:
            while True:
                s = self.fileobj.read(1)
                if not s or s == '\x00':
                    break

        if flag & FCOMMENT:
            while True:
                s = self.fileobj.read(1)
                if not s or s == '\x00':
                    break

        if flag & FHCRC:
            self.fileobj.read(2)

    def write(self, data):
        self._check_closed()
        if self.mode != WRITE:
            import errno
            raise IOError(errno.EBADF, 'write() on read-only GzipFile object')
        if self.fileobj is None:
            raise ValueError, 'write() on closed GzipFile object'
        if isinstance(data, memoryview):
            data = data.tobytes()
        if len(data) > 0:
            self.size = self.size + len(data)
            self.crc = zlib.crc32(data, self.crc) & 4294967295L
            self.fileobj.write(self.compress.compress(data))
            self.offset += len(data)
        return len(data)

    def read(self, size=-1):
        self._check_closed()
        if self.mode != READ:
            import errno
            raise IOError(errno.EBADF, 'read() on write-only GzipFile object')
        if self.extrasize <= 0 and self.fileobj is None:
            return ''
        else:
            readsize = 1024
            if size < 0:
                try:
                    while True:
                        self._read(readsize)
                        readsize = min(self.max_read_chunk, readsize * 2)

                except EOFError:
                    size = self.extrasize

            else:
                try:
                    while size > self.extrasize:
                        self._read(readsize)
                        readsize = min(self.max_read_chunk, readsize * 2)

                except EOFError:
                    if size > self.extrasize:
                        size = self.extrasize

            offset = self.offset - self.extrastart
            chunk = self.extrabuf[offset:offset + size]
            self.extrasize = self.extrasize - size
            self.offset += size
            return chunk

    def _unread(self, buf):
        self.extrasize = len(buf) + self.extrasize
        self.offset -= len(buf)

    def _read(self, size=1024):
        if self.fileobj is None:
            raise EOFError, 'Reached EOF'
        if self._new_member:
            pos = self.fileobj.tell()
            self.fileobj.seek(0, 2)
            if pos == self.fileobj.tell():
                raise EOFError, 'Reached EOF'
            else:
                self.fileobj.seek(pos)
            self._init_read()
            self._read_gzip_header()
            self.decompress = zlib.decompressobj(-zlib.MAX_WBITS)
            self._new_member = False
        buf = self.fileobj.read(size)
        if buf == '':
            uncompress = self.decompress.flush()
            self._read_eof()
            self._add_read_data(uncompress)
            raise EOFError, 'Reached EOF'
        uncompress = self.decompress.decompress(buf)
        self._add_read_data(uncompress)
        if self.decompress.unused_data != '':
            self.fileobj.seek(-len(self.decompress.unused_data) + 8, 1)
            self._read_eof()
            self._new_member = True
        return

    def _add_read_data(self, data):
        self.crc = zlib.crc32(data, self.crc) & 4294967295L
        offset = self.offset - self.extrastart
        self.extrabuf = self.extrabuf[offset:] + data
        self.extrasize = self.extrasize + len(data)
        self.extrastart = self.offset
        self.size = self.size + len(data)

    def _read_eof(self):
        self.fileobj.seek(-8, 1)
        crc32 = read32(self.fileobj)
        isize = read32(self.fileobj)
        if crc32 != self.crc:
            raise IOError('CRC check failed %s != %s' % (hex(crc32),
             hex(self.crc)))
        else:
            if isize != self.size & 4294967295L:
                raise IOError, 'Incorrect length of data produced'
            c = '\x00'
            while c == '\x00':
                c = self.fileobj.read(1)

        if c:
            self.fileobj.seek(-1, 1)

    @property
    def closed(self):
        return self.fileobj is None

    def close(self):
        if self.fileobj is None:
            return
        else:
            if self.mode == WRITE:
                self.fileobj.write(self.compress.flush())
                write32u(self.fileobj, self.crc)
                write32u(self.fileobj, self.size & 4294967295L)
                self.fileobj = None
            elif self.mode == READ:
                self.fileobj = None
            if self.myfileobj:
                self.myfileobj.close()
                self.myfileobj = None
            return

    def flush(self, zlib_mode=zlib.Z_SYNC_FLUSH):
        self._check_closed()
        if self.mode == WRITE:
            self.fileobj.write(self.compress.flush(zlib_mode))
            self.fileobj.flush()

    def fileno(self):
        """Invoke the underlying file object's fileno() method.
        
        This will raise AttributeError if the underlying file object
        doesn't support fileno().
        """
        return self.fileobj.fileno()

    def rewind(self):
        """Return the uncompressed stream file position indicator to the
        beginning of the file"""
        if self.mode != READ:
            raise IOError("Can't rewind in write mode")
        self.fileobj.seek(0)
        self._new_member = True
        self.extrabuf = ''
        self.extrasize = 0
        self.extrastart = 0
        self.offset = 0

    def readable(self):
        return self.mode == READ

    def writable(self):
        return self.mode == WRITE

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence:
            if whence == 1:
                offset = self.offset + offset
            else:
                raise ValueError('Seek from end not supported')
        if self.mode == WRITE:
            if offset < self.offset:
                raise IOError('Negative seek in write mode')
            count = offset - self.offset
            for i in range(count // 1024):
                self.write(1024 * '\x00')

            self.write(count % 1024 * '\x00')
        elif self.mode == READ:
            if offset < self.offset:
                self.rewind()
            count = offset - self.offset
            for i in range(count // 1024):
                self.read(1024)

            self.read(count % 1024)
        return self.offset

    def readline(self, size=-1):
        if size < 0:
            offset = self.offset - self.extrastart
            i = self.extrabuf.find('\n', offset) + 1
            if i > 0:
                self.extrasize -= i - offset
                self.offset += i - offset
                return self.extrabuf[offset:i]
            size = sys.maxint
            readsize = self.min_readsize
        else:
            readsize = size
        bufs = []
        while size != 0:
            c = self.read(readsize)
            i = c.find('\n')
            if size <= i or i == -1 and len(c) > size:
                i = size - 1
            if i >= 0 or c == '':
                bufs.append(c[:i + 1])
                self._unread(c[i + 1:])
                break
            bufs.append(c)
            size = size - len(c)
            readsize = min(size, readsize * 2)

        if readsize > self.min_readsize:
            self.min_readsize = min(readsize, self.min_readsize * 2, 512)
        return ''.join(bufs)


def _test():
    args = sys.argv[1:]
    decompress = args and args[0] == '-d'
    if decompress:
        args = args[1:]
    if not args:
        args = [
         '-']
    for arg in args:
        if decompress:
            if arg == '-':
                f = GzipFile(filename='', mode='rb', fileobj=sys.stdin)
                g = sys.stdout
            else:
                if arg[-3:] != '.gz':
                    print "filename doesn't end in .gz:", repr(arg)
                    continue
                f = open(arg, 'rb')
                g = __builtin__.open(arg[:-3], 'wb')
        elif arg == '-':
            f = sys.stdin
            g = GzipFile(filename='', mode='wb', fileobj=sys.stdout)
        else:
            f = __builtin__.open(arg, 'rb')
            g = open(arg + '.gz', 'wb')
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            g.write(chunk)

        if g is not sys.stdout:
            g.close()
        if f is not sys.stdin:
            f.close()


if __name__ == '__main__':
    _test()