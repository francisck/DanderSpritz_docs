# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: audit.py
ERR_AUDIT_SUCCESS = 0
ERR_AUDIT_DISABLE_FAILED = 1
ERR_AUDIT_ENABLE_FAILED = 2
ERR_AUDIT_UNKNOWN_TYPE = 3
ERR_AUDIT_EXCEPTION = 4
ERR_AUDIT_PROCESS_NOT_FOUND = 5
ERR_AUDIT_OPEN_PROCESS_FAILED = 6
ERR_AUDIT_MODULE_BASE_NOT_FOUND = 7
ERR_AUDIT_READ_MEMORY_FAILED = 8
ERR_AUDIT_MEMORY_ALLOC_FAILED = 9
ERR_AUDIT_PATTERN_MATCH_FAILED = 10
ERR_AUDIT_MODIFY_PROTECTION_FAILED = 11
ERR_AUDIT_FAILED_VALUE_READ = 12
ERR_AUDIT_FAILED_VALUE_WRITE = 13
ERR_AUDIT_VALUE_UNEXPECTED = 14
ERR_AUDIT_INVALID_PARAMETER = 15
errorStrings = {ERR_AUDIT_DISABLE_FAILED: 'Disable of auditing failed',
   ERR_AUDIT_ENABLE_FAILED: 'Enable of auditing failed',
   ERR_AUDIT_UNKNOWN_TYPE: 'Unknown audit type',
   ERR_AUDIT_EXCEPTION: 'Exception thrown attempting to modify auditing',
   ERR_AUDIT_PROCESS_NOT_FOUND: 'Process for audit change not found',
   ERR_AUDIT_OPEN_PROCESS_FAILED: 'Unable to open auditing process using all known methods',
   ERR_AUDIT_MODULE_BASE_NOT_FOUND: 'Base for necessary auditing dll not found',
   ERR_AUDIT_READ_MEMORY_FAILED: 'Read of audit related process memory failed',
   ERR_AUDIT_MEMORY_ALLOC_FAILED: 'Memory allocation failed',
   ERR_AUDIT_PATTERN_MATCH_FAILED: 'Pattern match of code failed',
   ERR_AUDIT_MODIFY_PROTECTION_FAILED: 'Change of memory protection failed',
   ERR_AUDIT_FAILED_VALUE_READ: 'Read of memory value needed for audit changes failed',
   ERR_AUDIT_FAILED_VALUE_WRITE: 'Write of memory value needed for audit changes failed',
   ERR_AUDIT_VALUE_UNEXPECTED: 'Unexpected value found in memory (** This may indicate that auditing has already been patched **)',
   ERR_AUDIT_INVALID_PARAMETER: 'Invalid parameter'
   }