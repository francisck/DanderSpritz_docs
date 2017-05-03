# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class LpGetEnv(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.EnvItem = list()
        try:
            for x in dsz.cmd.data.Get('EnvItem', dsz.TYPE_OBJECT):
                self.EnvItem.append(LpGetEnv.EnvItem(x))

        except:
            pass

    class EnvItem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.system = dsz.cmd.data.ObjectGet(obj, 'system', dsz.TYPE_BOOL)[0]
            except:
                self.system = None

            try:
                self.option = dsz.cmd.data.ObjectGet(obj, 'option', dsz.TYPE_STRING)[0]
            except:
                self.option = None

            try:
                self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
            except:
                self.value = None

            return


dsz.data.RegisterCommand('LpGetEnv', LpGetEnv)
LPGETENV = LpGetEnv
lpgetenv = LpGetEnv