# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Shares(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.MappedResource = Shares.MappedResource(dsz.cmd.data.Get('MappedResource', dsz.TYPE_OBJECT)[0])
        except:
            self.MappedResource = None

        self.Share = list()
        try:
            for x in dsz.cmd.data.Get('Share', dsz.TYPE_OBJECT):
                self.Share.append(Shares.Share(x))

        except:
            pass

        self.Resouce = list()
        try:
            for x in dsz.cmd.data.Get('Resouce', dsz.TYPE_OBJECT):
                self.Resouce.append(Shares.Resouce(x))

        except:
            pass

        return

    class MappedResource(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.RemotePath = dsz.cmd.data.ObjectGet(obj, 'RemotePath', dsz.TYPE_STRING)[0]
            except:
                self.RemotePath = None

            try:
                self.LocalPath = dsz.cmd.data.ObjectGet(obj, 'LocalPath', dsz.TYPE_STRING)[0]
            except:
                self.LocalPath = None

            return

    class Share(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Password = dsz.cmd.data.ObjectGet(obj, 'Password', dsz.TYPE_STRING)[0]
            except:
                self.Password = None

            try:
                self.LocalName = dsz.cmd.data.ObjectGet(obj, 'LocalName', dsz.TYPE_STRING)[0]
            except:
                self.LocalName = None

            try:
                self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
            except:
                self.Type = None

            try:
                self.DomainName = dsz.cmd.data.ObjectGet(obj, 'DomainName', dsz.TYPE_STRING)[0]
            except:
                self.DomainName = None

            try:
                self.RemoteName = dsz.cmd.data.ObjectGet(obj, 'RemoteName', dsz.TYPE_STRING)[0]
            except:
                self.RemoteName = None

            try:
                self.UserName = dsz.cmd.data.ObjectGet(obj, 'UserName', dsz.TYPE_STRING)[0]
            except:
                self.UserName = None

            try:
                self.Status = dsz.cmd.data.ObjectGet(obj, 'Status', dsz.TYPE_STRING)[0]
            except:
                self.Status = None

            try:
                self.ReferenceCount = dsz.cmd.data.ObjectGet(obj, 'ReferenceCount', dsz.TYPE_INT)[0]
            except:
                self.ReferenceCount = None

            try:
                self.UseCount = dsz.cmd.data.ObjectGet(obj, 'UseCount', dsz.TYPE_INT)[0]
            except:
                self.UseCount = None

            return

    class Resouce(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Admin = dsz.cmd.data.ObjectGet(obj, 'Admin', dsz.TYPE_BOOL)[0]
            except:
                self.Admin = None

            try:
                self.Description = dsz.cmd.data.ObjectGet(obj, 'Description', dsz.TYPE_STRING)[0]
            except:
                self.Description = None

            try:
                self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
            except:
                self.Name = None

            try:
                self.Path = dsz.cmd.data.ObjectGet(obj, 'Path', dsz.TYPE_STRING)
            except:
                self.Path = None

            try:
                self.Caption = dsz.cmd.data.ObjectGet(obj, 'Caption', dsz.TYPE_STRING)[0]
            except:
                self.Caption = None

            try:
                self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
            except:
                self.Type = None

            return


dsz.data.RegisterCommand('Shares', Shares)
SHARES = Shares
shares = Shares