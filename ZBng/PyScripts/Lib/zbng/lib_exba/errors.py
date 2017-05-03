# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAMETER = mcl.status.framework.ERR_START
ERR_UNSUPPORTED_PLATFORM = mcl.status.framework.ERR_START + 1
ERR_EXCEPTION = mcl.status.framework.ERR_START + 2
ERR_UNKNOWN = mcl.status.framework.ERR_START + 3
ERR_CANT_FIND_PROCESS = mcl.status.framework.ERR_START + 4
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 5
ERR_GET_SID_FAILED = mcl.status.framework.ERR_START + 6
ERR_INJECTION_SETUP_FAILED = mcl.status.framework.ERR_START + 7
ERR_REMOTE_ALLOC_FAILED = mcl.status.framework.ERR_START + 8
ERR_INJECTION_1_FAILED = mcl.status.framework.ERR_START + 9
ERR_INJECTION_2_FAILED = mcl.status.framework.ERR_START + 10
ERR_ALREADY_PATCHED = mcl.status.framework.ERR_START + 11
ERR_SEARCH_FAILED = mcl.status.framework.ERR_START + 12
ERR_INJECT_GPA_FAILED = mcl.status.framework.ERR_START + 13
ERR_INJECT_PATCH_FAILED = mcl.status.framework.ERR_START + 14
ERR_INJECT_WRITEPROCESSMEMORY = mcl.status.framework.ERR_START + 15
ERR_INJECT_LOADLIBRARY_FAILED = mcl.status.framework.ERR_START + 16
ERR_INJECT_LSAOPENPOLICY_FAILED = mcl.status.framework.ERR_START + 17
ERR_INJECT_LSAQUERYINFORMATIONPOLICY_FAILED = mcl.status.framework.ERR_START + 18
ERR_INJECT_SAMICONNECT_FAILED = mcl.status.framework.ERR_START + 19
ERR_INJECT_SAMROPENDOMAIN_FAILED = mcl.status.framework.ERR_START + 20
ERR_INJECT_SAMRENUMERATEUSERSINDOMAIN_FAILED = mcl.status.framework.ERR_START + 21
ERR_INJECT_SAMROPENUSER_FAILED = mcl.status.framework.ERR_START + 22
ERR_INJECT_SAMRQUERYINFORMATIONUSER_FAILED = mcl.status.framework.ERR_START + 23
errorStrings = {ERR_INVALID_PARAMETER: 'Invalid parameter(s)',
   ERR_UNSUPPORTED_PLATFORM: 'Unsupported platform',
   ERR_EXCEPTION: 'Exception thrown',
   ERR_UNKNOWN: 'Unknown error',
   ERR_CANT_FIND_PROCESS: 'Unable to find required process',
   ERR_ALLOC_FAILED: 'Memory allocation failed',
   ERR_GET_SID_FAILED: 'Failed to get user sid',
   ERR_INJECTION_SETUP_FAILED: 'Injection setup failed',
   ERR_REMOTE_ALLOC_FAILED: 'Memory allocation/manipulation in other process failed',
   ERR_INJECTION_1_FAILED: 'Injection failed (1)',
   ERR_INJECTION_2_FAILED: 'Injection failed (2)',
   ERR_ALREADY_PATCHED: 'Lsass seems to be patched already',
   ERR_SEARCH_FAILED: 'Search for required information failed',
   ERR_INJECT_GPA_FAILED: 'GetProcAddress failed (in injected function)',
   ERR_INJECT_PATCH_FAILED: 'Patch failed (in injected function)',
   ERR_INJECT_WRITEPROCESSMEMORY: 'Write memory failed (in injected function)',
   ERR_INJECT_LOADLIBRARY_FAILED: 'LoadLibrary failed (in injected function)',
   ERR_INJECT_LSAOPENPOLICY_FAILED: 'LsaOpenPolicy failed (in injected function)',
   ERR_INJECT_LSAQUERYINFORMATIONPOLICY_FAILED: 'LsaQueryInformationPolicy failed (in injected function)',
   ERR_INJECT_SAMICONNECT_FAILED: 'SamIConnect failed (in injected function)',
   ERR_INJECT_SAMROPENDOMAIN_FAILED: 'SamrOpenDomain failed (in injected function)',
   ERR_INJECT_SAMRENUMERATEUSERSINDOMAIN_FAILED: 'SamrEnumerateUsersInDomain failed (in injected function)',
   ERR_INJECT_SAMROPENUSER_FAILED: 'SamrOpenUser failed (in injected function)',
   ERR_INJECT_SAMRQUERYINFORMATIONUSER_FAILED: 'SamrQueryInformationUser failed (in injected function)'
   }