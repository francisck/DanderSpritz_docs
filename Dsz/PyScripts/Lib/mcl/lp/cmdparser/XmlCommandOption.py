# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: XmlCommandOption.py
from XmlCommandArgument import XmlCommandArgument

class XmlCommandOption(XmlCommandArgument):

    def __init__(self):
        XmlCommandArgument.__init__(self)
        self.m_found = False
        self.m_setData = {}
        self.m_arguments = []
        self.m_requiredList = []
        self.m_rejectedList = []
        self.m_minArgs = 0
        self.m_maxArgs = 0
        self.SetOptional(True)

    def AddArgument(self, arg):
        self.m_arguments.append(arg)
        if arg.IsOptional() == False:
            self.m_minArgs = self.m_minArgs + 1
        self.m_maxArgs = self.m_maxArgs + 1

    def AddRejectedOption(self, option):
        if len(option) > 0:
            self.m_rejectedList.append(option)

    def AddRequiredOption(self, option):
        if len(option) > 0:
            self.m_requiredList.append(option)

    def AddSetData(self, dataName, value):
        self.m_setData[dataName] = value

    def GetArgumentDataName(self, argIndex):
        return self.m_arguments[argIndex].GetDataName()

    def GetArgumentsList(self):
        return self.m_arguments

    def GetDataName(self):
        return None

    def GetMaximumNumArguments(self):
        return self.m_maxArgs

    def GetMinimumNumArguments(self):
        return self.m_minArgs

    def GetRejectedOptions(self):
        return list(self.m_rejectedList)

    def GetRequiredOptions(self):
        return list(self.m_requiredList)

    def GetSetDataMap(self):
        return self.m_setData

    def IsArgumentsEmpty(self):
        if len(self.m_arguments) == 0:
            return True
        else:
            return False

    def IsSetDataEmpty(self):
        if len(self.m_setData) == 0:
            return True
        else:
            return False

    def SetFound(self):
        self.m_found = True

    def SetDataName(self, newName):
        pass

    def WasFound(self):
        return self.m_found