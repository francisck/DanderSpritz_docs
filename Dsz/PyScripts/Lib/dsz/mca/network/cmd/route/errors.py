# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_NEEDED_FUNCS_NOT_FOUND = mcl.status.framework.ERR_START + 2
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 3
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 4
ERR_BAD_DESTINATION = mcl.status.framework.ERR_START + 5
ERR_BAD_NETMASK = mcl.status.framework.ERR_START + 6
ERR_BAD_GATEWAY = mcl.status.framework.ERR_START + 7
ERR_BAD_INTERFACE = mcl.status.framework.ERR_START + 8
ERR_INTERFACE_NOT_FOUND = mcl.status.framework.ERR_START + 9
ERR_GET_ROUTES_FAILED = mcl.status.framework.ERR_START + 10
ERR_ADD_FAILED = mcl.status.framework.ERR_START + 11
ERR_DELETE_FAILED = mcl.status.framework.ERR_START + 12
ERR_EXCEPTION_THROWN = mcl.status.framework.ERR_START + 13
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_NEEDED_FUNCS_NOT_FOUND: 'Failed to load all necessary functions',
   ERR_ALLOC_FAILED: 'Memory allocation error',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_BAD_DESTINATION: 'Invalid destination',
   ERR_BAD_NETMASK: 'Invalid netmask',
   ERR_BAD_GATEWAY: 'Invalid gateway',
   ERR_BAD_INTERFACE: 'Invalid interface',
   ERR_INTERFACE_NOT_FOUND: 'Interface not found',
   ERR_GET_ROUTES_FAILED: 'Failed to get routes',
   ERR_ADD_FAILED: 'Failed to add route',
   ERR_DELETE_FAILED: 'Failed to delete route',
   ERR_EXCEPTION_THROWN: 'The program threw an exception'
   }