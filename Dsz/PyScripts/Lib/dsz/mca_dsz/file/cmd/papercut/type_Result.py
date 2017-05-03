# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime
import array
RESULT_FLAG_OUTSIDE_OF_FILESIZE = 1

class ResultFileInfo:

    def __init__(self):
        self.__dict__['fileSize'] = 0
        self.__dict__['createTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['accessTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['modifyTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['openStatus'] = 0
        self.__dict__['offset'] = 0
        self.__dict__['fileName'] = ''
        self.__dict__['flags'] = 0

    def __getattr__(self, name):
        if name == 'fileSize':
            return self.__dict__['fileSize']
        if name == 'createTime':
            return self.__dict__['createTime']
        if name == 'accessTime':
            return self.__dict__['accessTime']
        if name == 'modifyTime':
            return self.__dict__['modifyTime']
        if name == 'openStatus':
            return self.__dict__['openStatus']
        if name == 'offset':
            return self.__dict__['offset']
        if name == 'fileName':
            return self.__dict__['fileName']
        if name == 'flags':
            return self.__dict__['flags']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'fileSize':
            self.__dict__['fileSize'] = value
        elif name == 'createTime':
            self.__dict__['createTime'] = value
        elif name == 'accessTime':
            self.__dict__['accessTime'] = value
        elif name == 'modifyTime':
            self.__dict__['modifyTime'] = value
        elif name == 'openStatus':
            self.__dict__['openStatus'] = value
        elif name == 'offset':
            self.__dict__['offset'] = value
        elif name == 'fileName':
            self.__dict__['fileName'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_FILE_INFO_FILE_SIZE, self.__dict__['fileSize'])
        submsg.AddTime(MSG_KEY_RESULT_FILE_INFO_CREATE_TIME, self.__dict__['createTime'])
        submsg.AddTime(MSG_KEY_RESULT_FILE_INFO_ACCESS_TIME, self.__dict__['accessTime'])
        submsg.AddTime(MSG_KEY_RESULT_FILE_INFO_MODIFY_TIME, self.__dict__['modifyTime'])
        submsg.AddU32(MSG_KEY_RESULT_FILE_INFO_OPEN_STATUS, self.__dict__['openStatus'])
        submsg.AddS64(MSG_KEY_RESULT_FILE_INFO_OFFSET, self.__dict__['offset'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_FILE_INFO_NAME, self.__dict__['fileName'])
        submsg.AddU16(MSG_KEY_RESULT_FILE_INFO_FLAGS, self.__dict__['flags'])
        mmsg.AddMessage(MSG_KEY_RESULT_FILE_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_FILE_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['fileSize'] = submsg.FindU64(MSG_KEY_RESULT_FILE_INFO_FILE_SIZE)
        self.__dict__['createTime'] = submsg.FindTime(MSG_KEY_RESULT_FILE_INFO_CREATE_TIME)
        self.__dict__['accessTime'] = submsg.FindTime(MSG_KEY_RESULT_FILE_INFO_ACCESS_TIME)
        self.__dict__['modifyTime'] = submsg.FindTime(MSG_KEY_RESULT_FILE_INFO_MODIFY_TIME)
        self.__dict__['openStatus'] = submsg.FindU32(MSG_KEY_RESULT_FILE_INFO_OPEN_STATUS)
        self.__dict__['offset'] = submsg.FindS64(MSG_KEY_RESULT_FILE_INFO_OFFSET)
        self.__dict__['fileName'] = submsg.FindString(MSG_KEY_RESULT_FILE_INFO_NAME)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_RESULT_FILE_INFO_FLAGS)


class ResultData:

    def __init__(self):
        self.__dict__['buffer'] = array.array('B')

    def __getattr__(self, name):
        if name == 'buffer':
            return self.__dict__['buffer']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'buffer':
            self.__dict__['buffer'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddData(MSG_KEY_RESULT_DATA_BUFFER, self.__dict__['buffer'])
        mmsg.AddMessage(MSG_KEY_RESULT_DATA, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_DATA, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['buffer'] = submsg.FindData(MSG_KEY_RESULT_DATA_BUFFER)


class ResultLock:

    def __init__(self):
        self.__dict__['filename'] = ''
        self.__dict__['locktime'] = mcl.object.MclTime.MclTime()

    def __getattr__(self, name):
        if name == 'filename':
            return self.__dict__['filename']
        if name == 'locktime':
            return self.__dict__['locktime']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'filename':
            self.__dict__['filename'] = value
        elif name == 'locktime':
            self.__dict__['locktime'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_LOCK_FILENAME, self.__dict__['filename'])
        submsg.AddTime(MSG_KEY_RESULT_LOCK_LOCK_TIME, self.__dict__['locktime'])
        mmsg.AddMessage(MSG_KEY_RESULT_LOCK, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_LOCK, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['filename'] = submsg.FindString(MSG_KEY_RESULT_LOCK_FILENAME)
        self.__dict__['locktime'] = submsg.FindTime(MSG_KEY_RESULT_LOCK_LOCK_TIME)


class ResultTrim:

    def __init__(self):
        self.__dict__['filename'] = ''
        self.__dict__['old_filesize'] = 0
        self.__dict__['new_filesize'] = 0

    def __getattr__(self, name):
        if name == 'filename':
            return self.__dict__['filename']
        if name == 'old_filesize':
            return self.__dict__['old_filesize']
        if name == 'new_filesize':
            return self.__dict__['new_filesize']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'filename':
            self.__dict__['filename'] = value
        elif name == 'old_filesize':
            self.__dict__['old_filesize'] = value
        elif name == 'new_filesize':
            self.__dict__['new_filesize'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TRIM_FILENAME, self.__dict__['filename'])
        submsg.AddU64(MSG_KEY_RESULT_TRIM_OLD_FILESIZE, self.__dict__['old_filesize'])
        submsg.AddU64(MSG_KEY_RESULT_TRIM_NEW_FILESIZE, self.__dict__['new_filesize'])
        mmsg.AddMessage(MSG_KEY_RESULT_TRIM, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TRIM, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['filename'] = submsg.FindString(MSG_KEY_RESULT_TRIM_FILENAME)
        self.__dict__['old_filesize'] = submsg.FindU64(MSG_KEY_RESULT_TRIM_OLD_FILESIZE)
        self.__dict__['new_filesize'] = submsg.FindU64(MSG_KEY_RESULT_TRIM_NEW_FILESIZE)


class ResultMap:

    def __init__(self):
        self.__dict__['filename'] = ''
        self.__dict__['pid'] = 0

    def __getattr__(self, name):
        if name == 'filename':
            return self.__dict__['filename']
        if name == 'pid':
            return self.__dict__['pid']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'filename':
            self.__dict__['filename'] = value
        elif name == 'pid':
            self.__dict__['pid'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_MAP_FILENAME, self.__dict__['filename'])
        submsg.AddU32(MSG_KEY_RESULT_MAP_PROCESS_ID, self.__dict__['pid'])
        mmsg.AddMessage(MSG_KEY_RESULT_MAP, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MAP, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['filename'] = submsg.FindString(MSG_KEY_RESULT_MAP_FILENAME)
        self.__dict__['pid'] = submsg.FindU32(MSG_KEY_RESULT_MAP_PROCESS_ID)