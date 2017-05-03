# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import mcl.object.MclTime
PARAMS_SET_TYPE_SET = 1
PARAMS_SET_TYPE_REPLACE = 2
PARAMS_SET_TYPE_REMOVE = 3
PARAMS_SET_TYPE_ADD = 4

class GetParams:

    def __init__(self):
        self.__dict__['file'] = ''

    def __getattr__(self, name):
        if name == 'file':
            return self.__dict__['file']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'file':
            self.__dict__['file'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_GET_FILE, self.__dict__['file'])
        mmsg.AddMessage(MSG_KEY_PARAMS_GET, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_GET, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['file'] = submsg.FindString(MSG_KEY_PARAMS_GET_FILE)


class SetParams:

    def __init__(self):
        self.__dict__['ftAccessed'] = mcl.object.MclTime.MclTime()
        self.__dict__['ftCreated'] = mcl.object.MclTime.MclTime()
        self.__dict__['ftModified'] = mcl.object.MclTime.MclTime()
        self.__dict__['attributes'] = 0
        self.__dict__['setType'] = 0
        self.__dict__['file'] = ''
        self.__dict__['owner'] = ''
        self.__dict__['group'] = ''

    def __getattr__(self, name):
        if name == 'ftAccessed':
            return self.__dict__['ftAccessed']
        if name == 'ftCreated':
            return self.__dict__['ftCreated']
        if name == 'ftModified':
            return self.__dict__['ftModified']
        if name == 'attributes':
            return self.__dict__['attributes']
        if name == 'setType':
            return self.__dict__['setType']
        if name == 'file':
            return self.__dict__['file']
        if name == 'owner':
            return self.__dict__['owner']
        if name == 'group':
            return self.__dict__['group']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'ftAccessed':
            self.__dict__['ftAccessed'] = value
        elif name == 'ftCreated':
            self.__dict__['ftCreated'] = value
        elif name == 'ftModified':
            self.__dict__['ftModified'] = value
        elif name == 'attributes':
            self.__dict__['attributes'] = value
        elif name == 'setType':
            self.__dict__['setType'] = value
        elif name == 'file':
            self.__dict__['file'] = value
        elif name == 'owner':
            self.__dict__['owner'] = value
        elif name == 'group':
            self.__dict__['group'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddTime(MSG_KEY_PARAMS_SET_FILETIME_ACCESSED, self.__dict__['ftAccessed'])
        submsg.AddTime(MSG_KEY_PARAMS_SET_FILETIME_CREATED, self.__dict__['ftCreated'])
        submsg.AddTime(MSG_KEY_PARAMS_SET_FILETIME_MODIFIED, self.__dict__['ftModified'])
        submsg.AddU64(MSG_KEY_PARAMS_SET_ATTRIBUTES, self.__dict__['attributes'])
        submsg.AddU8(MSG_KEY_PARAMS_SET_TYPE, self.__dict__['setType'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_SET_FILE, self.__dict__['file'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_SET_OWNER, self.__dict__['owner'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_SET_GROUP, self.__dict__['group'])
        mmsg.AddMessage(MSG_KEY_PARAMS_SET, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_SET, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['ftAccessed'] = submsg.FindTime(MSG_KEY_PARAMS_SET_FILETIME_ACCESSED)
        except:
            pass

        try:
            self.__dict__['ftCreated'] = submsg.FindTime(MSG_KEY_PARAMS_SET_FILETIME_CREATED)
        except:
            pass

        try:
            self.__dict__['ftModified'] = submsg.FindTime(MSG_KEY_PARAMS_SET_FILETIME_MODIFIED)
        except:
            pass

        try:
            self.__dict__['attributes'] = submsg.FindU64(MSG_KEY_PARAMS_SET_ATTRIBUTES)
        except:
            pass

        self.__dict__['setType'] = submsg.FindU8(MSG_KEY_PARAMS_SET_TYPE)
        self.__dict__['file'] = submsg.FindString(MSG_KEY_PARAMS_SET_FILE)
        try:
            self.__dict__['owner'] = submsg.FindString(MSG_KEY_PARAMS_SET_OWNER)
        except:
            pass

        try:
            self.__dict__['group'] = submsg.FindString(MSG_KEY_PARAMS_SET_GROUP)
        except:
            pass