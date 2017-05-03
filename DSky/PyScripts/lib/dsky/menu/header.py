# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: header.py
import dsky
import dsz
from dsky.menu.item import Item

class SectionHeader(Item):

    def __init__(self, text):
        self.text = text

    def IsOption(self):
        return False

    def Display(self, index):
        dsz.ui.Echo('')
        dsz.ui.Echo('%s' % self.text)


class MenuHeader(object):

    def __init__(self, func, params=None):
        self.func = func
        self.params = params

    def Display(self):
        if self.params == None:
            self.func()
        else:
            self.func(self.params)
        return