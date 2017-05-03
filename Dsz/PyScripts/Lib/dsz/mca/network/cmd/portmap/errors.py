# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_GET_API_FAILED = mcl.status.framework.ERR_START + 2
ERR_GETHANDLES_FAILED = mcl.status.framework.ERR_START + 3
ERR_ALLOCATION_FAILED = mcl.status.framework.ERR_START + 4
ERR_CORRUPT_HANDLE_DATA = mcl.status.framework.ERR_START + 5
ERR_JUMPUP_FAILED = mcl.status.framework.ERR_START + 6
ERR_EXCEPTION_THROWN = mcl.status.framework.ERR_START + 7
ERR_BAD_EXCEPTION_HANDLING = mcl.status.framework.ERR_START + 8
ERR_CANT_GET_FUNCTIONS = mcl.status.framework.ERR_START + 9
ERR_UNSUPPORTED_PLATFORM = mcl.status.framework.ERR_START + 10
ERR_UNKNOWN = mcl.status.framework.ERR_START + 11
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_GET_API_FAILED: 'Get of required API failed',
   ERR_GETHANDLES_FAILED: 'Query for open handles failed',
   ERR_ALLOCATION_FAILED: 'Memory allocation failed',
   ERR_CORRUPT_HANDLE_DATA: 'The returned handle data does not seem to be valid',
   ERR_JUMPUP_FAILED: 'Privilege elevation failed',
   ERR_EXCEPTION_THROWN: 'Portmap threw an exception.  Report this to the developer!',
   ERR_BAD_EXCEPTION_HANDLING: 'Exception handling not valid',
   ERR_CANT_GET_FUNCTIONS: 'Failed to find required functions',
   ERR_UNSUPPORTED_PLATFORM: 'Unsupported platform',
   ERR_UNKNOWN: 'Unknown error'
   }