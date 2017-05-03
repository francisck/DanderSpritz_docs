# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_OPEN_FAILED = mcl.status.framework.ERR_START + 2
ERR_GET_FIRST_FAILED = mcl.status.framework.ERR_START + 3
ERR_GET_NEXT_FAILED = mcl.status.framework.ERR_START + 4
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 5
ERR_ADD_TO_LIST_FAILED = mcl.status.framework.ERR_START + 6
ERR_GET_FROM_LIST_FAILED = mcl.status.framework.ERR_START + 7
ERR_EXCEPTION = mcl.status.framework.ERR_START + 8
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 9
ERR_INIT_FAILED = mcl.status.framework.ERR_START + 10
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_OPEN_FAILED: 'Open of process list failed',
   ERR_GET_FIRST_FAILED: 'Get of first process failed',
   ERR_GET_NEXT_FAILED: 'Get of next process failed',
   ERR_ALLOC_FAILED: 'Memory allocation failed',
   ERR_ADD_TO_LIST_FAILED: 'Failed to add process information to list',
   ERR_GET_FROM_LIST_FAILED: 'Failed to get process information from list',
   ERR_EXCEPTION: 'Exception while getting process list',
   ERR_NOT_IMPLEMENTED: 'Not supported on this platform',
   ERR_INIT_FAILED: 'Initialization failed'
   }