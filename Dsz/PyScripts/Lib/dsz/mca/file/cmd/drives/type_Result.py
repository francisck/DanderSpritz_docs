# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
RESULT_DRIVE_TYPE_UNKNOWN = 0
RESULT_DRIVE_TYPE_REMOVABLE = 1
RESULT_DRIVE_TYPE_FIXED = 2
RESULT_DRIVE_TYPE_NETWORK = 3
RESULT_DRIVE_TYPE_CDROM = 4
RESULT_DRIVE_TYPE_RAMDISK = 5
RESULT_DRIVE_TYPE_SIMULATED = 6
RESULT_FLAG_READ = 1
RESULT_FLAG_WRITE = 2
RESULT_FLAG_CASE_SENSITIVE_SEARCH = 4
RESULT_FLAG_CASE_PRESERVED_NAMES = 8
RESULT_FLAG_UNICODE_ON_DISK = 16
RESULT_FLAG_PERSISTENT_ACLS = 32
RESULT_FLAG_FILE_COMPRESSION = 64
RESULT_FLAG_QUOTAS = 128
RESULT_FLAG_SUPPORTS_SPARSE_FILES = 256
RESULT_FLAG_SUPPORTS_REPARSE_POINTS = 512
RESULT_FLAG_SUPPORTS_REMOTE_STORAGE = 1024
RESULT_FLAG_IS_COMPRESSED = 2048
RESULT_FLAG_SUPPORTS_OBJECT_IDS = 4096
RESULT_FLAG_SUPPORTS_ENCRYPTION = 8192
RESULT_FLAG_SUPPORTS_NAMED_STREAMS = 16384

class Result:

    def __init__(self):
        self.__dict__['type'] = RESULT_DRIVE_TYPE_UNKNOWN
        self.__dict__['flags'] = 0
        self.__dict__['volumeSerialNumber'] = 0
        self.__dict__['maxComponentLength'] = 0
        self.__dict__['location'] = ''
        self.__dict__['source'] = ''
        self.__dict__['filesystem'] = ''
        self.__dict__['options'] = ''

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'volumeSerialNumber':
            return self.__dict__['volumeSerialNumber']
        if name == 'maxComponentLength':
            return self.__dict__['maxComponentLength']
        if name == 'location':
            return self.__dict__['location']
        if name == 'source':
            return self.__dict__['source']
        if name == 'filesystem':
            return self.__dict__['filesystem']
        if name == 'options':
            return self.__dict__['options']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'volumeSerialNumber':
            self.__dict__['volumeSerialNumber'] = value
        elif name == 'maxComponentLength':
            self.__dict__['maxComponentLength'] = value
        elif name == 'location':
            self.__dict__['location'] = value
        elif name == 'source':
            self.__dict__['source'] = value
        elif name == 'filesystem':
            self.__dict__['filesystem'] = value
        elif name == 'options':
            self.__dict__['options'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_TYPE, self.__dict__['type'])
        submsg.AddU32(MSG_KEY_RESULT_FLAGS, self.__dict__['flags'])
        submsg.AddU32(MSG_KEY_RESULT_VOLUME_SERIAL_NUMBER, self.__dict__['volumeSerialNumber'])
        submsg.AddU32(MSG_KEY_RESULT_MAX_COMPONENT_LENGTH, self.__dict__['maxComponentLength'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_LOCATION, self.__dict__['location'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_SOURCE, self.__dict__['source'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_FILE_SYSTEM, self.__dict__['filesystem'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_OPTIONS, self.__dict__['options'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_TYPE)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_FLAGS)
        self.__dict__['volumeSerialNumber'] = submsg.FindU32(MSG_KEY_RESULT_VOLUME_SERIAL_NUMBER)
        self.__dict__['maxComponentLength'] = submsg.FindU32(MSG_KEY_RESULT_MAX_COMPONENT_LENGTH)
        self.__dict__['location'] = submsg.FindString(MSG_KEY_RESULT_LOCATION)
        self.__dict__['source'] = submsg.FindString(MSG_KEY_RESULT_SOURCE)
        self.__dict__['filesystem'] = submsg.FindString(MSG_KEY_RESULT_FILE_SYSTEM)
        self.__dict__['options'] = submsg.FindString(MSG_KEY_RESULT_OPTIONS)