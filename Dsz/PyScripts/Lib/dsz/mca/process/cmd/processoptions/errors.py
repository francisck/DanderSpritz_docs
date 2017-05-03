# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START
ERR_GET_API_FAILED = mcl.status.framework.ERR_START + 1
ERR_ID_WITH_API_NOT_SUPPORTED = mcl.status.framework.ERR_START + 2
ERR_ELEVATION_FAILED = mcl.status.framework.ERR_START + 3
ERR_SET_FAILED = mcl.status.framework.ERR_START + 4
ERR_RESET_LIMITED = mcl.status.framework.ERR_START + 5
ERR_QUERY_FAILED = mcl.status.framework.ERR_START + 6
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_GET_API_FAILED: 'Failed to get required API',
   ERR_ID_WITH_API_NOT_SUPPORTED: 'The use of a process id without elevation is not supported',
   ERR_ELEVATION_FAILED: 'Elevation failed',
   ERR_SET_FAILED: 'Set of options failed',
   ERR_RESET_LIMITED: 'Reseting of options without elevation is not supported',
   ERR_QUERY_FAILED: 'Query of options failed'
   }