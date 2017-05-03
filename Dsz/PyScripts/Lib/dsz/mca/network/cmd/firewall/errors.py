# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_CALLBACK_FAILED = mcl.status.framework.ERR_START + 1
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 2
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 3
ERR_REG_OPEN_KEY_FAILED = mcl.status.framework.ERR_START + 4
ERR_REG_SET_VALUE_FAILED = mcl.status.framework.ERR_START + 5
ERR_REG_DELETE_VALUE_FAILED = mcl.status.framework.ERR_START + 6
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 7
ERR_COM_INIT_FAILED = mcl.status.framework.ERR_START + 8
ERR_GET_API_FAILED = mcl.status.framework.ERR_START + 9
ERR_REMOVE_FAILED = mcl.status.framework.ERR_START + 10
ERR_GET_STATUS_FAILED = mcl.status.framework.ERR_START + 11
ERR_GET_PROFILE_FLAG_FAILED = mcl.status.framework.ERR_START + 12
ERR_GET_RULES_FAILED = mcl.status.framework.ERR_START + 13
ERR_GET_RULE_ACTION_FAILED = mcl.status.framework.ERR_START + 14
ERR_GET_RULE_PROTOCOL_FAILED = mcl.status.framework.ERR_START + 15
ERR_GET_RULE_ENABLED_FAILED = mcl.status.framework.ERR_START + 16
ERR_GET_PROFILE_MASK_FAILED = mcl.status.framework.ERR_START + 17
ERR_GET_RULE_DIRECTION_FAILED = mcl.status.framework.ERR_START + 18
ERR_GET_RULE_STRING_FAILED = mcl.status.framework.ERR_START + 19
ERR_CREATE_RULE_FAILED = mcl.status.framework.ERR_START + 20
ERR_SET_RULE_INFO_FAILED = mcl.status.framework.ERR_START + 21
ERR_ADD_RULE_FAILED = mcl.status.framework.ERR_START + 22
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_CALLBACK_FAILED: 'Error making callback',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_REG_OPEN_KEY_FAILED: 'Unable to open registry key',
   ERR_REG_SET_VALUE_FAILED: 'Unable to set registry value',
   ERR_REG_DELETE_VALUE_FAILED: 'Failed to delete registry value',
   ERR_ALLOC_FAILED: 'Unable to allocate memory',
   ERR_COM_INIT_FAILED: 'Failed to initialize COM',
   ERR_GET_API_FAILED: 'Failed to get required API',
   ERR_REMOVE_FAILED: 'Failed to remove rule',
   ERR_GET_STATUS_FAILED: 'Failed to get firewall status data',
   ERR_GET_PROFILE_FLAG_FAILED: 'Failed to get profile flags',
   ERR_GET_RULES_FAILED: 'Failed to get firewall rules',
   ERR_GET_RULE_ACTION_FAILED: 'Failed to get firewall rule action',
   ERR_GET_RULE_PROTOCOL_FAILED: 'Failed to get protocol',
   ERR_GET_RULE_ENABLED_FAILED: 'Failed to get enabled status of rule',
   ERR_GET_PROFILE_MASK_FAILED: 'Failed to get profile mask for rule',
   ERR_GET_RULE_DIRECTION_FAILED: 'Failed to get direction of rule',
   ERR_GET_RULE_STRING_FAILED: 'Failed to get rule information',
   ERR_CREATE_RULE_FAILED: 'Failed to create a new firewall rule',
   ERR_SET_RULE_INFO_FAILED: 'Failed to set rule settings',
   ERR_ADD_RULE_FAILED: 'Failed to add a firewall rule to rule list'
   }