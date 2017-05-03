# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: taskid.py
import dsz
from dsz.menu.input.values.value import Value
import uuid
import re
uuidNull = uuid.UUID(bytes='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

class TaskIdValue(Value):

    def CheckUuid(value, valueObject):
        try:
            tempUuid = None
            if isinstance(value, uuid.UUID):
                tempUuid = value
            else:
                m0 = re.match('([0-9a-fA-F]{8})-([0-9a-fA-F]{4})-([0-9a-fA-F]{4})-([0-9a-fA-F]{16})$', value)
                m1 = re.match('\\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\\}$', value)
                m2 = re.match('[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$', value)
                m3 = re.match('urn:uuid:[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$', value)
                m4 = re.match('[0-9a-fA-F]{32}$', value)
                m5 = re.match('0$', value)
                if m0 != None:
                    tempUuid = uuid.UUID('%s%s%s%s' % (m0.group(1), m0.group(2), m0.group(3), m0.group(4)))
                elif m1 != None:
                    tempUuid = uuid.UUID(value)
                elif m2 != None:
                    tempUuid = uuid.UUID('{%s}' % value)
                elif m3 != None:
                    tempUuid = uuid.UUID(value)
                elif m4 != None:
                    tempUuid = uuid.UUID(value)
                elif m5 != None:
                    tempUuid = uuid.UUID(bytes='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                else:
                    return False
            if tempUuid == None:
                return False
            if not valueObject.allowInvalid and tempUuid == uuidNull:
                return False
            valueObject.uuidValue = tempUuid
            return True
        except:
            return False

        return

    CheckUuid = staticmethod(CheckUuid)

    def __init__(self, name, value=None, comment='', allowInvalid=False, generate=False):
        if value != None and not isinstance(value, str):
            raise RuntimeError("Initial value not of type 'str'")
        if value != None and generate == True:
            raise RuntimeError('Cannot provide an initial value and set generate to True')
        if value == None and generate == True:
            value = uuid.uuid4()
        self.allowInvalid = allowInvalid
        self.uuidValue = None
        Value.__init__(self, name, 'TaskIdValue', value, comment, TaskIdValue.CheckUuid, self)
        return

    def __str__(self):
        if self.uuidValue == None:
            return '%s' % self.value
        else:
            return '%08x-%04x-%04x-%02x%02x%012x' % (self.uuidValue.time_low, self.uuidValue.time_mid, self.uuidValue.time_hi_version, self.uuidValue.clock_seq_hi_variant, self.uuidValue.clock_seq_low, self.uuidValue.node)
            return

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
            if self.uuidValue == None:
                newValue = dsz.ui.GetString(promptStr)
            else:
                newValue = dsz.ui.GetString(promptStr, str(self))
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

    def AsBytes(self):
        output = []
        i = 0
        str = self.uuidValue.hex
        while i < 16:
            i += 1
            b = str[0:2]
            str = str[2:]
            output.append(int('0x%s' % b, 16))

        return output