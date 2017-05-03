# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *

class ParamsMap:

    def __init__(self):
        self.__dict__['target'] = ''
        self.__dict__['resource'] = ''
        self.__dict__['drive'] = ''
        self.__dict__['username'] = ''
        self.__dict__['password'] = ''
        self.__dict__['domain'] = ''

    def __getattr__(self, name):
        if name == 'target':
            return self.__dict__['target']
        if name == 'resource':
            return self.__dict__['resource']
        if name == 'drive':
            return self.__dict__['drive']
        if name == 'username':
            return self.__dict__['username']
        if name == 'password':
            return self.__dict__['password']
        if name == 'domain':
            return self.__dict__['domain']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'target':
            self.__dict__['target'] = value
        elif name == 'resource':
            self.__dict__['resource'] = value
        elif name == 'drive':
            self.__dict__['drive'] = value
        elif name == 'username':
            self.__dict__['username'] = value
        elif name == 'password':
            self.__dict__['password'] = value
        elif name == 'domain':
            self.__dict__['domain'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_MAP_TARGET, self.__dict__['target'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_MAP_RESOURCE, self.__dict__['resource'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_MAP_DRIVE, self.__dict__['drive'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_MAP_USERNAME, self.__dict__['username'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_MAP_PASSWORD, self.__dict__['password'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_MAP_DOMAIN, self.__dict__['domain'])
        mmsg.AddMessage(MSG_KEY_PARAMS_MAP, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_MAP, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_MAP_TARGET)
        self.__dict__['resource'] = submsg.FindString(MSG_KEY_PARAMS_MAP_RESOURCE)
        self.__dict__['drive'] = submsg.FindString(MSG_KEY_PARAMS_MAP_DRIVE)
        self.__dict__['username'] = submsg.FindString(MSG_KEY_PARAMS_MAP_USERNAME)
        self.__dict__['password'] = submsg.FindString(MSG_KEY_PARAMS_MAP_PASSWORD)
        self.__dict__['domain'] = submsg.FindString(MSG_KEY_PARAMS_MAP_DOMAIN)


class ParamsQuery:

    def __init__(self):
        self.__dict__['target'] = ''
        self.__dict__['username'] = ''
        self.__dict__['password'] = ''
        self.__dict__['domain'] = ''

    def __getattr__(self, name):
        if name == 'target':
            return self.__dict__['target']
        if name == 'username':
            return self.__dict__['username']
        if name == 'password':
            return self.__dict__['password']
        if name == 'domain':
            return self.__dict__['domain']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'target':
            self.__dict__['target'] = value
        elif name == 'username':
            self.__dict__['username'] = value
        elif name == 'password':
            self.__dict__['password'] = value
        elif name == 'domain':
            self.__dict__['domain'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_QUERY_TARGET, self.__dict__['target'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_QUERY_USERNAME, self.__dict__['username'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_QUERY_PASSWORD, self.__dict__['password'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_QUERY_DOMAIN, self.__dict__['domain'])
        mmsg.AddMessage(MSG_KEY_PARAMS_QUERY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_QUERY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_QUERY_TARGET)
        self.__dict__['username'] = submsg.FindString(MSG_KEY_PARAMS_QUERY_USERNAME)
        self.__dict__['password'] = submsg.FindString(MSG_KEY_PARAMS_QUERY_PASSWORD)
        self.__dict__['domain'] = submsg.FindString(MSG_KEY_PARAMS_QUERY_DOMAIN)