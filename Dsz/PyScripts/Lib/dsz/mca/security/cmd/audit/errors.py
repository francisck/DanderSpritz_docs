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
ERR_OPEN_FAILED = mcl.status.framework.ERR_START + 3
ERR_QUERY_FAILED = mcl.status.framework.ERR_START + 4
ERR_CHANGE_AUDITED = mcl.status.framework.ERR_START + 5
ERR_CHANGE_NOT_FOUND = mcl.status.framework.ERR_START + 6
ERR_ALREADY_ON = mcl.status.framework.ERR_START + 7
ERR_ALREADY_OFF = mcl.status.framework.ERR_START + 8
ERR_SET_FAILED = mcl.status.framework.ERR_START + 9
ERR_PATCH_FAILED = mcl.status.framework.ERR_START + 10
ERR_FIND_PROCESS_FAILED = mcl.status.framework.ERR_START + 11
ERR_OPEN_PROCESS_FAILED = mcl.status.framework.ERR_START + 12
ERR_PATTERN_MATCH_FAILED = mcl.status.framework.ERR_START + 13
ERR_VALUE_UNEXPECTED = mcl.status.framework.ERR_START + 14
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_GET_API_FAILED: 'Get of required API failed',
   ERR_OPEN_FAILED: 'Open of LSA Policy failed',
   ERR_QUERY_FAILED: 'Query of current audit policy failed',
   ERR_CHANGE_AUDITED: "Auditing of policy changes is enabled.  You must use the '-force' option",
   ERR_CHANGE_NOT_FOUND: "Information on auditing of policy changes was not found.  You must use the '-force' option",
   ERR_ALREADY_ON: 'Auditing is already on',
   ERR_ALREADY_OFF: 'Auditing is already off',
   ERR_SET_FAILED: 'Set of new auditing status failed',
   ERR_PATCH_FAILED: 'Patch of auditing failed',
   ERR_FIND_PROCESS_FAILED: 'Process for audit change not found',
   ERR_OPEN_PROCESS_FAILED: 'Unable to open auditing process using all known methods',
   ERR_PATTERN_MATCH_FAILED: 'Pattern match of code failed',
   ERR_VALUE_UNEXPECTED: 'Unexpected value found in memory (** This may indicate that auditing has already been patched **)'
   }