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
ERR_OPEN_FAILED = mcl.status.framework.ERR_START + 3
ERR_QUERY_FAILED = mcl.status.framework.ERR_START + 4
ERR_NOT_FOUND = mcl.status.framework.ERR_START + 5
ERR_API_NOT_FOUND = mcl.status.framework.ERR_START + 6
ERR_CONNECT_FAILED = mcl.status.framework.ERR_START + 7
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_OPEN_FAILED: 'Could not open packages database',
   ERR_QUERY_FAILED: 'Query of packages information failed',
   ERR_NOT_FOUND: 'No packages found',
   ERR_API_NOT_FOUND: 'A required API was not found',
   ERR_CONNECT_FAILED: 'Failed to connect to remote target'
   }