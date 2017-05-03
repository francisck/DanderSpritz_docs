# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Ping(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = Ping.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        try:
            self.Response = Ping.Response(dsz.cmd.data.Get('Response', dsz.TYPE_OBJECT)[0])
        except:
            self.Response = None

        return

    class TaskingInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.recursive = dsz.cmd.data.ObjectGet(obj, 'recursive', dsz.TYPE_BOOL)[0]
            except:
                self.recursive = None

            try:
                self.Target = Ping.TaskingInfo.Target(dsz.cmd.data.ObjectGet(obj, 'Target', dsz.TYPE_OBJECT)[0])
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

    class Response(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.elapsed = dsz.cmd.data.ObjectGet(obj, 'elapsed', dsz.TYPE_INT)[0]
            except:
                self.elapsed = None

            try:
                self.length = dsz.cmd.data.ObjectGet(obj, 'length', dsz.TYPE_INT)[0]
            except:
                self.length = None

            try:
                self.ttl = dsz.cmd.data.ObjectGet(obj, 'ttl', dsz.TYPE_INT)[0]
            except:
                self.ttl = None

            try:
                self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_STRING)[0]
            except:
                self.type = None

            try:
                self.Data = Ping.Response.Data(dsz.cmd.data.ObjectGet(obj, 'Data', dsz.TYPE_OBJECT)[0])
            except:
                self.Data = None

            try:
                self.Ip = Ping.Response.Ip(dsz.cmd.data.ObjectGet(obj, 'Ip', dsz.TYPE_OBJECT)[0])
            except:
                self.Ip = None

            try:
                self.FromAddr = Ping.Response.FromAddr(dsz.cmd.data.ObjectGet(obj, 'FromAddr', dsz.TYPE_OBJECT)[0])
            except:
                self.FromAddr = None

            return

        class Data(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.data = dsz.cmd.data.ObjectGet(obj, 'data', dsz.TYPE_STRING)[0]
                except:
                    self.data = None

                return

        class Ip(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.protocol = dsz.cmd.data.ObjectGet(obj, 'protocol', dsz.TYPE_INT)[0]
                except:
                    self.protocol = None

                try:
                    self.headerLength = dsz.cmd.data.ObjectGet(obj, 'headerLength', dsz.TYPE_INT)[0]
                except:
                    self.headerLength = None

                try:
                    self.ttl = dsz.cmd.data.ObjectGet(obj, 'ttl', dsz.TYPE_INT)[0]
                except:
                    self.ttl = None

                try:
                    self.version = dsz.cmd.data.ObjectGet(obj, 'version', dsz.TYPE_INT)[0]
                except:
                    self.version = None

                try:
                    self.destination = dsz.cmd.data.ObjectGet(obj, 'destination', dsz.TYPE_STRING)[0]
                except:
                    self.destination = None

                try:
                    self.source = dsz.cmd.data.ObjectGet(obj, 'source', dsz.TYPE_STRING)[0]
                except:
                    self.source = None

                try:
                    self.icmp = Ping.Response.Ip.icmp(dsz.cmd.data.ObjectGet(obj, 'icmp', dsz.TYPE_OBJECT)[0])
                except:
                    self.icmp = None

                return

            class icmp(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.code = dsz.cmd.data.ObjectGet(obj, 'code', dsz.TYPE_INT)[0]
                    except:
                        self.code = None

                    try:
                        self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_INT)[0]
                    except:
                        self.type = None

                    return

        class FromAddr(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Addr = dsz.cmd.data.ObjectGet(obj, 'Addr', dsz.TYPE_STRING)[0]
                except:
                    self.Addr = None

                try:
                    self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                except:
                    self.Type = None

                return


dsz.data.RegisterCommand('Ping', Ping)
PING = Ping
ping = Ping