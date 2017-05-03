# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_FileItem.py
from types import *
import mcl.object.MclTime
FILE_ITEM_FLAG_TYPE_ACCESS_DENIED = 1
FILE_ITEM_FLAG_TYPE_UNIX = 2
FILE_ITEM_FLAG_TYPE_WINDOWS = 4
FILE_ITEM_FLAG_ATTRIBS_DIR = 1
FILE_ITEM_FLAG_ATTRIBS_LINK = 2
FILE_ITEM_FLAG_ATTRIBS_SOCKET = 4
FILE_ITEM_FLAG_ATTRIBS_BLOCK_DEV = 8
FILE_ITEM_FLAG_ATTRIBS_CHAR_DEV = 16
FILE_ITEM_FLAG_ATTRIBS_NAMED_PIPE = 32
FILE_ITEM_FLAG_ATTRIBS_ARCHIVE = 64
FILE_ITEM_FLAG_ATTRIBS_COMPRESSED = 128
FILE_ITEM_FLAG_ATTRIBS_ENCRYPTED = 256
FILE_ITEM_FLAG_ATTRIBS_HIDDEN = 512
FILE_ITEM_FLAG_ATTRIBS_OFFLINE = 1024
FILE_ITEM_FLAG_ATTRIBS_READONLY = 2048
FILE_ITEM_FLAG_ATTRIBS_SYSTEM = 4096
FILE_ITEM_FLAG_ATTRIBS_TEMPORARY = 8192
FILE_ITEM_FLAG_ATTRIBS_SPARSE_FILE = 16384
FILE_ITEM_FLAG_ATTRIBS_VIRTUAL = 32768
FILE_ITEM_FLAG_ATTRIBS_NOT_INDEXED = 65536
FILE_ITEM_FLAG_ATTRIBS_DEVICE = 131072

class FileItem:

    def __init__(self):
        self.__dict__['typeFlags'] = 0
        self.__dict__['attributes'] = 0
        self.__dict__['size'] = 0
        self.__dict__['createdTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['accessedTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['modifiedTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['name'] = ''

    def __getattr__(self, name):
        if name == 'typeFlags':
            return self.__dict__['typeFlags']
        if name == 'attributes':
            return self.__dict__['attributes']
        if name == 'size':
            return self.__dict__['size']
        if name == 'createdTime':
            return self.__dict__['createdTime']
        if name == 'accessedTime':
            return self.__dict__['accessedTime']
        if name == 'modifiedTime':
            return self.__dict__['modifiedTime']
        if name == 'name':
            return self.__dict__['name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'typeFlags':
            self.__dict__['typeFlags'] = value
        elif name == 'attributes':
            self.__dict__['attributes'] = value
        elif name == 'size':
            self.__dict__['size'] = value
        elif name == 'createdTime':
            self.__dict__['createdTime'] = value
        elif name == 'accessedTime':
            self.__dict__['accessedTime'] = value
        elif name == 'modifiedTime':
            self.__dict__['modifiedTime'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_FILE_ITEM_TYPE_FLAGS, self.__dict__['typeFlags'])
        submsg.AddU32(MSG_KEY_FILE_ITEM_ATTRIBUTES, self.__dict__['attributes'])
        submsg.AddU64(MSG_KEY_FILE_ITEM_SIZE, self.__dict__['size'])
        submsg.AddTime(MSG_KEY_FILE_ITEM_CREATED_TIME, self.__dict__['createdTime'])
        submsg.AddTime(MSG_KEY_FILE_ITEM_ACCESSED_TIME, self.__dict__['accessedTime'])
        submsg.AddTime(MSG_KEY_FILE_ITEM_MODIFIED_TIME, self.__dict__['modifiedTime'])
        submsg.AddStringUtf8(MSG_KEY_FILE_ITEM_NAME, self.__dict__['name'])
        mmsg.AddMessage(MSG_KEY_FILE_ITEM, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_FILE_ITEM, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['typeFlags'] = submsg.FindU16(MSG_KEY_FILE_ITEM_TYPE_FLAGS)
        self.__dict__['attributes'] = submsg.FindU32(MSG_KEY_FILE_ITEM_ATTRIBUTES)
        self.__dict__['size'] = submsg.FindU64(MSG_KEY_FILE_ITEM_SIZE)
        self.__dict__['createdTime'] = submsg.FindTime(MSG_KEY_FILE_ITEM_CREATED_TIME)
        self.__dict__['accessedTime'] = submsg.FindTime(MSG_KEY_FILE_ITEM_ACCESSED_TIME)
        self.__dict__['modifiedTime'] = submsg.FindTime(MSG_KEY_FILE_ITEM_MODIFIED_TIME)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_FILE_ITEM_NAME)