# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_MEMORY_ALLOC_FAILED = mcl.status.framework.ERR_START + 2
ERR_EXCEPTION = mcl.status.framework.ERR_START + 3
ERR_INTERNAL_ERROR = mcl.status.framework.ERR_START + 4
ERR_ADD_TO_LIST_FAILED = mcl.status.framework.ERR_START + 5
ERR_GET_FROM_LIST_FAILED = mcl.status.framework.ERR_START + 6
ERR_INVALID_ADDRESS = mcl.status.framework.ERR_START + 7
ERR_INVALID_PROTOCOL = mcl.status.framework.ERR_START + 8
ERR_ERROR_CREATING_SOCKET = mcl.status.framework.ERR_START + 9
ERR_ERROR_SETTING_NONBLOCKING = mcl.status.framework.ERR_START + 10
ERR_ERROR_BINDING_SOCKET = mcl.status.framework.ERR_START + 11
ERR_ERROR_LISTENING = mcl.status.framework.ERR_START + 12
ERR_THREAD_CREATE_FAILED = mcl.status.framework.ERR_START + 13
ERR_THREAD_SETUP_FAILED = mcl.status.framework.ERR_START + 14
ERR_THREAD_CLEANUP_FAILED = mcl.status.framework.ERR_START + 15
ERR_THREAD_STOP_FAILED = mcl.status.framework.ERR_START + 16
ERR_ERROR_RECV = mcl.status.framework.ERR_START + 17
ERR_ERROR_ACCEPT = mcl.status.framework.ERR_START + 18
ERR_CONNECT_FAILED = mcl.status.framework.ERR_START + 19
ERR_SOCKET_INDEX_NOT_FOUND = mcl.status.framework.ERR_START + 20
ERR_SOCKET_THREAD_ENDED = mcl.status.framework.ERR_START + 21
ERR_GET_LOCK_FAILED = mcl.status.framework.ERR_START + 22
ERR_UDP_SEND_FAILED = mcl.status.framework.ERR_START + 23
ERR_SHAREPORT_NOT_SUPPORTED = mcl.status.framework.ERR_START + 24
ERR_SO_SHAREPORT_FAILED = mcl.status.framework.ERR_START + 25
ERR_ADD_FILTER_FAILED = mcl.status.framework.ERR_START + 26
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling of data failed',
   ERR_MEMORY_ALLOC_FAILED: 'Allocation of memory failed',
   ERR_EXCEPTION: 'An exception occurred',
   ERR_INTERNAL_ERROR: 'An internal error occurred',
   ERR_ADD_TO_LIST_FAILED: 'Failed to add object to list',
   ERR_GET_FROM_LIST_FAILED: 'Failed to get object from list',
   ERR_INVALID_ADDRESS: 'Invalid address',
   ERR_INVALID_PROTOCOL: 'Invalid protocol',
   ERR_ERROR_CREATING_SOCKET: 'Error creating socket',
   ERR_ERROR_SETTING_NONBLOCKING: 'Failed to set socket to nonblocking',
   ERR_ERROR_BINDING_SOCKET: 'Error binding socket',
   ERR_ERROR_LISTENING: 'Error setting socket to listen',
   ERR_THREAD_CREATE_FAILED: 'Socket thread creation failed',
   ERR_THREAD_SETUP_FAILED: 'Setup of send/recv thread failed',
   ERR_THREAD_CLEANUP_FAILED: 'Cleanup of send/recv thread(s) failed',
   ERR_THREAD_STOP_FAILED: 'Error stopping send/recv thread',
   ERR_ERROR_RECV: "Error performing 'recv'",
   ERR_ERROR_ACCEPT: 'Error accepting new connection',
   ERR_CONNECT_FAILED: 'Failed to connect to target',
   ERR_SOCKET_INDEX_NOT_FOUND: 'Socket index not found',
   ERR_SOCKET_THREAD_ENDED: 'Socket send/recv thread ended',
   ERR_GET_LOCK_FAILED: 'Failed to get lock',
   ERR_UDP_SEND_FAILED: 'Port Unreachable message received for UDP send',
   ERR_SHAREPORT_NOT_SUPPORTED: 'Sharing of ports is not supported',
   ERR_SO_SHAREPORT_FAILED: 'Error setting FlewAvenue SO_SHAREPORT',
   ERR_ADD_FILTER_FAILED: 'Error adding FlewAvenue Filter'
   }