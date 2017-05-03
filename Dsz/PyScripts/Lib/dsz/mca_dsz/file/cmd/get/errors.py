# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAMETERS = mcl.status.framework.ERR_START
ERR_GET_FULL_PATH_FAILED = mcl.status.framework.ERR_START + 1
ERR_INVALID_DATE_TYPE = mcl.status.framework.ERR_START + 2
ERR_OFFSET_AND_MASK_USED = mcl.status.framework.ERR_START + 3
ERR_LOGFILE_ERROR = mcl.status.framework.ERR_START + 4
ERR_OPEN_FAILED = mcl.status.framework.ERR_START + 5
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 6
ERR_READ_FAILED = mcl.status.framework.ERR_START + 7
ERR_SEND_FAILED = mcl.status.framework.ERR_START + 8
ERR_FILE_SENT = mcl.status.framework.ERR_START + 9
ERR_ENUM_FAILED = mcl.status.framework.ERR_START + 10
ERR_DONE_MAX_ENTRIES = mcl.status.framework.ERR_START + 11
ERR_EXCEPTION_ERROR = mcl.status.framework.ERR_START + 12
ERR_GETTING_API_FAILED = mcl.status.framework.ERR_START + 13
errorStrings = {ERR_INVALID_PARAMETERS: 'Invalid parameter(s)',
   ERR_GET_FULL_PATH_FAILED: 'Failed to get full path',
   ERR_INVALID_DATE_TYPE: 'Invalid date type',
   ERR_OFFSET_AND_MASK_USED: 'Offset/GetSize cannot be used in combination with a file mask',
   ERR_LOGFILE_ERROR: 'Unable to create logging file',
   ERR_OPEN_FAILED: 'Open of file failed',
   ERR_ALLOC_FAILED: 'Memory allocation failed',
   ERR_READ_FAILED: 'Read of file failed',
   ERR_SEND_FAILED: 'Send of data failed',
   ERR_FILE_SENT: 'Get file sent to LP',
   ERR_ENUM_FAILED: 'Enumeration of files for get failed',
   ERR_DONE_MAX_ENTRIES: 'Get completed due to exceeding maximum entries',
   ERR_EXCEPTION_ERROR: 'Encountered an exception',
   ERR_GETTING_API_FAILED: 'Failed to get the file API'
   }