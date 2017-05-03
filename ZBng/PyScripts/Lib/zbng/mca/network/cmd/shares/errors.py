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
ERR_MAP_FAILED = mcl.status.framework.ERR_START + 3
ERR_REPORT_FAILED = mcl.status.framework.ERR_START + 4
ERR_ADD_FAILED_BAD_DRIVE = mcl.status.framework.ERR_START + 5
ERR_ADD_FAILED_BAD_SHARE = mcl.status.framework.ERR_START + 6
ERR_ADD_FAILED_BAD_PASSWORD = mcl.status.framework.ERR_START + 7
ERR_ADD_FAILED_WNET = mcl.status.framework.ERR_START + 8
ERR_CLEANUP_PREP_FAILED = mcl.status.framework.ERR_START + 9
ERR_DRIVES_ENUM_FAILED = mcl.status.framework.ERR_START + 10
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 11
ERR_NETUSEENUM_FAILED = mcl.status.framework.ERR_START + 12
ERR_LIST_ABORTED = mcl.status.framework.ERR_START + 13
ERR_NETUSEENUM_NO_DATA = mcl.status.framework.ERR_START + 14
ERR_WNETOPENENUM_FAILED = mcl.status.framework.ERR_START + 15
ERR_WNETENUMRESOURCE_FAILED = mcl.status.framework.ERR_START + 16
ERR_WMI_FAILED_INIT = mcl.status.framework.ERR_START + 17
ERR_CANCELLED = mcl.status.framework.ERR_START + 18
ERR_INFINITE_LOOP = mcl.status.framework.ERR_START + 19
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_MAP_FAILED: 'Failed to map the drive',
   ERR_REPORT_FAILED: 'Failed to report that the drive was mapped',
   ERR_ADD_FAILED_BAD_DRIVE: 'Local drive value is incorrect',
   ERR_ADD_FAILED_BAD_SHARE: 'Remote share/server name is invalid',
   ERR_ADD_FAILED_BAD_PASSWORD: 'Given password is not valid',
   ERR_ADD_FAILED_WNET: 'WNetAddConnection2 failed',
   ERR_CLEANUP_PREP_FAILED: 'Cleanup preperation failed',
   ERR_DRIVES_ENUM_FAILED: 'Enumerating drives failed',
   ERR_ALLOC_FAILED: 'Memory allocation failed',
   ERR_NETUSEENUM_FAILED: 'NetUseEnum failed',
   ERR_LIST_ABORTED: 'Shares list aborted',
   ERR_NETUSEENUM_NO_DATA: 'NetUseEnum returned no data',
   ERR_WNETOPENENUM_FAILED: 'WNetOpenEnum failed',
   ERR_WNETENUMRESOURCE_FAILED: 'WNetEnumResource failed',
   ERR_WMI_FAILED_INIT: 'WMI connection failed',
   ERR_CANCELLED: 'Command terminated externally',
   ERR_INFINITE_LOOP: 'Command unable to complete'
   }