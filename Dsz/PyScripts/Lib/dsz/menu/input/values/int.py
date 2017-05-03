# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: int.py
import dsz
from dsz.menu.input.values.value import Value

class IntValue(Value):

    def CheckValueRange(value, valueObject):
        if valueObject.minValue != None:
            if value < valueObject.minValue:
                return False
        if valueObject.maxValue != None:
            if value > valueObject.maxValue:
                return False
        return True

    CheckValueRange = staticmethod(CheckValueRange)

    def __init__(self, name, value=None, comment='', minValue=None, maxValue=None):
        if value != None and not isinstance(value, int) and not isinstance(value, long):
            raise RuntimeError("Initial value not of type 'int' or 'long'")
        self.minValue = minValue
        self.maxValue = maxValue
        Value.__init__(self, name, 'IntValue', value, comment, IntValue.CheckValueRange, self)
        return

    def GetRange(self):
        rangeStr = ''
        if self.minValue != None:
            rangeStr += 'minValue=%d' % self.minValue
        if self.maxValue != None:
            if len(rangeStr) > 0:
                rangeStr += ' '
            rangeStr += 'maxValue=%d' % self.maxValue
        return rangeStr

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
                newValue = dsz.ui.GetInt(promptStr)
            else:
                newValue = dsz.ui.GetInt(promptStr, '%s' % self.value)
            if self.validateFunc == None:
                valid = True
            else:
                valid = self.validateFunc(newValue, self.validateInfo)
                if valid:
                    self.value = newValue
                else:
                    dsz.ui.Echo('Invalid value', dsz.ERROR)
            if onlyOnce:
                break

        return valid