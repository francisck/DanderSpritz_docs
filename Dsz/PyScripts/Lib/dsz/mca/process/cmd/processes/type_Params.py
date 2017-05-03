# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import mcl.object.MclTime
import array
NUM_IGNORE_NAMES = 9

class Params:

    def __init__(self):
        self.__dict__['minimal'] = True
        self.__dict__['monitor'] = False
        self.__dict__['delay'] = mcl.object.MclTime.MclTime()
        self.__dict__['ignoreList'] = list()
        i = 0
        while i < NUM_IGNORE_NAMES:
            self.__dict__['ignoreList'].append('')
            i = i + 1

        self.__dict__['target'] = ''

    def __getattr__(self, name):
        if name == 'minimal':
            return self.__dict__['minimal']
        if name == 'monitor':
            return self.__dict__['monitor']
        if name == 'delay':
            return self.__dict__['delay']
        if name == 'ignoreList':
            return self.__dict__['ignoreList']
        if name == 'target':
            return self.__dict__['target']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'minimal':
            self.__dict__['minimal'] = value
        elif name == 'monitor':
            self.__dict__['monitor'] = value
        elif name == 'delay':
            self.__dict__['delay'] = value
        elif name == 'ignoreList':
            self.__dict__['ignoreList'] = value
        elif name == 'target':
            self.__dict__['target'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_PARAMS_MINIMAL, self.__dict__['minimal'])
        submsg.AddBool(MSG_KEY_PARAMS_MONITOR, self.__dict__['monitor'])
        submsg.AddTime(MSG_KEY_PARAMS_DELAY, self.__dict__['delay'])
        i = 0
        while i < NUM_IGNORE_NAMES:
            submsg.AddStringUtf8(MSG_KEY_PARAMS_IGNORE_LIST, self.__dict__['ignoreList'][i])
            i = i + 1

        submsg.AddStringUtf8(MSG_KEY_PARAMS_TARGET, self.__dict__['target'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['minimal'] = submsg.FindBool(MSG_KEY_PARAMS_MINIMAL)
        except:
            pass

        try:
            self.__dict__['monitor'] = submsg.FindBool(MSG_KEY_PARAMS_MONITOR)
        except:
            pass

        try:
            self.__dict__['delay'] = submsg.FindTime(MSG_KEY_PARAMS_DELAY)
        except:
            pass

        try:
            i = 0
            while i < NUM_IGNORE_NAMES:
                self.__dict__['ignoreList'][i] = submsg.FindString(MSG_KEY_PARAMS_IGNORE_LIST)
                i = i + 1

        except:
            pass

        try:
            self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_TARGET)
        except:
            pass