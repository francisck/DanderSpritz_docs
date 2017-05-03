# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import array

class ParamsGetStatus:

    def __init__(self):
        self.__dict__['driver'] = ''

    def __getattr__(self, name):
        if name == 'driver':
            return self.__dict__['driver']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'driver':
            self.__dict__['driver'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_GET_STATUS_DRIVER, self.__dict__['driver'])
        mmsg.AddMessage(MSG_KEY_PARAMS_GET_STATUS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_GET_STATUS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['driver'] = submsg.FindString(MSG_KEY_PARAMS_GET_STATUS_DRIVER)


class ParamsGetFilter:

    def __init__(self):
        self.__dict__['driver'] = ''

    def __getattr__(self, name):
        if name == 'driver':
            return self.__dict__['driver']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'driver':
            self.__dict__['driver'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_GET_FILTER_DRIVER, self.__dict__['driver'])
        mmsg.AddMessage(MSG_KEY_PARAMS_GET_FILTER, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_GET_FILTER, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['driver'] = submsg.FindString(MSG_KEY_PARAMS_GET_FILTER_DRIVER)


class ParamsValidateFilter:

    def __init__(self):
        self.__dict__['adapterFilter'] = 0
        self.__dict__['filter'] = array.array('B')
        self.__dict__['driver'] = ''

    def __getattr__(self, name):
        if name == 'adapterFilter':
            return self.__dict__['adapterFilter']
        if name == 'filter':
            return self.__dict__['filter']
        if name == 'driver':
            return self.__dict__['driver']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'adapterFilter':
            self.__dict__['adapterFilter'] = value
        elif name == 'filter':
            self.__dict__['filter'] = value
        elif name == 'driver':
            self.__dict__['driver'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_VALIDATE_FILTER_ADAPTER_FILTER, self.__dict__['adapterFilter'])
        submsg.AddData(MSG_KEY_PARAMS_VALIDATE_FILTER_FILTER, self.__dict__['filter'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_VALIDATE_FILTER_DRIVER, self.__dict__['driver'])
        mmsg.AddMessage(MSG_KEY_PARAMS_VALIDATE_FILTER, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_VALIDATE_FILTER, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['adapterFilter'] = submsg.FindU32(MSG_KEY_PARAMS_VALIDATE_FILTER_ADAPTER_FILTER)
        self.__dict__['filter'] = submsg.FindData(MSG_KEY_PARAMS_VALIDATE_FILTER_FILTER)
        self.__dict__['driver'] = submsg.FindString(MSG_KEY_PARAMS_VALIDATE_FILTER_DRIVER)


class ParamsSendControl:

    def __init__(self):
        self.__dict__['controlType'] = 0
        self.__dict__['driver'] = ''

    def __getattr__(self, name):
        if name == 'controlType':
            return self.__dict__['controlType']
        if name == 'driver':
            return self.__dict__['driver']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'controlType':
            self.__dict__['controlType'] = value
        elif name == 'driver':
            self.__dict__['driver'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_SEND_CONTROL_CONTROL_TYPE, self.__dict__['controlType'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_SEND_CONTROL_DRIVER, self.__dict__['driver'])
        mmsg.AddMessage(MSG_KEY_PARAMS_SEND_CONTROL, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_SEND_CONTROL, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['controlType'] = submsg.FindU8(MSG_KEY_PARAMS_SEND_CONTROL_CONTROL_TYPE)
        self.__dict__['driver'] = submsg.FindString(MSG_KEY_PARAMS_SEND_CONTROL_DRIVER)