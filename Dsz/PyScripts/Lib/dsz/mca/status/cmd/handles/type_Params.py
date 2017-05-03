# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *

class ParamsQuery:

    def __init__(self):
        self.__dict__['processId'] = 0
        self.__dict__['all'] = False
        self.__dict__['memory'] = 256000

    def __getattr__(self, name):
        if name == 'processId':
            return self.__dict__['processId']
        if name == 'all':
            return self.__dict__['all']
        if name == 'memory':
            return self.__dict__['memory']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'processId':
            self.__dict__['processId'] = value
        elif name == 'all':
            self.__dict__['all'] = value
        elif name == 'memory':
            self.__dict__['memory'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_QUERY_PROCESS_ID, self.__dict__['processId'])
        submsg.AddBool(MSG_KEY_PARAMS_QUERY_ALL, self.__dict__['all'])
        submsg.AddU32(MSG_KEY_PARAMS_QUERY_MEMORY, self.__dict__['memory'])
        mmsg.AddMessage(MSG_KEY_PARAMS_QUERY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_QUERY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['processId'] = submsg.FindU32(MSG_KEY_PARAMS_QUERY_PROCESS_ID)
        try:
            self.__dict__['all'] = submsg.FindBool(MSG_KEY_PARAMS_QUERY_ALL)
        except:
            pass

        try:
            self.__dict__['memory'] = submsg.FindU32(MSG_KEY_PARAMS_QUERY_MEMORY)
        except:
            pass


class ParamsDuplicate:

    def __init__(self):
        self.__dict__['processId'] = 0
        self.__dict__['handleValue'] = 0

    def __getattr__(self, name):
        if name == 'processId':
            return self.__dict__['processId']
        if name == 'handleValue':
            return self.__dict__['handleValue']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'processId':
            self.__dict__['processId'] = value
        elif name == 'handleValue':
            self.__dict__['handleValue'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_DUPLICATE_PROCESS_ID, self.__dict__['processId'])
        submsg.AddU64(MSG_KEY_PARAMS_DUPLICATE_HANDLE, self.__dict__['handleValue'])
        mmsg.AddMessage(MSG_KEY_PARAMS_DUPLICATE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_DUPLICATE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['processId'] = submsg.FindU32(MSG_KEY_PARAMS_DUPLICATE_PROCESS_ID)
        self.__dict__['handleValue'] = submsg.FindU64(MSG_KEY_PARAMS_DUPLICATE_HANDLE)


class ParamsClose:

    def __init__(self):
        self.__dict__['processId'] = 0
        self.__dict__['handleValue'] = 0

    def __getattr__(self, name):
        if name == 'processId':
            return self.__dict__['processId']
        if name == 'handleValue':
            return self.__dict__['handleValue']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'processId':
            self.__dict__['processId'] = value
        elif name == 'handleValue':
            self.__dict__['handleValue'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_CLOSE_PROCESS_ID, self.__dict__['processId'])
        submsg.AddU64(MSG_KEY_PARAMS_CLOSE_HANDLE, self.__dict__['handleValue'])
        mmsg.AddMessage(MSG_KEY_PARAMS_CLOSE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_CLOSE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['processId'] = submsg.FindU32(MSG_KEY_PARAMS_CLOSE_PROCESS_ID)
        self.__dict__['handleValue'] = submsg.FindU64(MSG_KEY_PARAMS_CLOSE_HANDLE)