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
ERR_BAD_TIME = mcl.status.framework.ERR_START + 3
ERR_JOB_ADD_FAILED = mcl.status.framework.ERR_START + 4
ERR_JOB_DELETE_FAILED = mcl.status.framework.ERR_START + 5
ERR_NOT_ALLOWED = mcl.status.framework.ERR_START + 6
ERR_COM_INIT_FAILED = mcl.status.framework.ERR_START + 7
ERR_FAILED_TO_OPEN = mcl.status.framework.ERR_START + 8
ERR_COM_CREATE_FAILED = mcl.status.framework.ERR_START + 9
ERR_COM_CONNECT_FAILED = mcl.status.framework.ERR_START + 10
ERR_COM_SECURITY_FAILED = mcl.status.framework.ERR_START + 11
ERR_COM_SECURITY2_FAILED = mcl.status.framework.ERR_START + 12
ERR_COM_QUERY_FAILED = mcl.status.framework.ERR_START + 13
ERR_ENUM_FAILED = mcl.status.framework.ERR_START + 14
ERR_GET_TIME_FAILED = mcl.status.framework.ERR_START + 15
ERR_TIME_CONVERT_FAILED = mcl.status.framework.ERR_START + 16
ERR_REMOTE_NOT_ALLOWED = mcl.status.framework.ERR_START + 17
ERR_FAILED_TO_CONNECT = mcl.status.framework.ERR_START + 18
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_BAD_TIME: 'Problem determining time',
   ERR_JOB_ADD_FAILED: 'Failed to schedule job',
   ERR_JOB_DELETE_FAILED: 'Failed to delete scheduled job(s)',
   ERR_NOT_ALLOWED: 'Given scheduler type not allowed / valid on this system version',
   ERR_COM_INIT_FAILED: 'Initialization of COM failed',
   ERR_FAILED_TO_OPEN: 'Failed to open task scheduler',
   ERR_COM_CREATE_FAILED: 'Failed to create COM object',
   ERR_COM_CONNECT_FAILED: 'Failed to connect through COM',
   ERR_COM_SECURITY_FAILED: 'Failed to initialize COM security',
   ERR_COM_SECURITY2_FAILED: 'Failed to initialize WMI security',
   ERR_COM_QUERY_FAILED: 'Failed query via COM',
   ERR_ENUM_FAILED: 'Enumeration of task failed',
   ERR_GET_TIME_FAILED: 'Unable to get time',
   ERR_TIME_CONVERT_FAILED: 'Time conversion failed',
   ERR_REMOTE_NOT_ALLOWED: 'Remote scheduler not available for this type',
   ERR_FAILED_TO_CONNECT: 'Failed to connect to specified target'
   }