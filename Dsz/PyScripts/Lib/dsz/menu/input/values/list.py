# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: list.py
import dsz

class ValueList(list):

    def __init__(self):
        self.values = list()

    def __getitem__(self, index):
        for item in self.values:
            if item.name.lower() == index.lower():
                return item

        return None

    def __iter__(self):
        return self.values.__iter__()

    def __len__(self):
        return len(self.values)

    def append(self, value):
        self.values.append(value)

    def Display(self, type, prename=''):
        if len(type) > 0:
            dsz.ui.Echo('%s Information:' % type)
        for value in self.values:
            dsz.script.CheckStop()
            if value.type == 'list':
                newprename = '%s%s.' % (prename, value.name)
                value.value.Display('', newprename)
            else:
                name = '%s%s (%s)' % (prename, value.name, value.type)
                if value.value == None:
                    dsz.ui.Echo('%45s : %s' % (name, value.value), dsz.ERROR)
                else:
                    dsz.ui.Echo('%45s : %s' % (name, value.value))

        if len(type) > 0:
            dsz.ui.Echo('')
        return

    def Update(self, type, prename='', givenField=''):
        itemUpdated = False
        while not itemUpdated:
            dsz.script.CheckStop()
            if len(type) > 0:
                self.Display(type)
            if len(givenField) == 0:
                field = dsz.ui.GetString("Enter the field to change (type 'none' to exit)").lower()
                if field == 'none':
                    break
            else:
                field = givenField
            key, sep, subkey = field.partition('.')
            itemFound = False
            for item in self.values:
                if item.name.lower() == key.lower():
                    if len(subkey) > 0:
                        if item.type == 'list':
                            itemUpdated = item.value.Update('', '%s%s.' % (prename, key), subkey)
                            itemFound = True
                    else:
                        itemFound = True
                        itemUpdated = item.UpdateValue(prename)
                    break

            if not itemFound:
                dsz.ui.Echo("Field '%s' not found" % field, dsz.ERROR)
                if len(givenField) == 0:
                    continue
                else:
                    return False

        return itemUpdated

    def UpdateAll(self, promptForCorrect=True):
        while True:
            dsz.script.CheckStop()
            for value in self.values:
                value.UpdateValue()

            if not promptForCorrect:
                break
            if self.Validate(''):
                if dsz.ui.Prompt('Correct values?', True):
                    break

    def Validate(self, type, prename=''):
        allPassed = True
        if len(type) > 0:
            dsz.ui.Echo('%s Validation:' % type)
        for value in self.values:
            dsz.script.CheckStop()
            if value.type == 'list':
                newprename = '%s%s.' % (prename, value.name)
                if not value.value.Validate('', newprename):
                    allPassed = False
            else:
                name = '%s%s' % (prename, value.name)
                try:
                    value.Validate()
                    dsz.ui.Echo('%45s : %s (PASSED)' % (name, value.value), dsz.GOOD)
                except:
                    dsz.ui.Echo('%45s : %s (FAILED)' % (name, value.value), dsz.ERROR)
                    allPassed = False

        if len(type) > 0:
            dsz.ui.Echo('')
        return allPassed