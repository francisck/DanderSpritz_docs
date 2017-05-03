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
ERR_MUTEX_TIMEOUT = mcl.status.framework.ERR_START + 3
ERR_DIBA_FAILURE = mcl.status.framework.ERR_START + 4
ERR_INVALID_PERSISTENCE = mcl.status.framework.ERR_START + 5
ERR_EXCEPTION = mcl.status.framework.ERR_START + 6
ERR_INIT_COMMS_FAILED = mcl.status.framework.ERR_START + 7
ERR_CANCELLED = mcl.status.framework.ERR_START + 8
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_MUTEX_FAILED: 'Not able to acquire exclusive access to KiSu module',
   ERR_MUTEX_TIMEOUT: 'Not able to acquire exclusive access to KiSu module within timeout period',
   ERR_DIBA_FAILURE: 'DiBa failure',
   ERR_INVALID_PERSISTENCE: 'Persistance method not supported',
   ERR_EXCEPTION: 'Exception encountered',
   ERR_INIT_COMMS_FAILED: 'Failed to initialize comms with KiSu instance',
   ERR_CANCELLED: 'Task was cancelled'
   }