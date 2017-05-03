# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: XmlCommandData.py


class XmlCommandData:
    CMD_DATA_VALUE_INVALID = 0
    CMD_DATA_VALUE_STRING = 1
    CMD_DATA_VALUE_UINT_8 = 2
    CMD_DATA_VALUE_UINT_16 = 3
    CMD_DATA_VALUE_UINT_32 = 4
    CMD_DATA_VALUE_INT_8 = 5
    CMD_DATA_VALUE_INT_16 = 6
    CMD_DATA_VALUE_INT_32 = 7
    CMD_DATA_VALUE_BOOL = 8
    CMD_DATA_VALUE_UINT_64 = 9
    CMD_DATA_VALUE_INT_64 = 10
    CMD_DATA_VALUE_BYTE_ARRAY = 11
    CMD_DATA_VALUE_DATE_TIME = 12
    CMD_DATA_VALUE_IPV4ADDR = 13
    CMD_DATA_VALUE_TIME = 14
    CMD_DATA_VALUE_IPV6ADDR = 15
    CMD_DATA_VALUE_IPADDR = 16
    CMD_DATA_VALUE_CPADDR = 17
    CMD_DATA_VALUE_CPCIDR = 18

    def __init__(self):
        import array
        from mcl.object.IpAddr import IpAddr
        from mcl.object.MclTime import MclTime
        self.m_intValue = 0
        self.m_boolValue = False
        self.m_dataType = self.CMD_DATA_VALUE_INVALID
        self.m_dataName = ''
        self.m_defaultValueStr = None
        self.m_defaultValueSet = False
        self.m_dataValueStr = None
        self.m_dataValueSet = False
        self.m_byteArray = array.array('B')
        self.m_ipAddr = IpAddr()
        self.m_dateTime = MclTime()
        return

    def __copy__(self):
        x = XmlCommandData()
        x.m_intValue = self.m_intValue
        x.m_boolValue = self.m_boolValue
        x.m_dataType = self.m_dataType
        x.m_dataName = self.m_dataName
        x.m_defaultValueStr = self.m_defaultValueStr
        x.m_defaultValueSet = self.m_defaultValueSet
        x.m_dataValueStr = self.m_dataValueStr
        x.m_dataValueSet = self.m_dataValueSet
        x.m_byteArray = self.m_byteArray
        x.m_ipAddr = self.m_ipAddr
        x.m_dateTime = self.m_dateTime
        return x

    def __deepcopy__(self, memo):
        import copy
        x = XmlCommandData()
        x.m_intValue = self.m_intValue
        x.m_boolValue = self.m_boolValue
        x.m_dataType = self.m_dataType
        x.m_dataName = copy.deepcopy(self.m_dataName)
        x.m_defaultValueStr = copy.deepcopy(self.m_defaultValueStr)
        x.m_defaultValueSet = self.m_defaultValueSet
        x.m_dataValueStr = copy.deepcopy(self.m_dataValueStr)
        x.m_dataValueSet = self.m_dataValueSet
        x.m_byteArray = copy.deepcopy(self.m_byteArray)
        x.m_ipAddr = copy.deepcopy(self.m_ipAddr)
        x.m_dateTime = copy.deepcopy(self.m_dateTime)
        return x

    def GetDataValue(self):
        import copy
        return copy.deepcopy(self.m_dataValueStr)

    def GetDefaultValue(self):
        import copy
        return copy.deepcopy(self.m_defaultValueStr)

    def GetName(self):
        return self.m_dataName

    def GetType(self):
        return self.m_dataType

    def IsDataSet(self):
        return self.m_dataValueSet

    def IsDefaultSet(self):
        return self.m_defaultValueSet

    def GetValue(self):
        if self.m_dataType == self.CMD_DATA_VALUE_STRING:
            return self.GetValueString()
        if self.m_dataType == self.CMD_DATA_VALUE_UINT_8:
            return self.GetValueU8()
        if self.m_dataType == self.CMD_DATA_VALUE_UINT_16:
            return self.GetValueU16()
        if self.m_dataType == self.CMD_DATA_VALUE_UINT_32:
            return self.GetValueU32()
        if self.m_dataType == self.CMD_DATA_VALUE_INT_8:
            return self.GetValueS8()
        if self.m_dataType == self.CMD_DATA_VALUE_INT_16:
            return self.GetValueS16()
        if self.m_dataType == self.CMD_DATA_VALUE_INT_32:
            return self.GetValueS32()
        if self.m_dataType == self.CMD_DATA_VALUE_BOOL:
            return self.GetValueBool()
        if self.m_dataType == self.CMD_DATA_VALUE_UINT_64:
            return self.GetValueU64()
        if self.m_dataType == self.CMD_DATA_VALUE_INT_64:
            return self.GetValueS64()
        if self.m_dataType == self.CMD_DATA_VALUE_BYTE_ARRAY:
            return self.GetValueByteArray()
        if self.m_dataType == self.CMD_DATA_VALUE_DATE_TIME:
            return self.GetValueTime()
        if self.m_dataType == self.CMD_DATA_VALUE_IPV4ADDR:
            return self.GetValueIpAddr()
        if self.m_dataType == self.CMD_DATA_VALUE_TIME:
            return self.GetValueTime()
        if self.m_dataType == self.CMD_DATA_VALUE_IPV6ADDR:
            return self.GetValueIpAddr()
        if self.m_dataType == self.CMD_DATA_VALUE_IPADDR:
            return self.GetValueIpAddr()
        if self.m_dataType == self.CMD_DATA_VALUE_CPADDR:
            return self.GetValueU32()
        if self.m_dataType == self.CMD_DATA_VALUE_CPCIDR:
            return self.GetValueU64()

    def GetValueU8(self):
        return self.m_intValue

    def GetValueS8(self):
        return self.m_intValue

    def GetValueU16(self):
        return self.m_intValue

    def GetValueS16(self):
        return self.m_intValue

    def GetValueU32(self):
        return self.m_intValue

    def GetValueS32(self):
        return self.m_intValue

    def GetValueU64(self):
        return self.m_intValue

    def GetValueS64(self):
        return self.m_intValue

    def GetValueBool(self):
        return self.m_boolValue

    def GetValueTime(self):
        return self.m_dateTime

    def GetValueByteArray(self):
        return self.m_byteArray

    def GetValueIpAddr(self):
        return self.m_ipAddr

    def GetValueString(self):
        if self.m_dataValueStr != None and len(self.m_dataValueStr) >= 2 and self.m_dataValueStr.startswith('"') and self.m_dataValueStr.endswith('"'):
            return self.m_dataValueStr[1:len(self.m_dataValueStr) - 1]
        else:
            return self.m_dataValueStr
            return

    def SetDefaultValue(self, value):
        if len(value) >= 2 and value.startswith('"') and value.endswith('"'):
            setValue = value[1:len(value) - 1]
        else:
            setValue = value
        self._StoreValue(setValue)
        self.m_defaultValueStr = value
        self.m_defaultValueSet = True

    def SetName(self, name):
        self.m_dataName = name

    def SetType(self, type):
        if type == 'int8_t':
            self.m_dataType = self.CMD_DATA_VALUE_INT_8
        elif type == 'uint8_t':
            self.m_dataType = self.CMD_DATA_VALUE_UINT_8
        elif type == 'int16_t':
            self.m_dataType = self.CMD_DATA_VALUE_INT_16
        elif type == 'uint16_t':
            self.m_dataType = self.CMD_DATA_VALUE_UINT_16
        elif type == 'int32_t':
            self.m_dataType = self.CMD_DATA_VALUE_INT_32
        elif type == 'uint32_t':
            self.m_dataType = self.CMD_DATA_VALUE_UINT_32
        elif type == 'int64_t':
            self.m_dataType = self.CMD_DATA_VALUE_INT_64
        elif type == 'uint64_t':
            self.m_dataType = self.CMD_DATA_VALUE_UINT_64
        elif type == 'bool':
            self.m_dataType = self.CMD_DATA_VALUE_BOOL
        elif type == 'string':
            self.m_dataType = self.CMD_DATA_VALUE_STRING
        elif type == 'bytearray':
            self.m_dataType = self.CMD_DATA_VALUE_BYTE_ARRAY
        elif type == 'datetime':
            self.m_dataType = self.CMD_DATA_VALUE_DATE_TIME
        elif type == 'ipv4addr':
            self.m_dataType = self.CMD_DATA_VALUE_IPV4ADDR
        elif type == 'ipv6addr':
            self.m_dataType = self.CMD_DATA_VALUE_IPV6ADDR
        elif type == 'ipaddr':
            self.m_dataType = self.CMD_DATA_VALUE_IPADDR
        elif type == 'time':
            self.m_dataType = self.CMD_DATA_VALUE_TIME
        elif type == 'cpaddr':
            self.m_dataType = self.CMD_DATA_VALUE_CPADDR
        elif type == 'cpcidr':
            self.m_dataType = self.CMD_DATA_VALUE_CPCIDR
        else:
            raise RuntimeError('Invalid type (%s)' % type)

    def SetValue(self, value):
        if len(value) >= 2 and value.startswith('"') and value.endswith('"'):
            setValue = value[1:len(value) - 1]
        else:
            setValue = value
        self._StoreValue(setValue)
        self.m_dataValueStr = value
        self.m_dataValueSet = True

    def _StoreValue(self, value):
        if self.m_dataType == self.CMD_DATA_VALUE_INT_8:
            intValue = int(value, 0)
            if intValue > 127 or intValue < -128:
                raise RuntimeError('Number (%s) outside of allowable range' % value)
            self.m_intValue = intValue
        elif self.m_dataType == self.CMD_DATA_VALUE_UINT_8:
            intValue = int(value, 0)
            if intValue > 255 or intValue < 0:
                raise RuntimeError('Number (%s) outside of allowable range' % value)
            self.m_intValue = intValue
        elif self.m_dataType == self.CMD_DATA_VALUE_INT_16:
            intValue = int(value, 0)
            if intValue > 32767 or intValue < -32768:
                raise RuntimeError('Number (%s) outside of allowable range' % value)
            self.m_intValue = intValue
        elif self.m_dataType == self.CMD_DATA_VALUE_UINT_16:
            intValue = int(value, 0)
            if intValue > 65535 or intValue < 0:
                raise RuntimeError('Number (%s) outside of allowable range' % value)
            self.m_intValue = intValue
        elif self.m_dataType == self.CMD_DATA_VALUE_INT_32:
            intValue = int(value, 0)
            if intValue > 2147483647 or intValue < -2147483648:
                raise RuntimeError('Number (%s) outside of allowable range' % value)
            self.m_intValue = intValue
        elif self.m_dataType == self.CMD_DATA_VALUE_UINT_32:
            intValue = int(value, 0)
            if intValue > 4294967295L or intValue < 0:
                raise RuntimeError('Number (%s) outside of allowable range' % value)
            self.m_intValue = intValue
        elif self.m_dataType == self.CMD_DATA_VALUE_INT_64:
            intValue = int(value, 0)
            if intValue > 9223372036854775807L or intValue < -9223372036854775808L:
                raise RuntimeError('Number (%s) outside of allowable range' % value)
            self.m_intValue = intValue
        elif self.m_dataType == self.CMD_DATA_VALUE_UINT_64:
            intValue = int(value, 0)
            if intValue > 18446744073709551615L or intValue < 0:
                raise RuntimeError('Number (%s) outside of allowable range' % value)
            self.m_intValue = intValue
        elif self.m_dataType == self.CMD_DATA_VALUE_BOOL:
            if value.lower() == 'true' or value.lower() == '1':
                self.m_boolValue = True
            elif value.lower() == 'false' or value.lower() == '0':
                self.m_boolValue = False
            else:
                raise RuntimeError('Invalid boolean value (%s)' % value)
        elif self.m_dataType == self.CMD_DATA_VALUE_BYTE_ARRAY:
            self.m_byteArray = array.array('B')
            if len(value) > 0:
                words = value.split()
                for word in words:
                    intValue = int(word, 16)
                    if intValue > 255 or intValue < 0:
                        raise RuntimeError('Invalid value (%s) for byte array' % word)
                    self.m_byteArray.append(intValue)

        elif self.m_dataType == self.CMD_DATA_VALUE_STRING:
            pass
        elif self.m_dataType == self.CMD_DATA_VALUE_DATE_TIME:
            import re
            from datetime import datetime
            m = re.match('(\\d{4})-(\\d{1,2})-(\\d{1,2})(?: (\\d{1,2})\\:(\\d{1,2})\\:(\\d{1,2}))?$', value)
            if m == None:
                raise RuntimeError('Invalid value (%s) for datetime (must be of the form YYYY-MM-DD [hh:mm:ss])' % value)
            year = int(m.group(1) if m.group(1) != None else 0)
            month = int(m.group(2) if m.group(2) != None else 0)
            day = int(m.group(3) if m.group(3) != None else 0)
            hour = int(m.group(4) if m.group(4) != None else 0)
            minute = int(m.group(5) if m.group(5) != None else 0)
            second = int(m.group(6) if m.group(6) != None else 0)
            micro = 0
            dt = datetime(year, month, day, hour, minute, second, micro)
            diff = dt - datetime.utcfromtimestamp(0)
            totalSeconds = diff.days * 3600 * 24 + diff.seconds
            from mcl.object.MclTime import MclTime
            self.m_dateTime = MclTime(seconds=totalSeconds, nanoseconds=micro * 1000, type=MclTime.MCL_TIME_TYPE_GMT)
        elif self.m_dataType == self.CMD_DATA_VALUE_TIME:
            import re
            m = re.match('(\\d+d)?(\\d+h)?(\\d+m(?!s))?(\\d+s)?(\\d+ms)?$', value)
            if m == None:
                raise RuntimeError('Invalid value (%s) for time (must be of the form [#d][#h][#m][#s][#ms])' % value)
            duration = {}
            duration['days'] = 0
            duration['hours'] = 0
            duration['minutes'] = 0
            duration['seconds'] = 0
            duration['milliseconds'] = 0
            duration['totalSeconds'] = 0
            i = 1
            while i <= 5:
                val = m.group(i)
                if val == None:
                    pass
                elif val.endswith('ms'):
                    duration['milliseconds'] = int(val.rstrip('ms'))
                elif val.endswith('d'):
                    duration['days'] = int(val.rstrip('d'))
                elif val.endswith('h'):
                    duration['hours'] = int(val.rstrip('h'))
                elif val.endswith('m'):
                    duration['minutes'] = int(val.rstrip('m'))
                elif val.endswith('s'):
                    duration['seconds'] = int(val.rstrip('s'))
                else:
                    return
                i = i + 1

            if duration['hours'] > 23:
                raise RuntimeError('Invalid hours (%u) given' % duration['hours'])
            if duration['minutes'] > 59:
                raise RuntimeError('Invalid minutes (%u) given' % duration['minutes'])
            if duration['seconds'] > 59:
                raise RuntimeError('Invalid seconds (%u) given' % duration['seconds'])
            if duration['milliseconds'] > 999:
                raise RuntimeError('Invalid milliseconds (%u) given' % duration['milliseconds'])
            totalSeconds = duration['days'] * 24 * 60 * 60 + duration['hours'] * 60 * 60 + duration['minutes'] * 60 + duration['seconds']
            from mcl.object.MclTime import MclTime
            self.m_dateTime = MclTime(seconds=totalSeconds, nanoseconds=duration['milliseconds'] * 1000000, type=MclTime.MCL_TIME_TYPE_DELTA)
        elif self.m_dataType == self.CMD_DATA_VALUE_IPV4ADDR:
            if value.find('.') == -1:
                raise RuntimeError('IPv4 address does not contain a . (%s)' % value)
            from mcl.object.IpAddr import IpAddr
            try:
                addr = IpAddr.CreateFromString(value)
            except:
                raise RuntimeError('Invalid IPv4 address (%s)' % value)

            if addr.GetType() != IpAddr.IPADDR_TYPE_IPV4:
                raise RuntimeError('Invalid IPv4 address (%s)' % value)
            self.m_ipAddr = addr
        elif self.m_dataType == self.CMD_DATA_VALUE_IPV6ADDR:
            if value.find(':') == -1:
                raise RuntimeError('IPv6 address does not contain a : (%s)' % value)
            from mcl.object.IpAddr import IpAddr
            try:
                addr = IpAddr.CreateFromString(value)
            except:
                raise RuntimeError('Invalid IPv6 address (%s)' % value)

            if addr.GetType() != IpAddr.IPADDR_TYPE_IPV6:
                raise RuntimeError('Invalid IPv6 address (%s)' % value)
            self.m_ipAddr = addr
        elif self.m_dataType == self.CMD_DATA_VALUE_IPADDR:
            if value.find('.') == -1 and value.find(':') == -1:
                raise RuntimeError('IP address does not contain a : or a . (%s)' % value)
            from mcl.object.IpAddr import IpAddr
            try:
                self.m_ipAddr = IpAddr.CreateFromString(value)
            except:
                raise RuntimeError('Invalid IP address (%s)' % value)

        elif self.m_dataType == self.CMD_DATA_VALUE_CPCIDR:
            loc = value.find('/')
            if loc == -1:
                raise RuntimeError("Invalid CPCidr value (%s) -- '/' not found" % value)
            addr = value[0:loc].lower()
            bits = value[loc + 1:]
            if addr == 'z0.0.0.0':
                addrValue = 0
            elif addr == 'z255.255.255.255':
                addrValue = 4294967295L
            else:
                import re
                m = re.match('z(\\d+)\\.(\\d+)\\.(\\d+)\\.(\\d+)$', addr)
                if m == None:
                    raise RuntimeError('Invalid CPCidr address value (%s)' % addr)
                val1 = int(m.group(1))
                val2 = int(m.group(2))
                val3 = int(m.group(3))
                val4 = int(m.group(4))
                if val1 < 0 or val1 > 255 or val2 < 0 or val2 > 255 or val3 < 0 or val3 > 255 or val4 < 0 or val4 > 255:
                    raise RuntimeError('Invalid CPCidr address value (%s)' % addr)
                addrValue = val1 << 24 | val2 << 16 | val3 << 8 | val4
            if bits == '0':
                maskValue = 0
            else:
                numBits = int(bits, 10)
                if numBits > 32:
                    raise RuntimeError('Bits value is too high (%u)' % numBits)
                maskValue = 0
                while numBits > 0:
                    maskValue |= 1 << 32 - numBits
                    numBits = numBits - 1

            self.m_intValue = patternValue << 32 | maskValue
        elif self.m_dataType == self.CMD_DATA_VALUE_CPADDR:
            import re
            m = re.match('z(\\d+)\\.(\\d+)\\.(\\d+)\\.(\\d+)$', addr)
            if m == None:
                raise RuntimeError('Invalid CP address value (%s)' % addr)
            val1 = int(m.group(1))
            val2 = int(m.group(2))
            val3 = int(m.group(3))
            val4 = int(m.group(4))
            if val1 < 0 or val1 > 255 or val2 < 0 or val2 > 255 or val3 < 0 or val3 > 255 or val4 < 0 or val4 > 255:
                raise RuntimeError('Invalid CP address value (%s)' % addr)
            self.m_intValue = val1 << 24 | val2 << 16 | val3 << 8 | val4
        else:
            raise RuntimeError('Invalid type (%u)' % self.m_dataType)
        return