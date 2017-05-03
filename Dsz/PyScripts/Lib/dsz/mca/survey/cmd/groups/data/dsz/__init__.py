# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Groups(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = Groups.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        self.Group = list()
        try:
            for x in dsz.cmd.data.Get('Group', dsz.TYPE_OBJECT):
                self.Group.append(Groups.Group(x))

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
                self.Target = Groups.TaskingInfo.Target(dsz.cmd.data.ObjectGet(obj, 'Target', dsz.TYPE_OBJECT)[0])
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

    class Group(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.groupid = dsz.cmd.data.ObjectGet(obj, 'groupid', dsz.TYPE_INT)[0]
            except:
                self.groupid = None

            try:
                self.group = dsz.cmd.data.ObjectGet(obj, 'group', dsz.TYPE_STRING)[0]
            except:
                self.group = None

            try:
                self.comment = dsz.cmd.data.ObjectGet(obj, 'comment', dsz.TYPE_STRING)[0]
            except:
                self.comment = None

            try:
                self.Attributes = Groups.Group.Attributes(dsz.cmd.data.ObjectGet(obj, 'Attributes', dsz.TYPE_OBJECT)[0])
            except:
                self.Attributes = None

            return

        class Attributes(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.mask = dsz.cmd.data.ObjectGet(obj, 'mask', dsz.TYPE_STRING)[0]
                except:
                    self.mask = None

                try:
                    self.groupmandatory = dsz.cmd.data.ObjectGet(obj, 'groupmandatory', dsz.TYPE_BOOL)[0]
                except:
                    self.groupmandatory = None

                try:
                    self.groupenabled = dsz.cmd.data.ObjectGet(obj, 'groupenabled', dsz.TYPE_BOOL)[0]
                except:
                    self.groupenabled = None

                try:
                    self.grouplogonid = dsz.cmd.data.ObjectGet(obj, 'grouplogonid', dsz.TYPE_BOOL)[0]
                except:
                    self.grouplogonid = None

                try:
                    self.groupresource = dsz.cmd.data.ObjectGet(obj, 'groupresource', dsz.TYPE_BOOL)[0]
                except:
                    self.groupresource = None

                try:
                    self.groupenabledbydefault = dsz.cmd.data.ObjectGet(obj, 'groupenabledbydefault', dsz.TYPE_BOOL)[0]
                except:
                    self.groupenabledbydefault = None

                try:
                    self.groupusefordenyonly = dsz.cmd.data.ObjectGet(obj, 'groupusefordenyonly', dsz.TYPE_BOOL)[0]
                except:
                    self.groupusefordenyonly = None

                try:
                    self.groupowner = dsz.cmd.data.ObjectGet(obj, 'groupowner', dsz.TYPE_BOOL)[0]
                except:
                    self.groupowner = None

                return


dsz.data.RegisterCommand('Groups', Groups)
GROUPS = Groups
groups = Groups