# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_SET_FAILED = mcl.status.framework.ERR_START + 1
ERR_GET_FAILED = mcl.status.framework.ERR_START + 2
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 3
ERR_NOT_A_DIR = mcl.status.framework.ERR_START + 4
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_SET_FAILED: 'Failed to change directory',
   ERR_GET_FAILED: 'Failed to get current working directory',
   ERR_MARSHAL_FAILED: 'Error marshaling data',
   ERR_NOT_A_DIR: 'The given path is not a directory'
   }