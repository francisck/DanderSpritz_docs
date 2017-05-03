# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Version(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.VersionItem = Version.VersionItem(dsz.cmd.data.Get('VersionItem', dsz.TYPE_OBJECT)[0])
        except:
            self.VersionItem = None

        return

    class VersionItem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Implant = Version.VersionItem.Implant(dsz.cmd.data.ObjectGet(obj, 'Implant', dsz.TYPE_OBJECT)[0])
            except:
                self.Implant = None

            try:
                self.ListeningPost = Version.VersionItem.ListeningPost(dsz.cmd.data.ObjectGet(obj, 'ListeningPost', dsz.TYPE_OBJECT)[0])
            except:
                self.ListeningPost = None

            return

        class Implant(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Compiled = Version.VersionItem.Implant.Compiled(dsz.cmd.data.ObjectGet(obj, 'Compiled', dsz.TYPE_OBJECT)[0])
                except:
                    self.Compiled = None

                return

            class Compiled(dsz.data.DataBean):

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
                        self.fix = dsz.cmd.data.ObjectGet(obj, 'fix', dsz.TYPE_INT)[0]
                    except:
                        self.fix = None

                    return

        class ListeningPost(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Base = Version.VersionItem.ListeningPost.Base(dsz.cmd.data.ObjectGet(obj, 'Base', dsz.TYPE_OBJECT)[0])
                except:
                    self.Base = None

                try:
                    self.Compiled = Version.VersionItem.ListeningPost.Compiled(dsz.cmd.data.ObjectGet(obj, 'Compiled', dsz.TYPE_OBJECT)[0])
                except:
                    self.Compiled = None

                return

            class Base(dsz.data.DataBean):

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
                        self.fix = dsz.cmd.data.ObjectGet(obj, 'fix', dsz.TYPE_INT)[0]
                    except:
                        self.fix = None

                    try:
                        self.build = dsz.cmd.data.ObjectGet(obj, 'build', dsz.TYPE_INT)[0]
                    except:
                        self.build = None

                    try:
                        self.description = dsz.cmd.data.ObjectGet(obj, 'description', dsz.TYPE_STRING)[0]
                    except:
                        self.description = None

                    return

            class Compiled(dsz.data.DataBean):

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
                        self.fix = dsz.cmd.data.ObjectGet(obj, 'fix', dsz.TYPE_INT)[0]
                    except:
                        self.fix = None

                    return


dsz.data.RegisterCommand('Version', Version)
VERSION = Version
version = Version