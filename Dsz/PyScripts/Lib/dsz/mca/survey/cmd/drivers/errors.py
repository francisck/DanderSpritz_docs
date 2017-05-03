# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_REQUIRED_FUNCTION_NOT_FOUND = mcl.status.framework.ERR_START + 2
ERR_LOAD_FAILED = mcl.status.framework.ERR_START + 3
ERR_UNLOAD_FAILED = mcl.status.framework.ERR_START + 4
ERR_GET_LIST_FAILED = mcl.status.framework.ERR_START + 5
ERR_BUFFER_INVALID = mcl.status.framework.ERR_START + 6
ERR_EXCEPTION = mcl.status.framework.ERR_START + 7
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 8
ERR_GET_API_FAILED = mcl.status.framework.ERR_START + 9
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_REQUIRED_FUNCTION_NOT_FOUND: 'A required function was not found',
   ERR_LOAD_FAILED: 'Load of driver failed',
   ERR_UNLOAD_FAILED: 'Unload of driver failed',
   ERR_GET_LIST_FAILED: 'Failed to query driver list',
   ERR_BUFFER_INVALID: 'System returned an invalid buffer',
   ERR_EXCEPTION: 'Unknown Exception',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_GET_API_FAILED: 'Failed to get required API'
   }