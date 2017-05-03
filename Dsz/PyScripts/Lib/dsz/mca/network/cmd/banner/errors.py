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
ERR_SOCKET_INIT_FAILURE = mcl.status.framework.ERR_START + 3
ERR_SOCKET_BIND_FAILURE = mcl.status.framework.ERR_START + 4
ERR_SOCKET_OPTION_FAILURE = mcl.status.framework.ERR_START + 5
ERR_CONNECT_FAILURE = mcl.status.framework.ERR_START + 6
ERR_SEND_FAILURE = mcl.status.framework.ERR_START + 7
ERR_PACKET_TOO_LARGE = mcl.status.framework.ERR_START + 8
ERR_RECV_ERROR = mcl.status.framework.ERR_START + 9
ERR_RECV_TIMEOUT = mcl.status.framework.ERR_START + 10
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 11
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_CALLBACK_FAILED: 'Error making callback',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_SOCKET_INIT_FAILURE: 'Socket initialization failed',
   ERR_SOCKET_BIND_FAILURE: 'Failed to bind to given source port',
   ERR_SOCKET_OPTION_FAILURE: 'Failed to set socket option',
   ERR_CONNECT_FAILURE: 'Connect request failed',
   ERR_SEND_FAILURE: 'Send failed',
   ERR_PACKET_TOO_LARGE: 'The given packet is too large to send',
   ERR_RECV_ERROR: 'Error receiving data',
   ERR_RECV_TIMEOUT: 'Timeout waiting for data',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform'
   }