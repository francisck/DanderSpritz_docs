# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_GET_FULL_PATH_FAILED = mcl.status.framework.ERR_START + 2
ERR_GET_FAILED = mcl.status.framework.ERR_START + 3
ERR_SET_ATTRIBS_FAILED = mcl.status.framework.ERR_START + 4
ERR_OPEN_FILE_FAILED = mcl.status.framework.ERR_START + 5
ERR_SETCOMPRESSION_FAILED = mcl.status.framework.ERR_START + 6
ERR_LOADLIBRARY_FAILED = mcl.status.framework.ERR_START + 7
ERR_GETPROC_FAILED = mcl.status.framework.ERR_START + 8
ERR_ENCRYPT_FAILED = mcl.status.framework.ERR_START + 9
ERR_DECRYPT_FAILED = mcl.status.framework.ERR_START + 10
ERR_ENCRYPT_NOT_SUPPORTED = mcl.status.framework.ERR_START + 11
ERR_TIME_CONVERSION_FAILED = mcl.status.framework.ERR_START + 12
ERR_SETTIMES_FAILED = mcl.status.framework.ERR_START + 13
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 14
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_GET_FULL_PATH_FAILED: 'Unable to get full file path',
   ERR_GET_FAILED: 'Get of file attributes failed',
   ERR_SET_ATTRIBS_FAILED: 'Set of file attributes failed',
   ERR_OPEN_FILE_FAILED: 'Open of file failed',
   ERR_SETCOMPRESSION_FAILED: 'Set of compression failed',
   ERR_LOADLIBRARY_FAILED: 'Load of required library failed',
   ERR_GETPROC_FAILED: 'Get of required procedure failed',
   ERR_ENCRYPT_FAILED: 'Encrypt of file failed',
   ERR_DECRYPT_FAILED: 'Decrypt of file failed',
   ERR_ENCRYPT_NOT_SUPPORTED: 'File encryption not supported on this platform',
   ERR_TIME_CONVERSION_FAILED: 'Conversion to native time failed',
   ERR_SETTIMES_FAILED: 'Set of file times failed',
   ERR_NOT_IMPLEMENTED: 'Feature not implemented on this platform/filesystem'
   }