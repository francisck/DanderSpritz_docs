# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: XmlOutput.py
import mcl.data.namespace.common

class XmlOutput:

    def __init__(self):
        self.Clear()

    def AddAttribute(self, attr, value):
        self.m_attributes[attr] = XmlOutput.CleanAttribute(value)

    def AddSubElement(self, name, namespace=''):
        if namespace == None or namespace == '':
            namespace = self.m_defaultNamespace
        sub = XmlOutput()
        sub.Start(name, namespace)
        sub.SetDefaultNamespace(self.m_defaultNamespace)
        self.m_subelements.append(sub)
        return sub

    def AddSubElementWithText(self, name, text, namespace=''):
        if namespace == None or namespace == '':
            namespace = self.m_defaultNamespace
        sub = XmlOutput()
        sub.Start(name, namespace)
        sub.SetDefaultNamespace(self.m_defaultNamespace)
        sub.SetText(text)
        self.m_subelements.append(sub)
        return

    def AddAddressIP(self, name, ipaddr=None, subnet=None):
        from mcl.object.IpAddr import IpAddr
        ipv4 = True
        ipStr = None
        if ipaddr != None:
            ipStr = ipaddr.__str__()
            if ipaddr.GetType() == IpAddr.IPADDR_TYPE_IPV6:
                ipv4 = False
        subnetStr = None
        if subnet != None:
            subnetStr = subnet.__str__()
            if subnet.GetType() == IpAddr.IPADDR_TYPE_IPV6:
                ipv4 = False
        if ipv4:
            self.AddAddressIPv4(name, ipStr, subnetStr)
        else:
            self.AddAddressIPv6(name, ipStr, subnetStr)
        return

    def AddAddressIPv4(self, name, ipaddrStr=None, subnetStr=None):
        sub = self.AddSubElement(name)
        if ipaddrStr != None:
            sub2 = sub.AddSubElement('IPv4Address', mcl.data.namespace.common.Name)
            sub2.AddNamespaceDefinition(mcl.data.namespace.common.Name, mcl.data.namespace.common.Path)
            sub2.SetText(ipaddrStr)
        if subnetStr != None:
            sub2 = sub.AddSubElement('IPv4SubnetMask', mcl.data.namespace.common.Name)
            sub2.AddNamespaceDefinition(mcl.data.namespace.common.Name, mcl.data.namespace.common.Path)
            sub2.SetText(subnetStr)
        return

    def AddAddressIPv6(self, name, ipaddrStr=None, subnetStr=None):
        sub = self.AddSubElement(name)
        if ipaddrStr != None:
            sub2 = sub.AddSubElement('IPv6Address', mcl.data.namespace.common.Name)
            sub2.AddNamespaceDefinition(mcl.data.namespace.common.Name, mcl.data.namespace.common.Path)
            sub2.SetText(ipaddrStr)
        if subnetStr != None:
            sub2 = sub.AddSubElement('IPv6SubnetMask', mcl.data.namespace.common.Name)
            sub2.AddNamespaceDefinition(mcl.data.namespace.common.Name, mcl.data.namespace.common.Path)
            sub2.SetText(subnetStr)
        return

    def AddAddressPhysical(self, name, physicalAddr, physicalAddrLen):
        if physicalAddrLen > 0:
            sub = self.AddSubElement(name)
            sub2 = sub.AddSubElement('MacAddress', mcl.data.namespace.common.Name)
            sub2.AddNamespaceDefinition(mcl.data.namespace.common.Name, mcl.data.namespace.common.Path)
            aList = list()
            i = 0
            while i < physicalAddrLen:
                aList.append('%02X' % physicalAddr[i])
                if i != physicalAddrLen - 1:
                    aList.append('-')
                i = i + 1

            sub2.SetText(''.join(aList))

    def AddNamespaceDefinition(self, nsName, nsPath):
        if len(nsName) > 0 and len(nsPath) > 0:
            self.m_namespaceDefs.append([nsName, nsPath])

    def AddTimeElement(self, name, t):
        from mcl.object.MclTime import MclTime
        type = t.GetTimeType()
        sub = self.AddSubElement(name, mcl.data.namespace.common.Name)
        sub.AddNamespaceDefinition(mcl.data.namespace.common.Name, mcl.data.namespace.common.Path)
        if type == MclTime.MCL_TIME_TYPE_INVALID:
            sub.AddAttribute('type', 'invalid')
        elif type == MclTime.MCL_TIME_TYPE_DELTA:
            sub.AddAttribute('type', 'delta')
        elif type == MclTime.MCL_TIME_TYPE_GMT:
            sub.AddAttribute('type', 'remotegmt')
        elif type == MclTime.MCL_TIME_TYPE_LOCAL:
            sub.AddAttribute('type', 'remotelocal')
        else:
            sub.AddAttribute('type', 'unknown')
        if type == MclTime.MCL_TIME_TYPE_DELTA:
            totalSeconds = t.GetSeconds()
            negative = False
            if t.GetSeconds() < 0:
                negative = True
                totalSeconds *= -1
            days = totalSeconds / 86400
            hours = totalSeconds / 3600 % 24
            minutes = totalSeconds / 60 % 60
            seconds = totalSeconds % 60
            sub.SetText('P%uDT%02uH%02uM%02u.%09uS' % (days, hours, minutes, seconds, t.GetNanoseconds()))
            if negative:
                sub.AddAttribute('negative', 'true')
        else:
            import datetime
            if type == MclTime.MCL_TIME_TYPE_INVALID:
                dt = datetime.datetime.utcfromtimestamp(0)
            else:
                try:
                    dt = datetime.datetime.utcfromtimestamp(t.GetSeconds())
                except:
                    dt = datetime.datetime.utcfromtimestamp(0)

            sub.SetText('%04u-%02u-%02uT%02u:%02u:%02u.%09u' % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, t.GetNanoseconds()))

    def Clear(self):
        self.m_subelements = []
        self.m_attributes = {}
        self.m_text = ''
        self.m_name = ''
        self.m_defaultNamespace = ''
        self.m_namespace = ''
        self.m_namespaceDefs = []

    def GetAttributes(self):
        if len(self.m_namespaceDefs) > 0:
            attribs = self.m_attributes.copy()
            for nsDef in self.m_namespaceDefs:
                attribs['xmlns:%s' % nsDef[0]] = XmlOutput.CleanString(nsDef[1])

            return attribs
        else:
            return self.m_attributes

    def GetDefaultNamespace(self):
        return self.m_defaultNamespace

    def GetName(self):
        return self.m_name

    def GetNamespace(self):
        return self.m_namespace

    def GetNamespaceDefs(self):
        return self.m_namespaceDefs

    def GetSubElements(self):
        return self.m_subelements

    def GetText(self):
        return self.m_text

    def GetXml(self, timestamp=True, indent=0):
        if self.m_name == None or len(self.m_name) == 0:
            raise RuntimeError('XML element name has not been set')
        xml = ''
        i = 0
        while i < indent:
            xml = xml + ' '
            i = i + 1

        if self.m_namespace != None and len(self.m_namespace) > 0:
            eName = '%s:%s' % (self.m_namespace, self.m_name)
        else:
            eName = self.m_name
        xml = xml + '<%s' % eName
        if timestamp:
            import datetime
            now = datetime.datetime.utcnow()
            self.AddAttribute('lptimestamp', '%04u-%02u-%02uT%02u:%02u:%02u' % (now.year, now.month, now.day, now.hour, now.minute, now.second))
        attrs = self.GetAttributes()
        for attrName in attrs.keys():
            xml = xml + " %s='%s'" % (attrName, attrs[attrName])

        if len(self.m_text) == 0 and len(self.m_subelements) == 0:
            xml = xml + '/>\n'
        else:
            xml = xml + '>%s' % self.m_text
            if len(self.m_subelements) > 0:
                xml = xml + '\n'
                for sub in self.m_subelements:
                    xml = xml + sub.GetXml(False, indent + 2)

                i = 0
                while i < indent:
                    xml = xml + ' '
                    i = i + 1

            xml = xml + '</%s>\n' % eName
        return xml

    def SetDefaultNamespace(self, namespace):
        self.m_defaultNamespace = namespace

    def SetText(self, text):
        self.m_text = XmlOutput.CleanText(text)

    def SetTextAsData(self, data):
        self.m_text = ''
        dataList = []
        for val in data:
            dataList.append('%02x' % val)

        self.m_text = ''.join(dataList)

    def Start(self, name, namespace=''):
        self.Clear()
        if namespace == None or namespace == '':
            namespace = self.m_defaultNamespace
        self.m_name = name
        self.m_namespace = namespace
        return

    def CleanAttribute(text):
        return XmlOutput.CleanString(text, bAttribute=True)

    def CleanText(text):
        return XmlOutput.CleanString(text, bText=True)

    def CleanString(text, bAttribute=False, bComment=False, bText=False):
        dataList = []
        text = unicode(text, 'utf-8')
        for char in text:
            if (bAttribute or bText) and char in '<':
                dataList.append('&lt;')
            elif (bAttribute or bText) and char in '>':
                dataList.append('&gt;')
            elif (bAttribute or bText) and char in '&':
                dataList.append('&amp;')
            elif bAttribute and char in '"':
                dataList.append('&quot;')
            elif bAttribute and char in "'":
                dataList.append('&apos;')
            elif char in '%%':
                dataList.append('%%')
            elif XmlOutput.IsBadCharacter(char):
                str = char.encode('utf-8')
                for s in str:
                    dataList.append('%%%02x' % ord(s))

            else:
                dataList.append(char.encode('utf-8'))

        return ''.join(dataList)

    def IsBadCharacter(c):
        try:
            val = ord(c)
        except:
            return True

        if val >= 0 and val <= 8:
            return True
        if val >= 11 and val <= 12:
            return True
        if val >= 14 and val <= 31:
            return True
        if val >= 127 and val <= 132:
            return True
        if val >= 134 and val <= 159:
            return True
        return False

    CleanAttribute = staticmethod(CleanAttribute)
    CleanString = staticmethod(CleanString)
    CleanText = staticmethod(CleanText)
    IsBadCharacter = staticmethod(IsBadCharacter)