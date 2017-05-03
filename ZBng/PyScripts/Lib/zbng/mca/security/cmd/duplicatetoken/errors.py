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
ERR_CALLBACK_FAILED = mcl.status.framework.ERR_START + 3
ERR_LIST_OPEN_FAILED = mcl.status.framework.ERR_START + 4
ERR_LIST_QUERY_FAILED = mcl.status.framework.ERR_START + 5
ERR_OPEN_PROCESS_FAILED = mcl.status.framework.ERR_START + 6
ERR_OPEN_TOKEN_FAILED = mcl.status.framework.ERR_START + 7
ERR_DUPLICATE_FAILED = mcl.status.framework.ERR_START + 8
ERR_IMPERSONATE_FAILED = mcl.status.framework.ERR_START + 9
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_GET_API_FAILED: 'Get of required API failed',
   ERR_CALLBACK_FAILED: 'Callback with token information failed',
   ERR_LIST_OPEN_FAILED: 'Open of process list failed',
   ERR_LIST_QUERY_FAILED: 'Query of process list failed',
   ERR_OPEN_PROCESS_FAILED: 'Open of process failed',
   ERR_OPEN_TOKEN_FAILED: 'Open of process token failed',
   ERR_DUPLICATE_FAILED: 'Unable to duplicate process token',
   ERR_IMPERSONATE_FAILED: 'Failed to impersonate user with duplicated token'
   }