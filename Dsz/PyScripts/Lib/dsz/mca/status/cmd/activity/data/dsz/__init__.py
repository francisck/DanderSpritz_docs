# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Activity(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.LastActivity = Activity.LastActivity(dsz.cmd.data.Get('LastActivity', dsz.TYPE_OBJECT)[0])
        except:
            self.LastActivity = None

        self.NewActivity = list()
        try:
            for x in dsz.cmd.data.Get('NewActivity', dsz.TYPE_OBJECT):
                self.NewActivity.append(Activity.NewActivity(x))

        except:
            pass

        return

    class LastActivity(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.days = dsz.cmd.data.ObjectGet(obj, 'days', dsz.TYPE_INT)[0]
            except:
                self.days = None

            try:
                self.hours = dsz.cmd.data.ObjectGet(obj, 'hours', dsz.TYPE_INT)[0]
            except:
                self.hours = None

            try:
                self.minutes = dsz.cmd.data.ObjectGet(obj, 'minutes', dsz.TYPE_INT)[0]
            except:
                self.minutes = None

            try:
                self.seconds = dsz.cmd.data.ObjectGet(obj, 'seconds', dsz.TYPE_INT)[0]
            except:
                self.seconds = None

            return

    class NewActivity(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_STRING)[0]
            except:
                self.type = None

            try:
                self.days = dsz.cmd.data.ObjectGet(obj, 'days', dsz.TYPE_INT)[0]
            except:
                self.days = None

            try:
                self.hours = dsz.cmd.data.ObjectGet(obj, 'hours', dsz.TYPE_INT)[0]
            except:
                self.hours = None

            try:
                self.minutes = dsz.cmd.data.ObjectGet(obj, 'minutes', dsz.TYPE_INT)[0]
            except:
                self.minutes = None

            try:
                self.seconds = dsz.cmd.data.ObjectGet(obj, 'seconds', dsz.TYPE_INT)[0]
            except:
                self.seconds = None

            try:
                self.nanos = dsz.cmd.data.ObjectGet(obj, 'nanos', dsz.TYPE_INT)[0]
            except:
                self.nanos = None

            try:
                self.typevalue = dsz.cmd.data.ObjectGet(obj, 'typevalue', dsz.TYPE_INT)[0]
            except:
                self.typevalue = None

            return


dsz.data.RegisterCommand('Activity', Activity)
ACTIVITY = Activity
activity = Activity