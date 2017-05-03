# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Drivers(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.driveritem = list()
        try:
            for x in dsz.cmd.data.Get('driveritem', dsz.TYPE_OBJECT):
                self.driveritem.append(Drivers.driveritem(x))

        except:
            pass

    class driveritem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.base = dsz.cmd.data.ObjectGet(obj, 'base', dsz.TYPE_INT)[0]
            except:
                self.base = None

            try:
                self.loadcount = dsz.cmd.data.ObjectGet(obj, 'loadcount', dsz.TYPE_INT)[0]
            except:
                self.loadcount = None

            try:
                self.flags = dsz.cmd.data.ObjectGet(obj, 'flags', dsz.TYPE_INT)[0]
            except:
                self.flags = None

            try:
                self.size = dsz.cmd.data.ObjectGet(obj, 'size', dsz.TYPE_INT)[0]
            except:
                self.size = None

            try:
                self.license = dsz.cmd.data.ObjectGet(obj, 'license', dsz.TYPE_STRING)[0]
            except:
                self.license = None

            try:
                self.dependencies = dsz.cmd.data.ObjectGet(obj, 'dependencies', dsz.TYPE_STRING)[0]
            except:
                self.dependencies = None

            try:
                self.loadparams = dsz.cmd.data.ObjectGet(obj, 'loadparams', dsz.TYPE_STRING)[0]
            except:
                self.loadparams = None

            try:
                self.description = dsz.cmd.data.ObjectGet(obj, 'description', dsz.TYPE_STRING)[0]
            except:
                self.description = None

            try:
                self.usedbymods = dsz.cmd.data.ObjectGet(obj, 'usedbymods', dsz.TYPE_STRING)[0]
            except:
                self.usedbymods = None

            try:
                self.filepath = dsz.cmd.data.ObjectGet(obj, 'filepath', dsz.TYPE_STRING)[0]
            except:
                self.filepath = None

            try:
                self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
            except:
                self.name = None

            try:
                self.author = dsz.cmd.data.ObjectGet(obj, 'author', dsz.TYPE_STRING)[0]
            except:
                self.author = None

            try:
                self.alias = dsz.cmd.data.ObjectGet(obj, 'alias', dsz.TYPE_STRING)[0]
            except:
                self.alias = None

            try:
                self.version = dsz.cmd.data.ObjectGet(obj, 'version', dsz.TYPE_STRING)[0]
            except:
                self.version = None

            try:
                self.Signed = dsz.cmd.data.ObjectGet(obj, 'Signed', dsz.TYPE_STRING)
            except:
                self.Signed = None

            return


dsz.data.RegisterCommand('Drivers', Drivers)
DRIVERS = Drivers
drivers = Drivers