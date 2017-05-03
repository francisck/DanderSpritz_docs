# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: bool.py
import dsz
from dsz.menu.input.values.value import Value

class BoolValue(Value):

    def CheckValueRange(value, valueObject):
        if value == 1 or isinstance(value, str) and (value.lower() == '1' or value.lower() == 'yes' or value.lower() == 'on' or value.lower() == 'true') or value == True:
            valueObject.value = True
            return True
        else:
            if value == 0 or isinstance(value, str) and (value.lower() == '0' or value.lower() == 'no' or value.lower() == 'off' or value.lower() == 'false') or value == False or value == None:
                valueObject.value = False
                return True
            return False

    CheckValueRange = staticmethod(CheckValueRange)

    def __init__(self, name, value=None, comment=''):
        if value != None and not isinstance(value, bool):
            raise RuntimeError("Initial value not of type 'bool'")
        Value.__init__(self, name, 'BoolValue', value, comment, BoolValue.CheckValueRange, self)
        return

    def GetRange(self):
        return 'True/False'

    def UpdateValue(self, prename='', onlyOnce=False):
        range = self.GetRange()
        if len(range) > 0:
            rangeStr = ' (%s)' % range
        else:
            rangeStr = ''
        promptStr = "Enter a new value for '%s%s'%s" % (prename, self.name, rangeStr)
        valid = False
        while not valid:
            dsz.script.CheckStop()
            if self.value == None:
                newValue = dsz.ui.GetString(promptStr)
            else:
                newValue = dsz.ui.GetString(promptStr, '%s' % self.value)
            if self.validateFunc == None:
                valid = True
            else:
                valid = self.validateFunc(newValue, self.validateInfo)
                if not valid:
                    dsz.ui.Echo('Invalid value', dsz.ERROR)
            if onlyOnce:
                break

        return valid