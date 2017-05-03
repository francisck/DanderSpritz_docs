# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: dumbdbm.py
"""A dumb and slow but simple dbm clone.

For database spam, spam.dir contains the index (a text file),
spam.bak *may* contain a backup of the index (also a text file),
while spam.dat contains the data (a binary file).

XXX TO DO:

- seems to contain a bug when updating...

- reclaim free space (currently, space once occupied by deleted or expanded
items is never reused)

- support concurrent access (currently, if two processes take turns making
updates, they can mess up the index)

- support efficient access to large databases (currently, the whole index
is read when the database is opened, and some updates rewrite the whole index)

- support opening for read-only (flag = 'm')

"""
import os as _os
import __builtin__
import UserDict
_open = __builtin__.open
_BLOCKSIZE = 512
error = IOError

class _Database(UserDict.DictMixin):
    _os = _os
    _open = _open

    def __init__(self, filebasename, mode):
        self._mode = mode
        self._dirfile = filebasename + _os.extsep + 'dir'
        self._datfile = filebasename + _os.extsep + 'dat'
        self._bakfile = filebasename + _os.extsep + 'bak'
        self._index = None
        try:
            f = _open(self._datfile, 'r')
        except IOError:
            f = _open(self._datfile, 'w')
            self._chmod(self._datfile)

        f.close()
        self._update()
        return

    def _update(self):
        self._index = {}
        try:
            f = _open(self._dirfile)
        except IOError:
            pass
        else:
            for line in f:
                line = line.rstrip()
                key, pos_and_siz_pair = eval(line)
                self._index[key] = pos_and_siz_pair

            f.close()

    def _commit(self):
        if self._index is None:
            return
        else:
            try:
                self._os.unlink(self._bakfile)
            except self._os.error:
                pass

            try:
                self._os.rename(self._dirfile, self._bakfile)
            except self._os.error:
                pass

            f = self._open(self._dirfile, 'w')
            self._chmod(self._dirfile)
            for key, pos_and_siz_pair in self._index.iteritems():
                f.write('%r, %r\n' % (key, pos_and_siz_pair))

            f.close()
            return

    sync = _commit

    def __getitem__(self, key):
        pos, siz = self._index[key]
        f = _open(self._datfile, 'rb')
        f.seek(pos)
        dat = f.read(siz)
        f.close()
        return dat

    def _addval(self, val):
        f = _open(self._datfile, 'rb+')
        f.seek(0, 2)
        pos = int(f.tell())
        npos = (pos + _BLOCKSIZE - 1) // _BLOCKSIZE * _BLOCKSIZE
        f.write('\x00' * (npos - pos))
        pos = npos
        f.write(val)
        f.close()
        return (
         pos, len(val))

    def _setval(self, pos, val):
        f = _open(self._datfile, 'rb+')
        f.seek(pos)
        f.write(val)
        f.close()
        return (
         pos, len(val))

    def _addkey(self, key, pos_and_siz_pair):
        self._index[key] = pos_and_siz_pair
        f = _open(self._dirfile, 'a')
        self._chmod(self._dirfile)
        f.write('%r, %r\n' % (key, pos_and_siz_pair))
        f.close()

    def __setitem__(self, key, val):
        if not type(key) == type('') == type(val):
            raise TypeError, 'keys and values must be strings'
        if key not in self._index:
            self._addkey(key, self._addval(val))
        else:
            pos, siz = self._index[key]
            oldblocks = (siz + _BLOCKSIZE - 1) // _BLOCKSIZE
            newblocks = (len(val) + _BLOCKSIZE - 1) // _BLOCKSIZE
            if newblocks <= oldblocks:
                self._index[key] = self._setval(pos, val)
            else:
                self._index[key] = self._addval(val)

    def __delitem__(self, key):
        del self._index[key]
        self._commit()

    def keys(self):
        return self._index.keys()

    def has_key(self, key):
        return key in self._index

    def __contains__(self, key):
        return key in self._index

    def iterkeys(self):
        return self._index.iterkeys()

    __iter__ = iterkeys

    def __len__(self):
        return len(self._index)

    def close(self):
        self._commit()
        self._index = self._datfile = self._dirfile = self._bakfile = None
        return

    __del__ = close

    def _chmod(self, file):
        if hasattr(self._os, 'chmod'):
            self._os.chmod(file, self._mode)


def open(file, flag=None, mode=438):
    """Open the database file, filename, and return corresponding object.
    
    The flag argument, used to control how the database is opened in the
    other DBM implementations, is ignored in the dumbdbm module; the
    database is always opened for update, and will be created if it does
    not exist.
    
    The optional mode argument is the UNIX mode of the file, used only when
    the database has to be created.  It defaults to octal code 0666 (and
    will be modified by the prevailing umask).
    
    """
    try:
        um = _os.umask(0)
        _os.umask(um)
    except AttributeError:
        pass
    else:
        mode = mode & ~um

    return _Database(file, mode)