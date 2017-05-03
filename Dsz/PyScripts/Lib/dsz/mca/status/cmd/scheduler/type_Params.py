# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import mcl.object.MclTime
PARAMS_SCHEDULER_TYPE_DEFAULT = 0
PARAMS_SCHEDULER_TYPE_WINDOWS_AT = 1
PARAMS_SCHEDULER_TYPE_WINDOWS_GUI = 2
PARAMS_SCHEDULER_TYPE_WINDOWS_SERVICE = 3

class ParamsQuery:

    def __init__(self):
        self.__dict__['schedulerType'] = PARAMS_SCHEDULER_TYPE_DEFAULT
        self.__dict__['folder'] = ''
        self.__dict__['target'] = ''

    def __getattr__(self, name):
        if name == 'schedulerType':
            return self.__dict__['schedulerType']
        if name == 'folder':
            return self.__dict__['folder']
        if name == 'target':
            return self.__dict__['target']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'schedulerType':
            self.__dict__['schedulerType'] = value
        elif name == 'folder':
            self.__dict__['folder'] = value
        elif name == 'target':
            self.__dict__['target'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_QUERY_SCHEDULER_TYPE, self.__dict__['schedulerType'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_QUERY_FOLDER, self.__dict__['folder'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_QUERY_TARGET, self.__dict__['target'])
        mmsg.AddMessage(MSG_KEY_PARAMS_QUERY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_QUERY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['schedulerType'] = submsg.FindU8(MSG_KEY_PARAMS_QUERY_SCHEDULER_TYPE)
        except:
            pass

        try:
            self.__dict__['folder'] = submsg.FindString(MSG_KEY_PARAMS_QUERY_FOLDER)
        except:
            pass

        try:
            self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_QUERY_TARGET)
        except:
            pass


class ParamsAdd:

    def __init__(self):
        self.__dict__['schedulerType'] = PARAMS_SCHEDULER_TYPE_DEFAULT
        self.__dict__['interval'] = mcl.object.MclTime.MclTime()
        self.__dict__['target'] = ''
        self.__dict__['cmd'] = ''
        self.__dict__['folder'] = ''

    def __getattr__(self, name):
        if name == 'schedulerType':
            return self.__dict__['schedulerType']
        if name == 'interval':
            return self.__dict__['interval']
        if name == 'target':
            return self.__dict__['target']
        if name == 'cmd':
            return self.__dict__['cmd']
        if name == 'folder':
            return self.__dict__['folder']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'schedulerType':
            self.__dict__['schedulerType'] = value
        elif name == 'interval':
            self.__dict__['interval'] = value
        elif name == 'target':
            self.__dict__['target'] = value
        elif name == 'cmd':
            self.__dict__['cmd'] = value
        elif name == 'folder':
            self.__dict__['folder'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_ADD_SCHEDULER_TYPE, self.__dict__['schedulerType'])
        submsg.AddTime(MSG_KEY_PARAMS_ADD_INTERVAL, self.__dict__['interval'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_ADD_TARGET, self.__dict__['target'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_ADD_COMMAND, self.__dict__['cmd'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_ADD_FOLDER, self.__dict__['folder'])
        mmsg.AddMessage(MSG_KEY_PARAMS_ADD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_ADD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['schedulerType'] = submsg.FindU8(MSG_KEY_PARAMS_ADD_SCHEDULER_TYPE)
        except:
            pass

        self.__dict__['interval'] = submsg.FindTime(MSG_KEY_PARAMS_ADD_INTERVAL)
        try:
            self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_ADD_TARGET)
        except:
            pass

        self.__dict__['cmd'] = submsg.FindString(MSG_KEY_PARAMS_ADD_COMMAND)
        try:
            self.__dict__['folder'] = submsg.FindString(MSG_KEY_PARAMS_ADD_FOLDER)
        except:
            pass


class ParamsDelete:

    def __init__(self):
        self.__dict__['schedulerType'] = PARAMS_SCHEDULER_TYPE_DEFAULT
        self.__dict__['job'] = ''
        self.__dict__['target'] = ''

    def __getattr__(self, name):
        if name == 'schedulerType':
            return self.__dict__['schedulerType']
        if name == 'job':
            return self.__dict__['job']
        if name == 'target':
            return self.__dict__['target']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'schedulerType':
            self.__dict__['schedulerType'] = value
        elif name == 'job':
            self.__dict__['job'] = value
        elif name == 'target':
            self.__dict__['target'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_DELETE_SCHEDULER_TYPE, self.__dict__['schedulerType'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_DELETE_JOB, self.__dict__['job'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_DELETE_TARGET, self.__dict__['target'])
        mmsg.AddMessage(MSG_KEY_PARAMS_DELETE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_DELETE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['schedulerType'] = submsg.FindU8(MSG_KEY_PARAMS_DELETE_SCHEDULER_TYPE)
        except:
            pass

        self.__dict__['job'] = submsg.FindString(MSG_KEY_PARAMS_DELETE_JOB)
        try:
            self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_DELETE_TARGET)
        except:
            pass