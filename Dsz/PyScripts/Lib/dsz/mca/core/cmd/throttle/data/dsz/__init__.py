# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Throttle(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.ThrottleItem = list()
        try:
            for x in dsz.cmd.data.Get('ThrottleItem', dsz.TYPE_OBJECT):
                self.ThrottleItem.append(Throttle.ThrottleItem(x))

        except:
            pass

    class ThrottleItem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.enabled = dsz.cmd.data.ObjectGet(obj, 'enabled', dsz.TYPE_BOOL)[0]
            except:
                self.enabled = None

            try:
                self.bytesPerSecond = dsz.cmd.data.ObjectGet(obj, 'bytesPerSecond', dsz.TYPE_INT)[0]
            except:
                self.bytesPerSecond = None

            try:
                self.address = dsz.cmd.data.ObjectGet(obj, 'address', dsz.TYPE_STRING)[0]
            except:
                self.address = None

            return


dsz.data.RegisterCommand('Throttle', Throttle)
THROTTLE = Throttle
throttle = Throttle