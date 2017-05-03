# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_GET_LOCK_FAILED = mcl.status.framework.ERR_START + 1
ERR_TASK_ID_NOT_FOUND = mcl.status.framework.ERR_START + 2
ERR_DATA_IS_INVALID = mcl.status.framework.ERR_START + 3
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 4
ERR_LIBRARY_LOAD_FAILED = mcl.status.framework.ERR_START + 5
ERR_GET_EXPORT_FAILED = mcl.status.framework.ERR_START + 6
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 7
ERR_GET_API_FAILED = mcl.status.framework.ERR_START + 8
ERR_INJECT_SETUP_FAILED = mcl.status.framework.ERR_START + 9
ERR_INJECT_FAILED = mcl.status.framework.ERR_START + 10
ERR_INJECT_BAD_PARAMS = mcl.status.framework.ERR_START + 11
ERR_INJECT_EXCEPTION = mcl.status.framework.ERR_START + 12
ERR_INJECT_UNKNOWN = mcl.status.framework.ERR_START + 13
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_GET_LOCK_FAILED: 'Get of data lock failed',
   ERR_TASK_ID_NOT_FOUND: 'Task id not found for data',
   ERR_DATA_IS_INVALID: 'Data found matching given task id is not consistent with sent data',
   ERR_ALLOC_FAILED: 'Allocation of memory failed',
   ERR_LIBRARY_LOAD_FAILED: 'Failed to load library',
   ERR_GET_EXPORT_FAILED: 'Failed to get export from loaded library',
   ERR_MARSHAL_FAILED: 'Marshal of results failed',
   ERR_GET_API_FAILED: 'Get of required API failed',
   ERR_INJECT_SETUP_FAILED: 'Injection setup failed',
   ERR_INJECT_FAILED: 'Injection failed',
   ERR_INJECT_BAD_PARAMS: 'Inject: Invalid parameters',
   ERR_INJECT_EXCEPTION: 'Inject: Exception',
   ERR_INJECT_UNKNOWN: 'Inject: Unknown error'
   }