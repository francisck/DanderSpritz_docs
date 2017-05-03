# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_GET_API_FAILED = mcl.status.framework.ERR_START + 2
ERR_EDIT_FAILED = mcl.status.framework.ERR_START + 3
ERR_INJECT_LOADLIBRARY_FAILED = mcl.status.framework.ERR_START + 4
ERR_INJECT_GETPROCADDRESS_FAILED = mcl.status.framework.ERR_START + 5
ERR_INJECT_ADDRESSNOTFOUND = mcl.status.framework.ERR_START + 6
ERR_INJECT_FILESIZEERROR = mcl.status.framework.ERR_START + 7
ERR_INJECT_RESOURCE_LOCK_FAILED = mcl.status.framework.ERR_START + 8
ERR_INJECT_SETFILEPOINTER = mcl.status.framework.ERR_START + 9
ERR_INJECT_LOGFILECORRUPT = mcl.status.framework.ERR_START + 10
ERR_INJECT_RECORDTOOLARGE = mcl.status.framework.ERR_START + 11
ERR_INJECT_EXCEPTIONTHROWN = mcl.status.framework.ERR_START + 12
ERR_INJECT_INVALID_RECORD_NUMBER = mcl.status.framework.ERR_START + 13
ERR_INJECT_GET_LOG_FAILED = mcl.status.framework.ERR_START + 14
ERR_INJECT_INJECTION_SETUP_FAILED = mcl.status.framework.ERR_START + 15
ERR_INJECT_OPEN_PROCESS_FAILED = mcl.status.framework.ERR_START + 16
ERR_INJECT_INJECTION_FAILED = mcl.status.framework.ERR_START + 17
ERR_INJECT_ALLOC_FAILED = mcl.status.framework.ERR_START + 18
ERR_INJECT_ATOMNOTFOUND = mcl.status.framework.ERR_START + 19
ERR_INJECT_ATOMMATCHNOTFOUND = mcl.status.framework.ERR_START + 20
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_GET_API_FAILED: 'Get of required API failed',
   ERR_EDIT_FAILED: 'Edit of log failed',
   ERR_INJECT_LOADLIBRARY_FAILED: 'LoadLibrary failed within injected code',
   ERR_INJECT_GETPROCADDRESS_FAILED: 'GetProcAddress failed within injected code',
   ERR_INJECT_ADDRESSNOTFOUND: 'Injection code unable to find usable address',
   ERR_INJECT_FILESIZEERROR: 'ViewSize does not match ActualMaxFileSize',
   ERR_INJECT_RESOURCE_LOCK_FAILED: 'Failed to obtain resource lock for requested log file',
   ERR_INJECT_SETFILEPOINTER: 'SetFilePointer failed within injected code',
   ERR_INJECT_LOGFILECORRUPT: 'Logfile is corrupt',
   ERR_INJECT_RECORDTOOLARGE: 'Record too large to delete',
   ERR_INJECT_EXCEPTIONTHROWN: 'Injected code threw an exception',
   ERR_INJECT_INVALID_RECORD_NUMBER: 'Record number not found within given log',
   ERR_INJECT_GET_LOG_FAILED: 'Failed to get location of log file',
   ERR_INJECT_INJECTION_SETUP_FAILED: 'Setup for injection failed',
   ERR_INJECT_OPEN_PROCESS_FAILED: 'Open of logging host process failed',
   ERR_INJECT_INJECTION_FAILED: 'Injection failed',
   ERR_INJECT_ALLOC_FAILED: 'Memory allocation failed',
   ERR_INJECT_ATOMNOTFOUND: 'ATOM value not found',
   ERR_INJECT_ATOMMATCHNOTFOUND: 'No ATOM match was found'
   }