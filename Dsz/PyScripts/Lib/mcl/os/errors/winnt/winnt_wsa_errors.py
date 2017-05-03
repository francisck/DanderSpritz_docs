# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: winnt_wsa_errors.py


def getErrorString(error):
    if error == 10004:
        return 'A blocking operation was interrupted by a call to WSACancelBlockingCall.'
    else:
        if error == 10009:
            return 'The file handle supplied is not valid.'
        if error == 10013:
            return 'An attempt was made to access a socket in a way forbidden by its access permissions.'
        if error == 10014:
            return 'The system detected an invalid pointer address in attempting to use a pointer argument in a call.'
        if error == 10022:
            return 'An invalid argument was supplied.'
        if error == 10024:
            return 'Too many open sockets.'
        if error == 10035:
            return 'A non-blocking socket operation could not be completed immediately.'
        if error == 10036:
            return 'A blocking operation is currently executing.'
        if error == 10037:
            return 'An operation was attempted on a non-blocking socket that already had an operation in progress.'
        if error == 10038:
            return 'An operation was attempted on something that is not a socket.'
        if error == 10039:
            return 'A required address was omitted from an operation on a socket.'
        if error == 10040:
            return 'A message sent on a datagram socket was larger than the internal message buffer or some other network limit, or the buffer used to receive a datagram into was smaller than the datagram itself.'
        if error == 10041:
            return 'A protocol was specified in the socket function call that does not support the semantics of the socket type requested.'
        if error == 10042:
            return 'An unknown, invalid, or unsupported option or level was specified in a getsockopt or setsockopt call.'
        if error == 10043:
            return 'The requested protocol has not been configured into the system, or no implementation for it exists.'
        if error == 10044:
            return 'The support for the specified socket type does not exist in this address family.'
        if error == 10045:
            return 'The attempted operation is not supported for the type of object referenced.'
        if error == 10046:
            return 'The protocol family has not been configured into the system or no implementation for it exists.'
        if error == 10047:
            return 'An address incompatible with the requested protocol was used.'
        if error == 10048:
            return 'Only one usage of each socket address (protocol/network address/port) is normally permitted.'
        if error == 10049:
            return 'The requested address is not valid in its context.'
        if error == 10050:
            return 'A socket operation encountered a dead network.'
        if error == 10051:
            return 'A socket operation was attempted to an unreachable network.'
        if error == 10052:
            return 'The connection has been broken due to keep-alive activity detecting a failure while the operation was in progress.'
        if error == 10053:
            return 'An established connection was aborted by the software in your host machine.'
        if error == 10054:
            return 'An existing connection was forcibly closed by the remote host.'
        if error == 10055:
            return 'An operation on a socket could not be performed because the system lacked sufficient buffer space or because a queue was full.'
        if error == 10056:
            return 'A connect request was made on an already connected socket.'
        if error == 10057:
            return 'A request to send or receive data was disallowed because the socket is not connected and (when sending on a datagram socket using a sendto call) no address was supplied.'
        if error == 10058:
            return 'A request to send or receive data was disallowed because the socket had already been shut down in that direction with a previous shutdown call.'
        if error == 10059:
            return 'Too many references to some kernel object.'
        if error == 10060:
            return 'A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond.'
        if error == 10061:
            return 'No connection could be made because the target machine actively refused it.'
        if error == 10062:
            return 'Cannot translate name.'
        if error == 10063:
            return 'Name component or name was too long.'
        if error == 10064:
            return 'A socket operation failed because the destination host was down.'
        if error == 10065:
            return 'A socket operation was attempted to an unreachable host.'
        if error == 10066:
            return 'Cannot remove a directory that is not empty.'
        if error == 10067:
            return 'A Windows Sockets implementation may have a limit on the number of applications that may use it simultaneously.'
        if error == 10068:
            return 'Ran out of quota.'
        if error == 10069:
            return 'Ran out of disk quota.'
        if error == 10070:
            return 'File handle reference is no longer available.'
        if error == 10071:
            return 'Item is not available locally.'
        if error == 10091:
            return 'WSAStartup cannot function at this time because the underlying system it uses to provide network services is currently unavailable.'
        if error == 10092:
            return 'The Windows Sockets version requested is not supported.'
        if error == 10093:
            return 'Either the application has not called WSAStartup, or WSAStartup failed.'
        if error == 10101:
            return 'Returned by WSARecv or WSARecvFrom to indicate the remote party has initiated a graceful shutdown sequence.'
        if error == 10102:
            return 'No more results can be returned by WSALookupServiceNext.'
        if error == 10103:
            return 'A call to WSALookupServiceEnd was made while this call was still processing. The call has been canceled.'
        if error == 10104:
            return 'The procedure call table is invalid.'
        if error == 10105:
            return 'The requested service provider is invalid.'
        if error == 10106:
            return 'The requested service provider could not be loaded or initialized.'
        if error == 10107:
            return 'A system call that should never fail has failed.'
        if error == 10108:
            return 'No such service is known. The service cannot be found in the specified name space.'
        if error == 10109:
            return 'The specified class was not found.'
        if error == 10110:
            return 'No more results can be returned by WSALookupServiceNext.'
        if error == 10111:
            return 'A call to WSALookupServiceEnd was made while this call was still processing. The call has been canceled.'
        if error == 10112:
            return 'A database query failed because it was actively refused.'
        if error == 11001:
            return 'No such host is known.'
        if error == 11002:
            return 'This is usually a temporary error during hostname resolution and means that the local server did not receive a response from an authoritative server.'
        if error == 11003:
            return 'A non-recoverable error occurred during a database lookup.'
        if error == 11004:
            return 'The requested name is valid, but no data of the requested type was found.'
        if error == 11005:
            return 'At least one reserve has arrived.'
        if error == 11006:
            return 'At least one path has arrived.'
        if error == 11007:
            return 'There are no senders.'
        if error == 11008:
            return 'There are no receivers.'
        if error == 11009:
            return 'Reserve has been confirmed.'
        if error == 11010:
            return 'Error due to lack of resources.'
        if error == 11011:
            return 'Rejected for administrative reasons - bad credentials.'
        if error == 11012:
            return 'Unknown or conflicting style.'
        if error == 11013:
            return 'Problem with some part of the filterspec or providerspecific buffer in general.'
        if error == 11014:
            return 'Problem with some part of the flowspec.'
        if error == 11015:
            return 'General QOS error.'
        if error == 11016:
            return 'An invalid or unrecognized service type was found in the flowspec.'
        if error == 11017:
            return 'An invalid or inconsistent flowspec was found in the QOS structure.'
        if error == 11018:
            return 'Invalid QOS provider-specific buffer.'
        if error == 11019:
            return 'An invalid QOS filter style was used.'
        if error == 11020:
            return 'An invalid QOS filter type was used.'
        if error == 11021:
            return 'An incorrect number of QOS FILTERSPECs were specified in the FLOWDESCRIPTOR.'
        if error == 11022:
            return 'An object with an invalid ObjectLength field was specified in the QOS provider-specific buffer.'
        if error == 11023:
            return 'An incorrect number of flow descriptors was specified in the QOS structure.'
        if error == 11024:
            return 'An unrecognized object was found in the QOS provider-specific buffer.'
        if error == 11025:
            return 'An invalid policy object was found in the QOS provider-specific buffer.'
        if error == 11026:
            return 'An invalid QOS flow descriptor was found in the flow descriptor list.'
        if error == 11027:
            return 'An invalid or inconsistent flowspec was found in the QOS provider specific buffer.'
        if error == 11028:
            return 'An invalid FILTERSPEC was found in the QOS provider-specific buffer.'
        if error == 11029:
            return 'An invalid shape discard mode object was found in the QOS provider specific buffer.'
        if error == 11030:
            return 'An invalid shaping rate object was found in the QOS provider-specific buffer.'
        if error == 11031:
            return 'A reserved policy element was found in the QOS provider-specific buffer.'
        return None
        return None