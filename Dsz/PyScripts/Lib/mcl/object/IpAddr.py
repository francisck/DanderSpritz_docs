# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: IpAddr.py


class IpAddr:
    IPADDR_TYPE_IPV4 = 0
    IPADDR_TYPE_IPV6 = 1

    def __init__(self):
        import array
        self.m_ipv4 = 0
        self.m_ipv6 = array.array('B', (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0))
        self.m_type = self.IPADDR_TYPE_IPV4
        self.m_ipv6_scope_id = 0

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.m_type == self.IPADDR_TYPE_IPV4:
            return '%u.%u.%u.%u' % (self.m_ipv4 >> 24 & 255,
             self.m_ipv4 >> 16 & 255,
             self.m_ipv4 >> 8 & 255,
             self.m_ipv4 & 255)
        else:
            hextets = []
            i = 0
            while i < 16:
                hextets.append('%x' % (self.m_ipv6[i] << 8 | self.m_ipv6[i + 1]))
                i = i + 2

            if self.m_ipv6_scope_id != 0:
                return ':'.join(self._compress_hextets(hextets)) + '%%%u' % self.m_ipv6_scope_id
            return ':'.join(self._compress_hextets(hextets))

    def __copy__(self):
        x = IpAddr()
        x.m_ipv4 = self.m_ipv4
        x.m_ipv6 = self.m_ipv6
        x.m_type = self.m_type
        x.m_ipv6_scope_id = self.m_ipv6_scope_id
        return x

    def __deepcopy__(self, memo):
        import array
        x = IpAddr()
        x.m_ipv4 = self.m_ipv4
        x.m_ipv6 = array.array('B', self.m_ipv6)
        x.m_type = self.m_type
        x.m_ipv6_scope_id = self.m_ipv6_scope_id
        return x

    def CreateFromString(addrStr):
        obj = IpAddr()
        if addrStr.find(':') != -1:
            obj.SetAddr(IpAddr.IPADDR_TYPE_IPV6, _inet_pton6(addrStr))
        elif addrStr.find('.') != -1:
            obj.SetAddr(IpAddr.IPADDR_TYPE_IPV4, _inet_pton4(addrStr))
        else:
            raise RuntimeError('Invalid address string (%s)' % addrStr)
        return obj

    CreateFromString = staticmethod(CreateFromString)

    def GetType(self):
        return self.m_type

    def GetAddr(self):
        if self.m_type == self.IPADDR_TYPE_IPV4:
            return self.m_ipv4
        else:
            return self.m_ipv6

    def GetScopeId(self):
        return self.m_ipv6_scope_id

    def IsValid(self):
        if self.m_type != self.IPADDR_TYPE_IPV4 or self.m_ipv4 != 0:
            return True
        else:
            return False

    def SetAddr(self, type, addr):
        if type == self.IPADDR_TYPE_IPV4:
            if not isinstance(addr, (int, long)):
                raise RuntimeError("IPv4 address must be an 'int' or 'long'")
            self.m_ipv4 = addr
            self.m_type = self.IPADDR_TYPE_IPV4
        elif type == self.IPADDR_TYPE_IPV6:
            import array
            if not isinstance(addr, array.array):
                raise RuntimeError("IPv6 address must be a 16 byte 'array'")
            if len(addr) != 16:
                raise RuntimeError("IPv6 address must be a 16 byte 'array'")
            self.m_ipv6 = array.array('B', addr)
            self.m_type = self.IPADDR_TYPE_IPV6
        else:
            raise RuntimeError('Invalid address type specified')

    def SetScopeId(self, scope_id):
        self.m_ipv6_scope_id = scope_id

    def _compress_hextets(self, hextets):
        best_doublecolon_start = -1
        best_doublecolon_len = 0
        doublecolon_start = -1
        doublecolon_len = 0
        for index in range(len(hextets)):
            if hextets[index] == '0':
                doublecolon_len += 1
                if doublecolon_start == -1:
                    doublecolon_start = index
                if doublecolon_len > best_doublecolon_len:
                    best_doublecolon_len = doublecolon_len
                    best_doublecolon_start = doublecolon_start
            else:
                doublecolon_len = 0
                doublecolon_start = -1

        if best_doublecolon_len > 1:
            best_doublecolon_end = best_doublecolon_start + best_doublecolon_len
            if best_doublecolon_end == len(hextets):
                hextets += ['']
            hextets[best_doublecolon_start:best_doublecolon_end] = [
             '']
            if best_doublecolon_start == 0:
                hextets = [
                 ''] + hextets
        return hextets


def _inet_pton4(addrStr):
    parts = addrStr.split('.')
    if len(parts) != 4:
        raise ValueError('Invalid IPv4 address string')
    addr = 0
    for part in parts:
        val = int(part, 10)
        if val < 0 or val > 255:
            raise ValueError('Invalid IPv4 address string')
        addr = addr << 8 | val

    return addr


def _inet_pton6(addrStr):
    import array
    NS_INT16SZ = 2
    NS_INADDRSZ = 4
    NS_IN6ADDRSZ = 16
    addrChars = list(addrStr)
    addr = array.array('B', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    if addrChars[0] == ':' and addrChars[1] != ':':
        raise ValueError('Invalid IPv6 address string')
    if addrChars[0] == ':' and addrChars[1] == ':':
        addrChars = [
         '0'] + addrChars
    colonReadIndex = -1
    colonWriteIndex = -1
    xdigits = '0123456789abcdefABCDEF'
    readIndex = 0
    writeIndex = 0
    saw_xdigit = False
    val = 0
    for ch in addrChars:
        if xdigits.find(ch) != -1:
            val = val << 4
            val = val | int(ch, 16)
            if val > 65535:
                raise ValueError('Invalid IPv6 address string')
            saw_xdigit = True
            readIndex = readIndex + 1
            continue
        if ch == ':':
            colonReadIndex = readIndex + 1
            if not saw_xdigit:
                if colonWriteIndex != -1:
                    raise ValueError('Invalid IPv6 address string')
                colonWriteIndex = writeIndex
                readIndex = readIndex + 1
                continue
            if writeIndex + NS_INT16SZ > 16:
                raise ValueError('Invalid IPv6 address string')
            addr[writeIndex] = val >> 8 & 255
            writeIndex = writeIndex + 1
            addr[writeIndex] = val & 255
            writeIndex = writeIndex + 1
            saw_xdigit = False
            val = 0
            readIndex = readIndex + 1
            continue
        if ch == '.' and writeIndex + NS_INADDRSZ <= 16:
            try:
                addrChars[0:colonReadIndex] = []
                ipv4Str = ''.join(addrChars)
                ipv4Addr = _inet_pton4(ipv4Str)
                addr[writeIndex] = ipv4Addr >> 24 & 255
                writeIndex = writeIndex + 1
                addr[writeIndex] = ipv4Addr >> 16 & 255
                writeIndex = writeIndex + 1
                addr[writeIndex] = ipv4Addr >> 8 & 255
                writeIndex = writeIndex + 1
                addr[writeIndex] = ipv4Addr & 255
                writeIndex = writeIndex + 1
                saw_xdigit = False
                break
            except:
                raise

        raise ValueError('Invalid IPv6 address string')

    if saw_xdigit:
        if writeIndex + NS_INT16SZ > 16:
            raise ValueError('Invalid IPv6 address string')
        addr[writeIndex] = val >> 8 & 255
        writeIndex = writeIndex + 1
        addr[writeIndex] = val & 255
        writeIndex = writeIndex + 1
    if colonWriteIndex != -1:
        n = writeIndex - colonWriteIndex
        i = 1
        while i <= n:
            addr[16 - i] = addr[colonWriteIndex + n - i]
            addr[colonWriteIndex + n - i] = 0
            i = i + 1

        writeIndex = 16
    if writeIndex != 16:
        raise ValueError('Invalid IPv6 address string')
    return addr