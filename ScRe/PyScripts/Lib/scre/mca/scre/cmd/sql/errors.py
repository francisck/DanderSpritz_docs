# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 2
ERR_ENV_ALLOC_FAILED = mcl.status.framework.ERR_START + 3
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 4
ERR_ODBC_ERROR = mcl.status.framework.ERR_START + 5
ERR_INVALID_HANDLE = mcl.status.framework.ERR_START + 6
ERR_NO_DATA = mcl.status.framework.ERR_START + 7
ERR_SERVER_STRING_PARSE_FAILED = mcl.status.framework.ERR_START + 8
ERR_DBC_ALLOC_FAILED = mcl.status.framework.ERR_START + 9
ERR_STMT_ALLOC_FAILED = mcl.status.framework.ERR_START + 10
ERR_CONN_FAILED = mcl.status.framework.ERR_START + 11
ERR_INTERNAL_ERROR = mcl.status.framework.ERR_START + 12
ERR_ROW_TOO_BIG = mcl.status.framework.ERR_START + 13
ERR_SET_COLUMN_INFO_FAILED = mcl.status.framework.ERR_START + 14
ERR_UNKNOWN_MESSAGE_TYPE = mcl.status.framework.ERR_START + 15
ERR_NO_CONNECTION = mcl.status.framework.ERR_START + 16
ERR_CONNECTION_LIST_LOCKED = mcl.status.framework.ERR_START + 17
ERR_INVALID_SQLITE_COMMAND = mcl.status.framework.ERR_START + 18
ERR_CLOSE_CONNECTION_FAILED = mcl.status.framework.ERR_START + 19
ERR_UNSUPPORTED_OPTION = mcl.status.framework.ERR_START + 20
ERR_STMT_ERROR = mcl.status.framework.ERR_START + 21
ERR_READONLY_ERROR = mcl.status.framework.ERR_START + 22
ERR_EXFIL_FAILED = mcl.status.framework.ERR_START + 23
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_ENV_ALLOC_FAILED: 'Alloc of SQL environment handle failed',
   ERR_ALLOC_FAILED: 'Memory allocation failed',
   ERR_ODBC_ERROR: 'ODBC error',
   ERR_INVALID_HANDLE: 'Invalid SQL Handle',
   ERR_NO_DATA: 'Query returned no SQL Data',
   ERR_SERVER_STRING_PARSE_FAILED: 'Parsing server list failed',
   ERR_DBC_ALLOC_FAILED: 'Alloc of SQL database handle failed',
   ERR_STMT_ALLOC_FAILED: 'Alloc of SQL statement handle failed',
   ERR_CONN_FAILED: 'Unable to establish connection to database',
   ERR_INTERNAL_ERROR: 'SQL: Internal error',
   ERR_ROW_TOO_BIG: 'SQL row data is too big for current collection size limit',
   ERR_SET_COLUMN_INFO_FAILED: 'Failed to set Column Info',
   ERR_UNKNOWN_MESSAGE_TYPE: 'Unknown LIST_DATA_TYPE',
   ERR_NO_CONNECTION: 'Unable to find connection',
   ERR_CONNECTION_LIST_LOCKED: 'Unable to add connection to list of handles.  Handle list is currently locked',
   ERR_INVALID_SQLITE_COMMAND: 'Command is not valid in SQLITE',
   ERR_CLOSE_CONNECTION_FAILED: 'Error occurred while closing the connection',
   ERR_UNSUPPORTED_OPTION: 'One or more options are not supported by the driver',
   ERR_STMT_ERROR: 'Error occurred while processing SQL statement',
   ERR_READONLY_ERROR: 'Invalid query.  Database is open in READ-ONLY mode',
   ERR_EXFIL_FAILED: 'Failed to exfil data'
   }