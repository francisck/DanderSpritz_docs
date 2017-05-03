# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: dbtables.py
_cvsid = '$Id$'
import re
import sys
import copy
import random
import struct
if sys.version_info[0] >= 3:
    import pickle
elif sys.version_info < (2, 6):
    import cPickle as pickle
else:
    import warnings
    w = warnings.catch_warnings()
    w.__enter__()
    try:
        warnings.filterwarnings('ignore', message='the cPickle module has been removed in Python 3.0', category=DeprecationWarning)
        import cPickle as pickle
    finally:
        w.__exit__()

    del w
try:
    from bsddb3 import db
except ImportError:
    from bsddb import db

class TableDBError(StandardError):
    pass


class TableAlreadyExists(TableDBError):
    pass


class Cond:
    """This condition matches everything"""

    def __call__(self, s):
        return 1


class ExactCond(Cond):
    """Acts as an exact match condition function"""

    def __init__(self, strtomatch):
        self.strtomatch = strtomatch

    def __call__(self, s):
        return s == self.strtomatch


class PrefixCond(Cond):
    """Acts as a condition function for matching a string prefix"""

    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, s):
        return s[:len(self.prefix)] == self.prefix


class PostfixCond(Cond):
    """Acts as a condition function for matching a string postfix"""

    def __init__(self, postfix):
        self.postfix = postfix

    def __call__(self, s):
        return s[-len(self.postfix):] == self.postfix


class LikeCond(Cond):
    """
    Acts as a function that will match using an SQL 'LIKE' style
    string.  Case insensitive and % signs are wild cards.
    This isn't perfect but it should work for the simple common cases.
    """

    def __init__(self, likestr, re_flags=re.IGNORECASE):
        chars_to_escape = '.*+()[]?'
        for char in chars_to_escape:
            likestr = likestr.replace(char, '\\' + char)

        self.likestr = likestr.replace('%', '.*')
        self.re = re.compile('^' + self.likestr + '$', re_flags)

    def __call__(self, s):
        return self.re.match(s)


_table_names_key = '__TABLE_NAMES__'
_columns = '._COLUMNS__'

def _columns_key(table):
    return table + _columns


_data = '._DATA_.'
_rowid = '._ROWID_.'
_rowid_str_len = 8

def _data_key(table, col, rowid):
    return table + _data + col + _data + rowid


def _search_col_data_key(table, col):
    return table + _data + col + _data


def _search_all_data_key(table):
    return table + _data


def _rowid_key(table, rowid):
    return table + _rowid + rowid + _rowid


def _search_rowid_key(table):
    return table + _rowid


def contains_metastrings(s):
    """Verify that the given string does not contain any
    metadata strings that might interfere with dbtables database operation.
    """
    if s.find(_table_names_key) >= 0 or s.find(_columns) >= 0 or s.find(_data) >= 0 or s.find(_rowid) >= 0:
        return 1
    else:
        return 0


class bsdTableDB:

    def __init__(self, filename, dbhome, create=0, truncate=0, mode=384, recover=0, dbflags=0):
        """bsdTableDB(filename, dbhome, create=0, truncate=0, mode=0600)
        
        Open database name in the dbhome Berkeley DB directory.
        Use keyword arguments when calling this constructor.
        """
        self.db = None
        myflags = db.DB_THREAD
        if create:
            myflags |= db.DB_CREATE
        flagsforenv = db.DB_INIT_MPOOL | db.DB_INIT_LOCK | db.DB_INIT_LOG | db.DB_INIT_TXN | dbflags
        try:
            dbflags |= db.DB_AUTO_COMMIT
        except AttributeError:
            pass

        if recover:
            flagsforenv = flagsforenv | db.DB_RECOVER
        self.env = db.DBEnv()
        self.env.set_lk_detect(db.DB_LOCK_DEFAULT)
        self.env.open(dbhome, myflags | flagsforenv)
        if truncate:
            myflags |= db.DB_TRUNCATE
        self.db = db.DB(self.env)
        self.db.set_get_returns_none(1)
        self.db.set_flags(db.DB_DUP)
        self.db.open(filename, db.DB_BTREE, dbflags | myflags, mode)
        self.dbfilename = filename
        if sys.version_info[0] >= 3:

            class cursor_py3k(object):

                def __init__(self, dbcursor):
                    self._dbcursor = dbcursor

                def close(self):
                    return self._dbcursor.close()

                def set_range(self, search):
                    v = self._dbcursor.set_range(bytes(search, 'iso8859-1'))
                    if v is not None:
                        v = (
                         v[0].decode('iso8859-1'),
                         v[1].decode('iso8859-1'))
                    return v

                def __next__(self):
                    v = getattr(self._dbcursor, 'next')()
                    if v is not None:
                        v = (
                         v[0].decode('iso8859-1'),
                         v[1].decode('iso8859-1'))
                    return v

            class db_py3k(object):

                def __init__(self, db):
                    self._db = db

                def cursor(self, txn=None):
                    return cursor_py3k(self._db.cursor(txn=txn))

                def has_key(self, key, txn=None):
                    return getattr(self._db, 'has_key')(bytes(key, 'iso8859-1'), txn=txn)

                def put(self, key, value, flags=0, txn=None):
                    key = bytes(key, 'iso8859-1')
                    if value is not None:
                        value = bytes(value, 'iso8859-1')
                    return self._db.put(key, value, flags=flags, txn=txn)

                def put_bytes(self, key, value, txn=None):
                    key = bytes(key, 'iso8859-1')
                    return self._db.put(key, value, txn=txn)

                def get(self, key, txn=None, flags=0):
                    key = bytes(key, 'iso8859-1')
                    v = self._db.get(key, txn=txn, flags=flags)
                    if v is not None:
                        v = v.decode('iso8859-1')
                    return v

                def get_bytes(self, key, txn=None, flags=0):
                    key = bytes(key, 'iso8859-1')
                    return self._db.get(key, txn=txn, flags=flags)

                def delete(self, key, txn=None):
                    key = bytes(key, 'iso8859-1')
                    return self._db.delete(key, txn=txn)

                def close(self):
                    return self._db.close()

            self.db = db_py3k(self.db)
        txn = self.env.txn_begin()
        try:
            if not getattr(self.db, 'has_key')(_table_names_key, txn):
                getattr(self.db, 'put_bytes', self.db.put)(_table_names_key, pickle.dumps([], 1), txn=txn)
        except:
            txn.abort()
            raise
        else:
            txn.commit()

        self.__tablecolumns = {}
        return

    def __del__(self):
        self.close()

    def close(self):
        if self.db is not None:
            self.db.close()
            self.db = None
        if self.env is not None:
            self.env.close()
            self.env = None
        return

    def checkpoint(self, mins=0):
        self.env.txn_checkpoint(mins)

    def sync(self):
        self.db.sync()

    def _db_print(self):
        """Print the database to stdout for debugging"""
        print '******** Printing raw database for debugging ********'
        cur = self.db.cursor()
        try:
            key, data = cur.first()
            while 1:
                print repr({key: data})
                next = cur.next()
                if next:
                    key, data = next
                else:
                    cur.close()
                    return

        except db.DBNotFoundError:
            cur.close()

    def CreateTable(self, table, columns):
        """CreateTable(table, columns) - Create a new table in the database.
        
        raises TableDBError if it already exists or for other DB errors.
        """
        txn = None
        try:
            if contains_metastrings(table):
                raise ValueError('bad table name: contains reserved metastrings')
            for column in columns:
                if contains_metastrings(column):
                    raise ValueError('bad column name: contains reserved metastrings')

            columnlist_key = _columns_key(table)
            if getattr(self.db, 'has_key')(columnlist_key):
                raise TableAlreadyExists, 'table already exists'
            txn = self.env.txn_begin()
            getattr(self.db, 'put_bytes', self.db.put)(columnlist_key, pickle.dumps(columns, 1), txn=txn)
            tablelist = pickle.loads(getattr(self.db, 'get_bytes', self.db.get)(_table_names_key, txn=txn, flags=db.DB_RMW))
            tablelist.append(table)
            self.db.delete(_table_names_key, txn=txn)
            getattr(self.db, 'put_bytes', self.db.put)(_table_names_key, pickle.dumps(tablelist, 1), txn=txn)
            txn.commit()
            txn = None
        except db.DBError as dberror:
            if txn:
                txn.abort()
            if sys.version_info < (2, 6):
                raise TableDBError, dberror[1]
            else:
                raise TableDBError, dberror.args[1]

        return

    def ListTableColumns(self, table):
        """Return a list of columns in the given table.
        [] if the table doesn't exist.
        """
        if contains_metastrings(table):
            raise ValueError, 'bad table name: contains reserved metastrings'
        columnlist_key = _columns_key(table)
        if not getattr(self.db, 'has_key')(columnlist_key):
            return []
        else:
            pickledcolumnlist = getattr(self.db, 'get_bytes', self.db.get)(columnlist_key)
            if pickledcolumnlist:
                return pickle.loads(pickledcolumnlist)
            return []

    def ListTables(self):
        """Return a list of tables in this database."""
        pickledtablelist = self.db.get_get(_table_names_key)
        if pickledtablelist:
            return pickle.loads(pickledtablelist)
        else:
            return []

    def CreateOrExtendTable(self, table, columns):
        """CreateOrExtendTable(table, columns)
        
        Create a new table in the database.
        
        If a table of this name already exists, extend it to have any
        additional columns present in the given list as well as
        all of its current columns.
        """
        try:
            self.CreateTable(table, columns)
        except TableAlreadyExists:
            txn = None
            try:
                columnlist_key = _columns_key(table)
                txn = self.env.txn_begin()
                oldcolumnlist = pickle.loads(getattr(self.db, 'get_bytes', self.db.get)(columnlist_key, txn=txn, flags=db.DB_RMW))
                oldcolumnhash = {}
                for c in oldcolumnlist:
                    oldcolumnhash[c] = c

                newcolumnlist = copy.copy(oldcolumnlist)
                for c in columns:
                    if c not in oldcolumnhash:
                        newcolumnlist.append(c)

                if newcolumnlist != oldcolumnlist:
                    self.db.delete(columnlist_key, txn=txn)
                    getattr(self.db, 'put_bytes', self.db.put)(columnlist_key, pickle.dumps(newcolumnlist, 1), txn=txn)
                txn.commit()
                txn = None
                self.__load_column_info(table)
            except db.DBError as dberror:
                if txn:
                    txn.abort()
                if sys.version_info < (2, 6):
                    raise TableDBError, dberror[1]
                else:
                    raise TableDBError, dberror.args[1]

        return

    def __load_column_info(self, table):
        """initialize the self.__tablecolumns dict"""
        try:
            tcolpickles = getattr(self.db, 'get_bytes', self.db.get)(_columns_key(table))
        except db.DBNotFoundError:
            raise TableDBError, 'unknown table: %r' % (table,)

        if not tcolpickles:
            raise TableDBError, 'unknown table: %r' % (table,)
        self.__tablecolumns[table] = pickle.loads(tcolpickles)

    def __new_rowid(self, table, txn):
        """Create a new unique row identifier"""
        unique = 0
        while not unique:
            blist = []
            for x in xrange(_rowid_str_len):
                blist.append(random.randint(0, 255))

            newid = struct.pack(('B' * _rowid_str_len), *blist)
            if sys.version_info[0] >= 3:
                newid = newid.decode('iso8859-1')
            try:
                self.db.put(_rowid_key(table, newid), None, txn=txn, flags=db.DB_NOOVERWRITE)
            except db.DBKeyExistError:
                pass
            else:
                unique = 1

        return newid

    def Insert(self, table, rowdict):
        """Insert(table, datadict) - Insert a new row into the table
        using the keys+values from rowdict as the column values.
        """
        txn = None
        try:
            if not getattr(self.db, 'has_key')(_columns_key(table)):
                raise TableDBError, 'unknown table'
            if table not in self.__tablecolumns:
                self.__load_column_info(table)
            for column in rowdict.keys():
                if not self.__tablecolumns[table].count(column):
                    raise TableDBError, 'unknown column: %r' % (column,)

            txn = self.env.txn_begin()
            rowid = self.__new_rowid(table, txn=txn)
            for column, dataitem in rowdict.items():
                self.db.put(_data_key(table, column, rowid), dataitem, txn=txn)

            txn.commit()
            txn = None
        except db.DBError as dberror:
            info = sys.exc_info()
            if txn:
                txn.abort()
                self.db.delete(_rowid_key(table, rowid))
            if sys.version_info < (2, 6):
                raise TableDBError, dberror[1], info[2]
            else:
                raise TableDBError, dberror.args[1], info[2]

        return

    def Modify(self, table, conditions={}, mappings={}):
        """Modify(table, conditions={}, mappings={}) - Modify items in rows matching 'conditions' using mapping functions in 'mappings'
        
        * table - the table name
        * conditions - a dictionary keyed on column names containing
          a condition callable expecting the data string as an
          argument and returning a boolean.
        * mappings - a dictionary keyed on column names containing a
          condition callable expecting the data string as an argument and
          returning the new string for that column.
        """
        try:
            matching_rowids = self.__Select(table, [], conditions)
            columns = mappings.keys()
            for rowid in matching_rowids.keys():
                txn = None
                try:
                    for column in columns:
                        txn = self.env.txn_begin()
                        try:
                            dataitem = self.db.get(_data_key(table, column, rowid), txn=txn)
                            self.db.delete(_data_key(table, column, rowid), txn=txn)
                        except db.DBNotFoundError:
                            dataitem = None

                        dataitem = mappings[column](dataitem)
                        if dataitem is not None:
                            self.db.put(_data_key(table, column, rowid), dataitem, txn=txn)
                        txn.commit()
                        txn = None

                except:
                    if txn:
                        txn.abort()
                    raise

        except db.DBError as dberror:
            if sys.version_info < (2, 6):
                raise TableDBError, dberror[1]
            else:
                raise TableDBError, dberror.args[1]

        return

    def Delete(self, table, conditions={}):
        """Delete(table, conditions) - Delete items matching the given
        conditions from the table.
        
        * conditions - a dictionary keyed on column names containing
          condition functions expecting the data string as an
          argument and returning a boolean.
        """
        try:
            matching_rowids = self.__Select(table, [], conditions)
            columns = self.__tablecolumns[table]
            for rowid in matching_rowids.keys():
                txn = None
                try:
                    txn = self.env.txn_begin()
                    for column in columns:
                        try:
                            self.db.delete(_data_key(table, column, rowid), txn=txn)
                        except db.DBNotFoundError:
                            pass

                    try:
                        self.db.delete(_rowid_key(table, rowid), txn=txn)
                    except db.DBNotFoundError:
                        pass

                    txn.commit()
                    txn = None
                except db.DBError as dberror:
                    if txn:
                        txn.abort()
                    raise

        except db.DBError as dberror:
            if sys.version_info < (2, 6):
                raise TableDBError, dberror[1]
            else:
                raise TableDBError, dberror.args[1]

        return

    def Select(self, table, columns, conditions={}):
        """Select(table, columns, conditions) - retrieve specific row data
        Returns a list of row column->value mapping dictionaries.
        
        * columns - a list of which column data to return.  If
          columns is None, all columns will be returned.
        * conditions - a dictionary keyed on column names
          containing callable conditions expecting the data string as an
          argument and returning a boolean.
        """
        try:
            if table not in self.__tablecolumns:
                self.__load_column_info(table)
            if columns is None:
                columns = self.__tablecolumns[table]
            matching_rowids = self.__Select(table, columns, conditions)
        except db.DBError as dberror:
            if sys.version_info < (2, 6):
                raise TableDBError, dberror[1]
            else:
                raise TableDBError, dberror.args[1]

        return matching_rowids.values()

    def __Select(self, table, columns, conditions):
        """__Select() - Used to implement Select and Delete (above)
        Returns a dictionary keyed on rowids containing dicts
        holding the row data for columns listed in the columns param
        that match the given conditions.
        * conditions is a dictionary keyed on column names
        containing callable conditions expecting the data string as an
        argument and returning a boolean.
        """
        if table not in self.__tablecolumns:
            self.__load_column_info(table)
        if columns is None:
            columns = self.tablecolumns[table]
        for column in columns + conditions.keys():
            if not self.__tablecolumns[table].count(column):
                raise TableDBError, 'unknown column: %r' % (column,)

        matching_rowids = {}
        rejected_rowids = {}

        def cmp_conditions(atuple, btuple):
            a = atuple[1]
            b = btuple[1]
            if type(a) is type(b):

                def cmp(a, b):
                    if a == b:
                        return 0
                    if a < b:
                        return -1
                    return 1

                if isinstance(a, PrefixCond) and isinstance(b, PrefixCond):
                    return cmp(len(b.prefix), len(a.prefix))
                if isinstance(a, LikeCond) and isinstance(b, LikeCond):
                    return cmp(len(b.likestr), len(a.likestr))
                return 0
            if isinstance(a, ExactCond):
                return -1
            if isinstance(b, ExactCond):
                return 1
            if isinstance(a, PrefixCond):
                return -1
            if isinstance(b, PrefixCond):
                return 1
            return 0

        if sys.version_info < (2, 6):
            conditionlist = conditions.items()
            conditionlist.sort(cmp_conditions)
        else:
            conditionlist = []
            for i in conditions.items():
                for j, k in enumerate(conditionlist):
                    r = cmp_conditions(k, i)
                    if r == 1:
                        conditionlist.insert(j, i)
                        break
                else:
                    conditionlist.append(i)

        cur = self.db.cursor()
        column_num = -1
        for column, condition in conditionlist:
            column_num = column_num + 1
            searchkey = _search_col_data_key(table, column)
            if column in columns:
                savethiscolumndata = 1
            else:
                savethiscolumndata = 0
            try:
                key, data = cur.set_range(searchkey)
                while key[:len(searchkey)] == searchkey:
                    rowid = key[-_rowid_str_len:]
                    if rowid not in rejected_rowids:
                        if not condition or condition(data):
                            if rowid not in matching_rowids:
                                matching_rowids[rowid] = {}
                            if savethiscolumndata:
                                matching_rowids[rowid][column] = data
                        else:
                            if rowid in matching_rowids:
                                del matching_rowids[rowid]
                            rejected_rowids[rowid] = rowid
                    key, data = cur.next()

            except db.DBError as dberror:
                if dberror.args[0] != db.DB_NOTFOUND:
                    raise
                continue

        cur.close()
        del rejected_rowids
        if len(columns) > 0:
            for rowid, rowdata in matching_rowids.items():
                for column in columns:
                    if column in rowdata:
                        continue
                    try:
                        rowdata[column] = self.db.get(_data_key(table, column, rowid))
                    except db.DBError as dberror:
                        if sys.version_info < (2, 6):
                            if dberror[0] != db.DB_NOTFOUND:
                                raise
                        elif dberror.args[0] != db.DB_NOTFOUND:
                            raise
                        rowdata[column] = None

        return matching_rowids

    def Drop(self, table):
        """Remove an entire table from the database"""
        txn = None
        try:
            txn = self.env.txn_begin()
            self.db.delete(_columns_key(table), txn=txn)
            cur = self.db.cursor(txn)
            table_key = _search_all_data_key(table)
            while 1:
                try:
                    key, data = cur.set_range(table_key)
                except db.DBNotFoundError:
                    break

                if key[:len(table_key)] != table_key:
                    break
                cur.delete()

            table_key = _search_rowid_key(table)
            while 1:
                try:
                    key, data = cur.set_range(table_key)
                except db.DBNotFoundError:
                    break

                if key[:len(table_key)] != table_key:
                    break
                cur.delete()

            cur.close()
            tablelist = pickle.loads(getattr(self.db, 'get_bytes', self.db.get)(_table_names_key, txn=txn, flags=db.DB_RMW))
            try:
                tablelist.remove(table)
            except ValueError:
                pass

            self.db.delete(_table_names_key, txn=txn)
            getattr(self.db, 'put_bytes', self.db.put)(_table_names_key, pickle.dumps(tablelist, 1), txn=txn)
            txn.commit()
            txn = None
            if table in self.__tablecolumns:
                del self.__tablecolumns[table]
        except db.DBError as dberror:
            if txn:
                txn.abort()
            raise TableDBError(dberror.args[1])

        return