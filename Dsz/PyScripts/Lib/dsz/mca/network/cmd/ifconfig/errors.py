# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_FAILED = mcl.status.framework.ERR_START + 1
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 2
ERR_LOADLIBRARY_FAILED = mcl.status.framework.ERR_START + 3
ERR_GETPROCADDRESS_FAILED = mcl.status.framework.ERR_START + 4
ERR_MEM_ALLOC_FAILED = mcl.status.framework.ERR_START + 5
ERR_GETNETWORKPARAMS = mcl.status.framework.ERR_START + 6
ERR_GETADAPTERSINFO = mcl.status.framework.ERR_START + 7
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_FAILED: 'Unspecified failure',
   ERR_MARSHAL_FAILED: 'Failed to marshal data',
   ERR_LOADLIBRARY_FAILED: 'Unable to load required library',
   ERR_GETPROCADDRESS_FAILED: 'Unable to find a required function',
   ERR_MEM_ALLOC_FAILED: 'Failed to allocate necessary memory',
   ERR_GETNETWORKPARAMS: 'Unable to get network parameters',
   ERR_GETADAPTERSINFO: 'Unable to get adapter info'
   }