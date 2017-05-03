# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 1
ERR_WMI_FAILED_TO_START = mcl.status.framework.ERR_START + 2
ERR_WMI_CREATE_PROCESS_FAILED = mcl.status.framework.ERR_START + 3
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_WMI_FAILED_TO_START: 'WMI interface failed to start',
   ERR_WMI_CREATE_PROCESS_FAILED: 'WMI failed to start the process'
   }