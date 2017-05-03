# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import mcl.object.MclTime
import mcl.object.IpAddr
PARAM_TYPE_ICMP = 0
PARAM_TYPE_UDP = 1
PARAM_TYPE_TCP = 2

class Params:

    def __init__(self):
        self.__dict__['protocol'] = PARAM_TYPE_ICMP
        self.__dict__['maxttl'] = 30
        self.__dict__['queries'] = 1
        self.__dict__['srcport'] = 0
        self.__dict__['dstport'] = 3235
        self.__dict__['timeout'] = mcl.object.MclTime.MclTime()
        self.__dict__['srcAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['dstAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['dstHost'] = ''
        self.__dict__['rawSendParam'] = ''

    def __getattr__(self, name):
        if name == 'protocol':
            return self.__dict__['protocol']
        if name == 'maxttl':
            return self.__dict__['maxttl']
        if name == 'queries':
            return self.__dict__['queries']
        if name == 'srcport':
            return self.__dict__['srcport']
        if name == 'dstport':
            return self.__dict__['dstport']
        if name == 'timeout':
            return self.__dict__['timeout']
        if name == 'srcAddr':
            return self.__dict__['srcAddr']
        if name == 'dstAddr':
            return self.__dict__['dstAddr']
        if name == 'dstHost':
            return self.__dict__['dstHost']
        if name == 'rawSendParam':
            return self.__dict__['rawSendParam']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'protocol':
            self.__dict__['protocol'] = value
        elif name == 'maxttl':
            self.__dict__['maxttl'] = value
        elif name == 'queries':
            self.__dict__['queries'] = value
        elif name == 'srcport':
            self.__dict__['srcport'] = value
        elif name == 'dstport':
            self.__dict__['dstport'] = value
        elif name == 'timeout':
            self.__dict__['timeout'] = value
        elif name == 'srcAddr':
            self.__dict__['srcAddr'] = value
        elif name == 'dstAddr':
            self.__dict__['dstAddr'] = value
        elif name == 'dstHost':
            self.__dict__['dstHost'] = value
        elif name == 'rawSendParam':
            self.__dict__['rawSendParam'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_PROTOCOL, self.__dict__['protocol'])
        submsg.AddU8(MSG_KEY_PARAMS_MAX_TTL, self.__dict__['maxttl'])
        submsg.AddU8(MSG_KEY_PARAMS_QUERIES, self.__dict__['queries'])
        submsg.AddU16(MSG_KEY_PARAMS_SOURCE_PORT, self.__dict__['srcport'])
        submsg.AddU16(MSG_KEY_PARAMS_DESTINATION_PORT, self.__dict__['dstport'])
        submsg.AddTime(MSG_KEY_PARAMS_TIMEOUT, self.__dict__['timeout'])
        submsg.AddIpAddr(MSG_KEY_PARAMS_SOURCE_ADDRESS, self.__dict__['srcAddr'])
        submsg.AddIpAddr(MSG_KEY_PARAMS_DESTINATION_ADDRESS, self.__dict__['dstAddr'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_DESTINATION_HOST, self.__dict__['dstHost'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_RAW_SEND_PARAMS, self.__dict__['rawSendParam'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['protocol'] = submsg.FindU8(MSG_KEY_PARAMS_PROTOCOL)
        except:
            pass

        try:
            self.__dict__['maxttl'] = submsg.FindU8(MSG_KEY_PARAMS_MAX_TTL)
        except:
            pass

        try:
            self.__dict__['queries'] = submsg.FindU8(MSG_KEY_PARAMS_QUERIES)
        except:
            pass

        try:
            self.__dict__['srcport'] = submsg.FindU16(MSG_KEY_PARAMS_SOURCE_PORT)
        except:
            pass

        try:
            self.__dict__['dstport'] = submsg.FindU16(MSG_KEY_PARAMS_DESTINATION_PORT)
        except:
            pass

        self.__dict__['timeout'] = submsg.FindTime(MSG_KEY_PARAMS_TIMEOUT)
        try:
            self.__dict__['srcAddr'] = submsg.FindIpAddr(MSG_KEY_PARAMS_SOURCE_ADDRESS)
        except:
            pass

        self.__dict__['dstAddr'] = submsg.FindIpAddr(MSG_KEY_PARAMS_DESTINATION_ADDRESS)
        self.__dict__['dstHost'] = submsg.FindString(MSG_KEY_PARAMS_DESTINATION_HOST)
        try:
            self.__dict__['rawSendParam'] = submsg.FindString(MSG_KEY_PARAMS_RAW_SEND_PARAMS)
        except:
            pass