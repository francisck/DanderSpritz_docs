# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_MUTEX_FAILED = mcl.status.framework.ERR_START + 2
ERR_MEMORY_ALLOCATION_FAILED = mcl.status.framework.ERR_START + 3
ERR_KISU_FAILURE = mcl.status.framework.ERR_START + 4
ERR_TOO_MANY_INSTANCES = mcl.status.framework.ERR_START + 5
ERR_NO_KISU_INSTANCES = mcl.status.framework.ERR_START + 6
ERR_KISU_NOT_INITALIZED = mcl.status.framework.ERR_START + 7
ERR_DATA_IS_INVALID = mcl.status.framework.ERR_START + 8
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_MUTEX_FAILED: 'Failed to acquire mutex',
   ERR_MEMORY_ALLOCATION_FAILED: 'Unable to allocate memory',
   ERR_KISU_FAILURE: 'KiSu failure',
   ERR_TOO_MANY_INSTANCES: 'Too many KiSu instances found',
   ERR_NO_KISU_INSTANCES: 'No KiSu instances found',
   ERR_KISU_NOT_INITALIZED: 'KiSu comms library not initialized',
   ERR_DATA_IS_INVALID: 'Data is invalid'
   }