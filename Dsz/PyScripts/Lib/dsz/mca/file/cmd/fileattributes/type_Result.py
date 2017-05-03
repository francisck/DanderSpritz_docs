# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime
REPARSE_TYPE_COULD_NOT_READ = 0
REPARSE_TYPE_MICROSOFT = 1
REPARSE_TYPE_THIRD_PARTY = 2
REPARSE_FLAG_SURROGATE = 1
REPARSE_FLAG_MOUNT_POINT = 2
REPARSE_FLAG_MICROSOFT_HSM = 4
REPARSE_FLAG_MICROSOFT_SIS = 8
REPARSE_FLAG_MICROSOFT_DFS = 16
REPARSE_FLAG_SYMLINK = 32
REPARSE_FLAG_DFSR = 64

class Result:

    def __init__(self):
        self.__dict__['set'] = False
        self.__dict__['ftAccessed'] = mcl.object.MclTime.MclTime()
        self.__dict__['ftCreated'] = mcl.object.MclTime.MclTime()
        self.__dict__['ftModified'] = mcl.object.MclTime.MclTime()
        self.__dict__['attributes'] = 0
        self.__dict__['size'] = 0
        self.__dict__['file'] = ''
        self.__dict__['owner'] = ''
        self.__dict__['group'] = ''

    def __getattr__(self, name):
        if name == 'set':
            return self.__dict__['set']
        if name == 'ftAccessed':
            return self.__dict__['ftAccessed']
        if name == 'ftCreated':
            return self.__dict__['ftCreated']
        if name == 'ftModified':
            return self.__dict__['ftModified']
        if name == 'attributes':
            return self.__dict__['attributes']
        if name == 'size':
            return self.__dict__['size']
        if name == 'file':
            return self.__dict__['file']
        if name == 'owner':
            return self.__dict__['owner']
        if name == 'group':
            return self.__dict__['group']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'set':
            self.__dict__['set'] = value
        elif name == 'ftAccessed':
            self.__dict__['ftAccessed'] = value
        elif name == 'ftCreated':
            self.__dict__['ftCreated'] = value
        elif name == 'ftModified':
            self.__dict__['ftModified'] = value
        elif name == 'attributes':
            self.__dict__['attributes'] = value
        elif name == 'size':
            self.__dict__['size'] = value
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
        submsg.AddBool(MSG_KEY_RESULT_SET, self.__dict__['set'])
        submsg.AddTime(MSG_KEY_RESULT_FILETIME_ACCESSED, self.__dict__['ftAccessed'])
        submsg.AddTime(MSG_KEY_RESULT_FILETIME_CREATED, self.__dict__['ftCreated'])
        submsg.AddTime(MSG_KEY_RESULT_FILETIME_MODIFIED, self.__dict__['ftModified'])
        submsg.AddU64(MSG_KEY_RESULT_ATTRIBUTES, self.__dict__['attributes'])
        submsg.AddU64(MSG_KEY_RESULT_SIZE, self.__dict__['size'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_FILE, self.__dict__['file'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_OWNER, self.__dict__['owner'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_GROUP, self.__dict__['group'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['set'] = submsg.FindBool(MSG_KEY_RESULT_SET)
        self.__dict__['ftAccessed'] = submsg.FindTime(MSG_KEY_RESULT_FILETIME_ACCESSED)
        self.__dict__['ftCreated'] = submsg.FindTime(MSG_KEY_RESULT_FILETIME_CREATED)
        self.__dict__['ftModified'] = submsg.FindTime(MSG_KEY_RESULT_FILETIME_MODIFIED)
        self.__dict__['attributes'] = submsg.FindU64(MSG_KEY_RESULT_ATTRIBUTES)
        self.__dict__['size'] = submsg.FindU64(MSG_KEY_RESULT_SIZE)
        self.__dict__['file'] = submsg.FindString(MSG_KEY_RESULT_FILE)
        self.__dict__['owner'] = submsg.FindString(MSG_KEY_RESULT_OWNER)
        self.__dict__['group'] = submsg.FindString(MSG_KEY_RESULT_GROUP)


class ReparseResult:

    def __init__(self):
        self.__dict__['type'] = REPARSE_TYPE_COULD_NOT_READ
        self.__dict__['flags'] = 0
        self.__dict__['reparseData1'] = ''
        self.__dict__['reparseData2'] = ''
        self.__dict__['reparseData3'] = ''
        self.__dict__['reparseData4'] = ''

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'reparseData1':
            return self.__dict__['reparseData1']
        if name == 'reparseData2':
            return self.__dict__['reparseData2']
        if name == 'reparseData3':
            return self.__dict__['reparseData3']
        if name == 'reparseData4':
            return self.__dict__['reparseData4']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'reparseData1':
            self.__dict__['reparseData1'] = value
        elif name == 'reparseData2':
            self.__dict__['reparseData2'] = value
        elif name == 'reparseData3':
            self.__dict__['reparseData3'] = value
        elif name == 'reparseData4':
            self.__dict__['reparseData4'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_REPARSE_TYPE, self.__dict__['type'])
        submsg.AddU32(MSG_KEY_RESULT_REPARSE_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_REPARSE_REPARSE_DATA1, self.__dict__['reparseData1'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_REPARSE_REPARSE_DATA2, self.__dict__['reparseData2'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_REPARSE_REPARSE_DATA3, self.__dict__['reparseData3'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_REPARSE_REPARSE_DATA4, self.__dict__['reparseData4'])
        mmsg.AddMessage(MSG_KEY_RESULT_REPARSE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_REPARSE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_REPARSE_TYPE)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_REPARSE_FLAGS)
        self.__dict__['reparseData1'] = submsg.FindString(MSG_KEY_RESULT_REPARSE_REPARSE_DATA1)
        self.__dict__['reparseData2'] = submsg.FindString(MSG_KEY_RESULT_REPARSE_REPARSE_DATA2)
        self.__dict__['reparseData3'] = submsg.FindString(MSG_KEY_RESULT_REPARSE_REPARSE_DATA3)
        self.__dict__['reparseData4'] = submsg.FindString(MSG_KEY_RESULT_REPARSE_REPARSE_DATA4)