# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class Result:

    def __init__(self):
        self.__dict__['afterReboot'] = False
        self.__dict__['deleteStatus'] = 0
        self.__dict__['filename'] = ''

    def __getattr__(self, name):
        if name == 'afterReboot':
            return self.__dict__['afterReboot']
        if name == 'deleteStatus':
            return self.__dict__['deleteStatus']
        if name == 'filename':
            return self.__dict__['filename']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'afterReboot':
            self.__dict__['afterReboot'] = value
        elif name == 'deleteStatus':
            self.__dict__['deleteStatus'] = value
        elif name == 'filename':
            self.__dict__['filename'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_AFTER_REBOOT, self.__dict__['afterReboot'])
        submsg.AddU32(MSG_KEY_RESULT_DELETE_STATUS, self.__dict__['deleteStatus'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_FILENAME, self.__dict__['filename'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['afterReboot'] = submsg.FindBool(MSG_KEY_RESULT_AFTER_REBOOT)
        self.__dict__['deleteStatus'] = submsg.FindU32(MSG_KEY_RESULT_DELETE_STATUS)
        self.__dict__['filename'] = submsg.FindString(MSG_KEY_RESULT_FILENAME)