# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_COM_INIT_FAILED = mcl.status.framework.ERR_START + 1
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 2
ERR_FUNC_NOT_FOUND = mcl.status.framework.ERR_START + 3
ERR_BIND_FAILED = mcl.status.framework.ERR_START + 4
ERR_GET_MODE_FAILED = mcl.status.framework.ERR_START + 5
ERR_EXFIL_FAILED = mcl.status.framework.ERR_START + 6
ERR_CREATE_ENUM_FAILED = mcl.status.framework.ERR_START + 7
ERR_GET_ENUM_INTERFACE_FAILED = mcl.status.framework.ERR_START + 8
ERR_ENUM_NEXT_FAILED = mcl.status.framework.ERR_START + 9
ERR_SEARCH_OBJECT_FAILED = mcl.status.framework.ERR_START + 10
ERR_SEARCH_FAILED = mcl.status.framework.ERR_START + 11
ERR_SETSEARCH_FAILED = mcl.status.framework.ERR_START + 12
ERR_GETNAME_FAILED = mcl.status.framework.ERR_START + 13
ERR_GET_NAME_CONTEXT_FAILED = mcl.status.framework.ERR_START + 14
ERR_GETPROPS_FAILED = mcl.status.framework.ERR_START + 15
ERR_GETUSER_FAILED = mcl.status.framework.ERR_START + 16
ERR_NO_DATA = mcl.status.framework.ERR_START + 17
ERR_EXCEPTION_THROWN = mcl.status.framework.ERR_START + 18
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_COM_INIT_FAILED: 'COM initialization failed',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_FUNC_NOT_FOUND: 'Required function is not available',
   ERR_BIND_FAILED: 'Bind to domain failed',
   ERR_GET_MODE_FAILED: 'Get of domain mode failed',
   ERR_EXFIL_FAILED: 'Return of data failed',
   ERR_CREATE_ENUM_FAILED: 'Create enum object failed',
   ERR_GET_ENUM_INTERFACE_FAILED: 'Get enum interface failed',
   ERR_ENUM_NEXT_FAILED: 'Get next from enumeration failed',
   ERR_SEARCH_OBJECT_FAILED: 'Failed to find search object',
   ERR_SEARCH_FAILED: 'Search for objects failed',
   ERR_SETSEARCH_FAILED: 'SetSearchPreference failed',
   ERR_GETNAME_FAILED: 'Failed to find user',
   ERR_GET_NAME_CONTEXT_FAILED: 'Get of default naming context failed',
   ERR_GETPROPS_FAILED: 'GetUserProperties failed',
   ERR_GETUSER_FAILED: 'Get of user object failed',
   ERR_NO_DATA: 'No matching data found',
   ERR_EXCEPTION_THROWN: 'Exception thrown'
   }