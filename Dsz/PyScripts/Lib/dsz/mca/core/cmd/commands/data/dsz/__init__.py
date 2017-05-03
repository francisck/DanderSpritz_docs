# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Commands(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.Command = list()
        try:
            for x in dsz.cmd.data.Get('Command', dsz.TYPE_OBJECT):
                self.Command.append(Commands.Command(x))

        except:
            pass

    class Command(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.parentId = dsz.cmd.data.ObjectGet(obj, 'parentId', dsz.TYPE_INT)[0]
            except:
                self.parentId = None

            try:
                self.id = dsz.cmd.data.ObjectGet(obj, 'id', dsz.TYPE_INT)[0]
            except:
                self.id = None

            try:
                self.commandAsTyped = dsz.cmd.data.ObjectGet(obj, 'commandAsTyped', dsz.TYPE_STRING)[0]
            except:
                self.commandAsTyped = None

            try:
                self.targetAddress = dsz.cmd.data.ObjectGet(obj, 'targetAddress', dsz.TYPE_STRING)[0]
            except:
                self.targetAddress = None

            try:
                self.BytesSent = dsz.cmd.data.ObjectGet(obj, 'BytesSent', dsz.TYPE_INT)[0]
            except:
                self.BytesSent = None

            try:
                self.BytesReceived = dsz.cmd.data.ObjectGet(obj, 'BytesReceived', dsz.TYPE_INT)[0]
            except:
                self.BytesReceived = None

            try:
                self.status = dsz.cmd.data.ObjectGet(obj, 'status', dsz.TYPE_STRING)[0]
            except:
                self.status = None

            try:
                self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
            except:
                self.name = None

            try:
                self.fullCommand = dsz.cmd.data.ObjectGet(obj, 'fullCommand', dsz.TYPE_STRING)[0]
            except:
                self.fullCommand = None

            self.Thread = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Thread', dsz.TYPE_OBJECT):
                    self.Thread.append(Commands.Command.Thread(x))

            except:
                pass

            return

        class Thread(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.exception = dsz.cmd.data.ObjectGet(obj, 'exception', dsz.TYPE_BOOL)[0]
                except:
                    self.exception = None

                try:
                    self.cmdId = dsz.cmd.data.ObjectGet(obj, 'cmdId', dsz.TYPE_INT)[0]
                except:
                    self.cmdId = None

                try:
                    self.rpcId = dsz.cmd.data.ObjectGet(obj, 'rpcId', dsz.TYPE_INT)[0]
                except:
                    self.rpcId = None

                try:
                    self.id = dsz.cmd.data.ObjectGet(obj, 'id', dsz.TYPE_INT)[0]
                except:
                    self.id = None

                try:
                    self.interface = dsz.cmd.data.ObjectGet(obj, 'interface', dsz.TYPE_STRING)[0]
                except:
                    self.interface = None

                try:
                    self.provider = dsz.cmd.data.ObjectGet(obj, 'provider', dsz.TYPE_STRING)[0]
                except:
                    self.provider = None

                return


dsz.data.RegisterCommand('Commands', Commands)
COMMANDS = Commands
commands = Commands