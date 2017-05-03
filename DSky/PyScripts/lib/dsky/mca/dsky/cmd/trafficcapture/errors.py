# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_DEVICE_OPEN_FAILED = mcl.status.framework.ERR_START + 2
ERR_IOCTL_FAILED = mcl.status.framework.ERR_START + 3
ERR_OUTPUT_SIZE_MISMATCH = mcl.status.framework.ERR_START + 4
ERR_FILTER_TOO_LONG = mcl.status.framework.ERR_START + 5
ERR_OPEN_KEY_FAILED = mcl.status.framework.ERR_START + 6
ERR_UPDATE_REGISTRY_FAILED = mcl.status.framework.ERR_START + 7
ERR_INVALID_CONTROL_TYPE = mcl.status.framework.ERR_START + 8
ERR_UNKNOWN_ERROR = mcl.status.framework.ERR_START + 9
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_DEVICE_OPEN_FAILED: 'Open of driver device failed',
   ERR_IOCTL_FAILED: 'Send/Receive of IOCTL to driver failed',
   ERR_OUTPUT_SIZE_MISMATCH: 'Returned data from driver does not match expected size',
   ERR_FILTER_TOO_LONG: 'Given filter exceeds maximum allowable filter size',
   ERR_OPEN_KEY_FAILED: 'Open of registry key failed',
   ERR_UPDATE_REGISTRY_FAILED: 'Update of registry failed',
   ERR_INVALID_CONTROL_TYPE: 'Invalid control type',
   ERR_UNKNOWN_ERROR: 'Unknown error'
   }