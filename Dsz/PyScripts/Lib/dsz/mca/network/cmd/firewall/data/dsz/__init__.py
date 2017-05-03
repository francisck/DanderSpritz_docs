# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Firewall(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.Enabled = Firewall.Enabled(dsz.cmd.data.Get('Enabled', dsz.TYPE_OBJECT)[0])
        except:
            self.Enabled = None

        try:
            self.Status = Firewall.Status(dsz.cmd.data.Get('Status', dsz.TYPE_OBJECT)[0])
        except:
            self.Status = None

        return

    class Enabled(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.closepending = dsz.cmd.data.ObjectGet(obj, 'closepending', dsz.TYPE_BOOL)[0]
            except:
                self.closepending = None

            try:
                self.port = dsz.cmd.data.ObjectGet(obj, 'port', dsz.TYPE_INT)[0]
            except:
                self.port = None

            try:
                self.protocol = dsz.cmd.data.ObjectGet(obj, 'protocol', dsz.TYPE_STRING)[0]
            except:
                self.protocol = None

            return

    class Status(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Domain = Firewall.Status.Domain(dsz.cmd.data.ObjectGet(obj, 'Domain', dsz.TYPE_OBJECT)[0])
            except:
                self.Domain = None

            try:
                self.Public = Firewall.Status.Public(dsz.cmd.data.ObjectGet(obj, 'Public', dsz.TYPE_OBJECT)[0])
            except:
                self.Public = None

            try:
                self.Private = Firewall.Status.Private(dsz.cmd.data.ObjectGet(obj, 'Private', dsz.TYPE_OBJECT)[0])
            except:
                self.Private = None

            try:
                self.Local = Firewall.Status.Local(dsz.cmd.data.ObjectGet(obj, 'Local', dsz.TYPE_OBJECT)[0])
            except:
                self.Local = None

            return

        class Domain(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.enabled = dsz.cmd.data.ObjectGet(obj, 'enabled', dsz.TYPE_BOOL)[0]
                except:
                    self.enabled = None

                try:
                    self.active = dsz.cmd.data.ObjectGet(obj, 'active', dsz.TYPE_BOOL)[0]
                except:
                    self.active = None

                try:
                    self.allowexceptions = dsz.cmd.data.ObjectGet(obj, 'allowexceptions', dsz.TYPE_BOOL)[0]
                except:
                    self.allowexceptions = None

                try:
                    self.inbound = dsz.cmd.data.ObjectGet(obj, 'inbound', dsz.TYPE_STRING)[0]
                except:
                    self.inbound = None

                try:
                    self.outbound = dsz.cmd.data.ObjectGet(obj, 'outbound', dsz.TYPE_STRING)[0]
                except:
                    self.outbound = None

                self.Port = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Port', dsz.TYPE_OBJECT):
                        self.Port.append(Firewall.Status.Domain.Port(x))

                except:
                    pass

                self.Application = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Application', dsz.TYPE_OBJECT):
                        self.Application.append(Firewall.Status.Domain.Application(x))

                except:
                    pass

                return

            class Port(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.port = dsz.cmd.data.ObjectGet(obj, 'port', dsz.TYPE_STRING)[0]
                    except:
                        self.port = None

                    try:
                        self.protocol = dsz.cmd.data.ObjectGet(obj, 'protocol', dsz.TYPE_STRING)[0]
                    except:
                        self.protocol = None

                    try:
                        self.scope = dsz.cmd.data.ObjectGet(obj, 'scope', dsz.TYPE_STRING)[0]
                    except:
                        self.scope = None

                    try:
                        self.status = dsz.cmd.data.ObjectGet(obj, 'status', dsz.TYPE_STRING)[0]
                    except:
                        self.status = None

                    try:
                        self.direction = dsz.cmd.data.ObjectGet(obj, 'direction', dsz.TYPE_STRING)[0]
                    except:
                        self.direction = None

                    try:
                        self.rule = dsz.cmd.data.ObjectGet(obj, 'rule', dsz.TYPE_STRING)[0]
                    except:
                        self.rule = None

                    try:
                        self.action = dsz.cmd.data.ObjectGet(obj, 'action', dsz.TYPE_STRING)[0]
                    except:
                        self.action = None

                    try:
                        self.portname = dsz.cmd.data.ObjectGet(obj, 'portname', dsz.TYPE_STRING)[0]
                    except:
                        self.portname = None

                    try:
                        self.group = dsz.cmd.data.ObjectGet(obj, 'group', dsz.TYPE_STRING)[0]
                    except:
                        self.group = None

                    return

            class Application(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.scope = dsz.cmd.data.ObjectGet(obj, 'scope', dsz.TYPE_STRING)[0]
                    except:
                        self.scope = None

                    try:
                        self.status = dsz.cmd.data.ObjectGet(obj, 'status', dsz.TYPE_STRING)[0]
                    except:
                        self.status = None

                    try:
                        self.direction = dsz.cmd.data.ObjectGet(obj, 'direction', dsz.TYPE_STRING)[0]
                    except:
                        self.direction = None

                    try:
                        self.programpath = dsz.cmd.data.ObjectGet(obj, 'programpath', dsz.TYPE_STRING)[0]
                    except:
                        self.programpath = None

                    try:
                        self.rule = dsz.cmd.data.ObjectGet(obj, 'rule', dsz.TYPE_STRING)[0]
                    except:
                        self.rule = None

                    try:
                        self.action = dsz.cmd.data.ObjectGet(obj, 'action', dsz.TYPE_STRING)[0]
                    except:
                        self.action = None

                    try:
                        self.programname = dsz.cmd.data.ObjectGet(obj, 'programname', dsz.TYPE_STRING)[0]
                    except:
                        self.programname = None

                    try:
                        self.group = dsz.cmd.data.ObjectGet(obj, 'group', dsz.TYPE_STRING)[0]
                    except:
                        self.group = None

                    return

        class Public(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.enabled = dsz.cmd.data.ObjectGet(obj, 'enabled', dsz.TYPE_BOOL)[0]
                except:
                    self.enabled = None

                try:
                    self.active = dsz.cmd.data.ObjectGet(obj, 'active', dsz.TYPE_BOOL)[0]
                except:
                    self.active = None

                try:
                    self.allowexceptions = dsz.cmd.data.ObjectGet(obj, 'allowexceptions', dsz.TYPE_BOOL)[0]
                except:
                    self.allowexceptions = None

                self.Port = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Port', dsz.TYPE_OBJECT):
                        self.Port.append(Firewall.Status.Public.Port(x))

                except:
                    pass

                self.Application = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Application', dsz.TYPE_OBJECT):
                        self.Application.append(Firewall.Status.Public.Application(x))

                except:
                    pass

                return

            class Port(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.port = dsz.cmd.data.ObjectGet(obj, 'port', dsz.TYPE_STRING)[0]
                    except:
                        self.port = None

                    try:
                        self.protocol = dsz.cmd.data.ObjectGet(obj, 'protocol', dsz.TYPE_STRING)[0]
                    except:
                        self.protocol = None

                    try:
                        self.scope = dsz.cmd.data.ObjectGet(obj, 'scope', dsz.TYPE_STRING)[0]
                    except:
                        self.scope = None

                    try:
                        self.status = dsz.cmd.data.ObjectGet(obj, 'status', dsz.TYPE_STRING)[0]
                    except:
                        self.status = None

                    try:
                        self.direction = dsz.cmd.data.ObjectGet(obj, 'direction', dsz.TYPE_STRING)[0]
                    except:
                        self.direction = None

                    try:
                        self.rule = dsz.cmd.data.ObjectGet(obj, 'rule', dsz.TYPE_STRING)[0]
                    except:
                        self.rule = None

                    try:
                        self.action = dsz.cmd.data.ObjectGet(obj, 'action', dsz.TYPE_STRING)[0]
                    except:
                        self.action = None

                    try:
                        self.portname = dsz.cmd.data.ObjectGet(obj, 'portname', dsz.TYPE_STRING)[0]
                    except:
                        self.portname = None

                    try:
                        self.group = dsz.cmd.data.ObjectGet(obj, 'group', dsz.TYPE_STRING)[0]
                    except:
                        self.group = None

                    return

            class Application(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.scope = dsz.cmd.data.ObjectGet(obj, 'scope', dsz.TYPE_STRING)[0]
                    except:
                        self.scope = None

                    try:
                        self.status = dsz.cmd.data.ObjectGet(obj, 'status', dsz.TYPE_STRING)[0]
                    except:
                        self.status = None

                    try:
                        self.direction = dsz.cmd.data.ObjectGet(obj, 'direction', dsz.TYPE_STRING)[0]
                    except:
                        self.direction = None

                    try:
                        self.programpath = dsz.cmd.data.ObjectGet(obj, 'programpath', dsz.TYPE_STRING)[0]
                    except:
                        self.programpath = None

                    try:
                        self.rule = dsz.cmd.data.ObjectGet(obj, 'rule', dsz.TYPE_STRING)[0]
                    except:
                        self.rule = None

                    try:
                        self.action = dsz.cmd.data.ObjectGet(obj, 'action', dsz.TYPE_STRING)[0]
                    except:
                        self.action = None

                    try:
                        self.programname = dsz.cmd.data.ObjectGet(obj, 'programname', dsz.TYPE_STRING)[0]
                    except:
                        self.programname = None

                    try:
                        self.group = dsz.cmd.data.ObjectGet(obj, 'group', dsz.TYPE_STRING)[0]
                    except:
                        self.group = None

                    return

        class Private(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.enabled = dsz.cmd.data.ObjectGet(obj, 'enabled', dsz.TYPE_BOOL)[0]
                except:
                    self.enabled = None

                try:
                    self.active = dsz.cmd.data.ObjectGet(obj, 'active', dsz.TYPE_BOOL)[0]
                except:
                    self.active = None

                try:
                    self.allowexceptions = dsz.cmd.data.ObjectGet(obj, 'allowexceptions', dsz.TYPE_BOOL)[0]
                except:
                    self.allowexceptions = None

                self.Port = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Port', dsz.TYPE_OBJECT):
                        self.Port.append(Firewall.Status.Private.Port(x))

                except:
                    pass

                self.Application = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Application', dsz.TYPE_OBJECT):
                        self.Application.append(Firewall.Status.Private.Application(x))

                except:
                    pass

                return

            class Port(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.port = dsz.cmd.data.ObjectGet(obj, 'port', dsz.TYPE_STRING)[0]
                    except:
                        self.port = None

                    try:
                        self.protocol = dsz.cmd.data.ObjectGet(obj, 'protocol', dsz.TYPE_STRING)[0]
                    except:
                        self.protocol = None

                    try:
                        self.scope = dsz.cmd.data.ObjectGet(obj, 'scope', dsz.TYPE_STRING)[0]
                    except:
                        self.scope = None

                    try:
                        self.status = dsz.cmd.data.ObjectGet(obj, 'status', dsz.TYPE_STRING)[0]
                    except:
                        self.status = None

                    try:
                        self.direction = dsz.cmd.data.ObjectGet(obj, 'direction', dsz.TYPE_STRING)[0]
                    except:
                        self.direction = None

                    try:
                        self.rule = dsz.cmd.data.ObjectGet(obj, 'rule', dsz.TYPE_STRING)[0]
                    except:
                        self.rule = None

                    try:
                        self.action = dsz.cmd.data.ObjectGet(obj, 'action', dsz.TYPE_STRING)[0]
                    except:
                        self.action = None

                    try:
                        self.portname = dsz.cmd.data.ObjectGet(obj, 'portname', dsz.TYPE_STRING)[0]
                    except:
                        self.portname = None

                    try:
                        self.group = dsz.cmd.data.ObjectGet(obj, 'group', dsz.TYPE_STRING)[0]
                    except:
                        self.group = None

                    return

            class Application(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.scope = dsz.cmd.data.ObjectGet(obj, 'scope', dsz.TYPE_STRING)[0]
                    except:
                        self.scope = None

                    try:
                        self.status = dsz.cmd.data.ObjectGet(obj, 'status', dsz.TYPE_STRING)[0]
                    except:
                        self.status = None

                    try:
                        self.direction = dsz.cmd.data.ObjectGet(obj, 'direction', dsz.TYPE_STRING)[0]
                    except:
                        self.direction = None

                    try:
                        self.programpath = dsz.cmd.data.ObjectGet(obj, 'programpath', dsz.TYPE_STRING)[0]
                    except:
                        self.programpath = None

                    try:
                        self.rule = dsz.cmd.data.ObjectGet(obj, 'rule', dsz.TYPE_STRING)[0]
                    except:
                        self.rule = None

                    try:
                        self.action = dsz.cmd.data.ObjectGet(obj, 'action', dsz.TYPE_STRING)[0]
                    except:
                        self.action = None

                    try:
                        self.programname = dsz.cmd.data.ObjectGet(obj, 'programname', dsz.TYPE_STRING)[0]
                    except:
                        self.programname = None

                    try:
                        self.group = dsz.cmd.data.ObjectGet(obj, 'group', dsz.TYPE_STRING)[0]
                    except:
                        self.group = None

                    return

        class Local(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.enabled = dsz.cmd.data.ObjectGet(obj, 'enabled', dsz.TYPE_BOOL)[0]
                except:
                    self.enabled = None

                try:
                    self.active = dsz.cmd.data.ObjectGet(obj, 'active', dsz.TYPE_BOOL)[0]
                except:
                    self.active = None

                try:
                    self.allowexceptions = dsz.cmd.data.ObjectGet(obj, 'allowexceptions', dsz.TYPE_BOOL)[0]
                except:
                    self.allowexceptions = None

                self.Port = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Port', dsz.TYPE_OBJECT):
                        self.Port.append(Firewall.Status.Local.Port(x))

                except:
                    pass

                self.Application = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Application', dsz.TYPE_OBJECT):
                        self.Application.append(Firewall.Status.Local.Application(x))

                except:
                    pass

                return

            class Port(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.port = dsz.cmd.data.ObjectGet(obj, 'port', dsz.TYPE_STRING)[0]
                    except:
                        self.port = None

                    try:
                        self.protocol = dsz.cmd.data.ObjectGet(obj, 'protocol', dsz.TYPE_STRING)[0]
                    except:
                        self.protocol = None

                    try:
                        self.scope = dsz.cmd.data.ObjectGet(obj, 'scope', dsz.TYPE_STRING)[0]
                    except:
                        self.scope = None

                    try:
                        self.status = dsz.cmd.data.ObjectGet(obj, 'status', dsz.TYPE_STRING)[0]
                    except:
                        self.status = None

                    try:
                        self.direction = dsz.cmd.data.ObjectGet(obj, 'direction', dsz.TYPE_STRING)[0]
                    except:
                        self.direction = None

                    try:
                        self.rule = dsz.cmd.data.ObjectGet(obj, 'rule', dsz.TYPE_STRING)[0]
                    except:
                        self.rule = None

                    try:
                        self.action = dsz.cmd.data.ObjectGet(obj, 'action', dsz.TYPE_STRING)[0]
                    except:
                        self.action = None

                    try:
                        self.portname = dsz.cmd.data.ObjectGet(obj, 'portname', dsz.TYPE_STRING)[0]
                    except:
                        self.portname = None

                    try:
                        self.group = dsz.cmd.data.ObjectGet(obj, 'group', dsz.TYPE_STRING)[0]
                    except:
                        self.group = None

                    return

            class Application(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.scope = dsz.cmd.data.ObjectGet(obj, 'scope', dsz.TYPE_STRING)[0]
                    except:
                        self.scope = None

                    try:
                        self.status = dsz.cmd.data.ObjectGet(obj, 'status', dsz.TYPE_STRING)[0]
                    except:
                        self.status = None

                    try:
                        self.direction = dsz.cmd.data.ObjectGet(obj, 'direction', dsz.TYPE_STRING)[0]
                    except:
                        self.direction = None

                    try:
                        self.programpath = dsz.cmd.data.ObjectGet(obj, 'programpath', dsz.TYPE_STRING)[0]
                    except:
                        self.programpath = None

                    try:
                        self.rule = dsz.cmd.data.ObjectGet(obj, 'rule', dsz.TYPE_STRING)[0]
                    except:
                        self.rule = None

                    try:
                        self.action = dsz.cmd.data.ObjectGet(obj, 'action', dsz.TYPE_STRING)[0]
                    except:
                        self.action = None

                    try:
                        self.programname = dsz.cmd.data.ObjectGet(obj, 'programname', dsz.TYPE_STRING)[0]
                    except:
                        self.programname = None

                    try:
                        self.group = dsz.cmd.data.ObjectGet(obj, 'group', dsz.TYPE_STRING)[0]
                    except:
                        self.group = None

                    return


dsz.data.RegisterCommand('Firewall', Firewall)
FIREWALL = Firewall
firewall = Firewall