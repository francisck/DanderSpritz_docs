# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: dbrecio.py
"""
File-like objects that read from or write to a bsddb record.

This implements (nearly) all stdio methods.

f = DBRecIO(db, key, txn=None)
f.close()           # explicitly release resources held
flag = f.isatty()   # always false
pos = f.tell()      # get current position
f.seek(pos)         # set current position
f.seek(pos, mode)   # mode 0: absolute; 1: relative; 2: relative to EOF
buf = f.read()      # read until EOF
buf = f.read(n)     # read up to n bytes
f.truncate([size])  # truncate file at to at most size (default: current pos)
f.write(buf)        # write at current position
f.writelines(list)  # for line in list: f.write(line)

Notes:
- fileno() is left unimplemented so that code which uses it triggers
  an exception early.
- There's a simple test set (see end of this file) - not yet updated
  for DBRecIO.
- readline() is not implemented yet.


From:
    Itamar Shtull-Trauring <itamar@maxnm.com>
"""
import errno
import string

class DBRecIO:

    def __init__(self, db, key, txn=None):
        self.db = db
        self.key = key
        self.txn = txn
        self.len = None
        self.pos = 0
        self.closed = 0
        self.softspace = 0
        return

    def close(self):
        if not self.closed:
            self.closed = 1
            del self.db
            del self.txn

    def isatty(self):
        if self.closed:
            raise ValueError, 'I/O operation on closed file'
        return 0

    def seek(self, pos, mode=0):
        if self.closed:
            raise ValueError, 'I/O operation on closed file'
        if mode == 1:
            pos = pos + self.pos
        elif mode == 2:
            pos = pos + self.len
        self.pos = max(0, pos)

    def tell(self):
        if self.closed:
            raise ValueError, 'I/O operation on closed file'
        return self.pos

    def read(self, n=-1):
        if self.closed:
            raise ValueError, 'I/O operation on closed file'
        if n < 0:
            newpos = self.len
        else:
            newpos = min(self.pos + n, self.len)
        dlen = newpos - self.pos
        r = self.db.get(self.key, txn=self.txn, dlen=dlen, doff=self.pos)
        self.pos = newpos
        return r

    __fixme = '\n    def readline(self, length=None):\n        if self.closed:\n            raise ValueError, "I/O operation on closed file"\n        if self.buflist:\n            self.buf = self.buf + string.joinfields(self.buflist, \'\')\n            self.buflist = []\n        i = string.find(self.buf, \'\n\', self.pos)\n        if i < 0:\n            newpos = self.len\n        else:\n            newpos = i+1\n        if length is not None:\n            if self.pos + length < newpos:\n                newpos = self.pos + length\n        r = self.buf[self.pos:newpos]\n        self.pos = newpos\n        return r\n\n    def readlines(self, sizehint = 0):\n        total = 0\n        lines = []\n        line = self.readline()\n        while line:\n            lines.append(line)\n            total += len(line)\n            if 0 < sizehint <= total:\n                break\n            line = self.readline()\n        return lines\n    '

    def truncate(self, size=None):
        if self.closed:
            raise ValueError, 'I/O operation on closed file'
        if size is None:
            size = self.pos
        elif size < 0:
            raise IOError(errno.EINVAL, 'Negative size not allowed')
        elif size < self.pos:
            self.pos = size
        self.db.put(self.key, '', txn=self.txn, dlen=self.len - size, doff=size)
        return

    def write(self, s):
        if self.closed:
            raise ValueError, 'I/O operation on closed file'
        if not s:
            return
        if self.pos > self.len:
            self.buflist.append('\x00' * (self.pos - self.len))
            self.len = self.pos
        newpos = self.pos + len(s)
        self.db.put(self.key, s, txn=self.txn, dlen=len(s), doff=self.pos)
        self.pos = newpos

    def writelines(self, list):
        self.write(string.joinfields(list, ''))

    def flush(self):
        if self.closed:
            raise ValueError, 'I/O operation on closed file'