# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Addresses(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.Local = list()
        try:
            for x in dsz.cmd.data.Get('Local', dsz.TYPE_OBJECT):
                self.Local.append(Addresses.Local(x))

        except:
            pass

        self.Remote = list()
        try:
            for x in dsz.cmd.data.Get('Remote', dsz.TYPE_OBJECT):
                self.Remote.append(Addresses.Remote(x))

        except:
            pass

        self.FrzAddresses = list()
        try:
            for x in dsz.cmd.data.Get('FrzAddresses', dsz.TYPE_OBJECT):
                self.FrzAddresses.append(Addresses.FrzAddresses(x))

        except:
            pass

        self.FrzLinks = list()
        try:
            for x in dsz.cmd.data.Get('FrzLinks', dsz.TYPE_OBJECT):
                self.FrzLinks.append(Addresses.FrzLinks(x))

        except:
            pass

        self.FrzRoutes = list()
        try:
            for x in dsz.cmd.data.Get('FrzRoutes', dsz.TYPE_OBJECT):
                self.FrzRoutes.append(Addresses.FrzRoutes(x))

        except:
            pass

        self.FrzSecAssociations = list()
        try:
            for x in dsz.cmd.data.Get('FrzSecAssociations', dsz.TYPE_OBJECT):
                self.FrzSecAssociations.append(Addresses.FrzSecAssociations(x))

        except:
            pass

        self.HardwareAddresses = list()
        try:
            for x in dsz.cmd.data.Get('HardwareAddresses', dsz.TYPE_OBJECT):
                self.HardwareAddresses.append(Addresses.HardwareAddresses(x))

        except:
            pass

        self.IpAddresses = list()
        try:
            for x in dsz.cmd.data.Get('IpAddresses', dsz.TYPE_OBJECT):
                self.IpAddresses.append(Addresses.IpAddresses(x))

        except:
            pass

        self.Modules = list()
        try:
            for x in dsz.cmd.data.Get('Modules', dsz.TYPE_OBJECT):
                self.Modules.append(Addresses.Modules(x))

        except:
            pass

        self.ToolVersions = list()
        try:
            for x in dsz.cmd.data.Get('ToolVersions', dsz.TYPE_OBJECT):
                self.ToolVersions.append(Addresses.ToolVersions(x))

        except:
            pass

        self.ConnectionManagerInfo = list()
        try:
            for x in dsz.cmd.data.Get('ConnectionManagerInfo', dsz.TYPE_OBJECT):
                self.ConnectionManagerInfo.append(Addresses.ConnectionManagerInfo(x))

        except:
            pass

    class Local(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Address = dsz.cmd.data.ObjectGet(obj, 'Address', dsz.TYPE_STRING)[0]
            except:
                self.Address = None

            try:
                self.Arch = dsz.cmd.data.ObjectGet(obj, 'Arch', dsz.TYPE_STRING)[0]
            except:
                self.Arch = None

            try:
                self.CompiledArch = dsz.cmd.data.ObjectGet(obj, 'CompiledArch', dsz.TYPE_STRING)[0]
            except:
                self.CompiledArch = None

            try:
                self.Platform = dsz.cmd.data.ObjectGet(obj, 'Platform', dsz.TYPE_STRING)[0]
            except:
                self.Platform = None

            try:
                self.Major = dsz.cmd.data.ObjectGet(obj, 'Major', dsz.TYPE_INT)[0]
            except:
                self.Major = None

            try:
                self.Minor = dsz.cmd.data.ObjectGet(obj, 'Minor', dsz.TYPE_INT)[0]
            except:
                self.Minor = None

            try:
                self.Other = dsz.cmd.data.ObjectGet(obj, 'Other', dsz.TYPE_INT)[0]
            except:
                self.Other = None

            try:
                self.Build = dsz.cmd.data.ObjectGet(obj, 'Build', dsz.TYPE_INT)[0]
            except:
                self.Build = None

            try:
                self.clibMajor = dsz.cmd.data.ObjectGet(obj, 'clibMajor', dsz.TYPE_INT)[0]
            except:
                self.clibMajor = None

            try:
                self.clibMinor = dsz.cmd.data.ObjectGet(obj, 'clibMinor', dsz.TYPE_INT)[0]
            except:
                self.clibMinor = None

            try:
                self.clibRevision = dsz.cmd.data.ObjectGet(obj, 'clibRevision', dsz.TYPE_INT)[0]
            except:
                self.clibRevision = None

            try:
                self.Pid = dsz.cmd.data.ObjectGet(obj, 'Pid', dsz.TYPE_INT)[0]
            except:
                self.Pid = None

            try:
                self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
            except:
                self.Type = None

            try:
                self.Metadata = dsz.cmd.data.ObjectGet(obj, 'Metadata', dsz.TYPE_STRING)[0]
            except:
                self.Metadata = None

            return

    class Remote(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Address = dsz.cmd.data.ObjectGet(obj, 'Address', dsz.TYPE_STRING)[0]
            except:
                self.Address = None

            try:
                self.Arch = dsz.cmd.data.ObjectGet(obj, 'Arch', dsz.TYPE_STRING)[0]
            except:
                self.Arch = None

            try:
                self.CompiledArch = dsz.cmd.data.ObjectGet(obj, 'CompiledArch', dsz.TYPE_STRING)[0]
            except:
                self.CompiledArch = None

            try:
                self.Platform = dsz.cmd.data.ObjectGet(obj, 'Platform', dsz.TYPE_STRING)[0]
            except:
                self.Platform = None

            try:
                self.Major = dsz.cmd.data.ObjectGet(obj, 'Major', dsz.TYPE_INT)[0]
            except:
                self.Major = None

            try:
                self.Minor = dsz.cmd.data.ObjectGet(obj, 'Minor', dsz.TYPE_INT)[0]
            except:
                self.Minor = None

            try:
                self.Other = dsz.cmd.data.ObjectGet(obj, 'Other', dsz.TYPE_INT)[0]
            except:
                self.Other = None

            try:
                self.Build = dsz.cmd.data.ObjectGet(obj, 'Build', dsz.TYPE_INT)[0]
            except:
                self.Build = None

            try:
                self.clibMajor = dsz.cmd.data.ObjectGet(obj, 'clibMajor', dsz.TYPE_INT)[0]
            except:
                self.clibMajor = None

            try:
                self.clibMinor = dsz.cmd.data.ObjectGet(obj, 'clibMinor', dsz.TYPE_INT)[0]
            except:
                self.clibMinor = None

            try:
                self.clibRevision = dsz.cmd.data.ObjectGet(obj, 'clibRevision', dsz.TYPE_INT)[0]
            except:
                self.clibRevision = None

            try:
                self.Pid = dsz.cmd.data.ObjectGet(obj, 'Pid', dsz.TYPE_INT)[0]
            except:
                self.Pid = None

            try:
                self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
            except:
                self.Type = None

            try:
                self.Metadata = dsz.cmd.data.ObjectGet(obj, 'Metadata', dsz.TYPE_STRING)[0]
            except:
                self.Metadata = None

            return

    class FrzAddresses(dsz.data.DataBean):

        def __init__(self, obj):
            self.FrzAddress = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'FrzAddress', dsz.TYPE_OBJECT):
                    self.FrzAddress.append(Addresses.FrzAddresses.FrzAddress(x))

            except:
                pass

        class FrzAddress(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Address = dsz.cmd.data.ObjectGet(obj, 'Address', dsz.TYPE_STRING)[0]
                except:
                    self.Address = None

                return

    class FrzLinks(dsz.data.DataBean):

        def __init__(self, obj):
            self.FrzLink = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'FrzLink', dsz.TYPE_OBJECT):
                    self.FrzLink.append(Addresses.FrzLinks.FrzLink(x))

            except:
                pass

        class FrzLink(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.State = dsz.cmd.data.ObjectGet(obj, 'State', dsz.TYPE_INT)[0]
                except:
                    self.State = None

                try:
                    self.LinkId = dsz.cmd.data.ObjectGet(obj, 'LinkId', dsz.TYPE_INT)[0]
                except:
                    self.LinkId = None

                try:
                    self.CryptProvider = dsz.cmd.data.ObjectGet(obj, 'CryptProvider', dsz.TYPE_STRING)[0]
                except:
                    self.CryptProvider = None

                try:
                    self.LinkParameters = dsz.cmd.data.ObjectGet(obj, 'LinkParameters', dsz.TYPE_STRING)[0]
                except:
                    self.LinkParameters = None

                try:
                    self.CryptKey = dsz.cmd.data.ObjectGet(obj, 'CryptKey', dsz.TYPE_STRING)[0]
                except:
                    self.CryptKey = None

                try:
                    self.CmProvider = dsz.cmd.data.ObjectGet(obj, 'CmProvider', dsz.TYPE_STRING)[0]
                except:
                    self.CmProvider = None

                try:
                    self.Provider = dsz.cmd.data.ObjectGet(obj, 'Provider', dsz.TYPE_STRING)[0]
                except:
                    self.Provider = None

                return

    class FrzRoutes(dsz.data.DataBean):

        def __init__(self, obj):
            self.FrzRoute = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'FrzRoute', dsz.TYPE_OBJECT):
                    self.FrzRoute.append(Addresses.FrzRoutes.FrzRoute(x))

            except:
                pass

        class FrzRoute(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Precedence = dsz.cmd.data.ObjectGet(obj, 'Precedence', dsz.TYPE_INT)[0]
                except:
                    self.Precedence = None

                try:
                    self.CidrBits = dsz.cmd.data.ObjectGet(obj, 'CidrBits', dsz.TYPE_INT)[0]
                except:
                    self.CidrBits = None

                try:
                    self.Pattern = dsz.cmd.data.ObjectGet(obj, 'Pattern', dsz.TYPE_STRING)[0]
                except:
                    self.Pattern = None

                try:
                    self.Mask = dsz.cmd.data.ObjectGet(obj, 'Mask', dsz.TYPE_STRING)[0]
                except:
                    self.Mask = None

                return

    class FrzSecAssociations(dsz.data.DataBean):

        def __init__(self, obj):
            self.FrzSecAssociation = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'FrzSecAssociation', dsz.TYPE_OBJECT):
                    self.FrzSecAssociation.append(Addresses.FrzSecAssociations.FrzSecAssociation(x))

            except:
                pass

        class FrzSecAssociation(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.SequenceCurrent = dsz.cmd.data.ObjectGet(obj, 'SequenceCurrent', dsz.TYPE_INT)[0]
                except:
                    self.SequenceCurrent = None

                try:
                    self.SequenceMax = dsz.cmd.data.ObjectGet(obj, 'SequenceMax', dsz.TYPE_INT)[0]
                except:
                    self.SequenceMax = None

                try:
                    self.CheckType = dsz.cmd.data.ObjectGet(obj, 'CheckType', dsz.TYPE_INT)[0]
                except:
                    self.CheckType = None

                try:
                    self.PrivacyProvider = dsz.cmd.data.ObjectGet(obj, 'PrivacyProvider', dsz.TYPE_STRING)[0]
                except:
                    self.PrivacyProvider = None

                try:
                    self.PrivacyData = dsz.cmd.data.ObjectGet(obj, 'PrivacyData', dsz.TYPE_STRING)[0]
                except:
                    self.PrivacyData = None

                try:
                    self.KeyExchangeProvider = dsz.cmd.data.ObjectGet(obj, 'KeyExchangeProvider', dsz.TYPE_STRING)[0]
                except:
                    self.KeyExchangeProvider = None

                try:
                    self.KeyExchangeData = dsz.cmd.data.ObjectGet(obj, 'KeyExchangeData', dsz.TYPE_STRING)[0]
                except:
                    self.KeyExchangeData = None

                try:
                    self.Flags = dsz.cmd.data.ObjectGet(obj, 'Flags', dsz.TYPE_STRING)[0]
                except:
                    self.Flags = None

                try:
                    self.KeyUpdateProvider = dsz.cmd.data.ObjectGet(obj, 'KeyUpdateProvider', dsz.TYPE_STRING)[0]
                except:
                    self.KeyUpdateProvider = None

                try:
                    self.KeyUpdateData = dsz.cmd.data.ObjectGet(obj, 'KeyUpdateData', dsz.TYPE_STRING)[0]
                except:
                    self.KeyUpdateData = None

                try:
                    self.DstAddress = dsz.cmd.data.ObjectGet(obj, 'DstAddress', dsz.TYPE_STRING)[0]
                except:
                    self.DstAddress = None

                try:
                    self.SrcAddress = dsz.cmd.data.ObjectGet(obj, 'SrcAddress', dsz.TYPE_STRING)[0]
                except:
                    self.SrcAddress = None

                try:
                    self.CheckProvider = dsz.cmd.data.ObjectGet(obj, 'CheckProvider', dsz.TYPE_STRING)[0]
                except:
                    self.CheckProvider = None

                try:
                    self.CheckData = dsz.cmd.data.ObjectGet(obj, 'CheckData', dsz.TYPE_STRING)[0]
                except:
                    self.CheckData = None

                return

    class HardwareAddresses(dsz.data.DataBean):

        def __init__(self, obj):
            self.HardwareAddress = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'HardwareAddress', dsz.TYPE_OBJECT):
                    self.HardwareAddress.append(Addresses.HardwareAddresses.HardwareAddress(x))

            except:
                pass

        class HardwareAddress(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Address = dsz.cmd.data.ObjectGet(obj, 'Address', dsz.TYPE_STRING)[0]
                except:
                    self.Address = None

                return

    class IpAddresses(dsz.data.DataBean):

        def __init__(self, obj):
            self.IpAddress = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'IpAddress', dsz.TYPE_OBJECT):
                    self.IpAddress.append(Addresses.IpAddresses.IpAddress(x))

            except:
                pass

        class IpAddress(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Address = dsz.cmd.data.ObjectGet(obj, 'Address', dsz.TYPE_STRING)[0]
                except:
                    self.Address = None

                return

    class Modules(dsz.data.DataBean):

        def __init__(self, obj):
            self.Module = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Module', dsz.TYPE_OBJECT):
                    self.Module.append(Addresses.Modules.Module(x))

            except:
                pass

        class Module(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_STRING)[0]
                except:
                    self.Id = None

                return

    class ToolVersions(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Lla = Addresses.ToolVersions.Lla(dsz.cmd.data.ObjectGet(obj, 'Lla', dsz.TYPE_OBJECT)[0])
            except:
                self.Lla = None

            try:
                self.Tool = Addresses.ToolVersions.Tool(dsz.cmd.data.ObjectGet(obj, 'Tool', dsz.TYPE_OBJECT)[0])
            except:
                self.Tool = None

            return

        class Lla(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Major = dsz.cmd.data.ObjectGet(obj, 'Major', dsz.TYPE_INT)[0]
                except:
                    self.Major = None

                try:
                    self.Minor = dsz.cmd.data.ObjectGet(obj, 'Minor', dsz.TYPE_INT)[0]
                except:
                    self.Minor = None

                return

        class Tool(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Major = dsz.cmd.data.ObjectGet(obj, 'Major', dsz.TYPE_INT)[0]
                except:
                    self.Major = None

                try:
                    self.Minor = dsz.cmd.data.ObjectGet(obj, 'Minor', dsz.TYPE_INT)[0]
                except:
                    self.Minor = None

                try:
                    self.Patch = dsz.cmd.data.ObjectGet(obj, 'Patch', dsz.TYPE_INT)[0]
                except:
                    self.Patch = None

                try:
                    self.Build = dsz.cmd.data.ObjectGet(obj, 'Build', dsz.TYPE_INT)[0]
                except:
                    self.Build = None

                return

    class ConnectionManagerInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.TimerMark = dsz.cmd.data.ObjectGet(obj, 'TimerMark', dsz.TYPE_INT)[0]
            except:
                self.TimerMark = None

            try:
                self.InactiveTimeMax = dsz.cmd.data.ObjectGet(obj, 'InactiveTimeMax', dsz.TYPE_INT)[0]
            except:
                self.InactiveTimeMax = None

            try:
                self.ConnectionUpTime = Addresses.ConnectionManagerInfo.ConnectionUpTime(dsz.cmd.data.ObjectGet(obj, 'ConnectionUpTime', dsz.TYPE_OBJECT)[0])
            except:
                self.ConnectionUpTime = None

            try:
                self.NextConnect = Addresses.ConnectionManagerInfo.NextConnect(dsz.cmd.data.ObjectGet(obj, 'NextConnect', dsz.TYPE_OBJECT)[0])
            except:
                self.NextConnect = None

            try:
                self.BackOff = Addresses.ConnectionManagerInfo.BackOff(dsz.cmd.data.ObjectGet(obj, 'BackOff', dsz.TYPE_OBJECT)[0])
            except:
                self.BackOff = None

            try:
                self.SilentRunning = Addresses.ConnectionManagerInfo.SilentRunning(dsz.cmd.data.ObjectGet(obj, 'SilentRunning', dsz.TYPE_OBJECT)[0])
            except:
                self.SilentRunning = None

            try:
                self.Timeout = Addresses.ConnectionManagerInfo.Timeout(dsz.cmd.data.ObjectGet(obj, 'Timeout', dsz.TYPE_OBJECT)[0])
            except:
                self.Timeout = None

            return

        class ConnectionUpTime(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Min = dsz.cmd.data.ObjectGet(obj, 'Min', dsz.TYPE_INT)[0]
                except:
                    self.Min = None

                try:
                    self.Max = dsz.cmd.data.ObjectGet(obj, 'Max', dsz.TYPE_INT)[0]
                except:
                    self.Max = None

                return

        class NextConnect(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Time = dsz.cmd.data.ObjectGet(obj, 'Time', dsz.TYPE_INT)[0]
                except:
                    self.Time = None

                try:
                    self.RangeBegin = dsz.cmd.data.ObjectGet(obj, 'RangeBegin', dsz.TYPE_INT)[0]
                except:
                    self.RangeBegin = None

                try:
                    self.RangeEnd = dsz.cmd.data.ObjectGet(obj, 'RangeEnd', dsz.TYPE_INT)[0]
                except:
                    self.RangeEnd = None

                return

        class BackOff(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Max = dsz.cmd.data.ObjectGet(obj, 'Max', dsz.TYPE_INT)[0]
                except:
                    self.Max = None

                try:
                    self.Delta = dsz.cmd.data.ObjectGet(obj, 'Delta', dsz.TYPE_INT)[0]
                except:
                    self.Delta = None

                try:
                    self.Multiplier = dsz.cmd.data.ObjectGet(obj, 'Multiplier', dsz.TYPE_INT)[0]
                except:
                    self.Multiplier = None

                return

        class SilentRunning(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Duration = dsz.cmd.data.ObjectGet(obj, 'Duration', dsz.TYPE_INT)[0]
                except:
                    self.Duration = None

                try:
                    self.Basetime = dsz.cmd.data.ObjectGet(obj, 'Basetime', dsz.TYPE_INT)[0]
                except:
                    self.Basetime = None

                return

        class Timeout(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.SequentialConnection = dsz.cmd.data.ObjectGet(obj, 'SequentialConnection', dsz.TYPE_INT)[0]
                except:
                    self.SequentialConnection = None

                try:
                    self.InitialConnection = dsz.cmd.data.ObjectGet(obj, 'InitialConnection', dsz.TYPE_INT)[0]
                except:
                    self.InitialConnection = None

                return


dsz.data.RegisterCommand('Addresses', Addresses)
ADDRESSES = Addresses
addresses = Addresses