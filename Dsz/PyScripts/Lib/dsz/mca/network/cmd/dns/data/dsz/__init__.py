# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Dns(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.CacheEntry = list()
        try:
            for x in dsz.cmd.data.Get('CacheEntry', dsz.TYPE_OBJECT):
                self.CacheEntry.append(Dns.CacheEntry(x))

        except:
            pass

        self.DnsAnswer = list()
        try:
            for x in dsz.cmd.data.Get('DnsAnswer', dsz.TYPE_OBJECT):
                self.DnsAnswer.append(Dns.DnsAnswer(x))

        except:
            pass

    class CacheEntry(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
            except:
                self.Name = None

            try:
                self.EntryName = dsz.cmd.data.ObjectGet(obj, 'EntryName', dsz.TYPE_STRING)[0]
            except:
                self.EntryName = None

            try:
                self.DataType = dsz.cmd.data.ObjectGet(obj, 'DataType', dsz.TYPE_INT)[0]
            except:
                self.DataType = None

            try:
                self.DataTypeStr = dsz.cmd.data.ObjectGet(obj, 'DataTypeStr', dsz.TYPE_STRING)[0]
            except:
                self.DataTypeStr = None

            try:
                self.Data = dsz.cmd.data.ObjectGet(obj, 'Data', dsz.TYPE_STRING)[0]
            except:
                self.Data = None

            try:
                self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
            except:
                self.Name = None

            return

    class DnsAnswer(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Ttl = dsz.cmd.data.ObjectGet(obj, 'Ttl', dsz.TYPE_INT)[0]
            except:
                self.Ttl = None

            try:
                self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
            except:
                self.Type = None

            try:
                self.Query = dsz.cmd.data.ObjectGet(obj, 'Query', dsz.TYPE_STRING)[0]
            except:
                self.Query = None

            try:
                self.DataType = dsz.cmd.data.ObjectGet(obj, 'DataType', dsz.TYPE_STRING)[0]
            except:
                self.DataType = None

            try:
                self.Data = dsz.cmd.data.ObjectGet(obj, 'Data', dsz.TYPE_STRING)[0]
            except:
                self.Data = None

            return


dsz.data.RegisterCommand('Dns', Dns)
DNS = Dns
dns = Dns