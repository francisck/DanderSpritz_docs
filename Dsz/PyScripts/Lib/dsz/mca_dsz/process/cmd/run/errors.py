# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_CHANGE_USERS_FAILED = mcl.status.framework.ERR_START + 1
ERR_GET_FULL_PATH_FAILED = mcl.status.framework.ERR_START + 2
ERR_SETUP_STREAMS_FAILED = mcl.status.framework.ERR_START + 3
ERR_CREATE_PROCESS_FAILED = mcl.status.framework.ERR_START + 4
ERR_CREATE_SEND_INFO_FAILED = mcl.status.framework.ERR_START + 5
ERR_CREATE_WAIT_FAILED = mcl.status.framework.ERR_START + 6
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 7
ERR_CREATE_REDIRECT_FAILED = mcl.status.framework.ERR_START + 8
ERR_WRITE_FAILED = mcl.status.framework.ERR_START + 9
ERR_EXCEPTION = mcl.status.framework.ERR_START + 10
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_CHANGE_USERS_FAILED: 'Unable to change users',
   ERR_GET_FULL_PATH_FAILED: 'Unable to get full path to executable',
   ERR_SETUP_STREAMS_FAILED: 'Setup of standard streams for redirection failed',
   ERR_CREATE_PROCESS_FAILED: 'Start of process failed',
   ERR_CREATE_SEND_INFO_FAILED: 'Send of started process information failed',
   ERR_CREATE_WAIT_FAILED: 'Wait for process termination failed',
   ERR_MARSHAL_FAILED: 'Marshaling of data failed',
   ERR_CREATE_REDIRECT_FAILED: 'Setup for I/O redirection failed',
   ERR_WRITE_FAILED: 'Write to process failed',
   ERR_EXCEPTION: 'Exception thrown starting process'
   }