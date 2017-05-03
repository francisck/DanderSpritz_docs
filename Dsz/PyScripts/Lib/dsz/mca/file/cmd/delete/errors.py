# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_GET_FULL_PATH_FAILED = mcl.status.framework.ERR_START + 1
ERR_ENUM_FAILED = mcl.status.framework.ERR_START + 2
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 3
ERR_FILE_IS_A_DIR = mcl.status.framework.ERR_START + 4
ERR_DELETE_FAILED = mcl.status.framework.ERR_START + 5
ERR_API_FAILED = mcl.status.framework.ERR_START + 6
ERR_STAT_FAILED = mcl.status.framework.ERR_START + 7
ERR_DEL_PATH_UNC_AFTER_REBOOT = mcl.status.framework.ERR_START + 8
ERR_DONE_MAX_ENTRIES = mcl.status.framework.ERR_START + 9
ERR_NO_MAX_SPECIFIED = mcl.status.framework.ERR_START + 10
ERR_SEND_FAILED = mcl.status.framework.ERR_START + 11
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_GET_FULL_PATH_FAILED: 'Failed to get full path for deletion',
   ERR_ENUM_FAILED: 'Failed to enumerate directory for matching files',
   ERR_MARSHAL_FAILED: 'Marshaling of deletion data failed',
   ERR_FILE_IS_A_DIR: 'Given file is a directory -- refusing deletion',
   ERR_DELETE_FAILED: 'Deletion failed',
   ERR_API_FAILED: 'Failed to get delete api',
   ERR_STAT_FAILED: 'Unable to check file',
   ERR_DEL_PATH_UNC_AFTER_REBOOT: 'Cannot do delete-after-reboot action with network paths.',
   ERR_DONE_MAX_ENTRIES: 'Delete completed due to exceeding maximum entries',
   ERR_NO_MAX_SPECIFIED: 'No Max Entries was given',
   ERR_SEND_FAILED: 'Failed to send back data'
   }