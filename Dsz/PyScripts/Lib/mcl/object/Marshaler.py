# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Marshaler.py
_BIG_ENDIAN = 0
_LITTLE_ENDIAN = 1

class Marshaler:
    BIG_ENDIAN = _BIG_ENDIAN
    LITTLE_ENDIAN = _LITTLE_ENDIAN

    def __init__(self):
        self.Clear()

    def AddBool(self, truefalse):
        if truefalse:
            self.AddU8(1)
        else:
            self.AddU8(0)

    def AddData(self, buffer, includeSize=True):
        if includeSize:
            self.AddU32(len(buffer))
        if len(buffer) > 0:
            self.m_data.extend(buffer)

    def AddError(self, moduleError, osError, endian=_BIG_ENDIAN):
        self.AddU32(moduleError, endian)
        self.AddU32(osError, endian)

    def AddIpAddr(self, addr, endian=_BIG_ENDIAN):
        import mcl.object.IpAddr
        if not isinstance(addr, mcl.object.IpAddr.IpAddr):
            raise RuntimeError('addr must be of type mcl.object.IpAddr.IpAddr')
        self.AddU8(addr.GetType())
        if addr.GetType() == mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV4:
            self.AddU32(addr.GetAddr(), endian)
        elif addr.GetType() == mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV6:
            self.AddData(addr.GetAddr(), False)
            self.AddU32(addr.GetScopeId(), endian)
        else:
            raise RuntimeError("IpAddr type doesn't match any expected value")

    def AddString(self, str):
        if str == None:
            str = ''
        self.AddU32(len(str) + 1)
        for c in str:
            self.m_data.append(ord(c))

        self.m_data.append(0)
        return

    def AddS8(self, data):
        self.m_data.append(data & 255)

    def AddS16(self, data, endian=_BIG_ENDIAN):
        if endian == self.BIG_ENDIAN:
            self.m_data.append(data >> 8 & 255)
            self.m_data.append(data & 255)
        elif endian == self.LITTLE_ENDIAN:
            self.m_data.append(data & 255)
            self.m_data.append(data >> 8 & 255)
        else:
            raise RuntimeError('Invalid endian type (%u)' % endian)

    def AddS32(self, data, endian=_BIG_ENDIAN):
        if endian == self.BIG_ENDIAN:
            self.m_data.append(data >> 24 & 255)
            self.m_data.append(data >> 16 & 255)
            self.m_data.append(data >> 8 & 255)
            self.m_data.append(data & 255)
        elif endian == self.LITTLE_ENDIAN:
            self.m_data.append(data & 255)
            self.m_data.append(data >> 8 & 255)
            self.m_data.append(data >> 16 & 255)
            self.m_data.append(data >> 24 & 255)
        else:
            raise RuntimeError('Invalid endian type (%u)' % endian)

    def AddS64(self, data, endian=_BIG_ENDIAN):
        if endian == self.BIG_ENDIAN:
            self.m_data.append(data >> 56 & 255)
            self.m_data.append(data >> 48 & 255)
            self.m_data.append(data >> 40 & 255)
            self.m_data.append(data >> 32 & 255)
            self.m_data.append(data >> 24 & 255)
            self.m_data.append(data >> 16 & 255)
            self.m_data.append(data >> 8 & 255)
            self.m_data.append(data & 255)
        elif endian == self.LITTLE_ENDIAN:
            self.m_data.append(data & 255)
            self.m_data.append(data >> 8 & 255)
            self.m_data.append(data >> 16 & 255)
            self.m_data.append(data >> 24 & 255)
            self.m_data.append(data >> 32 & 255)
            self.m_data.append(data >> 40 & 255)
            self.m_data.append(data >> 48 & 255)
            self.m_data.append(data >> 56 & 255)
        else:
            raise RuntimeError('Invalid endian type (%u)' % endian)

    def AddTime(self, t, endian=_BIG_ENDIAN):
        import mcl.object.MclTime
        if not isinstance(t, mcl.object.MclTime.MclTime):
            raise RuntimeError('addr must be of type mcl.object.MclTime.MclTime')
        self.AddS64(t.GetSeconds(), endian)
        self.AddU64(t.GetNanoseconds(), endian)
        self.AddU8(t.GetTimeType())

    def AddU8(self, data):
        self.AddS8(data)

    def AddU16(self, data, endian=_BIG_ENDIAN):
        self.AddS16(data, endian)

    def AddU32(self, data, endian=_BIG_ENDIAN):
        self.AddS32(data, endian)

    def AddU64(self, data, endian=_BIG_ENDIAN):
        self.AddS64(data, endian)

    def Clear(self):
        import array
        self.m_data = array.array('B')

    def GetData(self):
        return self.m_data

    def GetSize(self):
        return len(self.m_data)

    def __str__(self):
        rtnStr = ''
        for b in self.m_data:
            if len(rtnStr) > 0:
                rtnStr += ' '
            rtnStr += '0x%02x' % b

        return rtnStr