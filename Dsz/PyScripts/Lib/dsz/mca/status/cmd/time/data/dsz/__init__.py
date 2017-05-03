# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Time(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = Time.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        try:
            self.TimeItem = Time.TimeItem(dsz.cmd.data.Get('TimeItem', dsz.TYPE_OBJECT)[0])
        except:
            self.TimeItem = None

        return

    class TaskingInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Target = Time.TaskingInfo.Target(dsz.cmd.data.ObjectGet(obj, 'Target', dsz.TYPE_OBJECT)[0])
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

    class TimeItem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.DaylightSavingsTime = Time.TimeItem.DaylightSavingsTime(dsz.cmd.data.ObjectGet(obj, 'DaylightSavingsTime', dsz.TYPE_OBJECT)[0])
            except:
                self.DaylightSavingsTime = None

            try:
                self.LocalTime = Time.TimeItem.LocalTime(dsz.cmd.data.ObjectGet(obj, 'LocalTime', dsz.TYPE_OBJECT)[0])
            except:
                self.LocalTime = None

            try:
                self.GmtTime = Time.TimeItem.GmtTime(dsz.cmd.data.ObjectGet(obj, 'GmtTime', dsz.TYPE_OBJECT)[0])
            except:
                self.GmtTime = None

            return

        class DaylightSavingsTime(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Daylight = Time.TimeItem.DaylightSavingsTime.Daylight(dsz.cmd.data.ObjectGet(obj, 'Daylight', dsz.TYPE_OBJECT)[0])
                except:
                    self.Daylight = None

                try:
                    self.Standard = Time.TimeItem.DaylightSavingsTime.Standard(dsz.cmd.data.ObjectGet(obj, 'Standard', dsz.TYPE_OBJECT)[0])
                except:
                    self.Standard = None

                return

            class Daylight(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.month = dsz.cmd.data.ObjectGet(obj, 'month', dsz.TYPE_INT)[0]
                    except:
                        self.month = None

                    try:
                        self.day = dsz.cmd.data.ObjectGet(obj, 'day', dsz.TYPE_INT)[0]
                    except:
                        self.day = None

                    try:
                        self.week = dsz.cmd.data.ObjectGet(obj, 'week', dsz.TYPE_INT)[0]
                    except:
                        self.week = None

                    try:
                        self.bias = dsz.cmd.data.ObjectGet(obj, 'bias', dsz.TYPE_STRING)[0]
                    except:
                        self.bias = None

                    try:
                        self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
                    except:
                        self.name = None

                    return

            class Standard(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.month = dsz.cmd.data.ObjectGet(obj, 'month', dsz.TYPE_INT)[0]
                    except:
                        self.month = None

                    try:
                        self.day = dsz.cmd.data.ObjectGet(obj, 'day', dsz.TYPE_INT)[0]
                    except:
                        self.day = None

                    try:
                        self.week = dsz.cmd.data.ObjectGet(obj, 'week', dsz.TYPE_INT)[0]
                    except:
                        self.week = None

                    try:
                        self.bias = dsz.cmd.data.ObjectGet(obj, 'bias', dsz.TYPE_STRING)[0]
                    except:
                        self.bias = None

                    try:
                        self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
                    except:
                        self.name = None

                    return

        class LocalTime(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.date = dsz.cmd.data.ObjectGet(obj, 'date', dsz.TYPE_STRING)[0]
                except:
                    self.date = None

                try:
                    self.time = dsz.cmd.data.ObjectGet(obj, 'time', dsz.TYPE_STRING)[0]
                except:
                    self.time = None

                try:
                    self.nanoseconds = dsz.cmd.data.ObjectGet(obj, 'nanoseconds', dsz.TYPE_STRING)[0]
                except:
                    self.nanoseconds = None

                return

        class GmtTime(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.date = dsz.cmd.data.ObjectGet(obj, 'date', dsz.TYPE_STRING)[0]
                except:
                    self.date = None

                try:
                    self.time = dsz.cmd.data.ObjectGet(obj, 'time', dsz.TYPE_STRING)[0]
                except:
                    self.time = None

                try:
                    self.nanoseconds = dsz.cmd.data.ObjectGet(obj, 'nanoseconds', dsz.TYPE_STRING)[0]
                except:
                    self.nanoseconds = None

                return


dsz.data.RegisterCommand('Time', Time)
TIME = Time
time = Time