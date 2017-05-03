# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
ERR_SUCCESS = 0
ERR_CANNOT_FIND_SUPPORT_PROCESS = 1
ERR_CANNOT_FIND_REQUIRED_FUNCTION = 2
ERR_UNABLE_TO_OPEN_SUPPORT_PROCESS = 3
ERR_UNABLE_TO_OPEN_TARGET_PROCESS = 4
ERR_UNABLE_TO_OPEN_KERNEL = 5
ERR_UNABLE_TO_ALLOCATE_MEMORY_IN_SUPPORT_PROCESS = 6
ERR_UNABLE_TO_ALLOCATE_MEMORY_IN_TARGET_PROCESS = 7
ERR_UNABLE_TO_ALLOCATE_MEMORY_IN_KERNEL = 8
ERR_UNABLE_TO_INSTALL_SUPPORT_FUNCTIONS = 9
ERR_PRIVILEGE_LIBRARY_FAILED = 10
ERR_CREATE_REMOTE_THREAD_FAILED = 11
ERR_INVALID_PARAMETERS = 12
ERR_MEMORY_ALLOCATION_FAILED = 13
ERR_64_BIT_MISMATCH = 14
ERR_CANNOT_OPEN_PROCESS_FOR_INJECTION = 15
ERR_ALREADY_INSTALLED = 16
ERR_CANNOT_WRITE_FUNCTION = 17
ERR_NOT_YET_INSTALLED = 18
ERR_TARGET_PROCESS_MEMORY_MANIPULATION_FAILED = 19
ERR_WAIT_FAILED = 20
ERR_WAIT_TIMEOUT = 21
ERR_UNABLE_TO_GET_RETURN_CODE = 22
ERR_EXCEPTION_HANDLER_PROBLEM = 23
ERR_CANNOT_PARSE_SCOPE_TABLE = 24
ERR_UNHANDLED_EXCEPTION_IN_SETUP = 25
ERR_COULD_NOT_REBASE_FUNCTION = 26
ERR_PLATFORM_NOT_SUPPORTED = 27
ERR_UNKNOWN = 28
errorStrings = {ERR_CANNOT_FIND_SUPPORT_PROCESS: 'Unable to find required process',
   ERR_CANNOT_FIND_REQUIRED_FUNCTION: 'Cannot find required function',
   ERR_UNABLE_TO_OPEN_SUPPORT_PROCESS: 'Cannot create remote thread due to a problem with the support process',
   ERR_UNABLE_TO_OPEN_TARGET_PROCESS: 'Cannot create remote thread due to a problem with the target process',
   ERR_UNABLE_TO_OPEN_KERNEL: 'Cannot create remote thread due to a problem in the system kernel',
   ERR_UNABLE_TO_ALLOCATE_MEMORY_IN_SUPPORT_PROCESS: 'Cannot allocate memory in support process',
   ERR_UNABLE_TO_ALLOCATE_MEMORY_IN_TARGET_PROCESS: 'Cannot allocate memory in target process',
   ERR_UNABLE_TO_ALLOCATE_MEMORY_IN_KERNEL: 'Cannot allocate memory in kernel',
   ERR_UNABLE_TO_INSTALL_SUPPORT_FUNCTIONS: 'Cannot install support functions for injection',
   ERR_PRIVILEGE_LIBRARY_FAILED: 'Privilege Library failed',
   ERR_CREATE_REMOTE_THREAD_FAILED: 'Unable to create the remote thread',
   ERR_INVALID_PARAMETERS: 'Invalid parameters passed into function',
   ERR_MEMORY_ALLOCATION_FAILED: 'Memory allocation failed',
   ERR_64_BIT_MISMATCH: 'Target process and current process are 64-bit mismatched',
   ERR_CANNOT_OPEN_PROCESS_FOR_INJECTION: 'Failed to open target process for injection',
   ERR_ALREADY_INSTALLED: 'Target injection has already been installed',
   ERR_CANNOT_WRITE_FUNCTION: 'Cannot write target function into target process',
   ERR_NOT_YET_INSTALLED: 'Target injection has not yet been installed',
   ERR_TARGET_PROCESS_MEMORY_MANIPULATION_FAILED: 'Failed to manipulate target process memory',
   ERR_WAIT_FAILED: 'Wait for function to finish failed',
   ERR_WAIT_TIMEOUT: 'Wait for function to finish failed',
   ERR_UNABLE_TO_GET_RETURN_CODE: 'Could not get return code from function',
   ERR_EXCEPTION_HANDLER_PROBLEM: 'Unable to configure exception handler',
   ERR_CANNOT_PARSE_SCOPE_TABLE: 'Could not parse scope table in function',
   ERR_UNHANDLED_EXCEPTION_IN_SETUP: 'An unhandled exception occurred',
   ERR_COULD_NOT_REBASE_FUNCTION: 'Unable to rebase function for injection',
   ERR_PLATFORM_NOT_SUPPORTED: 'Platform not supported for injection',
   ERR_UNKNOWN: 'Unknown injection error'
   }