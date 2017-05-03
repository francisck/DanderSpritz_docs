# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
"""Support for Berkeley DB 4.1 through 4.8 with a simple interface.

For the full featured object oriented interface use the bsddb.db module
instead.  It mirrors the Oracle Berkeley DB C API.
"""
import sys
absolute_import = sys.version_info[0] >= 3
if sys.version_info >= (2, 6) and sys.version_info < (3, 0):
    import warnings
    if sys.py3kwarning and __name__ != 'bsddb3':
        warnings.warnpy3k('in 3.x, the bsddb module has been removed; please use the pybsddb project instead', DeprecationWarning, 2)
    warnings.filterwarnings('ignore', '.*CObject.*', DeprecationWarning, 'bsddb.__init__')
try:
    if __name__ == 'bsddb3':
        if absolute_import:
            exec 'from . import _pybsddb'
        else:
            import _pybsddb
        _bsddb = _pybsddb
        from bsddb3.dbutils import DeadlockWrap as _DeadlockWrap
    else:
        import _bsddb
        from bsddb.dbutils import DeadlockWrap as _DeadlockWrap
except ImportError:
    import sys
    del sys.modules[__name__]
    raise

db = _db = _bsddb
__version__ = db.__version__
error = db.DBError
import sys
import os
from weakref import ref
if sys.version_info < (2, 6):
    import UserDict
    MutableMapping = UserDict.DictMixin
else:
    import collections
    MutableMapping = collections.MutableMapping

class _iter_mixin(MutableMapping):

    def _make_iter_cursor(self):
        cur = _DeadlockWrap(self.db.cursor)
        key = id(cur)
        self._cursor_refs[key] = ref(cur, self._gen_cref_cleaner(key))
        return cur

    def _gen_cref_cleaner(self, key):
        return lambda ref: self._cursor_refs.pop(key, None)

    def __iter__(self):
        self._kill_iteration = False
        self._in_iter += 1
        try:
            try:
                cur = self._make_iter_cursor()
                key = _DeadlockWrap(cur.first, 0, 0, 0)[0]
                yield key
                next = getattr(cur, 'next')
                while 1:
                    try:
                        key = _DeadlockWrap(next, 0, 0, 0)[0]
                        yield key
                    except _bsddb.DBCursorClosedError:
                        if self._kill_iteration:
                            raise RuntimeError('Database changed size during iteration.')
                        cur = self._make_iter_cursor()
                        _DeadlockWrap(cur.set, key, 0, 0, 0)
                        next = getattr(cur, 'next')

            except _bsddb.DBNotFoundError:
                pass
            except _bsddb.DBCursorClosedError:
                pass

        except:
            self._in_iter -= 1
            raise

        self._in_iter -= 1

    def iteritems(self):
        if not self.db:
            return
        self._kill_iteration = False
        self._in_iter += 1
        try:
            try:
                cur = self._make_iter_cursor()
                kv = _DeadlockWrap(cur.first)
                key = kv[0]
                yield kv
                next = getattr(cur, 'next')
                while 1:
                    try:
                        kv = _DeadlockWrap(next)
                        key = kv[0]
                        yield kv
                    except _bsddb.DBCursorClosedError:
                        if self._kill_iteration:
                            raise RuntimeError('Database changed size during iteration.')
                        cur = self._make_iter_cursor()
                        _DeadlockWrap(cur.set, key, 0, 0, 0)
                        next = getattr(cur, 'next')

            except _bsddb.DBNotFoundError:
                pass
            except _bsddb.DBCursorClosedError:
                pass

        except:
            self._in_iter -= 1
            raise

        self._in_iter -= 1


class _DBWithCursor(_iter_mixin):
    """
    A simple wrapper around DB that makes it look like the bsddbobject in
    the old module.  It uses a cursor as needed to provide DB traversal.
    """

    def __init__(self, db):
        self.db = db
        self.db.set_get_returns_none(0)
        self.dbc = None
        self.saved_dbc_key = None
        self._cursor_refs = {}
        self._in_iter = 0
        self._kill_iteration = False
        return

    def __del__(self):
        self.close()

    def _checkCursor(self):
        if self.dbc is None:
            self.dbc = _DeadlockWrap(self.db.cursor)
            if self.saved_dbc_key is not None:
                _DeadlockWrap(self.dbc.set, self.saved_dbc_key)
                self.saved_dbc_key = None
        return

    def _closeCursors(self, save=1):
        if self.dbc:
            c = self.dbc
            self.dbc = None
            if save:
                try:
                    self.saved_dbc_key = _DeadlockWrap(c.current, 0, 0, 0)[0]
                except db.DBError:
                    pass

            _DeadlockWrap(c.close)
            del c
        for cref in self._cursor_refs.values():
            c = cref()
            if c is not None:
                _DeadlockWrap(c.close)

        return

    def _checkOpen(self):
        if self.db is None:
            raise error, 'BSDDB object has already been closed'
        return

    def isOpen(self):
        return self.db is not None

    def __len__(self):
        self._checkOpen()
        return _DeadlockWrap(lambda : len(self.db))

    if sys.version_info >= (2, 6):

        def __repr__(self):
            if self.isOpen():
                return repr(dict(_DeadlockWrap(self.db.items)))
            return repr(dict())

    def __getitem__(self, key):
        self._checkOpen()
        return _DeadlockWrap(lambda : self.db[key])

    def __setitem__(self, key, value):
        self._checkOpen()
        self._closeCursors()
        if self._in_iter and key not in self:
            self._kill_iteration = True

        def wrapF():
            self.db[key] = value

        _DeadlockWrap(wrapF)

    def __delitem__(self, key):
        self._checkOpen()
        self._closeCursors()
        if self._in_iter and key in self:
            self._kill_iteration = True

        def wrapF():
            del self.db[key]

        _DeadlockWrap(wrapF)

    def close(self):
        self._closeCursors(save=0)
        if self.dbc is not None:
            _DeadlockWrap(self.dbc.close)
        v = 0
        if self.db is not None:
            v = _DeadlockWrap(self.db.close)
        self.dbc = None
        self.db = None
        return v

    def keys(self):
        self._checkOpen()
        return _DeadlockWrap(self.db.keys)

    def has_key(self, key):
        self._checkOpen()
        return _DeadlockWrap(self.db.has_key, key)

    def set_location(self, key):
        self._checkOpen()
        self._checkCursor()
        return _DeadlockWrap(self.dbc.set_range, key)

    def next(self):
        self._checkOpen()
        self._checkCursor()
        rv = _DeadlockWrap(getattr(self.dbc, 'next'))
        return rv

    if sys.version_info[0] >= 3:
        next = __next__

    def previous(self):
        self._checkOpen()
        self._checkCursor()
        rv = _DeadlockWrap(self.dbc.prev)
        return rv

    def first(self):
        self._checkOpen()
        self.saved_dbc_key = None
        self._checkCursor()
        rv = _DeadlockWrap(self.dbc.first)
        return rv

    def last(self):
        self._checkOpen()
        self.saved_dbc_key = None
        self._checkCursor()
        rv = _DeadlockWrap(self.dbc.last)
        return rv

    def sync(self):
        self._checkOpen()
        return _DeadlockWrap(self.db.sync)


def hashopen(file, flag='c', mode=438, pgsize=None, ffactor=None, nelem=None, cachesize=None, lorder=None, hflags=0):
    flags = _checkflag(flag, file)
    e = _openDBEnv(cachesize)
    d = db.DB(e)
    d.set_flags(hflags)
    if pgsize is not None:
        d.set_pagesize(pgsize)
    if lorder is not None:
        d.set_lorder(lorder)
    if ffactor is not None:
        d.set_h_ffactor(ffactor)
    if nelem is not None:
        d.set_h_nelem(nelem)
    d.open(file, db.DB_HASH, flags, mode)
    return _DBWithCursor(d)


def btopen(file, flag='c', mode=438, btflags=0, cachesize=None, maxkeypage=None, minkeypage=None, pgsize=None, lorder=None):
    flags = _checkflag(flag, file)
    e = _openDBEnv(cachesize)
    d = db.DB(e)
    if pgsize is not None:
        d.set_pagesize(pgsize)
    if lorder is not None:
        d.set_lorder(lorder)
    d.set_flags(btflags)
    if minkeypage is not None:
        d.set_bt_minkey(minkeypage)
    if maxkeypage is not None:
        d.set_bt_maxkey(maxkeypage)
    d.open(file, db.DB_BTREE, flags, mode)
    return _DBWithCursor(d)


def rnopen(file, flag='c', mode=438, rnflags=0, cachesize=None, pgsize=None, lorder=None, rlen=None, delim=None, source=None, pad=None):
    flags = _checkflag(flag, file)
    e = _openDBEnv(cachesize)
    d = db.DB(e)
    if pgsize is not None:
        d.set_pagesize(pgsize)
    if lorder is not None:
        d.set_lorder(lorder)
    d.set_flags(rnflags)
    if delim is not None:
        d.set_re_delim(delim)
    if rlen is not None:
        d.set_re_len(rlen)
    if source is not None:
        d.set_re_source(source)
    if pad is not None:
        d.set_re_pad(pad)
    d.open(file, db.DB_RECNO, flags, mode)
    return _DBWithCursor(d)


def _openDBEnv(cachesize):
    e = db.DBEnv()
    if cachesize is not None:
        if cachesize >= 20480:
            e.set_cachesize(0, cachesize)
        else:
            raise error, 'cachesize must be >= 20480'
    e.set_lk_detect(db.DB_LOCK_DEFAULT)
    e.open('.', db.DB_PRIVATE | db.DB_CREATE | db.DB_THREAD | db.DB_INIT_LOCK | db.DB_INIT_MPOOL)
    return e


def _checkflag(flag, file):
    if flag == 'r':
        flags = db.DB_RDONLY
    elif flag == 'rw':
        flags = 0
    elif flag == 'w':
        flags = db.DB_CREATE
    elif flag == 'c':
        flags = db.DB_CREATE
    elif flag == 'n':
        flags = db.DB_CREATE
        if file is not None and os.path.isfile(file):
            os.unlink(file)
    else:
        raise error, "flags should be one of 'r', 'w', 'c' or 'n'"
    return flags | db.DB_THREAD


try:
    import thread as T
    del T
except ImportError:
    db.DB_THREAD = 0