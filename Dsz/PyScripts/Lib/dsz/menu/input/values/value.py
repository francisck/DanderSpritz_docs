# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: value.py
import dsz

class Value:

    def __init__(self, name, type, value=None, comment='', validateFunc=None, validateInfo=None):
        self.name = name
        self.type = type
        self.value = value
        self.comment = comment
        self.validateFunc = validateFunc
        self.validateInfo = validateInfo
        if value != None:
            if self.validateFunc != None and not self.validateFunc(self.value, self.validateInfo):
                raise RuntimeError('Initial value (%s) does not pass validation function' % self.value)
        return

    def __str__(self):
        return '%s' % self.value

    def GetRange(self):
        return ''

    def UpdateValue(self, prename='', onlyOnce=False, showRange=True):
        range = self.GetRange()
        if len(range) > 0:
            rangeStr = ' (%s)' % range
        else:
            rangeStr = ''
        promptStr = "Enter a value for '%s%s'%s" % (prename, self.name, rangeStr)
        valid = False
        while not valid:
            dsz.script.CheckStop()
            if self.value == None:
                newValue = dsz.ui.GetString(promptStr)
            else:
                newValue = dsz.ui.GetString(promptStr, self.value)
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

    def Validate(self):
        if self.value == None:
            raise RuntimeError("Value '%s' not set (none)" % self.name)
        if self.validateFunc != None and not self.validateFunc(self.value, self.validateInfo):
            raise RuntimeError('Value (%s) does not pass validation function' % self.value)
        return