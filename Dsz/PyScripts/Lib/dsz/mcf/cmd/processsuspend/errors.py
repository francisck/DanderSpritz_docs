# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_GET_API_FAILED = mcl.status.framework.ERR_START + 1
ERR_MODIFICATION_FAILED = mcl.status.framework.ERR_START + 2
ERR_JUMPUP_FAILED = mcl.status.framework.ERR_START + 3
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 4
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 5
ERR_THREAD_ACCESS_DENIED = mcl.status.framework.ERR_START + 6
ERR_SUSPEND_THREAD_FAILED = mcl.status.framework.ERR_START + 7
ERR_GET_SNAPSHOT_FAILED = mcl.status.framework.ERR_START + 8
ERR_SNAPSHOT_NO_THREADS = mcl.status.framework.ERR_START + 9
ERR_MEMORY_ALLOC_FAIL = mcl.status.framework.ERR_START + 10
ERR_NOT_ALL_THREADS_RESUMED = mcl.status.framework.ERR_START + 11
ERR_VERIFY_OPEN_FAILED = mcl.status.framework.ERR_START + 12
ERR_VERIFY_GET_FIRST_FAILED = mcl.status.framework.ERR_START + 13
ERR_VERIFY_PROCESS_NOT_FOUND = mcl.status.framework.ERR_START + 14
ERR_VERIFY_PROCESS_NT_AUTHORITY = mcl.status.framework.ERR_START + 15
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_GET_API_FAILED: 'Failed to get required API',
   ERR_MODIFICATION_FAILED: 'Process modification failed',
   ERR_JUMPUP_FAILED: 'Privilege elevation failed',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_THREAD_ACCESS_DENIED: 'Access Denied when attempting to suspend thread',
   ERR_SUSPEND_THREAD_FAILED: 'System Call Suspend Thread Failed',
   ERR_GET_SNAPSHOT_FAILED: "CreateToolhelp32Snapshot failed to get snapshot of system's threads",
   ERR_SNAPSHOT_NO_THREADS: 'No threads were found in snapshot that belonged to associated PID',
   ERR_MEMORY_ALLOC_FAIL: 'Failed to Allocate Memory',
   ERR_NOT_ALL_THREADS_RESUMED: 'Unable to resume all threads in process, system might be in a untrusted state',
   ERR_VERIFY_OPEN_FAILED: 'Unable to open process list',
   ERR_VERIFY_GET_FIRST_FAILED: 'Unable to get first process from process list',
   ERR_VERIFY_PROCESS_NOT_FOUND: "PID wasn't found within process list",
   ERR_VERIFY_PROCESS_NT_AUTHORITY: 'Process runs in context of NT_AUTHORITY. Use -force if you really want to suspend process'
   }