# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class SystemVersion(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = SystemVersion.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        try:
            self.VersionInfo = SystemVersion.VersionInfo(dsz.cmd.data.Get('VersionInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.VersionInfo = None

        return

    class TaskingInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.recursive = dsz.cmd.data.ObjectGet(obj, 'recursive', dsz.TYPE_BOOL)[0]
            except:
                self.recursive = None

            try:
                self.Target = SystemVersion.TaskingInfo.Target(dsz.cmd.data.ObjectGet(obj, 'Target', dsz.TYPE_OBJECT)[0])
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

    class VersionInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.major = dsz.cmd.data.ObjectGet(obj, 'major', dsz.TYPE_INT)[0]
            except:
                self.major = None

            try:
                self.minor = dsz.cmd.data.ObjectGet(obj, 'minor', dsz.TYPE_INT)[0]
            except:
                self.minor = None

            try:
                self.build = dsz.cmd.data.ObjectGet(obj, 'build', dsz.TYPE_INT)[0]
            except:
                self.build = None

            try:
                self.revisionMajor = dsz.cmd.data.ObjectGet(obj, 'revisionMajor', dsz.TYPE_INT)[0]
            except:
                self.revisionMajor = None

            try:
                self.revisionMinor = dsz.cmd.data.ObjectGet(obj, 'revisionMinor', dsz.TYPE_INT)[0]
            except:
                self.revisionMinor = None

            try:
                self.platform = dsz.cmd.data.ObjectGet(obj, 'platform', dsz.TYPE_STRING)[0]
            except:
                self.platform = None

            try:
                self.extraInfo = dsz.cmd.data.ObjectGet(obj, 'extraInfo', dsz.TYPE_STRING)[0]
            except:
                self.extraInfo = None

            try:
                self.arch = dsz.cmd.data.ObjectGet(obj, 'arch', dsz.TYPE_STRING)[0]
            except:
                self.arch = None

            try:
                self.Flags = SystemVersion.VersionInfo.Flags(dsz.cmd.data.ObjectGet(obj, 'Flags', dsz.TYPE_OBJECT)[0])
            except:
                self.Flags = None

            return

        class Flags(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_INT)[0]
                except:
                    self.value = None

                try:
                    self.blade = dsz.cmd.data.ObjectGet(obj, 'blade', dsz.TYPE_BOOL)[0]
                except:
                    self.blade = None

                try:
                    self.dataCenter = dsz.cmd.data.ObjectGet(obj, 'dataCenter', dsz.TYPE_BOOL)[0]
                except:
                    self.dataCenter = None

                try:
                    self.terminal = dsz.cmd.data.ObjectGet(obj, 'terminal', dsz.TYPE_BOOL)[0]
                except:
                    self.terminal = None

                try:
                    self.embeddedNt = dsz.cmd.data.ObjectGet(obj, 'embeddedNt', dsz.TYPE_BOOL)[0]
                except:
                    self.embeddedNt = None

                try:
                    self.smallBusiness = dsz.cmd.data.ObjectGet(obj, 'smallBusiness', dsz.TYPE_BOOL)[0]
                except:
                    self.smallBusiness = None

                try:
                    self.backOffice = dsz.cmd.data.ObjectGet(obj, 'backOffice', dsz.TYPE_BOOL)[0]
                except:
                    self.backOffice = None

                try:
                    self.domainController = dsz.cmd.data.ObjectGet(obj, 'domainController', dsz.TYPE_BOOL)[0]
                except:
                    self.domainController = None

                try:
                    self.personal = dsz.cmd.data.ObjectGet(obj, 'personal', dsz.TYPE_BOOL)[0]
                except:
                    self.personal = None

                try:
                    self.singleUserTS = dsz.cmd.data.ObjectGet(obj, 'singleUserTS', dsz.TYPE_BOOL)[0]
                except:
                    self.singleUserTS = None

                try:
                    self.smallBusinessRestricted = dsz.cmd.data.ObjectGet(obj, 'smallBusinessRestricted', dsz.TYPE_BOOL)[0]
                except:
                    self.smallBusinessRestricted = None

                try:
                    self.workstation = dsz.cmd.data.ObjectGet(obj, 'workstation', dsz.TYPE_BOOL)[0]
                except:
                    self.workstation = None

                try:
                    self.enterprise = dsz.cmd.data.ObjectGet(obj, 'enterprise', dsz.TYPE_BOOL)[0]
                except:
                    self.enterprise = None

                try:
                    self.server = dsz.cmd.data.ObjectGet(obj, 'server', dsz.TYPE_BOOL)[0]
                except:
                    self.server = None

                return


dsz.data.RegisterCommand('SystemVersion', SystemVersion)
SYSTEMVERSION = SystemVersion
systemversion = SystemVersion