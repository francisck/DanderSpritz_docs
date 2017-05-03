# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Arp(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.Entry = list()
        try:
            for x in dsz.cmd.data.Get('Entry', dsz.TYPE_OBJECT):
                self.Entry.append(Arp.Entry(x))

        except:
            pass

    class Entry(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.adapter = dsz.cmd.data.ObjectGet(obj, 'adapter', dsz.TYPE_STRING)[0]
            except:
                self.adapter = None

            try:
                self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_STRING)[0]
            except:
                self.type = None

            try:
                self.state = dsz.cmd.data.ObjectGet(obj, 'state', dsz.TYPE_STRING)[0]
            except:
                self.state = None

            try:
                self.ip = dsz.cmd.data.ObjectGet(obj, 'ip', dsz.TYPE_STRING)[0]
            except:
                self.ip = None

            try:
                self.ip = dsz.cmd.data.ObjectGet(obj, 'ip', dsz.TYPE_STRING)[0]
            except:
                self.ip = None

            try:
                self.mac = dsz.cmd.data.ObjectGet(obj, 'mac', dsz.TYPE_STRING)[0]
            except:
                self.mac = None

            try:
                self.IsRouter = dsz.cmd.data.ObjectGet(obj, 'IsRouter', dsz.TYPE_BOOL)[0]
            except:
                self.IsRouter = None

            try:
                self.IsUnreachable = dsz.cmd.data.ObjectGet(obj, 'IsUnreachable', dsz.TYPE_BOOL)[0]
            except:
                self.IsUnreachable = None

            return


dsz.data.RegisterCommand('Arp', Arp)
ARP = Arp
arp = Arp