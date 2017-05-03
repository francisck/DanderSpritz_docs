# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class FileAttributes(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.File = FileAttributes.File(dsz.cmd.data.Get('File', dsz.TYPE_OBJECT)[0])
        except:
            self.File = None

        return

    class File(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Size = dsz.cmd.data.ObjectGet(obj, 'Size', dsz.TYPE_INT)[0]
            except:
                self.Size = None

            try:
                self.Group = dsz.cmd.data.ObjectGet(obj, 'Group', dsz.TYPE_STRING)[0]
            except:
                self.Group = None

            try:
                self.Owner = dsz.cmd.data.ObjectGet(obj, 'Owner', dsz.TYPE_STRING)[0]
            except:
                self.Owner = None

            try:
                self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
            except:
                self.Name = None

            try:
                self.Attributes = FileAttributes.File.Attributes(dsz.cmd.data.ObjectGet(obj, 'Attributes', dsz.TYPE_OBJECT)[0])
            except:
                self.Attributes = None

            try:
                self.FileTimes = FileAttributes.File.FileTimes(dsz.cmd.data.ObjectGet(obj, 'FileTimes', dsz.TYPE_OBJECT)[0])
            except:
                self.FileTimes = None

            try:
                self.ReparseInfo = FileAttributes.File.ReparseInfo(dsz.cmd.data.ObjectGet(obj, 'ReparseInfo', dsz.TYPE_OBJECT)[0])
            except:
                self.ReparseInfo = None

            return

        class Attributes(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Directory = dsz.cmd.data.ObjectGet(obj, 'Directory', dsz.TYPE_BOOL)[0]
                except:
                    self.Directory = None

                try:
                    self.Offline = dsz.cmd.data.ObjectGet(obj, 'Offline', dsz.TYPE_BOOL)[0]
                except:
                    self.Offline = None

                try:
                    self.WorldRead = dsz.cmd.data.ObjectGet(obj, 'WorldRead', dsz.TYPE_BOOL)[0]
                except:
                    self.WorldRead = None

                try:
                    self.GroupRead = dsz.cmd.data.ObjectGet(obj, 'GroupRead', dsz.TYPE_BOOL)[0]
                except:
                    self.GroupRead = None

                try:
                    self.SetUID = dsz.cmd.data.ObjectGet(obj, 'SetUID', dsz.TYPE_BOOL)[0]
                except:
                    self.SetUID = None

                try:
                    self.Compressed = dsz.cmd.data.ObjectGet(obj, 'Compressed', dsz.TYPE_BOOL)[0]
                except:
                    self.Compressed = None

                try:
                    self.WorldWrite = dsz.cmd.data.ObjectGet(obj, 'WorldWrite', dsz.TYPE_BOOL)[0]
                except:
                    self.WorldWrite = None

                try:
                    self.OwnerExecute = dsz.cmd.data.ObjectGet(obj, 'OwnerExecute', dsz.TYPE_BOOL)[0]
                except:
                    self.OwnerExecute = None

                try:
                    self.Hidden = dsz.cmd.data.ObjectGet(obj, 'Hidden', dsz.TYPE_BOOL)[0]
                except:
                    self.Hidden = None

                try:
                    self.Normal = dsz.cmd.data.ObjectGet(obj, 'Normal', dsz.TYPE_BOOL)[0]
                except:
                    self.Normal = None

                try:
                    self.ReparsePoint = dsz.cmd.data.ObjectGet(obj, 'ReparsePoint', dsz.TYPE_BOOL)[0]
                except:
                    self.ReparsePoint = None

                try:
                    self.System = dsz.cmd.data.ObjectGet(obj, 'System', dsz.TYPE_BOOL)[0]
                except:
                    self.System = None

                try:
                    self.SparseFile = dsz.cmd.data.ObjectGet(obj, 'SparseFile', dsz.TYPE_BOOL)[0]
                except:
                    self.SparseFile = None

                try:
                    self.ReadOnly = dsz.cmd.data.ObjectGet(obj, 'ReadOnly', dsz.TYPE_BOOL)[0]
                except:
                    self.ReadOnly = None

                try:
                    self.Device = dsz.cmd.data.ObjectGet(obj, 'Device', dsz.TYPE_BOOL)[0]
                except:
                    self.Device = None

                try:
                    self.GroupExecute = dsz.cmd.data.ObjectGet(obj, 'GroupExecute', dsz.TYPE_BOOL)[0]
                except:
                    self.GroupExecute = None

                try:
                    self.Archive = dsz.cmd.data.ObjectGet(obj, 'Archive', dsz.TYPE_BOOL)[0]
                except:
                    self.Archive = None

                try:
                    self.SetGID = dsz.cmd.data.ObjectGet(obj, 'SetGID', dsz.TYPE_BOOL)[0]
                except:
                    self.SetGID = None

                try:
                    self.Sticky = dsz.cmd.data.ObjectGet(obj, 'Sticky', dsz.TYPE_BOOL)[0]
                except:
                    self.Sticky = None

                try:
                    self.Encrypted = dsz.cmd.data.ObjectGet(obj, 'Encrypted', dsz.TYPE_BOOL)[0]
                except:
                    self.Encrypted = None

                try:
                    self.GroupWrite = dsz.cmd.data.ObjectGet(obj, 'GroupWrite', dsz.TYPE_BOOL)[0]
                except:
                    self.GroupWrite = None

                try:
                    self.Temporary = dsz.cmd.data.ObjectGet(obj, 'Temporary', dsz.TYPE_BOOL)[0]
                except:
                    self.Temporary = None

                try:
                    self.OwnerRead = dsz.cmd.data.ObjectGet(obj, 'OwnerRead', dsz.TYPE_BOOL)[0]
                except:
                    self.OwnerRead = None

                try:
                    self.OwnerWrite = dsz.cmd.data.ObjectGet(obj, 'OwnerWrite', dsz.TYPE_BOOL)[0]
                except:
                    self.OwnerWrite = None

                try:
                    self.WorldExecute = dsz.cmd.data.ObjectGet(obj, 'WorldExecute', dsz.TYPE_BOOL)[0]
                except:
                    self.WorldExecute = None

                try:
                    self.NotContentIndexed = dsz.cmd.data.ObjectGet(obj, 'NotContentIndexed', dsz.TYPE_BOOL)[0]
                except:
                    self.NotContentIndexed = None

                try:
                    self.Value = dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_INT)[0]
                except:
                    self.Value = None

                return

        class FileTimes(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Created = FileAttributes.File.FileTimes.Created(dsz.cmd.data.ObjectGet(obj, 'Created', dsz.TYPE_OBJECT)[0])
                except:
                    self.Created = None

                try:
                    self.Accessed = FileAttributes.File.FileTimes.Accessed(dsz.cmd.data.ObjectGet(obj, 'Accessed', dsz.TYPE_OBJECT)[0])
                except:
                    self.Accessed = None

                try:
                    self.Modified = FileAttributes.File.FileTimes.Modified(dsz.cmd.data.ObjectGet(obj, 'Modified', dsz.TYPE_OBJECT)[0])
                except:
                    self.Modified = None

                return

            class Created(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                    except:
                        self.Type = None

                    try:
                        self.Time = dsz.cmd.data.ObjectGet(obj, 'Time', dsz.TYPE_STRING)[0]
                    except:
                        self.Time = None

                    try:
                        self.Date = dsz.cmd.data.ObjectGet(obj, 'Date', dsz.TYPE_STRING)[0]
                    except:
                        self.Date = None

                    return

            class Accessed(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                    except:
                        self.Type = None

                    try:
                        self.Time = dsz.cmd.data.ObjectGet(obj, 'Time', dsz.TYPE_STRING)[0]
                    except:
                        self.Time = None

                    try:
                        self.Date = dsz.cmd.data.ObjectGet(obj, 'Date', dsz.TYPE_STRING)[0]
                    except:
                        self.Date = None

                    return

            class Modified(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                    except:
                        self.Type = None

                    try:
                        self.Time = dsz.cmd.data.ObjectGet(obj, 'Time', dsz.TYPE_STRING)[0]
                    except:
                        self.Time = None

                    try:
                        self.Date = dsz.cmd.data.ObjectGet(obj, 'Date', dsz.TYPE_STRING)[0]
                    except:
                        self.Date = None

                    return

        class ReparseInfo(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Flags = dsz.cmd.data.ObjectGet(obj, 'Flags', dsz.TYPE_INT)[0]
                except:
                    self.Flags = None

                try:
                    self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                except:
                    self.Type = None

                try:
                    self.TargetPath = dsz.cmd.data.ObjectGet(obj, 'TargetPath', dsz.TYPE_STRING)[0]
                except:
                    self.TargetPath = None

                try:
                    self.AltTargetPath = dsz.cmd.data.ObjectGet(obj, 'AltTargetPath', dsz.TYPE_STRING)[0]
                except:
                    self.AltTargetPath = None

                return


dsz.data.RegisterCommand('FileAttributes', FileAttributes)
FILEATTRIBUTES = FileAttributes
fileattributes = FileAttributes