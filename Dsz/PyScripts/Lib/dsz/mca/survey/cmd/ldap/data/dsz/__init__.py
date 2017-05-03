# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Ldap(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.taskinginfo = Ldap.taskinginfo(dsz.cmd.data.Get('taskinginfo', dsz.TYPE_OBJECT)[0])
        except:
            self.taskinginfo = None

        try:
            self.LdapEntries = Ldap.LdapEntries(dsz.cmd.data.Get('LdapEntries', dsz.TYPE_OBJECT)[0])
        except:
            self.LdapEntries = None

        return

    class taskinginfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.CommandTarget = Ldap.taskinginfo.CommandTarget(dsz.cmd.data.ObjectGet(obj, 'CommandTarget', dsz.TYPE_OBJECT)[0])
            except:
                self.CommandTarget = None

            try:
                self.SearchMask = Ldap.taskinginfo.SearchMask(dsz.cmd.data.ObjectGet(obj, 'SearchMask', dsz.TYPE_OBJECT)[0])
            except:
                self.SearchMask = None

            try:
                self.SearchParam = Ldap.taskinginfo.SearchParam(dsz.cmd.data.ObjectGet(obj, 'SearchParam', dsz.TYPE_OBJECT)[0])
            except:
                self.SearchParam = None

            return

        class CommandTarget(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.target = dsz.cmd.data.ObjectGet(obj, 'target', dsz.TYPE_STRING)[0]
                except:
                    self.target = None

                return

        class SearchMask(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

                return

        class SearchParam(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

                return

    class LdapEntries(dsz.data.DataBean):

        def __init__(self, obj):
            self.LdapEntry = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'LdapEntry', dsz.TYPE_OBJECT):
                    self.LdapEntry.append(Ldap.LdapEntries.LdapEntry(x))

            except:
                pass

        class LdapEntry(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Attribute = Ldap.LdapEntries.LdapEntry.Attribute(dsz.cmd.data.ObjectGet(obj, 'Attribute', dsz.TYPE_OBJECT)[0])
                except:
                    self.Attribute = None

                return

            class Attribute(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_STRING)[0]
                    except:
                        self.type = None

                    try:
                        self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                    except:
                        self.value = None

                    try:
                        self.dataType = dsz.cmd.data.ObjectGet(obj, 'dataType', dsz.TYPE_INT)[0]
                    except:
                        self.dataType = None

                    return


dsz.data.RegisterCommand('Ldap', Ldap)
LDAP = Ldap
ldap = Ldap