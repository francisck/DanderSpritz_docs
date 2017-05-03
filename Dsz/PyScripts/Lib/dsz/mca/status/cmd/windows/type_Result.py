# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
RESULT_BUTTON_FLAG_IS_ENABLED = 1
RESULT_WINSTA_FLAG_VISIBLE = 1
RESULT_WININFO_FLAG_IS_VISIBLE = 1
RESULT_WININFO_FLAG_IS_MINIMIZED = 2

class ResultButton:

    def __init__(self):
        self.__dict__['id'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['text'] = ''

    def __getattr__(self, name):
        if name == 'id':
            return self.__dict__['id']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'text':
            return self.__dict__['text']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'id':
            self.__dict__['id'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'text':
            self.__dict__['text'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_BUTTON_ID, self.__dict__['id'])
        submsg.AddU16(MSG_KEY_RESULT_BUTTON_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_BUTTON_TEXT, self.__dict__['text'])
        mmsg.AddMessage(MSG_KEY_RESULT_BUTTON, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_BUTTON, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_BUTTON_ID)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_RESULT_BUTTON_FLAGS)
        self.__dict__['text'] = submsg.FindString(MSG_KEY_RESULT_BUTTON_TEXT)


class ResultWindowStations:

    def __init__(self):
        self.__dict__['openStatus'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['name'] = ''

    def __getattr__(self, name):
        if name == 'openStatus':
            return self.__dict__['openStatus']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'name':
            return self.__dict__['name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'openStatus':
            self.__dict__['openStatus'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_WINDOW_STATION_INFO_OPEN_STATUS, self.__dict__['openStatus'])
        submsg.AddU16(MSG_KEY_RESULT_WINDOW_STATION_INFO_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_WINDOW_STATION_INFO_NAME, self.__dict__['name'])
        mmsg.AddMessage(MSG_KEY_RESULT_WINDOW_STATION_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_WINDOW_STATION_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['openStatus'] = submsg.FindU32(MSG_KEY_RESULT_WINDOW_STATION_INFO_OPEN_STATUS)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_RESULT_WINDOW_STATION_INFO_FLAGS)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_WINDOW_STATION_INFO_NAME)


class ResultWindowInfo:

    def __init__(self):
        self.__dict__['hWnd'] = 0
        self.__dict__['hParent'] = 0
        self.__dict__['owningPid'] = 0
        self.__dict__['owningTid'] = 0
        self.__dict__['x'] = 0
        self.__dict__['y'] = 0
        self.__dict__['width'] = 0
        self.__dict__['height'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['text'] = ''

    def __getattr__(self, name):
        if name == 'hWnd':
            return self.__dict__['hWnd']
        if name == 'hParent':
            return self.__dict__['hParent']
        if name == 'owningPid':
            return self.__dict__['owningPid']
        if name == 'owningTid':
            return self.__dict__['owningTid']
        if name == 'x':
            return self.__dict__['x']
        if name == 'y':
            return self.__dict__['y']
        if name == 'width':
            return self.__dict__['width']
        if name == 'height':
            return self.__dict__['height']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'text':
            return self.__dict__['text']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'hWnd':
            self.__dict__['hWnd'] = value
        elif name == 'hParent':
            self.__dict__['hParent'] = value
        elif name == 'owningPid':
            self.__dict__['owningPid'] = value
        elif name == 'owningTid':
            self.__dict__['owningTid'] = value
        elif name == 'x':
            self.__dict__['x'] = value
        elif name == 'y':
            self.__dict__['y'] = value
        elif name == 'width':
            self.__dict__['width'] = value
        elif name == 'height':
            self.__dict__['height'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'text':
            self.__dict__['text'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_WINDOW_INFO_HWND, self.__dict__['hWnd'])
        submsg.AddU64(MSG_KEY_RESULT_WINDOW_INFO_HPARENT, self.__dict__['hParent'])
        submsg.AddU32(MSG_KEY_RESULT_WINDOW_INFO_OWNING_PROCESS_ID, self.__dict__['owningPid'])
        submsg.AddU32(MSG_KEY_RESULT_WINDOW_INFO_OWNING_THREAD_ID, self.__dict__['owningTid'])
        submsg.AddS32(MSG_KEY_RESULT_WINDOW_INFO_X, self.__dict__['x'])
        submsg.AddS32(MSG_KEY_RESULT_WINDOW_INFO_Y, self.__dict__['y'])
        submsg.AddU32(MSG_KEY_RESULT_WINDOW_INFO_WIDTH, self.__dict__['width'])
        submsg.AddU32(MSG_KEY_RESULT_WINDOW_INFO_HEIGHT, self.__dict__['height'])
        submsg.AddU16(MSG_KEY_RESULT_WINDOW_INFO_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_WINDOW_INFO_TEXT, self.__dict__['text'])
        mmsg.AddMessage(MSG_KEY_RESULT_WINDOW_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_WINDOW_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['hWnd'] = submsg.FindU64(MSG_KEY_RESULT_WINDOW_INFO_HWND)
        self.__dict__['hParent'] = submsg.FindU64(MSG_KEY_RESULT_WINDOW_INFO_HPARENT)
        self.__dict__['owningPid'] = submsg.FindU32(MSG_KEY_RESULT_WINDOW_INFO_OWNING_PROCESS_ID)
        self.__dict__['owningTid'] = submsg.FindU32(MSG_KEY_RESULT_WINDOW_INFO_OWNING_THREAD_ID)
        self.__dict__['x'] = submsg.FindS32(MSG_KEY_RESULT_WINDOW_INFO_X)
        self.__dict__['y'] = submsg.FindS32(MSG_KEY_RESULT_WINDOW_INFO_Y)
        self.__dict__['width'] = submsg.FindU32(MSG_KEY_RESULT_WINDOW_INFO_WIDTH)
        self.__dict__['height'] = submsg.FindU32(MSG_KEY_RESULT_WINDOW_INFO_HEIGHT)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_RESULT_WINDOW_INFO_FLAGS)
        self.__dict__['text'] = submsg.FindString(MSG_KEY_RESULT_WINDOW_INFO_TEXT)