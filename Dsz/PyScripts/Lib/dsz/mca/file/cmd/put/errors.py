# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_OPEN_FAILED = mcl.status.framework.ERR_START + 1
ERR_WRITE_FAILED = mcl.status.framework.ERR_START + 2
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 3
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 4
ERR_GET_FULL_PATH_FAILED = mcl.status.framework.ERR_START + 5
ERR_RECORD_FOR_DELETION_FAILED = mcl.status.framework.ERR_START + 6
ERR_GET_API_FAILED = mcl.status.framework.ERR_START + 7
ERR_LOCK_FAILED = mcl.status.framework.ERR_START + 8
ERR_CALLBACK_FAILED = mcl.status.framework.ERR_START + 9
ERR_NODE_GET_FAILED = mcl.status.framework.ERR_START + 10
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_OPEN_FAILED: 'Failed to open file for write',
   ERR_WRITE_FAILED: 'Failed to write data to file',
   ERR_MARSHAL_FAILED: 'Error marshaling data',
   ERR_ALLOC_FAILED: 'Allocation of memory failed',
   ERR_GET_FULL_PATH_FAILED: 'Error obtaining absolute path',
   ERR_RECORD_FOR_DELETION_FAILED: 'Failed to register file for deletion',
   ERR_GET_API_FAILED: 'Unable to obtain a required API',
   ERR_LOCK_FAILED: 'Get of lock failed',
   ERR_CALLBACK_FAILED: 'Callback for file data failed',
   ERR_NODE_GET_FAILED: 'Failed to find file node for task'
   }