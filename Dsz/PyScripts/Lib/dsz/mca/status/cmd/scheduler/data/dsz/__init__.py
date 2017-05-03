# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Scheduler(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = Scheduler.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        self.AtJob = list()
        try:
            for x in dsz.cmd.data.Get('AtJob', dsz.TYPE_OBJECT):
                self.AtJob.append(Scheduler.AtJob(x))

        except:
            pass

        self.NetJob = list()
        try:
            for x in dsz.cmd.data.Get('NetJob', dsz.TYPE_OBJECT):
                self.NetJob.append(Scheduler.NetJob(x))

        except:
            pass

        self.Folder = list()
        try:
            for x in dsz.cmd.data.Get('Folder', dsz.TYPE_OBJECT):
                self.Folder.append(Scheduler.Folder(x))

        except:
            pass

        self.NewJob = list()
        try:
            for x in dsz.cmd.data.Get('NewJob', dsz.TYPE_OBJECT):
                self.NewJob.append(Scheduler.NewJob(x))

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
                self.TaskType = Scheduler.TaskingInfo.TaskType(dsz.cmd.data.ObjectGet(obj, 'TaskType', dsz.TYPE_OBJECT)[0])
            except:
                self.TaskType = None

            try:
                self.SearchParam = Scheduler.TaskingInfo.SearchParam(dsz.cmd.data.ObjectGet(obj, 'SearchParam', dsz.TYPE_OBJECT)[0])
            except:
                self.SearchParam = None

            try:
                self.Target = Scheduler.TaskingInfo.Target(dsz.cmd.data.ObjectGet(obj, 'Target', dsz.TYPE_OBJECT)[0])
            except:
                self.Target = None

            return

        class TaskType(dsz.data.DataBean):

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

    class AtJob(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.id = dsz.cmd.data.ObjectGet(obj, 'id', dsz.TYPE_INT)[0]
            except:
                self.id = None

            try:
                self.time = dsz.cmd.data.ObjectGet(obj, 'time', dsz.TYPE_STRING)[0]
            except:
                self.time = None

            try:
                self.frequency = dsz.cmd.data.ObjectGet(obj, 'frequency', dsz.TYPE_STRING)[0]
            except:
                self.frequency = None

            try:
                self.commandText = dsz.cmd.data.ObjectGet(obj, 'commandText', dsz.TYPE_STRING)[0]
            except:
                self.commandText = None

            return

    class NetJob(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.ExitCode = dsz.cmd.data.ObjectGet(obj, 'ExitCode', dsz.TYPE_INT)[0]
            except:
                self.ExitCode = None

            try:
                self.Application = dsz.cmd.data.ObjectGet(obj, 'Application', dsz.TYPE_STRING)[0]
            except:
                self.Application = None

            try:
                self.JobName = dsz.cmd.data.ObjectGet(obj, 'JobName', dsz.TYPE_STRING)[0]
            except:
                self.JobName = None

            try:
                self.NextRunTime = dsz.cmd.data.ObjectGet(obj, 'NextRunTime', dsz.TYPE_STRING)[0]
            except:
                self.NextRunTime = None

            try:
                self.NextRunDate = dsz.cmd.data.ObjectGet(obj, 'NextRunDate', dsz.TYPE_STRING)[0]
            except:
                self.NextRunDate = None

            try:
                self.FlagsMask = dsz.cmd.data.ObjectGet(obj, 'FlagsMask', dsz.TYPE_STRING)[0]
            except:
                self.FlagsMask = None

            try:
                self.Account = dsz.cmd.data.ObjectGet(obj, 'Account', dsz.TYPE_STRING)[0]
            except:
                self.Account = None

            try:
                self.Parameters = dsz.cmd.data.ObjectGet(obj, 'Parameters', dsz.TYPE_STRING)[0]
            except:
                self.Parameters = None

            return

    class Folder(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
            except:
                self.Name = None

            try:
                self.Path = dsz.cmd.data.ObjectGet(obj, 'Path', dsz.TYPE_STRING)[0]
            except:
                self.Path = None

            self.Job = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Job', dsz.TYPE_OBJECT):
                    self.Job.append(Scheduler.Folder.Job(x))

            except:
                pass

            return

        class Job(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Disabled = dsz.cmd.data.ObjectGet(obj, 'Disabled', dsz.TYPE_BOOL)[0]
                except:
                    self.Disabled = None

                try:
                    self.NumMissedRuns = dsz.cmd.data.ObjectGet(obj, 'NumMissedRuns', dsz.TYPE_INT)[0]
                except:
                    self.NumMissedRuns = None

                try:
                    self.LastRunResult = dsz.cmd.data.ObjectGet(obj, 'LastRunResult', dsz.TYPE_INT)[0]
                except:
                    self.LastRunResult = None

                try:
                    self.Compatibility = dsz.cmd.data.ObjectGet(obj, 'Compatibility', dsz.TYPE_STRING)[0]
                except:
                    self.Compatibility = None

                try:
                    self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
                except:
                    self.Name = None

                try:
                    self.State = dsz.cmd.data.ObjectGet(obj, 'State', dsz.TYPE_STRING)[0]
                except:
                    self.State = None

                try:
                    self.Path = dsz.cmd.data.ObjectGet(obj, 'Path', dsz.TYPE_STRING)[0]
                except:
                    self.Path = None

                try:
                    self.Xml = dsz.cmd.data.ObjectGet(obj, 'Xml', dsz.TYPE_STRING)[0]
                except:
                    self.Xml = None

                self.Trigger = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Trigger', dsz.TYPE_OBJECT):
                        self.Trigger.append(Scheduler.Folder.Job.Trigger(x))

                except:
                    pass

                self.Principal = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Principal', dsz.TYPE_OBJECT):
                        self.Principal.append(Scheduler.Folder.Job.Principal(x))

                except:
                    pass

                try:
                    self.LastRunTime = Scheduler.Folder.Job.LastRunTime(dsz.cmd.data.ObjectGet(obj, 'LastRunTime', dsz.TYPE_OBJECT)[0])
                except:
                    self.LastRunTime = None

                try:
                    self.NextRunTime = Scheduler.Folder.Job.NextRunTime(dsz.cmd.data.ObjectGet(obj, 'NextRunTime', dsz.TYPE_OBJECT)[0])
                except:
                    self.NextRunTime = None

                self.Action = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Action', dsz.TYPE_OBJECT):
                        self.Action.append(Scheduler.Folder.Job.Action(x))

                except:
                    pass

                return

            class Trigger(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Enabled = dsz.cmd.data.ObjectGet(obj, 'Enabled', dsz.TYPE_BOOL)[0]
                    except:
                        self.Enabled = None

                    try:
                        self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
                    except:
                        self.Id = None

                    try:
                        self.StartBoundary = dsz.cmd.data.ObjectGet(obj, 'StartBoundary', dsz.TYPE_STRING)[0]
                    except:
                        self.StartBoundary = None

                    try:
                        self.EndBoundary = dsz.cmd.data.ObjectGet(obj, 'EndBoundary', dsz.TYPE_STRING)[0]
                    except:
                        self.EndBoundary = None

                    try:
                        self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                    except:
                        self.Type = None

                    return

            class Principal(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_STRING)[0]
                    except:
                        self.Id = None

                    try:
                        self.LogonType = dsz.cmd.data.ObjectGet(obj, 'LogonType', dsz.TYPE_STRING)[0]
                    except:
                        self.LogonType = None

                    try:
                        self.UserId = dsz.cmd.data.ObjectGet(obj, 'UserId', dsz.TYPE_STRING)[0]
                    except:
                        self.UserId = None

                    try:
                        self.GroupId = dsz.cmd.data.ObjectGet(obj, 'GroupId', dsz.TYPE_STRING)[0]
                    except:
                        self.GroupId = None

                    try:
                        self.RunLevel = dsz.cmd.data.ObjectGet(obj, 'RunLevel', dsz.TYPE_STRING)[0]
                    except:
                        self.RunLevel = None

                    try:
                        self.DisplayName = dsz.cmd.data.ObjectGet(obj, 'DisplayName', dsz.TYPE_STRING)[0]
                    except:
                        self.DisplayName = None

                    return

            class LastRunTime(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Time = dsz.cmd.data.ObjectGet(obj, 'Time', dsz.TYPE_STRING)[0]
                    except:
                        self.Time = None

                    try:
                        self.Date = dsz.cmd.data.ObjectGet(obj, 'Date', dsz.TYPE_STRING)[0]
                    except:
                        self.Date = None

                    try:
                        self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                    except:
                        self.Type = None

                    return

            class NextRunTime(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Time = dsz.cmd.data.ObjectGet(obj, 'Time', dsz.TYPE_STRING)[0]
                    except:
                        self.Time = None

                    try:
                        self.Date = dsz.cmd.data.ObjectGet(obj, 'Date', dsz.TYPE_STRING)[0]
                    except:
                        self.Date = None

                    try:
                        self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                    except:
                        self.Type = None

                    return

            class Action(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_STRING)[0]
                    except:
                        self.Id = None

                    try:
                        self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                    except:
                        self.Type = None

                    self.Exec = list()
                    try:
                        for x in dsz.cmd.data.ObjectGet(obj, 'Exec', dsz.TYPE_OBJECT):
                            self.Exec.append(Scheduler.Folder.Job.Action.Exec(x))

                    except:
                        pass

                    self.COM = list()
                    try:
                        for x in dsz.cmd.data.ObjectGet(obj, 'COM', dsz.TYPE_OBJECT):
                            self.COM.append(Scheduler.Folder.Job.Action.COM(x))

                    except:
                        pass

                    return

                class Exec(dsz.data.DataBean):

                    def __init__(self, obj):
                        try:
                            self.Path = dsz.cmd.data.ObjectGet(obj, 'Path', dsz.TYPE_STRING)[0]
                        except:
                            self.Path = None

                        try:
                            self.Arguments = dsz.cmd.data.ObjectGet(obj, 'Arguments', dsz.TYPE_STRING)[0]
                        except:
                            self.Arguments = None

                        try:
                            self.WorkingDir = dsz.cmd.data.ObjectGet(obj, 'WorkingDir', dsz.TYPE_STRING)[0]
                        except:
                            self.WorkingDir = None

                        return

                class COM(dsz.data.DataBean):

                    def __init__(self, obj):
                        try:
                            self.Data = dsz.cmd.data.ObjectGet(obj, 'Data', dsz.TYPE_STRING)[0]
                        except:
                            self.Data = None

                        try:
                            self.ClassId = dsz.cmd.data.ObjectGet(obj, 'ClassId', dsz.TYPE_STRING)[0]
                        except:
                            self.ClassId = None

                        return

    class NewJob(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
            except:
                self.Id = None

            try:
                self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
            except:
                self.Name = None

            return


dsz.data.RegisterCommand('Scheduler', Scheduler)
SCHEDULER = Scheduler
scheduler = Scheduler