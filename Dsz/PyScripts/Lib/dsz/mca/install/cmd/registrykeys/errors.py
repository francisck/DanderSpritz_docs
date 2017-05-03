# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_CREATE_KEY_FAILED = mcl.status.framework.ERR_START + 1
ERR_OPEN_REGISTRY_FAILED = mcl.status.framework.ERR_START + 2
ERR_OPEN_KEY_FAILED = mcl.status.framework.ERR_START + 3
ERR_SETVALUE_FAILED = mcl.status.framework.ERR_START + 4
ERR_DELETE_FAILED = mcl.status.framework.ERR_START + 5
ERR_API_UNAVAILABLE = mcl.status.framework.ERR_START + 6
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_CREATE_KEY_FAILED: 'Failed to create the specified registry key',
   ERR_OPEN_REGISTRY_FAILED: 'Failed to open registry',
   ERR_OPEN_KEY_FAILED: 'Failed to open the specified registry key',
   ERR_SETVALUE_FAILED: 'Set of value failed',
   ERR_DELETE_FAILED: 'Delete of key(s) / value(s) failed',
   ERR_API_UNAVAILABLE: 'Unable to access the registry API'
   }