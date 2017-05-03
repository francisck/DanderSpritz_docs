# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_LOOKUP_FAILED = mcl.status.framework.ERR_START + 2
ERR_PACKET_SETUP_FAILED = mcl.status.framework.ERR_START + 3
ERR_CREATE_SOCKET_FAILED = mcl.status.framework.ERR_START + 4
ERR_SEND_PACKET_FAILED = mcl.status.framework.ERR_START + 5
ERR_INVALID_SOURCE = mcl.status.framework.ERR_START + 6
ERR_INVALID_DEST = mcl.status.framework.ERR_START + 7
ERR_CREATE_SOCKET_ERROR = mcl.status.framework.ERR_START + 8
ERR_BIND_ERROR = mcl.status.framework.ERR_START + 9
ERR_RECEIVE_ERROR = mcl.status.framework.ERR_START + 10
ERR_RAW_RECV_ERROR = mcl.status.framework.ERR_START + 11
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 12
ERR_MAX_HOPS_EXCEEDED = mcl.status.framework.ERR_START + 13
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_LOOKUP_FAILED: 'Hostname lookup failed',
   ERR_PACKET_SETUP_FAILED: 'Packet generation failed',
   ERR_CREATE_SOCKET_FAILED: 'Unable to create a socket',
   ERR_SEND_PACKET_FAILED: 'Unable to send packet',
   ERR_INVALID_SOURCE: 'Invalid source address specified',
   ERR_INVALID_DEST: 'Invalid destination address specified',
   ERR_CREATE_SOCKET_ERROR: 'Unable to create socket',
   ERR_BIND_ERROR: 'Unable to bind socket',
   ERR_RECEIVE_ERROR: 'Error receiving data on socket',
   ERR_RAW_RECV_ERROR: 'Raw receive error',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_MAX_HOPS_EXCEEDED: 'Maximum number of hops exceeded'
   }