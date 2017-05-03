# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Language(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.Languages = Language.Languages(dsz.cmd.data.Get('Languages', dsz.TYPE_OBJECT)[0])
        except:
            self.Languages = None

        return

    class Languages(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.LocaleLanguage = Language.Languages.LocaleLanguage(dsz.cmd.data.ObjectGet(obj, 'LocaleLanguage', dsz.TYPE_OBJECT)[0])
            except:
                self.LocaleLanguage = None

            try:
                self.InstalledLanguage = Language.Languages.InstalledLanguage(dsz.cmd.data.ObjectGet(obj, 'InstalledLanguage', dsz.TYPE_OBJECT)[0])
            except:
                self.InstalledLanguage = None

            try:
                self.UiLanguage = Language.Languages.UiLanguage(dsz.cmd.data.ObjectGet(obj, 'UiLanguage', dsz.TYPE_OBJECT)[0])
            except:
                self.UiLanguage = None

            try:
                self.OsLanguages = Language.Languages.OsLanguages(dsz.cmd.data.ObjectGet(obj, 'OsLanguages', dsz.TYPE_OBJECT)[0])
            except:
                self.OsLanguages = None

            return

        class LocaleLanguage(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Native = dsz.cmd.data.ObjectGet(obj, 'Native', dsz.TYPE_STRING)[0]
                except:
                    self.Native = None

                try:
                    self.English = dsz.cmd.data.ObjectGet(obj, 'English', dsz.TYPE_STRING)[0]
                except:
                    self.English = None

                try:
                    self.Value = dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_INT)[0]
                except:
                    self.Value = None

                return

        class InstalledLanguage(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Native = dsz.cmd.data.ObjectGet(obj, 'Native', dsz.TYPE_STRING)[0]
                except:
                    self.Native = None

                try:
                    self.English = dsz.cmd.data.ObjectGet(obj, 'English', dsz.TYPE_STRING)[0]
                except:
                    self.English = None

                try:
                    self.Value = dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_INT)[0]
                except:
                    self.Value = None

                return

        class UiLanguage(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Native = dsz.cmd.data.ObjectGet(obj, 'Native', dsz.TYPE_STRING)[0]
                except:
                    self.Native = None

                try:
                    self.English = dsz.cmd.data.ObjectGet(obj, 'English', dsz.TYPE_STRING)[0]
                except:
                    self.English = None

                try:
                    self.Value = dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_INT)[0]
                except:
                    self.Value = None

                return

        class OsLanguages(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.AvailableLanguages = dsz.cmd.data.ObjectGet(obj, 'AvailableLanguages', dsz.TYPE_INT)[0]
                except:
                    self.AvailableLanguages = None

                try:
                    self.OsFile = dsz.cmd.data.ObjectGet(obj, 'OsFile', dsz.TYPE_STRING)[0]
                except:
                    self.OsFile = None

                self.OsLanguage = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'OsLanguage', dsz.TYPE_OBJECT):
                        self.OsLanguage.append(Language.Languages.OsLanguages.OsLanguage(x))

                except:
                    pass

                return

            class OsLanguage(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.Native = dsz.cmd.data.ObjectGet(obj, 'Native', dsz.TYPE_STRING)[0]
                    except:
                        self.Native = None

                    try:
                        self.English = dsz.cmd.data.ObjectGet(obj, 'English', dsz.TYPE_STRING)[0]
                    except:
                        self.English = None

                    try:
                        self.Value = dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_INT)[0]
                    except:
                        self.Value = None

                    return


dsz.data.RegisterCommand('Language', Language)
LANGUAGE = Language
language = Language