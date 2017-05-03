# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_ScanParams.py
from types import *
import mcl.object.MclTime
import mcl.object.IpAddr

class ScanParams:

    def __init__(self):
        self.__dict__['delay'] = mcl.object.MclTime.MclTime()
        self.__dict__['startIp'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['endIp'] = mcl.object.IpAddr.IpAddr()

    def __getattr__(self, name):
        if name == 'delay':
            return self.__dict__['delay']
        if name == 'startIp':
            return self.__dict__['startIp']
        if name == 'endIp':
            return self.__dict__['endIp']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'delay':
            self.__dict__['delay'] = value
        elif name == 'startIp':
            self.__dict__['startIp'] = value
        elif name == 'endIp':
            self.__dict__['endIp'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddTime(MSG_KEY_PARAMS_SCAN_DELAY, self.__dict__['delay'])
        submsg.AddIpAddr(MSG_KEY_PARAMS_SCAN_START_IP, self.__dict__['startIp'])
        submsg.AddIpAddr(MSG_KEY_PARAMS_SCAN_END_IP, self.__dict__['endIp'])
        mmsg.AddMessage(MSG_KEY_PARAMS_SCAN, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_SCAN, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['delay'] = submsg.FindTime(MSG_KEY_PARAMS_SCAN_DELAY)
        self.__dict__['startIp'] = submsg.FindIpAddr(MSG_KEY_PARAMS_SCAN_START_IP)
        self.__dict__['endIp'] = submsg.FindIpAddr(MSG_KEY_PARAMS_SCAN_END_IP)