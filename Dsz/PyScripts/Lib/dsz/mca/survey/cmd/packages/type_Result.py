# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime

class Result:

    def __init__(self):
        self.__dict__['name'] = ''
        self.__dict__['description'] = ''
        self.__dict__['version'] = ''
        self.__dict__['revision'] = ''
        self.__dict__['size'] = 0
        self.__dict__['installDate'] = mcl.object.MclTime.MclTime()

    def __getattr__(self, name):
        if name == 'name':
            return self.__dict__['name']
        if name == 'description':
            return self.__dict__['description']
        if name == 'version':
            return self.__dict__['version']
        if name == 'revision':
            return self.__dict__['revision']
        if name == 'size':
            return self.__dict__['size']
        if name == 'installDate':
            return self.__dict__['installDate']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'name':
            self.__dict__['name'] = value
        elif name == 'description':
            self.__dict__['description'] = value
        elif name == 'version':
            self.__dict__['version'] = value
        elif name == 'revision':
            self.__dict__['revision'] = value
        elif name == 'size':
            self.__dict__['size'] = value
        elif name == 'installDate':
            self.__dict__['installDate'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DESCRIPTION, self.__dict__['description'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_VERSION, self.__dict__['version'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_REVISION, self.__dict__['revision'])
        submsg.AddU64(MSG_KEY_RESULT_SIZE_, self.__dict__['size'])
        submsg.AddTime(MSG_KEY_RESULT_INSTALL_DATE, self.__dict__['installDate'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_NAME)
        self.__dict__['description'] = submsg.FindString(MSG_KEY_RESULT_DESCRIPTION)
        self.__dict__['version'] = submsg.FindString(MSG_KEY_RESULT_VERSION)
        self.__dict__['revision'] = submsg.FindString(MSG_KEY_RESULT_REVISION)
        self.__dict__['size'] = submsg.FindU64(MSG_KEY_RESULT_SIZE_)
        self.__dict__['installDate'] = submsg.FindTime(MSG_KEY_RESULT_INSTALL_DATE)