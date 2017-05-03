# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Packages(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = Packages.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        self.package = list()
        try:
            for x in dsz.cmd.data.Get('package', dsz.TYPE_OBJECT):
                self.package.append(Packages.package(x))

        except:
            pass

        return

    class TaskingInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.recursive = dsz.cmd.data.ObjectGet(obj, 'recursive', dsz.TYPE_BOOL)[0]
            except:
                self.recursive = None

            try:
                self.Target = Packages.TaskingInfo.Target(dsz.cmd.data.ObjectGet(obj, 'Target', dsz.TYPE_OBJECT)[0])
            except:
                self.Target = None

            return

        class Target(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.local = dsz.cmd.data.ObjectGet(obj, 'local', dsz.TYPE_BOOL)[0]
                except:
                    self.local = None

                try:
                    self.location = dsz.cmd.data.ObjectGet(obj, 'location', dsz.TYPE_STRING)[0]
                except:
                    self.location = None

                return

    class package(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.size = dsz.cmd.data.ObjectGet(obj, 'size', dsz.TYPE_INT)[0]
            except:
                self.size = None

            try:
                self.installDate = dsz.cmd.data.ObjectGet(obj, 'installDate', dsz.TYPE_STRING)[0]
            except:
                self.installDate = None

            try:
                self.installTime = dsz.cmd.data.ObjectGet(obj, 'installTime', dsz.TYPE_STRING)[0]
            except:
                self.installTime = None

            try:
                self.Description = dsz.cmd.data.ObjectGet(obj, 'Description', dsz.TYPE_STRING)[0]
            except:
                self.Description = None

            try:
                self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
            except:
                self.name = None

            try:
                self.version = dsz.cmd.data.ObjectGet(obj, 'version', dsz.TYPE_STRING)[0]
            except:
                self.version = None

            try:
                self.revision = dsz.cmd.data.ObjectGet(obj, 'revision', dsz.TYPE_STRING)[0]
            except:
                self.revision = None

            return


dsz.data.RegisterCommand('Packages', Packages)
PACKAGES = Packages
packages = Packages