# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAMETERS = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 2
ERR_BAD_PROCESS = mcl.status.framework.ERR_START + 3
ERR_DUPLICATE_FAILED = mcl.status.framework.ERR_START + 4
ERR_CREATE_FILEMAP_FAILED = mcl.status.framework.ERR_START + 5
ERR_EMPTY_FILE = mcl.status.framework.ERR_START + 6
ERR_MAP_VIEW_FAILED = mcl.status.framework.ERR_START + 7
ERR_CALLBACK_FAILED = mcl.status.framework.ERR_START + 8
ERR_MEMORY_ALLOC_FAILED = mcl.status.framework.ERR_START + 9
ERR_MEMORY_READ_FAILED = mcl.status.framework.ERR_START + 10
ERR_ELEVATION_API_FAILED = mcl.status.framework.ERR_START + 11
ERR_ELEVATED_OPEN_FAILED = mcl.status.framework.ERR_START + 12
ERR_LOCK_FAILED = mcl.status.framework.ERR_START + 13
ERR_INVALID_OFFSET = mcl.status.framework.ERR_START + 14
ERR_FP_MOVE_FAILED = mcl.status.framework.ERR_START + 15
ERR_EOF_FAILED = mcl.status.framework.ERR_START + 16
ERR_TRIM_ERROR = mcl.status.framework.ERR_START + 17
ERR_FILE_READ_FAILED = mcl.status.framework.ERR_START + 18
ERR_FILE_WRITE_FAILED = mcl.status.framework.ERR_START + 19
ERR_GET_NAME_FAILED = mcl.status.framework.ERR_START + 20
ERR_GET_HANDLES_FAILED = mcl.status.framework.ERR_START + 21
ERR_GETTYPES_FAILED = mcl.status.framework.ERR_START + 22
ERR_LOAD_LIBRARY = mcl.status.framework.ERR_START + 23
ERR_PROC_ADDR = mcl.status.framework.ERR_START + 24
ERR_UNLOCK_FAILED = mcl.status.framework.ERR_START + 25
errorStrings = {ERR_INVALID_PARAMETERS: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_BAD_PROCESS: 'Unable to open process',
   ERR_DUPLICATE_FAILED: 'Unable to duplicate file handle',
   ERR_CREATE_FILEMAP_FAILED: 'Unable to create file mapping',
   ERR_EMPTY_FILE: 'File contains 0 bytes of data',
   ERR_MAP_VIEW_FAILED: 'Unable to map view of file',
   ERR_CALLBACK_FAILED: 'Callback failed',
   ERR_MEMORY_ALLOC_FAILED: 'Failed to allocate memory',
   ERR_MEMORY_READ_FAILED: 'Failed to read process memory',
   ERR_ELEVATION_API_FAILED: 'Failed to acquire elevation API',
   ERR_ELEVATED_OPEN_FAILED: 'Elevated open process failed',
   ERR_LOCK_FAILED: 'Failed to lock end of file',
   ERR_INVALID_OFFSET: 'Invalid offsets specified',
   ERR_FP_MOVE_FAILED: 'Failed to move the file pointer',
   ERR_EOF_FAILED: 'Failed to set EOF',
   ERR_TRIM_ERROR: 'Incorrect new filesize after trim',
   ERR_FILE_READ_FAILED: 'Failed to read from file',
   ERR_FILE_WRITE_FAILED: 'Failed to write to file',
   ERR_GET_NAME_FAILED: 'Failed to get a filename associated with the address',
   ERR_GET_HANDLES_FAILED: 'Failed to get handles',
   ERR_GETTYPES_FAILED: 'Failed to get required object types',
   ERR_LOAD_LIBRARY: 'Failed to load needed library',
   ERR_PROC_ADDR: 'Failed to acquired needed procedure',
   ERR_UNLOCK_FAILED: 'Failed to unlock a locked file'
   }