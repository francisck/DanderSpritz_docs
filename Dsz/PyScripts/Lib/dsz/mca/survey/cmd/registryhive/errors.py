# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_INVALID_HIVE = mcl.status.framework.ERR_START + 1
ERR_INVALID_ACTION = mcl.status.framework.ERR_START + 2
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 3
ERR_OPEN_FAILED = mcl.status.framework.ERR_START + 4
ERR_API_UNAVAILABLE = mcl.status.framework.ERR_START + 5
ERR_LOAD_FAILED = mcl.status.framework.ERR_START + 6
ERR_UNLOAD_FAILED = mcl.status.framework.ERR_START + 7
ERR_SAVE_FAILED = mcl.status.framework.ERR_START + 8
ERR_RESTORE_FAILED = mcl.status.framework.ERR_START + 9
ERR_UNLOAD_LIST_LOCKED = mcl.status.framework.ERR_START + 10
ERR_GET_FULL_PATH_FAILED = mcl.status.framework.ERR_START + 11
ERR_SEND_FAILED = mcl.status.framework.ERR_START + 12
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_INVALID_HIVE: 'Invalid hive',
   ERR_INVALID_ACTION: 'Invalid action',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_OPEN_FAILED: 'Failed to open registry key',
   ERR_API_UNAVAILABLE: 'Unable to access the registry API',
   ERR_LOAD_FAILED: 'Failed to load hive',
   ERR_UNLOAD_FAILED: 'Failed to unload hive',
   ERR_SAVE_FAILED: 'Failed to save hive to file',
   ERR_RESTORE_FAILED: 'Failed to restore key from file',
   ERR_UNLOAD_LIST_LOCKED: 'Unable to add hive to list of hives to unload.  Unload list is currently locked',
   ERR_GET_FULL_PATH_FAILED: 'Failed to get full path to hive',
   ERR_SEND_FAILED: 'Failed to send marshalled message'
   }