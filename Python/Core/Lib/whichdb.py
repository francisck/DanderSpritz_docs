# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: whichdb.py
"""Guess which db package to use to open a db file."""
import os
import struct
import sys
try:
    import dbm
    _dbmerror = dbm.error
except ImportError:
    dbm = None
    _dbmerror = IOError

def whichdb(filename):
    """Guess which db package to use to open a db file.
    
    Return values:
    
    - None if the database file can't be read;
    - empty string if the file can be read but can't be recognized
    - the module name (e.g. "dbm" or "gdbm") if recognized.
    
    Importing the given module may still fail, and opening the
    database using that module may still fail.
    """
    try:
        f = open(filename + os.extsep + 'pag', 'rb')
        f.close()
        if not (dbm.library == 'GNU gdbm' and sys.platform == 'os2emx'):
            f = open(filename + os.extsep + 'dir', 'rb')
            f.close()
        return 'dbm'
    except IOError:
        try:
            f = open(filename + os.extsep + 'db', 'rb')
            f.close()
            if dbm is not None:
                d = dbm.open(filename)
                d.close()
                return 'dbm'
        except (IOError, _dbmerror):
            pass

    try:
        os.stat(filename + os.extsep + 'dat')
        size = os.stat(filename + os.extsep + 'dir').st_size
        if size == 0:
            return 'dumbdbm'
        f = open(filename + os.extsep + 'dir', 'rb')
        try:
            if f.read(1) in ("'", '"'):
                return 'dumbdbm'
        finally:
            f.close()

    except (OSError, IOError):
        pass

    try:
        f = open(filename, 'rb')
    except IOError:
        return

    s16 = f.read(16)
    f.close()
    s = s16[0:4]
    if len(s) != 4:
        return ''
    else:
        try:
            magic, = struct.unpack('=l', s)
        except struct.error:
            return ''

        if magic == 324508366:
            return 'gdbm'
        if magic in (398689, 1628767744):
            return 'bsddb185'
        try:
            magic, = struct.unpack('=l', s16[-4:])
        except struct.error:
            return ''

        if magic in (398689, 1628767744):
            return 'dbhash'
        return ''


if __name__ == '__main__':
    for filename in sys.argv[1:]:
        print whichdb(filename) or 'UNKNOWN', filename