# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Traceroute(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = Traceroute.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        self.hopinfo = list()
        try:
            for x in dsz.cmd.data.Get('hopinfo', dsz.TYPE_OBJECT):
                self.hopinfo.append(Traceroute.hopinfo(x))

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
                self.TaskType = Traceroute.TaskingInfo.TaskType(dsz.cmd.data.ObjectGet(obj, 'TaskType', dsz.TYPE_OBJECT)[0])
            except:
                self.TaskType = None

            try:
                self.Target = Traceroute.TaskingInfo.Target(dsz.cmd.data.ObjectGet(obj, 'Target', dsz.TYPE_OBJECT)[0])
            except:
                self.Target = None

            return

        class TaskType(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

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

    class hopinfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.hop = dsz.cmd.data.ObjectGet(obj, 'hop', dsz.TYPE_INT)[0]
            except:
                self.hop = None

            try:
                self.time = dsz.cmd.data.ObjectGet(obj, 'time', dsz.TYPE_INT)[0]
            except:
                self.time = None

            try:
                self.host = dsz.cmd.data.ObjectGet(obj, 'host', dsz.TYPE_STRING)[0]
            except:
                self.host = None

            return


dsz.data.RegisterCommand('Traceroute', Traceroute)
TRACEROUTE = Traceroute
traceroute = Traceroute