# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class KiSu_Config(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.Configuration = KiSu_Config.Configuration(dsz.cmd.data.Get('Configuration', dsz.TYPE_OBJECT)[0])
        except:
            self.Configuration = None

        return

    class Configuration(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.version = dsz.cmd.data.ObjectGet(obj, 'version', dsz.TYPE_STRING)[0]
            except:
                self.version = None

            try:
                self.Persistence = KiSu_Config.Configuration.Persistence(dsz.cmd.data.ObjectGet(obj, 'Persistence', dsz.TYPE_OBJECT)[0])
            except:
                self.Persistence = None

            try:
                self.KernelModuleLoader = KiSu_Config.Configuration.KernelModuleLoader(dsz.cmd.data.ObjectGet(obj, 'KernelModuleLoader', dsz.TYPE_OBJECT)[0])
            except:
                self.KernelModuleLoader = None

            try:
                self.UserModuleLoader = KiSu_Config.Configuration.UserModuleLoader(dsz.cmd.data.ObjectGet(obj, 'UserModuleLoader', dsz.TYPE_OBJECT)[0])
            except:
                self.UserModuleLoader = None

            try:
                self.ModuleStoreDirectory = KiSu_Config.Configuration.ModuleStoreDirectory(dsz.cmd.data.ObjectGet(obj, 'ModuleStoreDirectory', dsz.TYPE_OBJECT)[0])
            except:
                self.ModuleStoreDirectory = None

            try:
                self.Launcher = KiSu_Config.Configuration.Launcher(dsz.cmd.data.ObjectGet(obj, 'Launcher', dsz.TYPE_OBJECT)[0])
            except:
                self.Launcher = None

            self.Module = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Module', dsz.TYPE_OBJECT):
                    self.Module.append(KiSu_Config.Configuration.Module(x))

            except:
                pass

            return

        class Persistence(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Method = dsz.cmd.data.ObjectGet(obj, 'Method', dsz.TYPE_STRING)[0]
                except:
                    self.Method = None

                return

        class KernelModuleLoader(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.RegistryValue = dsz.cmd.data.ObjectGet(obj, 'RegistryValue', dsz.TYPE_STRING)[0]
                except:
                    self.RegistryValue = None

                try:
                    self.RegistryKey = dsz.cmd.data.ObjectGet(obj, 'RegistryKey', dsz.TYPE_STRING)[0]
                except:
                    self.RegistryKey = None

                return

        class UserModuleLoader(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.RegistryValue = dsz.cmd.data.ObjectGet(obj, 'RegistryValue', dsz.TYPE_STRING)[0]
                except:
                    self.RegistryValue = None

                try:
                    self.RegistryKey = dsz.cmd.data.ObjectGet(obj, 'RegistryKey', dsz.TYPE_STRING)[0]
                except:
                    self.RegistryKey = None

                return

        class ModuleStoreDirectory(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.RegistryValue = dsz.cmd.data.ObjectGet(obj, 'RegistryValue', dsz.TYPE_STRING)[0]
                except:
                    self.RegistryValue = None

                try:
                    self.RegistryKey = dsz.cmd.data.ObjectGet(obj, 'RegistryKey', dsz.TYPE_STRING)[0]
                except:
                    self.RegistryKey = None

                return

        class Launcher(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.RegistryValue = dsz.cmd.data.ObjectGet(obj, 'RegistryValue', dsz.TYPE_STRING)[0]
                except:
                    self.RegistryValue = None

                try:
                    self.ServiceName = dsz.cmd.data.ObjectGet(obj, 'ServiceName', dsz.TYPE_STRING)[0]
                except:
                    self.ServiceName = None

                return

        class Module(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.id = dsz.cmd.data.ObjectGet(obj, 'id', dsz.TYPE_INT)[0]
                except:
                    self.id = None

                try:
                    self.order = dsz.cmd.data.ObjectGet(obj, 'order', dsz.TYPE_INT)[0]
                except:
                    self.order = None

                try:
                    self.size = dsz.cmd.data.ObjectGet(obj, 'size', dsz.TYPE_INT)[0]
                except:
                    self.size = None

                try:
                    self.processName = dsz.cmd.data.ObjectGet(obj, 'processName', dsz.TYPE_STRING)[0]
                except:
                    self.processName = None

                try:
                    self.moduleName = dsz.cmd.data.ObjectGet(obj, 'moduleName', dsz.TYPE_STRING)[0]
                except:
                    self.moduleName = None

                try:
                    self.Flags = KiSu_Config.Configuration.Module.Flags(dsz.cmd.data.ObjectGet(obj, 'Flags', dsz.TYPE_OBJECT)[0])
                except:
                    self.Flags = None

                try:
                    self.Hash = KiSu_Config.Configuration.Module.Hash(dsz.cmd.data.ObjectGet(obj, 'Hash', dsz.TYPE_OBJECT)[0])
                except:
                    self.Hash = None

                return

            class Flags(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.encrypted = dsz.cmd.data.ObjectGet(obj, 'encrypted', dsz.TYPE_BOOL)[0]
                    except:
                        self.encrypted = None

                    try:
                        self.compressed = dsz.cmd.data.ObjectGet(obj, 'compressed', dsz.TYPE_BOOL)[0]
                    except:
                        self.compressed = None

                    try:
                        self.demand_load = dsz.cmd.data.ObjectGet(obj, 'demand_load', dsz.TYPE_BOOL)[0]
                    except:
                        self.demand_load = None

                    try:
                        self.service_key = dsz.cmd.data.ObjectGet(obj, 'service_key', dsz.TYPE_BOOL)[0]
                    except:
                        self.service_key = None

                    try:
                        self.user_mode = dsz.cmd.data.ObjectGet(obj, 'user_mode', dsz.TYPE_BOOL)[0]
                    except:
                        self.user_mode = None

                    try:
                        self.kernel_driver = dsz.cmd.data.ObjectGet(obj, 'kernel_driver', dsz.TYPE_BOOL)[0]
                    except:
                        self.kernel_driver = None

                    try:
                        self.boot_start = dsz.cmd.data.ObjectGet(obj, 'boot_start', dsz.TYPE_BOOL)[0]
                    except:
                        self.boot_start = None

                    try:
                        self.auto_start_once = dsz.cmd.data.ObjectGet(obj, 'auto_start_once', dsz.TYPE_BOOL)[0]
                    except:
                        self.auto_start_once = None

                    try:
                        self.system_start = dsz.cmd.data.ObjectGet(obj, 'system_start', dsz.TYPE_BOOL)[0]
                    except:
                        self.system_start = None

                    try:
                        self.auto_start = dsz.cmd.data.ObjectGet(obj, 'auto_start', dsz.TYPE_BOOL)[0]
                    except:
                        self.auto_start = None

                    try:
                        self.system_mode = dsz.cmd.data.ObjectGet(obj, 'system_mode', dsz.TYPE_BOOL)[0]
                    except:
                        self.system_mode = None

                    try:
                        self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_INT)[0]
                    except:
                        self.value = None

                    return

            class Hash(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.sha1 = dsz.cmd.data.ObjectGet(obj, 'sha1', dsz.TYPE_STRING)[0]
                    except:
                        self.sha1 = None

                    return


dsz.data.RegisterCommand('KiSu_Config', KiSu_Config)
KISU_CONFIG = KiSu_Config
kisu_config = KiSu_Config

class KiSu_List(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.Enumeration = KiSu_List.Enumeration(dsz.cmd.data.Get('Enumeration', dsz.TYPE_OBJECT)[0])
        except:
            self.Enumeration = None

        return

    class Enumeration(dsz.data.DataBean):

        def __init__(self, obj):
            self.Item = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Item', dsz.TYPE_OBJECT):
                    self.Item.append(KiSu_List.Enumeration.Item(x))

            except:
                pass

        class Item(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
                except:
                    self.Id = None

                try:
                    self.VersionMajor = dsz.cmd.data.ObjectGet(obj, 'VersionMajor', dsz.TYPE_INT)[0]
                except:
                    self.VersionMajor = None

                try:
                    self.VersionMinor = dsz.cmd.data.ObjectGet(obj, 'VersionMinor', dsz.TYPE_INT)[0]
                except:
                    self.VersionMinor = None

                try:
                    self.VersionFix = dsz.cmd.data.ObjectGet(obj, 'VersionFix', dsz.TYPE_INT)[0]
                except:
                    self.VersionFix = None

                try:
                    self.VersionBuild = dsz.cmd.data.ObjectGet(obj, 'VersionBuild', dsz.TYPE_INT)[0]
                except:
                    self.VersionBuild = None

                try:
                    self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
                except:
                    self.Name = None

                return


dsz.data.RegisterCommand('KiSu_List', KiSu_List)
KISU_LIST = KiSu_List
kisu_list = KiSu_List

class KiSu_LoadModule(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.LoadModule = KiSu_LoadModule.LoadModule(dsz.cmd.data.Get('LoadModule', dsz.TYPE_OBJECT)[0])
        except:
            self.LoadModule = None

        return

    class LoadModule(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
            except:
                self.Id = None

            try:
                self.Handle = dsz.cmd.data.ObjectGet(obj, 'Handle', dsz.TYPE_INT)[0]
            except:
                self.Handle = None

            try:
                self.Instance = dsz.cmd.data.ObjectGet(obj, 'Instance', dsz.TYPE_INT)[0]
            except:
                self.Instance = None

            return


dsz.data.RegisterCommand('KiSu_LoadModule', KiSu_LoadModule)
KISU_LOADMODULE = KiSu_LoadModule
kisu_loadmodule = KiSu_LoadModule

class KiSu_ReadModule(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.Module = KiSu_ReadModule.Module(dsz.cmd.data.Get('Module', dsz.TYPE_OBJECT)[0])
        except:
            self.Module = None

        return

    class Module(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.id = dsz.cmd.data.ObjectGet(obj, 'id', dsz.TYPE_INT)[0]
            except:
                self.id = None

            try:
                self.instance = dsz.cmd.data.ObjectGet(obj, 'instance', dsz.TYPE_INT)[0]
            except:
                self.instance = None

            try:
                self.size = dsz.cmd.data.ObjectGet(obj, 'size', dsz.TYPE_INT)[0]
            except:
                self.size = None

            try:
                self.module = dsz.cmd.data.ObjectGet(obj, 'module', dsz.TYPE_STRING)[0]
            except:
                self.module = None

            return


dsz.data.RegisterCommand('KiSu_ReadModule', KiSu_ReadModule)
KISU_READMODULE = KiSu_ReadModule
kisu_readmodule = KiSu_ReadModule