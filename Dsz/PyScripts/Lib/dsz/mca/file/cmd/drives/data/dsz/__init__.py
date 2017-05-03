# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Drives(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.DriveItem = list()
        try:
            for x in dsz.cmd.data.Get('DriveItem', dsz.TYPE_OBJECT):
                self.DriveItem.append(Drives.DriveItem(x))

        except:
            pass

    class DriveItem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.MaximumComponentLength = dsz.cmd.data.ObjectGet(obj, 'MaximumComponentLength', dsz.TYPE_INT)[0]
            except:
                self.MaximumComponentLength = None

            try:
                self.SerialNumber = dsz.cmd.data.ObjectGet(obj, 'SerialNumber', dsz.TYPE_STRING)[0]
            except:
                self.SerialNumber = None

            try:
                self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
            except:
                self.Type = None

            try:
                self.FileSystem = dsz.cmd.data.ObjectGet(obj, 'FileSystem', dsz.TYPE_STRING)[0]
            except:
                self.FileSystem = None

            try:
                self.DriveSource = dsz.cmd.data.ObjectGet(obj, 'DriveSource', dsz.TYPE_STRING)[0]
            except:
                self.DriveSource = None

            try:
                self.Timestamp = dsz.cmd.data.ObjectGet(obj, 'Timestamp', dsz.TYPE_STRING)[0]
            except:
                self.Timestamp = None

            try:
                self.Options = dsz.cmd.data.ObjectGet(obj, 'Options', dsz.TYPE_STRING)[0]
            except:
                self.Options = None

            try:
                self.Drive = dsz.cmd.data.ObjectGet(obj, 'Drive', dsz.TYPE_STRING)[0]
            except:
                self.Drive = None

            try:
                self.Attributes = Drives.DriveItem.Attributes(dsz.cmd.data.ObjectGet(obj, 'Attributes', dsz.TYPE_OBJECT)[0])
            except:
                self.Attributes = None

            return

        class Attributes(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Quotas = dsz.cmd.data.ObjectGet(obj, 'Quotas', dsz.TYPE_BOOL)[0]
                except:
                    self.Quotas = None

                try:
                    self.IsCompressed = dsz.cmd.data.ObjectGet(obj, 'IsCompressed', dsz.TYPE_BOOL)[0]
                except:
                    self.IsCompressed = None

                try:
                    self.WritePermission = dsz.cmd.data.ObjectGet(obj, 'WritePermission', dsz.TYPE_BOOL)[0]
                except:
                    self.WritePermission = None

                try:
                    self.SupportsEncryption = dsz.cmd.data.ObjectGet(obj, 'SupportsEncryption', dsz.TYPE_BOOL)[0]
                except:
                    self.SupportsEncryption = None

                try:
                    self.CaseSensitiveSearch = dsz.cmd.data.ObjectGet(obj, 'CaseSensitiveSearch', dsz.TYPE_BOOL)[0]
                except:
                    self.CaseSensitiveSearch = None

                try:
                    self.SupportsSparseFiles = dsz.cmd.data.ObjectGet(obj, 'SupportsSparseFiles', dsz.TYPE_BOOL)[0]
                except:
                    self.SupportsSparseFiles = None

                try:
                    self.CasePreservedNames = dsz.cmd.data.ObjectGet(obj, 'CasePreservedNames', dsz.TYPE_BOOL)[0]
                except:
                    self.CasePreservedNames = None

                try:
                    self.UnicodeOnDisk = dsz.cmd.data.ObjectGet(obj, 'UnicodeOnDisk', dsz.TYPE_BOOL)[0]
                except:
                    self.UnicodeOnDisk = None

                try:
                    self.SupportsObjectIds = dsz.cmd.data.ObjectGet(obj, 'SupportsObjectIds', dsz.TYPE_BOOL)[0]
                except:
                    self.SupportsObjectIds = None

                try:
                    self.SupportsNameStreams = dsz.cmd.data.ObjectGet(obj, 'SupportsNameStreams', dsz.TYPE_BOOL)[0]
                except:
                    self.SupportsNameStreams = None

                try:
                    self.SupportsRemoteStorage = dsz.cmd.data.ObjectGet(obj, 'SupportsRemoteStorage', dsz.TYPE_BOOL)[0]
                except:
                    self.SupportsRemoteStorage = None

                try:
                    self.ReadPermission = dsz.cmd.data.ObjectGet(obj, 'ReadPermission', dsz.TYPE_BOOL)[0]
                except:
                    self.ReadPermission = None

                try:
                    self.PersistentACLs = dsz.cmd.data.ObjectGet(obj, 'PersistentACLs', dsz.TYPE_BOOL)[0]
                except:
                    self.PersistentACLs = None

                try:
                    self.SupportsReparsePoints = dsz.cmd.data.ObjectGet(obj, 'SupportsReparsePoints', dsz.TYPE_BOOL)[0]
                except:
                    self.SupportsReparsePoints = None

                try:
                    self.FileCompression = dsz.cmd.data.ObjectGet(obj, 'FileCompression', dsz.TYPE_BOOL)[0]
                except:
                    self.FileCompression = None

                return


dsz.data.RegisterCommand('Drives', Drives)
DRIVES = Drives
drives = Drives