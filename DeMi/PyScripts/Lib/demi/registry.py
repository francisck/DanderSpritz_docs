# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: registry.py
import demi.windows
import dsz.env
import re
Kisu_IdRange = 3489660928L
Longterm_IdRange = 2147483648L

class ModuleId:

    def __init__(self, id, fileName, moduleName):
        Max = 268435456
        if id >= Max:
            raise StandardError('Base Id (0x%08x) cannot be equal to or greater than maximum (0x%08x)' % (id, Max))
        self.Id = id + Kisu_IdRange
        self.Name = fileName
        self.ModuleName = moduleName


PC = ModuleId(256, 'PC', 'PC')
DMGZ = ModuleId(257, 'ntfltmgr', 'DMGZ')
FLAV = ModuleId(258, 'ntevt', 'FLAV')