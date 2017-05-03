# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Delegator.py


class Delegator:

    def __init__(self, delegate=None):
        self.delegate = delegate
        self.__cache = {}

    def __getattr__(self, name):
        attr = getattr(self.delegate, name)
        setattr(self, name, attr)
        self.__cache[name] = attr
        return attr

    def resetcache(self):
        for key in self.__cache.keys():
            try:
                delattr(self, key)
            except AttributeError:
                pass

        self.__cache.clear()

    def cachereport(self):
        keys = self.__cache.keys()
        keys.sort()
        print keys

    def setdelegate(self, delegate):
        self.resetcache()
        self.delegate = delegate

    def getdelegate(self):
        return self.delegate