# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Ifconfig(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.FixedDataItem = Ifconfig.FixedDataItem(dsz.cmd.data.Get('FixedDataItem', dsz.TYPE_OBJECT)[0])
        except:
            self.FixedDataItem = None

        self.InterfaceItem = list()
        try:
            for x in dsz.cmd.data.Get('InterfaceItem', dsz.TYPE_OBJECT):
                self.InterfaceItem.append(Ifconfig.InterfaceItem(x))

        except:
            pass

        return

    class FixedDataItem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.enableproxy = dsz.cmd.data.ObjectGet(obj, 'enableproxy', dsz.TYPE_BOOL)[0]
            except:
                self.enableproxy = None

            try:
                self.enablerouting = dsz.cmd.data.ObjectGet(obj, 'enablerouting', dsz.TYPE_BOOL)[0]
            except:
                self.enablerouting = None

            try:
                self.enabledns = dsz.cmd.data.ObjectGet(obj, 'enabledns', dsz.TYPE_BOOL)[0]
            except:
                self.enabledns = None

            try:
                self.domainname = dsz.cmd.data.ObjectGet(obj, 'domainname', dsz.TYPE_STRING)[0]
            except:
                self.domainname = None

            try:
                self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_STRING)[0]
            except:
                self.type = None

            try:
                self.hostname = dsz.cmd.data.ObjectGet(obj, 'hostname', dsz.TYPE_STRING)[0]
            except:
                self.hostname = None

            try:
                self.scopeid = dsz.cmd.data.ObjectGet(obj, 'scopeid', dsz.TYPE_STRING)[0]
            except:
                self.scopeid = None

            try:
                self.dnsservers = Ifconfig.FixedDataItem.dnsservers(dsz.cmd.data.ObjectGet(obj, 'dnsservers', dsz.TYPE_OBJECT)[0])
            except:
                self.dnsservers = None

            return

        class dnsservers(dsz.data.DataBean):

            def __init__(self, obj):
                self.dnsserver = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'dnsserver', dsz.TYPE_OBJECT):
                        self.dnsserver.append(Ifconfig.FixedDataItem.dnsservers.dnsserver(x))

                except:
                    pass

            class dnsserver(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.ip = dsz.cmd.data.ObjectGet(obj, 'ip', dsz.TYPE_STRING)[0]
                    except:
                        self.ip = None

                    return

    class InterfaceItem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.status = dsz.cmd.data.ObjectGet(obj, 'status', dsz.TYPE_STRING)[0]
            except:
                self.status = None

            try:
                self.dhcpenabled = dsz.cmd.data.ObjectGet(obj, 'dhcpenabled', dsz.TYPE_BOOL)[0]
            except:
                self.dhcpenabled = None

            try:
                self.enabled = dsz.cmd.data.ObjectGet(obj, 'enabled', dsz.TYPE_BOOL)[0]
            except:
                self.enabled = None

            try:
                self.enabledarp = dsz.cmd.data.ObjectGet(obj, 'enabledarp', dsz.TYPE_BOOL)[0]
            except:
                self.enabledarp = None

            try:
                self.havewins = dsz.cmd.data.ObjectGet(obj, 'havewins', dsz.TYPE_BOOL)[0]
            except:
                self.havewins = None

            try:
                self.mtu = dsz.cmd.data.ObjectGet(obj, 'mtu', dsz.TYPE_INT)[0]
            except:
                self.mtu = None

            try:
                self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_STRING)[0]
            except:
                self.type = None

            try:
                self.address = dsz.cmd.data.ObjectGet(obj, 'address', dsz.TYPE_STRING)[0]
            except:
                self.address = None

            try:
                self.description = dsz.cmd.data.ObjectGet(obj, 'description', dsz.TYPE_STRING)[0]
            except:
                self.description = None

            try:
                self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
            except:
                self.name = None

            try:
                self.DnsSuffix = dsz.cmd.data.ObjectGet(obj, 'DnsSuffix', dsz.TYPE_STRING)[0]
            except:
                self.DnsSuffix = None

            try:
                self.SubnetMask = dsz.cmd.data.ObjectGet(obj, 'SubnetMask', dsz.TYPE_STRING)[0]
            except:
                self.SubnetMask = None

            try:
                self.Gateway = Ifconfig.InterfaceItem.Gateway(dsz.cmd.data.ObjectGet(obj, 'Gateway', dsz.TYPE_OBJECT)[0])
            except:
                self.Gateway = None

            try:
                self.Lease = Ifconfig.InterfaceItem.Lease(dsz.cmd.data.ObjectGet(obj, 'Lease', dsz.TYPE_OBJECT)[0])
            except:
                self.Lease = None

            try:
                self.Dhcp = Ifconfig.InterfaceItem.Dhcp(dsz.cmd.data.ObjectGet(obj, 'Dhcp', dsz.TYPE_OBJECT)[0])
            except:
                self.Dhcp = None

            try:
                self.Wins = Ifconfig.InterfaceItem.Wins(dsz.cmd.data.ObjectGet(obj, 'Wins', dsz.TYPE_OBJECT)[0])
            except:
                self.Wins = None

            try:
                self.IpAddress = Ifconfig.InterfaceItem.IpAddress(dsz.cmd.data.ObjectGet(obj, 'IpAddress', dsz.TYPE_OBJECT)[0])
            except:
                self.IpAddress = None

            try:
                self.IpAddressV6 = Ifconfig.InterfaceItem.IpAddressV6(dsz.cmd.data.ObjectGet(obj, 'IpAddressV6', dsz.TYPE_OBJECT)[0])
            except:
                self.IpAddressV6 = None

            try:
                self.DnsServers = Ifconfig.InterfaceItem.DnsServers(dsz.cmd.data.ObjectGet(obj, 'DnsServers', dsz.TYPE_OBJECT)[0])
            except:
                self.DnsServers = None

            return

        class Gateway(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.ip = dsz.cmd.data.ObjectGet(obj, 'ip', dsz.TYPE_STRING)[0]
                except:
                    self.ip = None

                return

        class Lease(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.obtained = Ifconfig.InterfaceItem.Lease.obtained(dsz.cmd.data.ObjectGet(obj, 'obtained', dsz.TYPE_OBJECT)[0])
                except:
                    self.obtained = None

                try:
                    self.expires = Ifconfig.InterfaceItem.Lease.expires(dsz.cmd.data.ObjectGet(obj, 'expires', dsz.TYPE_OBJECT)[0])
                except:
                    self.expires = None

                return

            class obtained(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.time = dsz.cmd.data.ObjectGet(obj, 'time', dsz.TYPE_STRING)[0]
                    except:
                        self.time = None

                    try:
                        self.date = dsz.cmd.data.ObjectGet(obj, 'date', dsz.TYPE_STRING)[0]
                    except:
                        self.date = None

                    return

            class expires(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.time = dsz.cmd.data.ObjectGet(obj, 'time', dsz.TYPE_STRING)[0]
                    except:
                        self.time = None

                    try:
                        self.date = dsz.cmd.data.ObjectGet(obj, 'date', dsz.TYPE_STRING)[0]
                    except:
                        self.date = None

                    return

        class Dhcp(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.ip = dsz.cmd.data.ObjectGet(obj, 'ip', dsz.TYPE_STRING)[0]
                except:
                    self.ip = None

                return

        class Wins(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Primary = Ifconfig.InterfaceItem.Wins.Primary(dsz.cmd.data.ObjectGet(obj, 'Primary', dsz.TYPE_OBJECT)[0])
                except:
                    self.Primary = None

                try:
                    self.Secondary = Ifconfig.InterfaceItem.Wins.Secondary(dsz.cmd.data.ObjectGet(obj, 'Secondary', dsz.TYPE_OBJECT)[0])
                except:
                    self.Secondary = None

                return

            class Primary(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.ip = dsz.cmd.data.ObjectGet(obj, 'ip', dsz.TYPE_STRING)[0]
                    except:
                        self.ip = None

                    return

            class Secondary(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.ip = dsz.cmd.data.ObjectGet(obj, 'ip', dsz.TYPE_STRING)[0]
                    except:
                        self.ip = None

                    return

        class IpAddress(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.ip = dsz.cmd.data.ObjectGet(obj, 'ip', dsz.TYPE_STRING)[0]
                except:
                    self.ip = None

                return

        class IpAddressV6(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.ip = dsz.cmd.data.ObjectGet(obj, 'ip', dsz.TYPE_STRING)[0]
                except:
                    self.ip = None

                return

        class DnsServers(dsz.data.DataBean):

            def __init__(self, obj):
                self.DnsServer = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'DnsServer', dsz.TYPE_OBJECT):
                        self.DnsServer.append(Ifconfig.InterfaceItem.DnsServers.DnsServer(x))

                except:
                    pass

            class DnsServer(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.ip = dsz.cmd.data.ObjectGet(obj, 'ip', dsz.TYPE_STRING)[0]
                    except:
                        self.ip = None

                    return


dsz.data.RegisterCommand('Ifconfig', Ifconfig)
IFCONFIG = Ifconfig
ifconfig = Ifconfig