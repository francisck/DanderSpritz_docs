# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Help(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.Prefixes = Help.Prefixes(dsz.cmd.data.Get('Prefixes', dsz.TYPE_OBJECT)[0])
        except:
            self.Prefixes = None

        try:
            self.Commands = Help.Commands(dsz.cmd.data.Get('Commands', dsz.TYPE_OBJECT)[0])
        except:
            self.Commands = None

        return

    class Prefixes(dsz.data.DataBean):

        def __init__(self, obj):
            self.Prefix = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Prefix', dsz.TYPE_OBJECT):
                    self.Prefix.append(Help.Prefixes.Prefix(x))

            except:
                pass

        class Prefix(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
                except:
                    self.name = None

                return

    class Commands(dsz.data.DataBean):

        def __init__(self, obj):
            self.Command = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Command', dsz.TYPE_OBJECT):
                    self.Command.append(Help.Commands.Command(x))

            except:
                pass

        class Command(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
                except:
                    self.name = None

                try:
                    self.builtin = dsz.cmd.data.ObjectGet(obj, 'builtin', dsz.TYPE_BOOL)[0]
                except:
                    self.builtin = None

                try:
                    self.loaded = dsz.cmd.data.ObjectGet(obj, 'loaded', dsz.TYPE_BOOL)[0]
                except:
                    self.loaded = None

                return


dsz.data.RegisterCommand('Help', Help)
HELP = Help
help = Help