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
ERR_GET_API_FAILED = mcl.status.framework.ERR_START + 3
ERR_OPEN_DATA_PIPE_FAILED = mcl.status.framework.ERR_START + 4
ERR_INJECT_SETUP_FAILED = mcl.status.framework.ERR_START + 5
ERR_INJECT_FAILED = mcl.status.framework.ERR_START + 6
ERR_FAILED_TO_FIND_PROCESS = mcl.status.framework.ERR_START + 7
ERR_OPEN_PROCESS_FAILED = mcl.status.framework.ERR_START + 8
ERR_CONNECT_PIPE_FAILED = mcl.status.framework.ERR_START + 9
ERR_READ_PIPE_FAILED = mcl.status.framework.ERR_START + 10
ERR_EXCEPTION = mcl.status.framework.ERR_START + 11
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 12
ERR_INJECTION_FINISHED = mcl.status.framework.ERR_START + 13
ERR_GET_EXIT_CODE_FAILED = mcl.status.framework.ERR_START + 14
ERR_MISSING_BUFFER_DATA = mcl.status.framework.ERR_START + 15
ERR_INJECT_WRITE_FAILED = mcl.status.framework.ERR_START + 16
ERR_INJECT_THREAD_ENDED = mcl.status.framework.ERR_START + 17
ERR_INJECT_OPEN_PIPE_FAILED = mcl.status.framework.ERR_START + 18
ERR_INJECT_LOAD_LIBRARY_FAILED = mcl.status.framework.ERR_START + 19
ERR_INJECT_LSA_OPEN_FAILED = mcl.status.framework.ERR_START + 20
ERR_INJECT_LSA_QUERY_FAILED = mcl.status.framework.ERR_START + 21
ERR_INJECT_SAMI_CONNECT_FAILED = mcl.status.framework.ERR_START + 22
ERR_INJECT_SAMR_OPEN_DOMAIN_FAILED = mcl.status.framework.ERR_START + 23
ERR_INJECT_SAMR_ENUM_USERS_FAILED = mcl.status.framework.ERR_START + 24
ERR_INJECT_SAMR_OPEN_USER_FAILED = mcl.status.framework.ERR_START + 25
ERR_INJECT_SAMR_QUERY_USER_FAILED = mcl.status.framework.ERR_START + 26
ERR_INJECT_LSAI_OPEN_POLICY_FAILED = mcl.status.framework.ERR_START + 27
ERR_INJECT_REG_OPEN_FAILED = mcl.status.framework.ERR_START + 28
ERR_INJECT_LSAR_OPEN_SECRET_FAILED = mcl.status.framework.ERR_START + 29
ERR_INJECT_LSAR_QUERY_SECRET_FAILED = mcl.status.framework.ERR_START + 30
ERR_INJECT_POINTER_NULL = mcl.status.framework.ERR_START + 31
ERR_INJECT_EXCEPTION = mcl.status.framework.ERR_START + 32
ERR_REQUIRED_LIBRARY_NOT_LOADED = mcl.status.framework.ERR_START + 33
ERR_INJECT_DIGEST_ENUM_FAILED = mcl.status.framework.ERR_START + 34
ERR_INJECT_DIGEST_GET_LOGON_DATA_FAILED = mcl.status.framework.ERR_START + 35
ERR_INJECT_DIGEST_LOGON_TO_ID_FAILED = mcl.status.framework.ERR_START + 36
ERR_INJECT_DIGEST_LOG_SESS_PASSWD_GET_FAILED = mcl.status.framework.ERR_START + 37
ERR_INJECT_FIND_FUNCTION_1 = mcl.status.framework.ERR_START + 38
ERR_INJECT_FIND_FUNCTION_2 = mcl.status.framework.ERR_START + 39
ERR_INJECT_FIND_FUNCTION_3 = mcl.status.framework.ERR_START + 40
ERR_INJECT_FIND_FUNCTION_4 = mcl.status.framework.ERR_START + 41
ERR_INJECT_FIND_FUNCTION_5 = mcl.status.framework.ERR_START + 42
ERR_INJECT_GPA_FAILED_1 = mcl.status.framework.ERR_START + 50
ERR_INJECT_GPA_FAILED_2 = mcl.status.framework.ERR_START + 51
ERR_INJECT_GPA_FAILED_3 = mcl.status.framework.ERR_START + 52
ERR_INJECT_GPA_FAILED_4 = mcl.status.framework.ERR_START + 53
ERR_INJECT_GPA_FAILED_5 = mcl.status.framework.ERR_START + 54
ERR_INJECT_GPA_FAILED_6 = mcl.status.framework.ERR_START + 55
ERR_INJECT_GPA_FAILED_7 = mcl.status.framework.ERR_START + 56
ERR_INJECT_GPA_FAILED_8 = mcl.status.framework.ERR_START + 57
ERR_INJECT_GPA_FAILED_9 = mcl.status.framework.ERR_START + 58
ERR_INJECT_GPA_FAILED_10 = mcl.status.framework.ERR_START + 59
ERR_UNSUPPORTED_PLATFORM = mcl.status.framework.ERR_START + 60
ERR_INJECT_FUNCTION_INVALID = mcl.status.framework.ERR_START + 61
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_GET_API_FAILED: 'Failed to get required API',
   ERR_OPEN_DATA_PIPE_FAILED: 'Open of data pipe for transfer failed',
   ERR_INJECT_SETUP_FAILED: 'Setup of necessary injection functions failed',
   ERR_INJECT_FAILED: 'Injection into process failed',
   ERR_FAILED_TO_FIND_PROCESS: 'Failed to find required process',
   ERR_OPEN_PROCESS_FAILED: 'Unable to open process for injection',
   ERR_CONNECT_PIPE_FAILED: 'Connect to data pipe failed',
   ERR_READ_PIPE_FAILED: 'Read from data pipe failed',
   ERR_EXCEPTION: 'Exception encountered',
   ERR_ALLOC_FAILED: 'Memory allocation failed',
   ERR_INJECTION_FINISHED: 'Injection finished',
   ERR_GET_EXIT_CODE_FAILED: 'Get of injected thread exit code failed',
   ERR_MISSING_BUFFER_DATA: 'Data returned from injected thread is invalid',
   ERR_INJECT_WRITE_FAILED: 'Write of data to pipe failed',
   ERR_INJECT_THREAD_ENDED: 'Injection thread has closed abnormally',
   ERR_INJECT_OPEN_PIPE_FAILED: 'InjectThread: Open of data pipe failed',
   ERR_INJECT_LOAD_LIBRARY_FAILED: 'InjectThread: Failed to load required library',
   ERR_INJECT_LSA_OPEN_FAILED: 'InjectThread: LsaOpenPolicy call failed',
   ERR_INJECT_LSA_QUERY_FAILED: 'InjectThread: LsaQueryInformationPolicy call failed',
   ERR_INJECT_SAMI_CONNECT_FAILED: 'InjectThread: SamIConnect call failed',
   ERR_INJECT_SAMR_OPEN_DOMAIN_FAILED: 'InjectThread: SamrOpenDomain call failed',
   ERR_INJECT_SAMR_ENUM_USERS_FAILED: 'InjectThread: SamrEnumerateUsersInDomain call failed',
   ERR_INJECT_SAMR_OPEN_USER_FAILED: 'InjectThread: SamrOpenUser call failed',
   ERR_INJECT_SAMR_QUERY_USER_FAILED: 'InjectThread: SamrQueryInformationUser call failed',
   ERR_INJECT_LSAI_OPEN_POLICY_FAILED: 'InjectThread: LsaIOpenPolicyTrusted call failed',
   ERR_INJECT_REG_OPEN_FAILED: 'InjectThread: Failed to open registry key',
   ERR_INJECT_LSAR_OPEN_SECRET_FAILED: 'InjectThread: LsarOpenSecret call failed',
   ERR_INJECT_LSAR_QUERY_SECRET_FAILED: 'InjectThread: LsarQuerySecret call failed',
   ERR_INJECT_POINTER_NULL: 'InjectThread: Internal pointer is NULL',
   ERR_INJECT_EXCEPTION: 'InjectThread: Exception encountered',
   ERR_REQUIRED_LIBRARY_NOT_LOADED: 'Library required for operation not loaded',
   ERR_INJECT_DIGEST_ENUM_FAILED: 'InjectThread:  LsaEnumerateLogonSessions failed',
   ERR_INJECT_DIGEST_GET_LOGON_DATA_FAILED: 'InjectThread:  LsaGetLogonSessionData failed',
   ERR_INJECT_DIGEST_LOGON_TO_ID_FAILED: 'InjectThread:  LogSessHandlerLogonIdToPtr failed',
   ERR_INJECT_DIGEST_LOG_SESS_PASSWD_GET_FAILED: 'InjectThread:  LogSessHandlerPasswdGet failed',
   ERR_INJECT_FIND_FUNCTION_1: 'InjectThread:  Pattern match for function LogSessHandlerLogonIdToPtr failed',
   ERR_INJECT_FIND_FUNCTION_2: 'InjectThread:  Pattern match for function LogSessHandlerPasswdGet failed',
   ERR_INJECT_FIND_FUNCTION_3: 'InjectThread:  Pattern match for function LogSessHandlerRelease failed',
   ERR_INJECT_FIND_FUNCTION_4: 'InjectThread:  Pattern match for function StringFree failed',
   ERR_INJECT_FIND_FUNCTION_5: 'InjectThread:  Pattern match for function LsaEncryptMemory failed',
   ERR_INJECT_GPA_FAILED_1: 'InjectThread: Failed to get required procedure address (1)',
   ERR_INJECT_GPA_FAILED_2: 'InjectThread: Failed to get required procedure address (2)',
   ERR_INJECT_GPA_FAILED_3: 'InjectThread: Failed to get required procedure address (3)',
   ERR_INJECT_GPA_FAILED_4: 'InjectThread: Failed to get required procedure address (4)',
   ERR_INJECT_GPA_FAILED_5: 'InjectThread: Failed to get required procedure address (5)',
   ERR_INJECT_GPA_FAILED_6: 'InjectThread: Failed to get required procedure address (6)',
   ERR_INJECT_GPA_FAILED_7: 'InjectThread: Failed to get required procedure address (7)',
   ERR_INJECT_GPA_FAILED_8: 'InjectThread: Failed to get required procedure address (8)',
   ERR_INJECT_GPA_FAILED_9: 'InjectThread: Failed to get required procedure address (9)',
   ERR_INJECT_GPA_FAILED_10: 'InjectThread: Failed to get required procedure address (10)',
   ERR_UNSUPPORTED_PLATFORM: 'The desired operation is not supported on this platform.',
   ERR_INJECT_FUNCTION_INVALID: 'The function to inject cannot be located'
   }