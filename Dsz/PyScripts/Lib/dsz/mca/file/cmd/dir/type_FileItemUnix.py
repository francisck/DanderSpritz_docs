# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_FileItemUnix.py
from types import *
FILE_ITEM_UNIX_FLAG_PERM_SET_UID = 1
FILE_ITEM_UNIX_FLAG_PERM_SET_GID = 2
FILE_ITEM_UNIX_FLAG_PERM_STICKY = 4
FILE_ITEM_UNIX_FLAG_PERM_OWNER_READ = 8
FILE_ITEM_UNIX_FLAG_PERM_OWNER_WRITE = 16
FILE_ITEM_UNIX_FLAG_PERM_OWNER_EXEC = 32
FILE_ITEM_UNIX_FLAG_PERM_GROUP_READ = 64
FILE_ITEM_UNIX_FLAG_PERM_GROUP_WRITE = 128
FILE_ITEM_UNIX_FLAG_PERM_GROUP_EXEC = 256
FILE_ITEM_UNIX_FLAG_PERM_WORLD_READ = 512
FILE_ITEM_UNIX_FLAG_PERM_WORLD_WRITE = 1024
FILE_ITEM_UNIX_FLAG_PERM_WORLD_EXEC = 2048

class FileItemUnix:

    def __init__(self):
        self.__dict__['inode'] = 0
        self.__dict__['numHardLinks'] = 0
        self.__dict__['groupId'] = 0
        self.__dict__['ownerId'] = 0
        self.__dict__['permissions'] = 0
        self.__dict__['owner'] = ''
        self.__dict__['group'] = ''

    def __getattr__(self, name):
        if name == 'inode':
            return self.__dict__['inode']
        if name == 'numHardLinks':
            return self.__dict__['numHardLinks']
        if name == 'groupId':
            return self.__dict__['groupId']
        if name == 'ownerId':
            return self.__dict__['ownerId']
        if name == 'permissions':
            return self.__dict__['permissions']
        if name == 'owner':
            return self.__dict__['owner']
        if name == 'group':
            return self.__dict__['group']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'inode':
            self.__dict__['inode'] = value
        elif name == 'numHardLinks':
            self.__dict__['numHardLinks'] = value
        elif name == 'groupId':
            self.__dict__['groupId'] = value
        elif name == 'ownerId':
            self.__dict__['ownerId'] = value
        elif name == 'permissions':
            self.__dict__['permissions'] = value
        elif name == 'owner':
            self.__dict__['owner'] = value
        elif name == 'group':
            self.__dict__['group'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_FILE_ITEM_UNIX_INODE, self.__dict__['inode'])
        submsg.AddU32(MSG_KEY_FILE_ITEM_UNIX_NUM_HARD_LINKS, self.__dict__['numHardLinks'])
        submsg.AddU32(MSG_KEY_FILE_ITEM_UNIX_GROUP_ID, self.__dict__['groupId'])
        submsg.AddU32(MSG_KEY_FILE_ITEM_UNIX_OWNER_ID, self.__dict__['ownerId'])
        submsg.AddU32(MSG_KEY_FILE_ITEM_UNIX_PERMISSIONS, self.__dict__['permissions'])
        submsg.AddStringUtf8(MSG_KEY_FILE_ITEM_UNIX_OWNER, self.__dict__['owner'])
        submsg.AddStringUtf8(MSG_KEY_FILE_ITEM_UNIX_GROUP, self.__dict__['group'])
        mmsg.AddMessage(MSG_KEY_FILE_ITEM_UNIX, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_FILE_ITEM_UNIX, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['inode'] = submsg.FindU64(MSG_KEY_FILE_ITEM_UNIX_INODE)
        self.__dict__['numHardLinks'] = submsg.FindU32(MSG_KEY_FILE_ITEM_UNIX_NUM_HARD_LINKS)
        self.__dict__['groupId'] = submsg.FindU32(MSG_KEY_FILE_ITEM_UNIX_GROUP_ID)
        self.__dict__['ownerId'] = submsg.FindU32(MSG_KEY_FILE_ITEM_UNIX_OWNER_ID)
        self.__dict__['permissions'] = submsg.FindU32(MSG_KEY_FILE_ITEM_UNIX_PERMISSIONS)
        self.__dict__['owner'] = submsg.FindString(MSG_KEY_FILE_ITEM_UNIX_OWNER)
        self.__dict__['group'] = submsg.FindString(MSG_KEY_FILE_ITEM_UNIX_GROUP)