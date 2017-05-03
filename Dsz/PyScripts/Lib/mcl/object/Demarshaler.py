# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Demarshaler.py
_BIG_ENDIAN = 0
_LITTLE_ENDIAN = 1

class Demarshaler:
    BIG_ENDIAN = _BIG_ENDIAN
    LITTLE_ENDIAN = _LITTLE_ENDIAN

    def __init__(self, data=None):
        self.m_data = None
        self.m_onIndex = 0
        self.m_isValid = True
        if data != None:
            self.SetData(data)
        return

    def BytesLeft(self):
        return len(self.m_data) - self.m_onIndex

    def GetData(self, expectedSize=0, lengthBytes=4):
        import array
        if lengthBytes == 0:
            if expectedSize == 0:
                raise RuntimeError('Expected size must be specified if lengthBytes is zero')
            sLen = expectedSize
        elif lengthBytes == 1:
            sLen = self.GetU8()
        elif lengthBytes == 2:
            sLen = self.GetU16()
        elif lengthBytes == 4:
            sLen = self.GetU32()
        else:
            raise RuntimeError('Invalid lengthBytes (%u) specified for data demarshal' % lengthBytes)
        if expectedSize != 0 and sLen != expectedSize:
            raise RuntimeError("Length of data (%u) doesn't match expected size (%u)" % (sLen, expectedSize))
        if not self.m_isValid or self.BytesLeft() < sLen:
            self.m_isValid = False
            raise RuntimeError('Not enough data left for demarshal')
        data = array.array('B', self.m_data[self.m_onIndex:self.m_onIndex + sLen])
        self.m_onIndex += sLen
        return data

    def GetDataRemaining(self):
        import array
        if not self.m_isValid or self.BytesLeft() == 0:
            self.m_isValid = False
            raise RuntimeError('Not enough data left for demarshal')
        data = array.array('B', self.m_data[self.m_onIndex:self.m_onIndex + self.BytesLeft()])
        self.m_onIndex += self.BytesLeft()
        return data

    def GetBool(self):
        val = self.GetU8()
        if val == 0:
            return False
        else:
            return True

    def GetError(self, endian=_BIG_ENDIAN):
        return (
         self.GetU32(endian), self.GetU32(endian))

    def GetIndex(self):
        return self.m_onIndex

    def GetIpAddr(self, endian=_BIG_ENDIAN):
        import mcl.object.IpAddr
        type = self.GetU8()
        if type == mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV4:
            addr = self.GetU32(endian)
        elif type == mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV6:
            addr = self.GetData(expectedSize=16, lengthBytes=0)
            scope_id = self.GetU32(endian)
        else:
            raise RuntimeError('Demarshal of IpAddr type returned unexpected value')
        ipaddr = mcl.object.IpAddr.IpAddr()
        ipaddr.SetAddr(type, addr)
        if type == mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV6:
            ipaddr.SetScopeId(scope_id)
        return ipaddr

    def GetStringUtf8(self):
        strArray = self.GetData()
        if len(strArray) == 0:
            return ''
        if strArray[len(strArray) - 1] != 0:
            self.m_isValid = False
            raise RuntimeError('String to demarshal is not NULL-terminated')
        cList = list()
        for val in strArray:
            if val == 0:
                break
            cList.append(chr(val))

        return ''.join(cList)

    def GetTime(self, endian=_BIG_ENDIAN):
        import mcl.object.MclTime
        seconds = self.GetS64(endian)
        nanoseconds = self.GetU64(endian)
        type = self.GetU8()
        return mcl.object.MclTime.MclTime(seconds, nanoseconds, type)

    def GetU8(self):
        if not self.m_isValid or self.BytesLeft() < 1:
            self.m_isValid = False
            raise RuntimeError('Not enough data left for demarshal')
        val = self.m_data[self.m_onIndex]
        self.m_onIndex = self.m_onIndex + 1
        return val

    def GetS8(self):
        val = self.GetU8()
        if val & 128:
            val = (val & 127) - 128
        return val

    def GetU16(self, endian=_BIG_ENDIAN):
        if not self.m_isValid or self.BytesLeft() < 2:
            self.m_isValid = False
            raise RuntimeError('Not enough data left for demarshal')
        if endian == _BIG_ENDIAN:
            val = self.m_data[self.m_onIndex] << 8 | self.m_data[self.m_onIndex + 1]
        else:
            val = self.m_data[self.m_onIndex] | self.m_data[self.m_onIndex + 1] << 8
        self.m_onIndex = self.m_onIndex + 2
        return val

    def GetS16(self, endian=_BIG_ENDIAN):
        val = self.GetU16(endian)
        if val & 32768:
            val = (val & 32767) - 32768
        return val

    def GetU32(self, endian=_BIG_ENDIAN):
        if not self.m_isValid or self.BytesLeft() < 4:
            self.m_isValid = False
            raise RuntimeError('Not enough data left for demarshal')
        if endian == _BIG_ENDIAN:
            val = self.m_data[self.m_onIndex] << 24 | self.m_data[self.m_onIndex + 1] << 16 | self.m_data[self.m_onIndex + 2] << 8 | self.m_data[self.m_onIndex + 3]
        else:
            val = self.m_data[self.m_onIndex] | self.m_data[self.m_onIndex + 1] << 8 | self.m_data[self.m_onIndex + 2] << 16 | self.m_data[self.m_onIndex + 3] << 24
        self.m_onIndex = self.m_onIndex + 4
        return val

    def GetS32(self, endian=_BIG_ENDIAN):
        val = self.GetU32(endian)
        if val & 2147483648L:
            val = (val & 2147483647) - 2147483648L
        return val

    def GetU64(self, endian=_BIG_ENDIAN):
        if not self.m_isValid or self.BytesLeft() < 8:
            self.m_isValid = False
            raise RuntimeError('Not enough data left for demarshal')
        if endian == _BIG_ENDIAN:
            val = self.m_data[self.m_onIndex] << 56 | self.m_data[self.m_onIndex + 1] << 48 | self.m_data[self.m_onIndex + 2] << 40 | self.m_data[self.m_onIndex + 3] << 32 | self.m_data[self.m_onIndex + 4] << 24 | self.m_data[self.m_onIndex + 5] << 16 | self.m_data[self.m_onIndex + 6] << 8 | self.m_data[self.m_onIndex + 7]
        else:
            val = self.m_data[self.m_onIndex] | self.m_data[self.m_onIndex + 1] << 8 | self.m_data[self.m_onIndex + 2] << 16 | self.m_data[self.m_onIndex + 3] << 24 | self.m_data[self.m_onIndex + 4] << 32 | self.m_data[self.m_onIndex + 5] << 40 | self.m_data[self.m_onIndex + 6] << 48 | self.m_data[self.m_onIndex + 7] << 56
        self.m_onIndex = self.m_onIndex + 8
        return val

    def GetS64(self, endian=_BIG_ENDIAN):
        val = self.GetU64(endian)
        if val & 9223372036854775808L:
            val = (val & 9223372036854775807L) - 9223372036854775808L
        return val

    def IsValid(self):
        return self.m_isValid

    def Reset(self):
        self.m_onIndex = 0
        self.m_isValid = True

    def SetData(self, data):
        import array
        if not isinstance(data, array.array) or data.typecode != 'B':
            raise RuntimeError('data must be an array of unsigned chars')
        self.m_data = data
        self.m_onIndex = 0
        self.m_isValid = True

    def SetIndex(self, newIndex):
        self.m_onIndex = newIndex
        self.m_isValid = True

    def Size(self):
        return len(self.m_data)