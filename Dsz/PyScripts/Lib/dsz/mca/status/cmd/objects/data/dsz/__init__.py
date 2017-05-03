# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Objects(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.DirectoryItem = list()
        try:
            for x in dsz.cmd.data.Get('DirectoryItem', dsz.TYPE_OBJECT):
                self.DirectoryItem.append(Objects.DirectoryItem(x))

        except:
            pass

    class DirectoryItem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Path = dsz.cmd.data.ObjectGet(obj, 'Path', dsz.TYPE_STRING)[0]
            except:
                self.Path = None

            try:
                self.QueryFailure = dsz.cmd.data.ObjectGet(obj, 'QueryFailure', dsz.TYPE_BOOL)[0]
            except:
                self.QueryFailure = None

            try:
                self.ErrorString = dsz.cmd.data.ObjectGet(obj, 'ErrorString', dsz.TYPE_STRING)
            except:
                self.ErrorString = None

            self.ObjectItem = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'ObjectItem', dsz.TYPE_OBJECT):
                    self.ObjectItem.append(Objects.DirectoryItem.ObjectItem(x))

            except:
                pass

            return

        class ObjectItem(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
                except:
                    self.Name = None

                try:
                    self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                except:
                    self.Type = None

                return


dsz.data.RegisterCommand('Objects', Objects)
OBJECTS = Objects
objects = Objects