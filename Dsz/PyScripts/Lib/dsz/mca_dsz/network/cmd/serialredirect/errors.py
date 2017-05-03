# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_MEMORY_ALLOC_FAILED = mcl.status.framework.ERR_START + 2
ERR_EXCEPTION = mcl.status.framework.ERR_START + 3
ERR_INTERNAL_ERROR = mcl.status.framework.ERR_START + 4
ERR_ADD_TO_LIST_FAILED = mcl.status.framework.ERR_START + 5
ERR_GET_FROM_LIST_FAILED = mcl.status.framework.ERR_START + 6
ERR_CONNECT_FAILURE = mcl.status.framework.ERR_START + 7
ERR_CONNECT_ACCESS_DENIED = mcl.status.framework.ERR_START + 8
ERR_CONNECT_FILE_NOT_FOUND = mcl.status.framework.ERR_START + 9
ERR_UNABLE_TO_DUPLICATE_HANDLE = mcl.status.framework.ERR_START + 10
ERR_GET_COMM_STATE = mcl.status.framework.ERR_START + 11
ERR_SET_COMM_STATE = mcl.status.framework.ERR_START + 12
ERR_COMM_PORT_UNDEFINED = mcl.status.framework.ERR_START + 13
ERR_INDEX_NOT_FOUND = mcl.status.framework.ERR_START + 14
ERR_THREAD_FAILED = mcl.status.framework.ERR_START + 15
ERR_MUTEX_FAILED = mcl.status.framework.ERR_START + 16
ERR_SHUTDOWN = mcl.status.framework.ERR_START + 17
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling of data failed',
   ERR_MEMORY_ALLOC_FAILED: 'Allocation of memory failed',
   ERR_EXCEPTION: 'An exception occurred',
   ERR_INTERNAL_ERROR: 'An internal error occurred',
   ERR_ADD_TO_LIST_FAILED: 'Failed to add object to list',
   ERR_GET_FROM_LIST_FAILED: 'Failed to get object from list',
   ERR_CONNECT_FAILURE: 'Unable to connect to COM Port',
   ERR_CONNECT_ACCESS_DENIED: 'Access Denied to Serial Port',
   ERR_CONNECT_FILE_NOT_FOUND: 'Unable to find defined COM Port',
   ERR_UNABLE_TO_DUPLICATE_HANDLE: 'Failed to duplicate given handle',
   ERR_GET_COMM_STATE: 'Failed to get state of COM port defined',
   ERR_SET_COMM_STATE: 'Failed to set state of COM port defined with given parameters',
   ERR_COMM_PORT_UNDEFINED: 'COM Port name was not defined',
   ERR_INDEX_NOT_FOUND: 'Index for comm port not found',
   ERR_THREAD_FAILED: 'Failed to start thread',
   ERR_MUTEX_FAILED: 'Could not reserve the connection',
   ERR_SHUTDOWN: 'COMM port is shutdown / shutting-down'
   }