# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_OPEN_PROCESS_FAILED = mcl.status.framework.ERR_START + 2
ERR_MODULES_OPEN_FAILED = mcl.status.framework.ERR_START + 3
ERR_MODULES_GET_FAILED = mcl.status.framework.ERR_START + 4
ERR_TOKEN_OPEN_FAILED = mcl.status.framework.ERR_START + 5
ERR_TOKEN_USER_QUERY_FAILED = mcl.status.framework.ERR_START + 6
ERR_TOKEN_OWNER_QUERY_FAILED = mcl.status.framework.ERR_START + 7
ERR_TOKEN_PGROUP_QUERY_FAILED = mcl.status.framework.ERR_START + 8
ERR_TOKEN_GROUPS_QUERY_FAILED = mcl.status.framework.ERR_START + 9
ERR_TOKEN_PRIVS_QUERY_FAILED = mcl.status.framework.ERR_START + 10
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 11
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_OPEN_PROCESS_FAILED: 'Open of process failed',
   ERR_MODULES_OPEN_FAILED: 'Open of process module list failed',
   ERR_MODULES_GET_FAILED: 'Get of first module in process failed',
   ERR_TOKEN_OPEN_FAILED: 'Open of process token failed',
   ERR_TOKEN_USER_QUERY_FAILED: 'Query of process user failed',
   ERR_TOKEN_OWNER_QUERY_FAILED: 'Query of process owner failed',
   ERR_TOKEN_PGROUP_QUERY_FAILED: 'Query of process primary group failed',
   ERR_TOKEN_GROUPS_QUERY_FAILED: 'Query of process groups failed',
   ERR_TOKEN_PRIVS_QUERY_FAILED: 'Query of process privileges failed',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform'
   }