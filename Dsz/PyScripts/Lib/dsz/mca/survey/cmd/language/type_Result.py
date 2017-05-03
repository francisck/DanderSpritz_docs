# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class ResultLanguageInfo:

    def __init__(self):
        self.__dict__['languageValue'] = 0
        self.__dict__['language'] = ''

    def __getattr__(self, name):
        if name == 'languageValue':
            return self.__dict__['languageValue']
        if name == 'language':
            return self.__dict__['language']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'languageValue':
            self.__dict__['languageValue'] = value
        elif name == 'language':
            self.__dict__['language'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_LANG_INFO_LANGUAGE_VALUE, self.__dict__['languageValue'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_LANG_INFO_LANGUAGE, self.__dict__['language'])
        mmsg.AddMessage(MSG_KEY_RESULT_LANG_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_LANG_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['languageValue'] = submsg.FindU32(MSG_KEY_RESULT_LANG_INFO_LANGUAGE_VALUE)
        self.__dict__['language'] = submsg.FindString(MSG_KEY_RESULT_LANG_INFO_LANGUAGE)


class Result:

    def __init__(self):
        self.__dict__['locale'] = ResultLanguageInfo()
        self.__dict__['ui'] = ResultLanguageInfo()
        self.__dict__['installed'] = ResultLanguageInfo()
        self.__dict__['osFile'] = ''
        self.__dict__['fileCode'] = 0
        self.__dict__['numAvailLanguages'] = 0
        self.__dict__['numReturned'] = 0

    def __getattr__(self, name):
        if name == 'locale':
            return self.__dict__['locale']
        if name == 'ui':
            return self.__dict__['ui']
        if name == 'installed':
            return self.__dict__['installed']
        if name == 'osFile':
            return self.__dict__['osFile']
        if name == 'fileCode':
            return self.__dict__['fileCode']
        if name == 'numAvailLanguages':
            return self.__dict__['numAvailLanguages']
        if name == 'numReturned':
            return self.__dict__['numReturned']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'locale':
            self.__dict__['locale'] = value
        elif name == 'ui':
            self.__dict__['ui'] = value
        elif name == 'installed':
            self.__dict__['installed'] = value
        elif name == 'osFile':
            self.__dict__['osFile'] = value
        elif name == 'fileCode':
            self.__dict__['fileCode'] = value
        elif name == 'numAvailLanguages':
            self.__dict__['numAvailLanguages'] = value
        elif name == 'numReturned':
            self.__dict__['numReturned'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg2 = MarshalMessage()
        self.__dict__['locale'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_RESULT_LANGAUGE_LOCALE, submsg2)
        submsg2 = MarshalMessage()
        self.__dict__['ui'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_RESULT_LANGAUGE_UI, submsg2)
        submsg2 = MarshalMessage()
        self.__dict__['installed'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_RESULT_LANGAUGE_INSTALLED, submsg2)
        submsg.AddStringUtf8(MSG_KEY_RESULT_LANGAUGE_OS_FILE, self.__dict__['osFile'])
        submsg.AddU32(MSG_KEY_RESULT_LANGAUGE_FILE_CODE, self.__dict__['fileCode'])
        submsg.AddU32(MSG_KEY_RESULT_LANGAUGE_NUM_AVAILABLE_LANGUAGES, self.__dict__['numAvailLanguages'])
        submsg.AddU32(MSG_KEY_RESULT_LANGAUGE_NUM_RETURNED, self.__dict__['numReturned'])
        mmsg.AddMessage(MSG_KEY_RESULT_LANGAUGE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_LANGAUGE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        submsg2 = submsg.FindMessage(MSG_KEY_RESULT_LANGAUGE_LOCALE)
        self.__dict__['locale'].Demarshal(submsg2)
        submsg2 = submsg.FindMessage(MSG_KEY_RESULT_LANGAUGE_UI)
        self.__dict__['ui'].Demarshal(submsg2)
        submsg2 = submsg.FindMessage(MSG_KEY_RESULT_LANGAUGE_INSTALLED)
        self.__dict__['installed'].Demarshal(submsg2)
        self.__dict__['osFile'] = submsg.FindString(MSG_KEY_RESULT_LANGAUGE_OS_FILE)
        self.__dict__['fileCode'] = submsg.FindU32(MSG_KEY_RESULT_LANGAUGE_FILE_CODE)
        self.__dict__['numAvailLanguages'] = submsg.FindU32(MSG_KEY_RESULT_LANGAUGE_NUM_AVAILABLE_LANGUAGES)
        self.__dict__['numReturned'] = submsg.FindU32(MSG_KEY_RESULT_LANGAUGE_NUM_RETURNED)