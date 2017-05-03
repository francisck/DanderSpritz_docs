# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class ProcessInfo(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.ProcessInfo = ProcessInfo.ProcessInfo(dsz.cmd.data.Get('ProcessInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.ProcessInfo = None

        return

    class ProcessInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
            except:
                self.Id = None

            try:
                self.Groups = ProcessInfo.ProcessInfo.Groups(dsz.cmd.data.ObjectGet(obj, 'Groups', dsz.TYPE_OBJECT)[0])
            except:
                self.Groups = None

            try:
                self.Privileges = ProcessInfo.ProcessInfo.Privileges(dsz.cmd.data.ObjectGet(obj, 'Privileges', dsz.TYPE_OBJECT)[0])
            except:
                self.Privileges = None

            try:
                self.BasicInfo = ProcessInfo.ProcessInfo.BasicInfo(dsz.cmd.data.ObjectGet(obj, 'BasicInfo', dsz.TYPE_OBJECT)[0])
            except:
                self.BasicInfo = None

            try:
                self.Modules = ProcessInfo.ProcessInfo.Modules(dsz.cmd.data.ObjectGet(obj, 'Modules', dsz.TYPE_OBJECT)[0])
            except:
                self.Modules = None

            return

        class Groups(dsz.data.DataBean):

            def __init__(self, obj):
                self.Group = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Group', dsz.TYPE_OBJECT):
                        self.Group.append(ProcessInfo.ProcessInfo.Groups.Group(x))

                except:
                    pass

            class Group(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                    except:
                        self.Type = None

                    try:
                        self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
                    except:
                        self.Name = None

                    try:
                        self.Attributes = ProcessInfo.ProcessInfo.Groups.Group.Attributes(dsz.cmd.data.ObjectGet(obj, 'Attributes', dsz.TYPE_OBJECT)[0])
                    except:
                        self.Attributes = None

                    return

                class Attributes(dsz.data.DataBean):

                    def __init__(self, obj):
                        try:
                            self.GroupUseDeny = dsz.cmd.data.ObjectGet(obj, 'GroupUseDeny', dsz.TYPE_BOOL)[0]
                        except:
                            self.GroupUseDeny = None

                        try:
                            self.GroupMandatory = dsz.cmd.data.ObjectGet(obj, 'GroupMandatory', dsz.TYPE_BOOL)[0]
                        except:
                            self.GroupMandatory = None

                        try:
                            self.GroupEnabled = dsz.cmd.data.ObjectGet(obj, 'GroupEnabled', dsz.TYPE_BOOL)[0]
                        except:
                            self.GroupEnabled = None

                        try:
                            self.GroupLogonId = dsz.cmd.data.ObjectGet(obj, 'GroupLogonId', dsz.TYPE_BOOL)[0]
                        except:
                            self.GroupLogonId = None

                        try:
                            self.GroupResource = dsz.cmd.data.ObjectGet(obj, 'GroupResource', dsz.TYPE_BOOL)[0]
                        except:
                            self.GroupResource = None

                        try:
                            self.GroupEnabledByDefault = dsz.cmd.data.ObjectGet(obj, 'GroupEnabledByDefault', dsz.TYPE_BOOL)[0]
                        except:
                            self.GroupEnabledByDefault = None

                        try:
                            self.GroupOwner = dsz.cmd.data.ObjectGet(obj, 'GroupOwner', dsz.TYPE_BOOL)[0]
                        except:
                            self.GroupOwner = None

                        try:
                            self.Mask = dsz.cmd.data.ObjectGet(obj, 'Mask', dsz.TYPE_INT)[0]
                        except:
                            self.Mask = None

                        return

        class Privileges(dsz.data.DataBean):

            def __init__(self, obj):
                self.Privilege = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Privilege', dsz.TYPE_OBJECT):
                        self.Privilege.append(ProcessInfo.ProcessInfo.Privileges.Privilege(x))

                except:
                    pass

            class Privilege(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
                    except:
                        self.name = None

                    try:
                        self.Attributes = ProcessInfo.ProcessInfo.Privileges.Privilege.Attributes(dsz.cmd.data.ObjectGet(obj, 'Attributes', dsz.TYPE_OBJECT)[0])
                    except:
                        self.Attributes = None

                    return

                class Attributes(dsz.data.DataBean):

                    def __init__(self, obj):
                        try:
                            self.Priv_Enabled = dsz.cmd.data.ObjectGet(obj, 'Priv_Enabled', dsz.TYPE_BOOL)[0]
                        except:
                            self.Priv_Enabled = None

                        try:
                            self.Priv_Enabled_By_Default = dsz.cmd.data.ObjectGet(obj, 'Priv_Enabled_By_Default', dsz.TYPE_BOOL)[0]
                        except:
                            self.Priv_Enabled_By_Default = None

                        try:
                            self.Priv_Used_Access = dsz.cmd.data.ObjectGet(obj, 'Priv_Used_Access', dsz.TYPE_BOOL)[0]
                        except:
                            self.Priv_Used_Access = None

                        try:
                            self.Mask = dsz.cmd.data.ObjectGet(obj, 'Mask', dsz.TYPE_INT)[0]
                        except:
                            self.Mask = None

                        return

        class BasicInfo(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.User = ProcessInfo.ProcessInfo.BasicInfo.User(dsz.cmd.data.ObjectGet(obj, 'User', dsz.TYPE_OBJECT)[0])
                except:
                    self.User = None

                try:
                    self.Owner = ProcessInfo.ProcessInfo.BasicInfo.Owner(dsz.cmd.data.ObjectGet(obj, 'Owner', dsz.TYPE_OBJECT)[0])
                except:
                    self.Owner = None

                try:
                    self.PrimaryGroup = ProcessInfo.ProcessInfo.BasicInfo.PrimaryGroup(dsz.cmd.data.ObjectGet(obj, 'PrimaryGroup', dsz.TYPE_OBJECT)[0])
                except:
                    self.PrimaryGroup = None

                return

            class User(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Attributes = dsz.cmd.data.ObjectGet(obj, 'Attributes', dsz.TYPE_STRING)[0]
                    except:
                        self.Attributes = None

                    try:
                        self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                    except:
                        self.Type = None

                    try:
                        self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
                    except:
                        self.Name = None

                    return

            class Owner(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Attributes = dsz.cmd.data.ObjectGet(obj, 'Attributes', dsz.TYPE_STRING)[0]
                    except:
                        self.Attributes = None

                    try:
                        self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                    except:
                        self.Type = None

                    try:
                        self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
                    except:
                        self.Name = None

                    return

            class PrimaryGroup(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Attributes = dsz.cmd.data.ObjectGet(obj, 'Attributes', dsz.TYPE_STRING)[0]
                    except:
                        self.Attributes = None

                    try:
                        self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                    except:
                        self.Type = None

                    try:
                        self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
                    except:
                        self.Name = None

                    return

        class Modules(dsz.data.DataBean):

            def __init__(self, obj):
                self.Module = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Module', dsz.TYPE_OBJECT):
                        self.Module.append(ProcessInfo.ProcessInfo.Modules.Module(x))

                except:
                    pass

            class Module(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.BaseAddress = dsz.cmd.data.ObjectGet(obj, 'BaseAddress', dsz.TYPE_INT)[0]
                    except:
                        self.BaseAddress = None

                    try:
                        self.ImageSize = dsz.cmd.data.ObjectGet(obj, 'ImageSize', dsz.TYPE_INT)[0]
                    except:
                        self.ImageSize = None

                    try:
                        self.EntryPoint = dsz.cmd.data.ObjectGet(obj, 'EntryPoint', dsz.TYPE_INT)[0]
                    except:
                        self.EntryPoint = None

                    try:
                        self.ModuleName = dsz.cmd.data.ObjectGet(obj, 'ModuleName', dsz.TYPE_STRING)[0]
                    except:
                        self.ModuleName = None

                    self.Checksum = list()
                    try:
                        for x in dsz.cmd.data.ObjectGet(obj, 'Checksum', dsz.TYPE_OBJECT):
                            self.Checksum.append(ProcessInfo.ProcessInfo.Modules.Module.Checksum(x))

                    except:
                        pass

                    return

                class Checksum(dsz.data.DataBean):

                    def __init__(self, obj):
                        try:
                            self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                        except:
                            self.Type = None

                        try:
                            self.Value = dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_STRING)[0]
                        except:
                            self.Value = None

                        return


dsz.data.RegisterCommand('ProcessInfo', ProcessInfo)
PROCESSINFO = ProcessInfo
processinfo = ProcessInfo