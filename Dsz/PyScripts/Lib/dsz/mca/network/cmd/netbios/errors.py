# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_GET_LOCAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 2
ERR_BAD_SERVER_NAME = mcl.status.framework.ERR_START + 3
ERR_RESET_FAILED = mcl.status.framework.ERR_START + 4
ERR_QUERY_FAILED = mcl.status.framework.ERR_START + 5
ERR_ENUM_FAILED = mcl.status.framework.ERR_START + 6
ERR_QUERIES_FAILED = mcl.status.framework.ERR_START + 7
ERR_GET_NAMES_FAILED = mcl.status.framework.ERR_START + 8
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_GET_LOCAL_FAILED: 'Get of local name failed',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_BAD_SERVER_NAME: 'Invalid server name (too long?)',
   ERR_RESET_FAILED: 'Reset of netbios adapter failed',
   ERR_QUERY_FAILED: 'Netbios query failed',
   ERR_ENUM_FAILED: 'Unable to enumerate the netbios adapters',
   ERR_QUERIES_FAILED: 'No results were returned from any query',
   ERR_GET_NAMES_FAILED: 'Could not get network names due to null structure'
   }