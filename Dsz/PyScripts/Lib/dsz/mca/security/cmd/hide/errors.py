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
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 3
ERR_LIBRARY_CALL_FAILED = mcl.status.framework.ERR_START + 4
ERR_JUMPUP_FAILED = mcl.status.framework.ERR_START + 5
ERR_HIDE_UNSUPPORTED_PLATFORM = mcl.status.framework.ERR_START + 6
ERR_HIDE_PROCESS_NOT_FOUND = mcl.status.framework.ERR_START + 7
ERR_HIDE_INVALID_LINKS = mcl.status.framework.ERR_START + 8
ERR_HIDE_SYSTEM_NOT_FOUND = mcl.status.framework.ERR_START + 9
ERR_HIDE_EXCEPTION = mcl.status.framework.ERR_START + 10
ERR_HIDE_NOT_HIDDEN = mcl.status.framework.ERR_START + 11
ERR_HIDE_INVALID_LOCATION = mcl.status.framework.ERR_START + 12
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_GET_API_FAILED: 'Failed to get required API',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_LIBRARY_CALL_FAILED: 'Library call failed',
   ERR_JUMPUP_FAILED: 'Privilege call failed',
   ERR_HIDE_UNSUPPORTED_PLATFORM: 'Unsupported platform',
   ERR_HIDE_PROCESS_NOT_FOUND: 'Process not found',
   ERR_HIDE_INVALID_LINKS: 'Invalid process links found in EPROCESS',
   ERR_HIDE_SYSTEM_NOT_FOUND: 'Unable to find SYSTEM process',
   ERR_HIDE_EXCEPTION: 'Exception thrown hiding process',
   ERR_HIDE_NOT_HIDDEN: 'Process is not hidden',
   ERR_HIDE_INVALID_LOCATION: 'Invalid EPROCESS location for given ID'
   }