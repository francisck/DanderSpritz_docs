# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_INVALID_LOGNAME = mcl.status.framework.ERR_START + 2
ERR_QUERY_FAILED = mcl.status.framework.ERR_START + 3
ERR_EXCEPTION_THROWN = mcl.status.framework.ERR_START + 4
ERR_READ_FAILURE = mcl.status.framework.ERR_START + 5
ERR_NO_ENTRIES = mcl.status.framework.ERR_START + 6
ERR_BAD_COUNT = mcl.status.framework.ERR_START + 7
ERR_OPEN_FAILURE = mcl.status.framework.ERR_START + 8
ERR_MEMORY_FAILURE = mcl.status.framework.ERR_START + 9
ERR_GET_COUNT_FAILED = mcl.status.framework.ERR_START + 10
ERR_API_NOT_FOUND = mcl.status.framework.ERR_START + 11
ERR_CONNECT_FAILED = mcl.status.framework.ERR_START + 12
ERR_CREATE_RENDER_FAILURE = mcl.status.framework.ERR_START + 13
ERR_NO_MATCHING_ENTRIES = mcl.status.framework.ERR_START + 14
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_INVALID_LOGNAME: 'Invalid log name',
   ERR_QUERY_FAILED: 'Query failed',
   ERR_EXCEPTION_THROWN: 'The program threw an exception',
   ERR_READ_FAILURE: 'Unable to read event log',
   ERR_NO_ENTRIES: 'Specified event log is empty',
   ERR_BAD_COUNT: 'Unable to obtain number of event log records',
   ERR_OPEN_FAILURE: 'Could not open event logs',
   ERR_MEMORY_FAILURE: 'Failed to allocate memory',
   ERR_GET_COUNT_FAILED: 'Failed to get start/end entry',
   ERR_API_NOT_FOUND: 'Required API was not found',
   ERR_CONNECT_FAILED: 'Connect to remote target failed',
   ERR_CREATE_RENDER_FAILURE: 'Failed to create render context',
   ERR_NO_MATCHING_ENTRIES: 'No matching entries found'
   }