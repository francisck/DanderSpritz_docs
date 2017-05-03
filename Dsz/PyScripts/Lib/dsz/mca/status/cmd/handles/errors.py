# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 1
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 2
ERR_GET_FAILED = mcl.status.framework.ERR_START + 3
ERR_GETTYPES_FAILED = mcl.status.framework.ERR_START + 4
ERR_GET_API_FAILED = mcl.status.framework.ERR_START + 5
ERR_PROCESS_NOT_FOUND = mcl.status.framework.ERR_START + 6
ERR_HANDLE_CANNOT_CLOSE = mcl.status.framework.ERR_START + 7
ERR_PROCESS_CANNOT_OPEN = mcl.status.framework.ERR_START + 8
ERR_EXCEPTION = mcl.status.framework.ERR_START + 9
ERR_QUERY_FAILED = mcl.status.framework.ERR_START + 10
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_GET_FAILED: 'Failed to get handles',
   ERR_GETTYPES_FAILED: 'Failed to get required object types',
   ERR_GET_API_FAILED: 'Get of required API failed',
   ERR_PROCESS_NOT_FOUND: 'Matching process not found',
   ERR_HANDLE_CANNOT_CLOSE: 'Failed to close handle',
   ERR_PROCESS_CANNOT_OPEN: 'Unable to open process',
   ERR_EXCEPTION: 'Exception encountered',
   ERR_QUERY_FAILED: 'Handle query failed'
   }