# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Plugins(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.Local = Plugins.Local(dsz.cmd.data.Get('Local', dsz.TYPE_OBJECT)[0])
        except:
            self.Local = None

        try:
            self.Remote = Plugins.Remote(dsz.cmd.data.Get('Remote', dsz.TYPE_OBJECT)[0])
        except:
            self.Remote = None

        return

    class Local(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.address = dsz.cmd.data.ObjectGet(obj, 'address', dsz.TYPE_STRING)[0]
            except:
                self.address = None

            self.Plugin = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Plugin', dsz.TYPE_OBJECT):
                    self.Plugin.append(Plugins.Local.Plugin(x))

            except:
                pass

            return

        class Plugin(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.core = dsz.cmd.data.ObjectGet(obj, 'core', dsz.TYPE_BOOL)[0]
                except:
                    self.core = None

                try:
                    self.ReallyLoaded = dsz.cmd.data.ObjectGet(obj, 'ReallyLoaded', dsz.TYPE_BOOL)[0]
                except:
                    self.ReallyLoaded = None

                try:
                    self.loadCount = dsz.cmd.data.ObjectGet(obj, 'loadCount', dsz.TYPE_INT)[0]
                except:
                    self.loadCount = None

                try:
                    self.id = dsz.cmd.data.ObjectGet(obj, 'id', dsz.TYPE_INT)[0]
                except:
                    self.id = None

                try:
                    self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
                except:
                    self.name = None

                try:
                    self.loaderInfo = dsz.cmd.data.ObjectGet(obj, 'loaderInfo', dsz.TYPE_STRING)[0]
                except:
                    self.loaderInfo = None

                self.RegisteredApis = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'RegisteredApis', dsz.TYPE_OBJECT):
                        self.RegisteredApis.append(Plugins.Local.Plugin.RegisteredApis(x))

                except:
                    pass

                self.AcquiredApis = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'AcquiredApis', dsz.TYPE_OBJECT):
                        self.AcquiredApis.append(Plugins.Local.Plugin.AcquiredApis(x))

                except:
                    pass

                try:
                    self.Version = Plugins.Local.Plugin.Version(dsz.cmd.data.ObjectGet(obj, 'Version', dsz.TYPE_OBJECT)[0])
                except:
                    self.Version = None

                return

            class RegisteredApis(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.interface = dsz.cmd.data.ObjectGet(obj, 'interface', dsz.TYPE_INT)[0]
                    except:
                        self.interface = None

                    try:
                        self.provider = dsz.cmd.data.ObjectGet(obj, 'provider', dsz.TYPE_INT)[0]
                    except:
                        self.provider = None

                    return

            class AcquiredApis(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.interface = dsz.cmd.data.ObjectGet(obj, 'interface', dsz.TYPE_INT)[0]
                    except:
                        self.interface = None

                    try:
                        self.provider = dsz.cmd.data.ObjectGet(obj, 'provider', dsz.TYPE_INT)[0]
                    except:
                        self.provider = None

                    try:
                        self.providedBy = dsz.cmd.data.ObjectGet(obj, 'providedBy', dsz.TYPE_STRING)[0]
                    except:
                        self.providedBy = None

                    return

            class Version(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Lla = Plugins.Local.Plugin.Version.Lla(dsz.cmd.data.ObjectGet(obj, 'Lla', dsz.TYPE_OBJECT)[0])
                    except:
                        self.Lla = None

                    try:
                        self.Module = Plugins.Local.Plugin.Version.Module(dsz.cmd.data.ObjectGet(obj, 'Module', dsz.TYPE_OBJECT)[0])
                    except:
                        self.Module = None

                    try:
                        self.BuildEnvironment = Plugins.Local.Plugin.Version.BuildEnvironment(dsz.cmd.data.ObjectGet(obj, 'BuildEnvironment', dsz.TYPE_OBJECT)[0])
                    except:
                        self.BuildEnvironment = None

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

                        try:
                            self.Revision = dsz.cmd.data.ObjectGet(obj, 'Revision', dsz.TYPE_INT)[0]
                        except:
                            self.Revision = None

                        return

                class Module(dsz.data.DataBean):

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
                            self.Revision = dsz.cmd.data.ObjectGet(obj, 'Revision', dsz.TYPE_INT)[0]
                        except:
                            self.Revision = None

                        try:
                            self.Flags = Plugins.Local.Plugin.Version.Module.Flags(dsz.cmd.data.ObjectGet(obj, 'Flags', dsz.TYPE_OBJECT)[0])
                        except:
                            self.Flags = None

                        return

                    class Flags(dsz.data.DataBean):

                        def __init__(self, obj):
                            try:
                                self.Value = dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_INT)[0]
                            except:
                                self.Value = None

                            try:
                                self.Target = dsz.cmd.data.ObjectGet(obj, 'Target', dsz.TYPE_BOOL)[0]
                            except:
                                self.Target = None

                            try:
                                self.Lp = dsz.cmd.data.ObjectGet(obj, 'Lp', dsz.TYPE_BOOL)[0]
                            except:
                                self.Lp = None

                            return

                class BuildEnvironment(dsz.data.DataBean):

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
                            self.Revision = dsz.cmd.data.ObjectGet(obj, 'Revision', dsz.TYPE_INT)[0]
                        except:
                            self.Revision = None

                        try:
                            self.TypeValue = dsz.cmd.data.ObjectGet(obj, 'TypeValue', dsz.TYPE_INT)[0]
                        except:
                            self.TypeValue = None

                        try:
                            self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                        except:
                            self.Type = None

                        return

    class Remote(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.address = dsz.cmd.data.ObjectGet(obj, 'address', dsz.TYPE_STRING)[0]
            except:
                self.address = None

            self.Plugin = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Plugin', dsz.TYPE_OBJECT):
                    self.Plugin.append(Plugins.Remote.Plugin(x))

            except:
                pass

            return

        class Plugin(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.core = dsz.cmd.data.ObjectGet(obj, 'core', dsz.TYPE_BOOL)[0]
                except:
                    self.core = None

                try:
                    self.ReallyLoaded = dsz.cmd.data.ObjectGet(obj, 'ReallyLoaded', dsz.TYPE_BOOL)[0]
                except:
                    self.ReallyLoaded = None

                try:
                    self.loadCount = dsz.cmd.data.ObjectGet(obj, 'loadCount', dsz.TYPE_INT)[0]
                except:
                    self.loadCount = None

                try:
                    self.id = dsz.cmd.data.ObjectGet(obj, 'id', dsz.TYPE_INT)[0]
                except:
                    self.id = None

                try:
                    self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
                except:
                    self.name = None

                try:
                    self.loaderInfo = dsz.cmd.data.ObjectGet(obj, 'loaderInfo', dsz.TYPE_STRING)[0]
                except:
                    self.loaderInfo = None

                self.RegisteredApis = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'RegisteredApis', dsz.TYPE_OBJECT):
                        self.RegisteredApis.append(Plugins.Remote.Plugin.RegisteredApis(x))

                except:
                    pass

                self.AcquiredApis = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'AcquiredApis', dsz.TYPE_OBJECT):
                        self.AcquiredApis.append(Plugins.Remote.Plugin.AcquiredApis(x))

                except:
                    pass

                try:
                    self.Version = Plugins.Remote.Plugin.Version(dsz.cmd.data.ObjectGet(obj, 'Version', dsz.TYPE_OBJECT)[0])
                except:
                    self.Version = None

                return

            class RegisteredApis(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.interface = dsz.cmd.data.ObjectGet(obj, 'interface', dsz.TYPE_INT)[0]
                    except:
                        self.interface = None

                    try:
                        self.provider = dsz.cmd.data.ObjectGet(obj, 'provider', dsz.TYPE_INT)[0]
                    except:
                        self.provider = None

                    return

            class AcquiredApis(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.interface = dsz.cmd.data.ObjectGet(obj, 'interface', dsz.TYPE_INT)[0]
                    except:
                        self.interface = None

                    try:
                        self.provider = dsz.cmd.data.ObjectGet(obj, 'provider', dsz.TYPE_INT)[0]
                    except:
                        self.provider = None

                    try:
                        self.providedBy = dsz.cmd.data.ObjectGet(obj, 'providedBy', dsz.TYPE_STRING)[0]
                    except:
                        self.providedBy = None

                    return

            class Version(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Lla = Plugins.Remote.Plugin.Version.Lla(dsz.cmd.data.ObjectGet(obj, 'Lla', dsz.TYPE_OBJECT)[0])
                    except:
                        self.Lla = None

                    try:
                        self.Module = Plugins.Remote.Plugin.Version.Module(dsz.cmd.data.ObjectGet(obj, 'Module', dsz.TYPE_OBJECT)[0])
                    except:
                        self.Module = None

                    try:
                        self.BuildEnvironment = Plugins.Remote.Plugin.Version.BuildEnvironment(dsz.cmd.data.ObjectGet(obj, 'BuildEnvironment', dsz.TYPE_OBJECT)[0])
                    except:
                        self.BuildEnvironment = None

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

                        try:
                            self.Revision = dsz.cmd.data.ObjectGet(obj, 'Revision', dsz.TYPE_INT)[0]
                        except:
                            self.Revision = None

                        return

                class Module(dsz.data.DataBean):

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
                            self.Revision = dsz.cmd.data.ObjectGet(obj, 'Revision', dsz.TYPE_INT)[0]
                        except:
                            self.Revision = None

                        try:
                            self.Flags = Plugins.Remote.Plugin.Version.Module.Flags(dsz.cmd.data.ObjectGet(obj, 'Flags', dsz.TYPE_OBJECT)[0])
                        except:
                            self.Flags = None

                        return

                    class Flags(dsz.data.DataBean):

                        def __init__(self, obj):
                            try:
                                self.Value = dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_INT)[0]
                            except:
                                self.Value = None

                            try:
                                self.Target = dsz.cmd.data.ObjectGet(obj, 'Target', dsz.TYPE_BOOL)[0]
                            except:
                                self.Target = None

                            try:
                                self.Lp = dsz.cmd.data.ObjectGet(obj, 'Lp', dsz.TYPE_BOOL)[0]
                            except:
                                self.Lp = None

                            return

                class BuildEnvironment(dsz.data.DataBean):

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
                            self.Revision = dsz.cmd.data.ObjectGet(obj, 'Revision', dsz.TYPE_INT)[0]
                        except:
                            self.Revision = None

                        try:
                            self.TypeValue = dsz.cmd.data.ObjectGet(obj, 'TypeValue', dsz.TYPE_INT)[0]
                        except:
                            self.TypeValue = None

                        try:
                            self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                        except:
                            self.Type = None

                        return


dsz.data.RegisterCommand('Plugins', Plugins)
PLUGINS = Plugins
plugins = Plugins