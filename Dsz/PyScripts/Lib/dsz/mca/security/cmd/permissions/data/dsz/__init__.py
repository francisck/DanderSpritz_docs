# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Permissions(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.Modified = Permissions.Modified(dsz.cmd.data.Get('Modified', dsz.TYPE_OBJECT)[0])
        except:
            self.Modified = None

        try:
            self.object = Permissions.object(dsz.cmd.data.Get('object', dsz.TYPE_OBJECT)[0])
        except:
            self.object = None

        self.acl = list()
        try:
            for x in dsz.cmd.data.Get('acl', dsz.TYPE_OBJECT):
                self.acl.append(Permissions.acl(x))

        except:
            pass

        return

    class Modified(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.removepending = dsz.cmd.data.ObjectGet(obj, 'removepending', dsz.TYPE_BOOL)[0]
            except:
                self.removepending = None

            return

    class object(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.group = dsz.cmd.data.ObjectGet(obj, 'group', dsz.TYPE_STRING)[0]
            except:
                self.group = None

            try:
                self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_STRING)[0]
            except:
                self.type = None

            try:
                self.owner = dsz.cmd.data.ObjectGet(obj, 'owner', dsz.TYPE_STRING)[0]
            except:
                self.owner = None

            try:
                self.groupdomain = dsz.cmd.data.ObjectGet(obj, 'groupdomain', dsz.TYPE_STRING)[0]
            except:
                self.groupdomain = None

            try:
                self.ownerdomain = dsz.cmd.data.ObjectGet(obj, 'ownerdomain', dsz.TYPE_STRING)[0]
            except:
                self.ownerdomain = None

            try:
                self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
            except:
                self.name = None

            try:
                self.PermissionString = dsz.cmd.data.ObjectGet(obj, 'PermissionString', dsz.TYPE_STRING)[0]
            except:
                self.PermissionString = None

            try:
                self.Flags = Permissions.object.Flags(dsz.cmd.data.ObjectGet(obj, 'Flags', dsz.TYPE_OBJECT)[0])
            except:
                self.Flags = None

            return

        class Flags(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.SE_DACL_AUTO_INHERIT_REQ = dsz.cmd.data.ObjectGet(obj, 'SE_DACL_AUTO_INHERIT_REQ', dsz.TYPE_BOOL)[0]
                except:
                    self.SE_DACL_AUTO_INHERIT_REQ = None

                try:
                    self.SE_DACL_AUTO_INHERITED = dsz.cmd.data.ObjectGet(obj, 'SE_DACL_AUTO_INHERITED', dsz.TYPE_BOOL)[0]
                except:
                    self.SE_DACL_AUTO_INHERITED = None

                try:
                    self.SE_DACL_DEFAULTED = dsz.cmd.data.ObjectGet(obj, 'SE_DACL_DEFAULTED', dsz.TYPE_BOOL)[0]
                except:
                    self.SE_DACL_DEFAULTED = None

                try:
                    self.SE_DACL_PRESENT = dsz.cmd.data.ObjectGet(obj, 'SE_DACL_PRESENT', dsz.TYPE_BOOL)[0]
                except:
                    self.SE_DACL_PRESENT = None

                try:
                    self.SE_DACL_PROTECTED = dsz.cmd.data.ObjectGet(obj, 'SE_DACL_PROTECTED', dsz.TYPE_BOOL)[0]
                except:
                    self.SE_DACL_PROTECTED = None

                try:
                    self.SE_GROUP_DEFAULTED = dsz.cmd.data.ObjectGet(obj, 'SE_GROUP_DEFAULTED', dsz.TYPE_BOOL)[0]
                except:
                    self.SE_GROUP_DEFAULTED = None

                try:
                    self.SE_OWNER_DEFAULTED = dsz.cmd.data.ObjectGet(obj, 'SE_OWNER_DEFAULTED', dsz.TYPE_BOOL)[0]
                except:
                    self.SE_OWNER_DEFAULTED = None

                try:
                    self.SE_RM_CONTROL_VALID = dsz.cmd.data.ObjectGet(obj, 'SE_RM_CONTROL_VALID', dsz.TYPE_BOOL)[0]
                except:
                    self.SE_RM_CONTROL_VALID = None

                try:
                    self.SE_SACL_AUTO_INHERIT_REQ = dsz.cmd.data.ObjectGet(obj, 'SE_SACL_AUTO_INHERIT_REQ', dsz.TYPE_BOOL)[0]
                except:
                    self.SE_SACL_AUTO_INHERIT_REQ = None

                try:
                    self.SE_SACL_AUTO_INHERITED = dsz.cmd.data.ObjectGet(obj, 'SE_SACL_AUTO_INHERITED', dsz.TYPE_BOOL)[0]
                except:
                    self.SE_SACL_AUTO_INHERITED = None

                try:
                    self.SE_SACL_DEFAULTED = dsz.cmd.data.ObjectGet(obj, 'SE_SACL_DEFAULTED', dsz.TYPE_BOOL)[0]
                except:
                    self.SE_SACL_DEFAULTED = None

                try:
                    self.SE_SACL_PRESENT = dsz.cmd.data.ObjectGet(obj, 'SE_SACL_PRESENT', dsz.TYPE_BOOL)[0]
                except:
                    self.SE_SACL_PRESENT = None

                try:
                    self.SE_SACL_PROTECTED = dsz.cmd.data.ObjectGet(obj, 'SE_SACL_PROTECTED', dsz.TYPE_BOOL)[0]
                except:
                    self.SE_SACL_PROTECTED = None

                try:
                    self.SE_SELF_RELATIVE = dsz.cmd.data.ObjectGet(obj, 'SE_SELF_RELATIVE', dsz.TYPE_BOOL)[0]
                except:
                    self.SE_SELF_RELATIVE = None

                return

    class acl(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_STRING)[0]
            except:
                self.type = None

            self.ace = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'ace', dsz.TYPE_OBJECT):
                    self.ace.append(Permissions.acl.ace(x))

            except:
                pass

            return

        class ace(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.typeValue = dsz.cmd.data.ObjectGet(obj, 'typeValue', dsz.TYPE_INT)[0]
                except:
                    self.typeValue = None

                try:
                    self.user = dsz.cmd.data.ObjectGet(obj, 'user', dsz.TYPE_STRING)[0]
                except:
                    self.user = None

                try:
                    self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_STRING)[0]
                except:
                    self.type = None

                try:
                    self.domain = dsz.cmd.data.ObjectGet(obj, 'domain', dsz.TYPE_STRING)[0]
                except:
                    self.domain = None

                try:
                    self.Flags = Permissions.acl.ace.Flags(dsz.cmd.data.ObjectGet(obj, 'Flags', dsz.TYPE_OBJECT)[0])
                except:
                    self.Flags = None

                try:
                    self.Mask = Permissions.acl.ace.Mask(dsz.cmd.data.ObjectGet(obj, 'Mask', dsz.TYPE_OBJECT)[0])
                except:
                    self.Mask = None

                return

            class Flags(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.inherited_ace = dsz.cmd.data.ObjectGet(obj, 'inherited_ace', dsz.TYPE_BOOL)[0]
                    except:
                        self.inherited_ace = None

                    try:
                        self.no_propagate_inherit_ace = dsz.cmd.data.ObjectGet(obj, 'no_propagate_inherit_ace', dsz.TYPE_BOOL)[0]
                    except:
                        self.no_propagate_inherit_ace = None

                    try:
                        self.successful_access_ace = dsz.cmd.data.ObjectGet(obj, 'successful_access_ace', dsz.TYPE_BOOL)[0]
                    except:
                        self.successful_access_ace = None

                    try:
                        self.container_inherit_ace = dsz.cmd.data.ObjectGet(obj, 'container_inherit_ace', dsz.TYPE_BOOL)[0]
                    except:
                        self.container_inherit_ace = None

                    try:
                        self.object_inherit = dsz.cmd.data.ObjectGet(obj, 'object_inherit', dsz.TYPE_BOOL)[0]
                    except:
                        self.object_inherit = None

                    try:
                        self.failed_access_ace = dsz.cmd.data.ObjectGet(obj, 'failed_access_ace', dsz.TYPE_BOOL)[0]
                    except:
                        self.failed_access_ace = None

                    try:
                        self.inherit_only_ace = dsz.cmd.data.ObjectGet(obj, 'inherit_only_ace', dsz.TYPE_BOOL)[0]
                    except:
                        self.inherit_only_ace = None

                    return

            class Mask(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.write_dac = dsz.cmd.data.ObjectGet(obj, 'write_dac', dsz.TYPE_BOOL)[0]
                    except:
                        self.write_dac = None

                    try:
                        self.file_read_ea = dsz.cmd.data.ObjectGet(obj, 'file_read_ea', dsz.TYPE_BOOL)[0]
                    except:
                        self.file_read_ea = None

                    try:
                        self.generic_read_mask = dsz.cmd.data.ObjectGet(obj, 'generic_read_mask', dsz.TYPE_BOOL)[0]
                    except:
                        self.generic_read_mask = None

                    try:
                        self.file_write_data = dsz.cmd.data.ObjectGet(obj, 'file_write_data', dsz.TYPE_BOOL)[0]
                    except:
                        self.file_write_data = None

                    try:
                        self.read_control = dsz.cmd.data.ObjectGet(obj, 'read_control', dsz.TYPE_BOOL)[0]
                    except:
                        self.read_control = None

                    try:
                        self.file_read_attr = dsz.cmd.data.ObjectGet(obj, 'file_read_attr', dsz.TYPE_BOOL)[0]
                    except:
                        self.file_read_attr = None

                    try:
                        self.file_write_attr = dsz.cmd.data.ObjectGet(obj, 'file_write_attr', dsz.TYPE_BOOL)[0]
                    except:
                        self.file_write_attr = None

                    try:
                        self.file_delete_child = dsz.cmd.data.ObjectGet(obj, 'file_delete_child', dsz.TYPE_BOOL)[0]
                    except:
                        self.file_delete_child = None

                    try:
                        self.file_read_data = dsz.cmd.data.ObjectGet(obj, 'file_read_data', dsz.TYPE_BOOL)[0]
                    except:
                        self.file_read_data = None

                    try:
                        self.file_append_data = dsz.cmd.data.ObjectGet(obj, 'file_append_data', dsz.TYPE_BOOL)[0]
                    except:
                        self.file_append_data = None

                    try:
                        self.file_write_ea = dsz.cmd.data.ObjectGet(obj, 'file_write_ea', dsz.TYPE_BOOL)[0]
                    except:
                        self.file_write_ea = None

                    try:
                        self.file_execute = dsz.cmd.data.ObjectGet(obj, 'file_execute', dsz.TYPE_BOOL)[0]
                    except:
                        self.file_execute = None

                    try:
                        self.write_owner = dsz.cmd.data.ObjectGet(obj, 'write_owner', dsz.TYPE_BOOL)[0]
                    except:
                        self.write_owner = None

                    try:
                        self.synchronize = dsz.cmd.data.ObjectGet(obj, 'synchronize', dsz.TYPE_BOOL)[0]
                    except:
                        self.synchronize = None

                    try:
                        self.generic_write_mask = dsz.cmd.data.ObjectGet(obj, 'generic_write_mask', dsz.TYPE_BOOL)[0]
                    except:
                        self.generic_write_mask = None

                    try:
                        self.execute_file_mask = dsz.cmd.data.ObjectGet(obj, 'execute_file_mask', dsz.TYPE_BOOL)[0]
                    except:
                        self.execute_file_mask = None

                    try:
                        self.delete_mask = dsz.cmd.data.ObjectGet(obj, 'delete_mask', dsz.TYPE_BOOL)[0]
                    except:
                        self.delete_mask = None

                    try:
                        self.full_control_mask = dsz.cmd.data.ObjectGet(obj, 'full_control_mask', dsz.TYPE_BOOL)[0]
                    except:
                        self.full_control_mask = None

                    try:
                        self.read_write_mask = dsz.cmd.data.ObjectGet(obj, 'read_write_mask', dsz.TYPE_BOOL)[0]
                    except:
                        self.read_write_mask = None

                    return


dsz.data.RegisterCommand('Permissions', Permissions)
PERMISSIONS = Permissions
permissions = Permissions