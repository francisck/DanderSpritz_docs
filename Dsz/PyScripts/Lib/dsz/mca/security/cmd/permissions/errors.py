# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_GET_FULL_PATH_FAILED = mcl.status.framework.ERR_START + 2
ERR_GETSEC_FAILED = mcl.status.framework.ERR_START + 3
ERR_CALLBACK_FAILED = mcl.status.framework.ERR_START + 4
ERR_SET_ENTRIES_FAILED = mcl.status.framework.ERR_START + 5
ERR_SET_SECURITY_FAILED = mcl.status.framework.ERR_START + 6
ERR_INVALID_ACCESS_MODE = mcl.status.framework.ERR_START + 7
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_GET_FULL_PATH_FAILED: 'Get of full file path failed',
   ERR_GETSEC_FAILED: 'Get of security information failed',
   ERR_CALLBACK_FAILED: 'Callback failed',
   ERR_SET_ENTRIES_FAILED: 'Failed to add SID to ACL',
   ERR_SET_SECURITY_FAILED: 'Failed to set security info',
   ERR_INVALID_ACCESS_MODE: 'Invalid access mode'
   }