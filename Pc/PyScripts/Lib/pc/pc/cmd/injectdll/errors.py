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
ERR_OPEN_PROCESS_FAILED = mcl.status.framework.ERR_START + 3
ERR_INJECT_SETUP_FAILED = mcl.status.framework.ERR_START + 4
ERR_INJECT_FAILED = mcl.status.framework.ERR_START + 5
ERR_LOAD_FAILED = mcl.status.framework.ERR_START + 6
ERR_LOAD_MAY_HAVE_FAILED = mcl.status.framework.ERR_START + 7
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 8
ERR_EXCEPTION_THROWN = mcl.status.framework.ERR_START + 9
ERR_UNKNOWN = mcl.status.framework.ERR_START + 10
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Failed to marshal data',
   ERR_GET_API_FAILED: 'Failed to get required API',
   ERR_OPEN_PROCESS_FAILED: 'Open of process failed',
   ERR_INJECT_SETUP_FAILED: 'Setup for thread injection failed',
   ERR_INJECT_FAILED: 'Thread injection failed',
   ERR_LOAD_FAILED: 'Unable to load requested library',
   ERR_LOAD_MAY_HAVE_FAILED: 'Injected thread returned success, but no load address was reported.  The lib may or may not have been run',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_EXCEPTION_THROWN: 'An exception was thrown completing the action',
   ERR_UNKNOWN: 'An unknown failure occurred'
   }