# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Handles(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.Process = list()
        try:
            for x in dsz.cmd.data.Get('Process', dsz.TYPE_OBJECT):
                self.Process.append(Handles.Process(x))

        except:
            pass

        try:
            self.DuplicatedHandle = Handles.DuplicatedHandle(dsz.cmd.data.Get('DuplicatedHandle', dsz.TYPE_OBJECT)[0])
        except:
            self.DuplicatedHandle = None

        return

    class Process(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
            except:
                self.Id = None

            self.Handle = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Handle', dsz.TYPE_OBJECT):
                    self.Handle.append(Handles.Process.Handle(x))

            except:
                pass

            return

        class Handle(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
                except:
                    self.Id = None

                try:
                    self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                except:
                    self.Type = None

                try:
                    self.Metadata = dsz.cmd.data.ObjectGet(obj, 'Metadata', dsz.TYPE_STRING)[0]
                except:
                    self.Metadata = None

                return

    class DuplicatedHandle(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.OrigHandle = dsz.cmd.data.ObjectGet(obj, 'OrigHandle', dsz.TYPE_INT)[0]
            except:
                self.OrigHandle = None

            try:
                self.OrigProcessId = dsz.cmd.data.ObjectGet(obj, 'OrigProcessId', dsz.TYPE_INT)[0]
            except:
                self.OrigProcessId = None

            try:
                self.NewHandle = dsz.cmd.data.ObjectGet(obj, 'NewHandle', dsz.TYPE_INT)[0]
            except:
                self.NewHandle = None

            try:
                self.NewProcessId = dsz.cmd.data.ObjectGet(obj, 'NewProcessId', dsz.TYPE_INT)[0]
            except:
                self.NewProcessId = None

            return


dsz.data.RegisterCommand('Handles', Handles)
HANDLES = Handles
handles = Handles