# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *

class Params:

    def __init__(self):
        self.__dict__['maxPorts'] = 500
        self.__dict__['memory'] = 256000

    def __getattr__(self, name):
        if name == 'maxPorts':
            return self.__dict__['maxPorts']
        if name == 'memory':
            return self.__dict__['memory']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'maxPorts':
            self.__dict__['maxPorts'] = value
        elif name == 'memory':
            self.__dict__['memory'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_MAX_PORTS, self.__dict__['maxPorts'])
        submsg.AddU32(MSG_KEY_PARAMS_MEMORY, self.__dict__['memory'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['maxPorts'] = submsg.FindU32(MSG_KEY_PARAMS_MAX_PORTS)
        except:
            pass

        try:
            self.__dict__['memory'] = submsg.FindU32(MSG_KEY_PARAMS_MEMORY)
        except:
            pass