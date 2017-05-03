# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_REGISTRY_WRITE_FAILED = mcl.status.framework.ERR_START + 1
ERR_DISK_WRITE_INSTALLER_FAILED = mcl.status.framework.ERR_START + 2
ERR_DISK_WRITE_DB_FAILED = mcl.status.framework.ERR_START + 3
ERR_FREEPARKING_CALL_FAILED = mcl.status.framework.ERR_START + 4
ERR_ALLOCATION_FAILED = mcl.status.framework.ERR_START + 5
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 6
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_REGISTRY_WRITE_FAILED: 'Failed to write to registry',
   ERR_DISK_WRITE_INSTALLER_FAILED: 'Failed to write installer to disk',
   ERR_DISK_WRITE_DB_FAILED: 'Failed to write AppCompat database to disk',
   ERR_FREEPARKING_CALL_FAILED: 'Failed while calculating installation vector',
   ERR_ALLOCATION_FAILED: 'Failed to gain a critical resource',
   ERR_MARSHAL_FAILED: 'Failed to marshall data'
   }