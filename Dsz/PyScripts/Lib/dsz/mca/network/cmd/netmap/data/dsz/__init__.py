# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Netmap(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.NetmapEntryItem = list()
        try:
            for x in dsz.cmd.data.Get('NetmapEntryItem', dsz.TYPE_OBJECT):
                self.NetmapEntryItem.append(Netmap.NetmapEntryItem(x))

        except:
            pass

    class NetmapEntryItem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.level = dsz.cmd.data.ObjectGet(obj, 'level', dsz.TYPE_INT)[0]
            except:
                self.level = None

            try:
                self.LocalName = dsz.cmd.data.ObjectGet(obj, 'LocalName', dsz.TYPE_STRING)[0]
            except:
                self.LocalName = None

            try:
                self.RemoteName = dsz.cmd.data.ObjectGet(obj, 'RemoteName', dsz.TYPE_STRING)[0]
            except:
                self.RemoteName = None

            try:
                self.ParentName = dsz.cmd.data.ObjectGet(obj, 'ParentName', dsz.TYPE_STRING)[0]
            except:
                self.ParentName = None

            try:
                self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
            except:
                self.Type = None

            try:
                self.Provider = dsz.cmd.data.ObjectGet(obj, 'Provider', dsz.TYPE_STRING)[0]
            except:
                self.Provider = None

            try:
                self.Comment = dsz.cmd.data.ObjectGet(obj, 'Comment', dsz.TYPE_STRING)[0]
            except:
                self.Comment = None

            try:
                self.Ip = dsz.cmd.data.ObjectGet(obj, 'Ip', dsz.TYPE_STRING)[0]
            except:
                self.Ip = None

            try:
                self.Time = dsz.cmd.data.ObjectGet(obj, 'Time', dsz.TYPE_STRING)[0]
            except:
                self.Time = None

            try:
                self.TimezoneOffset = dsz.cmd.data.ObjectGet(obj, 'TimezoneOffset', dsz.TYPE_STRING)[0]
            except:
                self.TimezoneOffset = None

            try:
                self.OsPlatform = dsz.cmd.data.ObjectGet(obj, 'OsPlatform', dsz.TYPE_STRING)[0]
            except:
                self.OsPlatform = None

            try:
                self.OsVersionMajor = dsz.cmd.data.ObjectGet(obj, 'OsVersionMajor', dsz.TYPE_INT)[0]
            except:
                self.OsVersionMajor = None

            try:
                self.OsVersionMinor = dsz.cmd.data.ObjectGet(obj, 'OsVersionMinor', dsz.TYPE_INT)[0]
            except:
                self.OsVersionMinor = None

            try:
                self.Software = Netmap.NetmapEntryItem.Software(dsz.cmd.data.ObjectGet(obj, 'Software', dsz.TYPE_OBJECT)[0])
            except:
                self.Software = None

            return

        class Software(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
                except:
                    self.Name = None

                try:
                    self.Description = dsz.cmd.data.ObjectGet(obj, 'Description', dsz.TYPE_STRING)[0]
                except:
                    self.Description = None

                return


dsz.data.RegisterCommand('Netmap', Netmap)
NETMAP = Netmap
netmap = Netmap