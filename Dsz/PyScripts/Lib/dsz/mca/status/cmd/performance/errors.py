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
ERR_REG_OPEN_FAILED = mcl.status.framework.ERR_START + 3
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 4
ERR_QUERY_FAILED = mcl.status.framework.ERR_START + 5
ERR_INVALID_FORMAT = mcl.status.framework.ERR_START + 6
ERR_UNHANDLED_REVISION = mcl.status.framework.ERR_START + 7
ERR_INTERNAL_ERROR = mcl.status.framework.ERR_START + 8
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_REG_OPEN_FAILED: 'Open of registry failed',
   ERR_ALLOC_FAILED: 'Failed to allocate memory',
   ERR_QUERY_FAILED: 'Failed to query performance data',
   ERR_INVALID_FORMAT: 'Performance data is not formed correctly',
   ERR_UNHANDLED_REVISION: 'Unhandled performance data revision',
   ERR_INTERNAL_ERROR: 'Internal error parsing performance data'
   }