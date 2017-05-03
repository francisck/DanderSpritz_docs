# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Message.py
CURRENT_VERSION = 0
MSG_TYPE_MASK = 31
MSG_TYPE_MODIFIER_MASK = 224
MSG_TYPE_INVALID = 0
MSG_TYPE_BOOL = 1
MSG_TYPE_U8 = 2
MSG_TYPE_U16 = 3
MSG_TYPE_U32 = 4
MSG_TYPE_U64 = 5
MSG_TYPE_S8 = 6
MSG_TYPE_S16 = 7
MSG_TYPE_S32 = 8
MSG_TYPE_S64 = 9
MSG_TYPE_BINARY = 10
MSG_TYPE_UTF8 = 11
MSG_TYPE_MSG = 12
MSG_TYPE_UTF16 = 13
MSG_TYPE_RESERVED = 31
MSG_TYPE_MODIFIER_LITTLE_ENDIAN = 0
MSG_TYPE_MODIFIER_BIG_ENDIAN = 128
MSG_TYPE_MODIFIER_SIZE_32 = 96
MSG_TYPE_MODIFIER_NATIVE_ENDIAN = MSG_TYPE_MODIFIER_LITTLE_ENDIAN
MSG_KEY_INVALID = 0
MSG_KEY_TASKING_METADATA = 4294901760L
MSG_KEY_TASKING_DATA = 4294901761L
MSG_KEY_TASKING_METADATA_TASK_ID = 4294901762L
MSG_KEY_TASKING_METADATA_ADDRESS = 4294901763L
MSG_KEY_TASKING_METADATA_PRIORITY = 4294901764L
MSG_KEY_TASKING_METADATA_FLAGS = 4294901765L
MSG_KEY_TASKING_METADATA_CMD_ID = 4294901766L
MSG_KEY_RESULT_ERROR = 4294905856L
MSG_KEY_RESULT_ERROR_MODULE = 4294905857L
MSG_KEY_RESULT_ERROR_OS = 4294905858L
MSG_KEY_RESULT_METADATA = 4294909952L
MSG_KEY_RESULT_METADATA_MSG_TYPE = 4294909953L
MSG_KEY_RESULT_METADATA_DATA_FLAGS = 4294909954L
MSG_KEY_RESULT_METADATA_STATUS = 4294909955L
MSG_KEY_RESULT_METADATA_ARCH = 4294909956L
MSG_KEY_RESULT_METADATA_OS = 4294909957L
MSG_KEY_RESULT_METADATA_OS_MAJOR = 4294909958L
MSG_KEY_RESULT_METADATA_OS_MINOR = 4294909959L
MSG_KEY_RESULT_METADATA_OS_REVISION = 4294909960L
MSG_KEY_RESULT_METADATA_TASK_ID = 4294909961L
MSG_KEY_RESULT_METADATA_COLLECT_TIME = 4294909962L
MSG_KEY_RESULT_METADATA_CMD_ID = 4294909963L
MSG_KEY_RESULT_DATA = 4294914048L

def IsBigEndian(type):
    if type & (MSG_TYPE_MODIFIER_LITTLE_ENDIAN | MSG_TYPE_MODIFIER_BIG_ENDIAN) == MSG_TYPE_MODIFIER_BIG_ENDIAN:
        return True
    else:
        return False


def IsLittleEndian(type):
    if type & (MSG_TYPE_MODIFIER_LITTLE_ENDIAN | MSG_TYPE_MODIFIER_BIG_ENDIAN) == MSG_TYPE_MODIFIER_LITTLE_ENDIAN:
        return True
    else:
        return False


def IsNativeEndianess(endianess):
    if endianess & (MSG_TYPE_MODIFIER_LITTLE_ENDIAN | MSG_TYPE_MODIFIER_BIG_ENDIAN) == MSG_TYPE_MODIFIER_NATIVE_ENDIAN:
        return True
    else:
        return False


class DemarshalMessage():

    def __init__(self, data=None):
        from mcl.object.Demarshaler import Demarshaler
        self.demarsh = Demarshaler()
        self.SetData(data)

    def __getitem__(self, index):
        onIndex = 0
        for key in self.m_cache.keys():
            for entry in self.m_cache[key]:
                if onIndex == index:
                    return {'key': entry['key'],'type': entry['type'],
                       'retrieved': entry['retrieved']
                       }
                onIndex = onIndex + 1

    def __iter__(self):
        self.onIndex = 0
        return self

    def next(self):
        if self.onIndex >= self.m_totalEntries:
            raise StopIteration
        else:
            entry = self.__getitem__(self.onIndex)
            self.onIndex = self.onIndex + 1
            return entry

    def FindBool(self, key, instance=-1):
        return self._GetCacheEntryData(key, MSG_TYPE_BOOL, instance)

    def FindData(self, key, type=MSG_TYPE_BINARY, instance=-1):
        return self._GetCacheEntryData(key, type, instance)

    def FindError(self, key, instance=-1):
        entry = self._GetCacheEntry(key, MSG_TYPE_BINARY, instance)
        self.demarsh.SetData(entry['data'])
        if IsBigEndian(entry['type']):
            endian = self.demarsh.BIG_ENDIAN
        else:
            endian = self.demarsh.LITTLE_ENDIAN
        errors = self.demarsh.GetError(endian)
        if self.demarsh.BytesLeft() != 0:
            if entry['retrieved'] == True:
                self.m_numRetrieved = self.m_numRetrieved - 1
            entry['retrieved'] = False
            raise RuntimeError('Failed to demarshal errors')
        return errors

    def FindMessage(self, key, instance=-1):
        return DemarshalMessage(self._GetCacheEntryData(key, MSG_TYPE_MSG, instance))

    def FindIpAddr(self, key, instance=-1):
        entry = self._GetCacheEntry(key, MSG_TYPE_BINARY, instance)
        self.demarsh.SetData(entry['data'])
        if IsBigEndian(entry['type']):
            endian = self.demarsh.BIG_ENDIAN
        else:
            endian = self.demarsh.LITTLE_ENDIAN
        ipAddr = self.demarsh.GetIpAddr(endian)
        if self.demarsh.BytesLeft() != 0:
            if entry['retrieved'] == True:
                self.m_numRetrieved = self.m_numRetrieved - 1
            entry['retrieved'] = False
            raise RuntimeError('Failed to demarshal IpAddr object')
        return ipAddr

    def FindS8(self, key, instance=-1):
        return self._GetCacheEntryData(key, MSG_TYPE_S8, instance)

    def FindS16(self, key, instance=-1):
        return self._GetCacheEntryData(key, MSG_TYPE_S16, instance)

    def FindS32(self, key, instance=-1):
        return self._GetCacheEntryData(key, MSG_TYPE_S32, instance)

    def FindS64(self, key, instance=-1):
        return self._GetCacheEntryData(key, MSG_TYPE_S64, instance)

    def FindString(self, key, instance=-1, encoding='utf-8', replace='backslashreplace'):
        entry = self.PeekByKey(key, instance)
        if entry == None:
            raise RuntimeError("Failed to find instance %d of key '0x%08x'" % (instance, key))
        if entry['type'] & MSG_TYPE_MASK == MSG_TYPE_UTF16:
            str = self.FindStringUtf16(key, instance)
            if encoding != None:
                return str.encode(encoding, replace)
            else:
                return str

        else:
            return self.FindStringUtf8(key, instance)
        return

    def FindStringUtf8(self, key, instance=-1):
        entry = self._GetCacheEntry(key, MSG_TYPE_UTF8, instance)
        strArray = entry['data']
        if len(strArray) == 0:
            return ''
        if strArray[len(strArray) - 1] != 0:
            if entry['retrieved'] == True:
                self.m_numRetrieved = self.m_numRetrieved - 1
            entry['retrieved'] = False
            raise RuntimeError('String to demarshal is not NULL-terminated')
        cList = list()
        for val in strArray:
            if val == 0:
                break
            cList.append(chr(val))

        return ''.join(cList)

    def FindStringUtf16(self, key, instance=-1):
        entry = self._GetCacheEntry(key, MSG_TYPE_UTF16, instance)
        if len(entry['data']) == 0:
            return u''
        cList = list()
        i = 0
        while i < len(entry['data']):
            if IsBigEndian(entry['type']):
                cList.append(unichr(entry['data'][i] << 8 | entry['data'][i + 1]))
            else:
                cList.append(unichr(entry['data'][i] | entry['data'][i + 1] << 8))
            i = i + 2

        if cList[len(cList) - 1] != u'\x00':
            if entry['retrieved'] == True:
                self.m_numRetrieved = self.m_numRetrieved - 1
            entry['retrieved'] = False
            raise RuntimeError('String to demarshal is not NULL-terminated')
        del cList[len(cList) - 1]
        return u''.join(cList)

    def FindTime(self, key, instance=-1):
        entry = self._GetCacheEntry(key, MSG_TYPE_BINARY, instance)
        self.demarsh.SetData(entry['data'])
        if IsBigEndian(entry['type']):
            endian = self.demarsh.BIG_ENDIAN
        else:
            endian = self.demarsh.LITTLE_ENDIAN
        t = self.demarsh.GetTime(endian)
        if self.demarsh.BytesLeft() != 0:
            if entry['retrieved'] == True:
                self.m_numRetrieved = self.m_numRetrieved - 1
            entry['retrieved'] = False
            raise RuntimeError('Failed to demarshal Time object')
        return t

    def FindU8(self, key, instance=-1):
        return self._GetCacheEntryData(key, MSG_TYPE_U8, instance)

    def FindU16(self, key, instance=-1):
        return self._GetCacheEntryData(key, MSG_TYPE_U16, instance)

    def FindU32(self, key, instance=-1):
        return self._GetCacheEntryData(key, MSG_TYPE_U32, instance)

    def FindU64(self, key, instance=-1):
        return self._GetCacheEntryData(key, MSG_TYPE_U64, instance)

    def GetCount(self, key=MSG_KEY_INVALID):
        if key == MSG_KEY_INVALID:
            return self.m_totalEntries
        else:
            if self.m_cache.has_key(key):
                return len(self.m_cache[key])
            return 0

    def GetNumRetrieved(self):
        return self.m_numRetrieved

    def PeekByKey(self, key, instance=-1):
        try:
            entry = self._FindCacheEntry(key, instance)
            return {'key': entry['key'],'type': entry['type']}
        except:
            return None

        return None

    def Reset(self, key=MSG_KEY_INVALID, instance=-1):
        if self.m_cache != None:
            if key == MSG_KEY_INVALID and instance < 0:
                self.m_cache = None
            elif instance < 0:
                for entry in self.m_cache:
                    if entry['key'] == key:
                        if entry['retrieved'] == True:
                            self.m_numRetrieved = self.m_numRetrieved - 1
                        entry['retrieved'] = False

            elif instance < len(self.m_cache):
                if key == MSG_KEY_INVALID or self.m_cache[instance]['key'] == key:
                    if self.m_cache[instance]['retrieved'] == True:
                        self.m_numRetrieved = self.m_numRetrieved - 1
                    self.m_cache[instance]['retrieved'] = False
        return

    def SetData(self, data):
        self.m_cache = dict()
        self.m_numRetrieved = 0
        self.m_totalEntries = 0
        if data != None:
            self._ParseData(data)
        return

    def _FindCacheEntry(self, key, instance):
        if key == MSG_KEY_INVALID:
            onInstance = 0
            for key in self.m_cache.keys():
                for entry in self.m_cache[key]:
                    if instance < 0:
                        if not entry['retrieved']:
                            return entry
                    else:
                        if instance == onInstance:
                            return entry
                        onInstance = onInstance + 1

        else:
            onInstance = 0
            if self.m_cache.has_key(key):
                for entry in self.m_cache[key]:
                    if instance < 0:
                        if not entry['retrieved']:
                            return entry
                    else:
                        if instance == onInstance:
                            return entry
                        onInstance = onInstance + 1

        raise RuntimeError("Failed to find instance %d of key '0x%08x'" % (instance, key))

    def _GetCacheEntry(self, key, type, instance):
        entry = self._FindCacheEntry(key, instance)
        if type != MSG_TYPE_INVALID:
            if entry['type'] & MSG_TYPE_MASK != type:
                raise RuntimeError('Instance %d of key 0x%08x is not the correct type (expected=%u found=%u)' % (instance, key, type, entry['type'] & MSG_TYPE_MASK))
        entry['retrieved'] = True
        self.m_numRetrieved = self.m_numRetrieved + 1
        return entry

    def _GetCacheEntryData(self, key, type, instance):
        entry = self._GetCacheEntry(key, type, instance)
        self.demarsh.SetData(entry['data'])
        baseType = entry['type'] & MSG_TYPE_MASK
        if IsBigEndian(type):
            endian = self.demarsh.BIG_ENDIAN
        else:
            endian = self.demarsh.LITTLE_ENDIAN
        if baseType == MSG_TYPE_BOOL:
            if self.demarsh.GetU8() == 0:
                return False
            else:
                return True

        else:
            if baseType == MSG_TYPE_U8:
                return self.demarsh.GetU8()
            if baseType == MSG_TYPE_S8:
                return self.demarsh.GetS8()
            if baseType == MSG_TYPE_U16:
                return self.demarsh.GetU16(endian)
            if baseType == MSG_TYPE_S16:
                return self.demarsh.GetS16(endian)
            if baseType == MSG_TYPE_U32:
                return self.demarsh.GetU32(endian)
            if baseType == MSG_TYPE_S32:
                return self.demarsh.GetS32(endian)
            if baseType == MSG_TYPE_U64:
                return self.demarsh.GetU64(endian)
            if baseType == MSG_TYPE_S64:
                return self.demarsh.GetS64(endian)
            return entry['data']

    def _ParseData(self, data):
        import array
        if data == None or len(data) == 0:
            self.m_cache = dict()
            return
        else:
            version = data[0]
            if version != CURRENT_VERSION:
                raise RuntimeError('Failed to get valid version from data')
            currentIndex = 1
            while currentIndex < len(data):
                entry = {'retrieved': False}
                entry['type'] = data[currentIndex]
                currentIndex = currentIndex + 1
                if IsBigEndian(entry['type']):
                    entry['key'] = data[currentIndex] << 24 | data[currentIndex + 1] << 16 | data[currentIndex + 2] << 8 | data[currentIndex + 3]
                else:
                    entry['key'] = data[currentIndex] | data[currentIndex + 1] << 8 | data[currentIndex + 2] << 16 | data[currentIndex + 3] << 24
                currentIndex = currentIndex + 4
                entry['data'] = array.array('B')
                baseType = entry['type'] & MSG_TYPE_MASK
                if baseType == MSG_TYPE_BOOL or baseType == MSG_TYPE_U8 or baseType == MSG_TYPE_S8:
                    entry['data'].append(data[currentIndex])
                    currentIndex = currentIndex + 1
                elif baseType == MSG_TYPE_U16 or baseType == MSG_TYPE_S16:
                    entry['data'].extend(data[currentIndex:currentIndex + 2])
                    currentIndex = currentIndex + 2
                elif baseType == MSG_TYPE_U32 or baseType == MSG_TYPE_S32:
                    entry['data'].extend(data[currentIndex:currentIndex + 4])
                    currentIndex = currentIndex + 4
                elif baseType == MSG_TYPE_U64 or baseType == MSG_TYPE_S64:
                    entry['data'].extend(data[currentIndex:currentIndex + 8])
                    currentIndex = currentIndex + 8
                else:
                    if entry['type'] & MSG_TYPE_MODIFIER_SIZE_32:
                        if IsBigEndian(entry['type']):
                            size = data[currentIndex] << 24 | data[currentIndex + 1] << 16 | data[currentIndex + 2] << 8 | data[currentIndex + 3]
                        else:
                            size = data[currentIndex] | data[currentIndex + 1] << 8 | data[currentIndex + 2] << 16 | data[currentIndex + 3] << 24
                        currentIndex = currentIndex + 4
                    else:
                        size = data[currentIndex]
                        currentIndex = currentIndex + 1
                    entry['data'].extend(data[currentIndex:currentIndex + size])
                    currentIndex = currentIndex + size
                if not self.m_cache.has_key(entry['key']):
                    self.m_cache[entry['key']] = list()
                self.m_cache[entry['key']].append(entry)
                self.m_totalEntries = self.m_totalEntries + 1

            return


class MarshalMessage():

    def __init__(self):
        from mcl.object.Marshaler import Marshaler
        self.m_marsh = Marshaler()

    def Add(self, type, key, data, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        endianess &= MSG_TYPE_MODIFIER_BIG_ENDIAN | MSG_TYPE_MODIFIER_LITTLE_ENDIAN
        if IsBigEndian(endianess):
            marshalEndian = self.m_marsh.BIG_ENDIAN
        else:
            marshalEndian = self.m_marsh.LITTLE_ENDIAN
        type |= endianess
        if self.m_marsh.GetSize() == 0:
            self.m_marsh.AddU8(CURRENT_VERSION)
        if type & MSG_TYPE_MASK == MSG_TYPE_BOOL or type & MSG_TYPE_MASK == MSG_TYPE_U8 or type & MSG_TYPE_MASK == MSG_TYPE_S8:
            self.m_marsh.AddU8(type)
            self.m_marsh.AddU32(key, marshalEndian)
            self.m_marsh.AddU8(data)
        elif type & MSG_TYPE_MASK == MSG_TYPE_U16 or type & MSG_TYPE_MASK == MSG_TYPE_S16:
            self.m_marsh.AddU8(type)
            self.m_marsh.AddU32(key, marshalEndian)
            self.m_marsh.AddU16(data, marshalEndian)
        elif type & MSG_TYPE_MASK == MSG_TYPE_U32 or type & MSG_TYPE_MASK == MSG_TYPE_S32:
            self.m_marsh.AddU8(type)
            self.m_marsh.AddU32(key, marshalEndian)
            self.m_marsh.AddU32(data, marshalEndian)
        elif type & MSG_TYPE_MASK == MSG_TYPE_U64 or type & MSG_TYPE_MASK == MSG_TYPE_S64:
            self.m_marsh.AddU8(type)
            self.m_marsh.AddU32(key, marshalEndian)
            self.m_marsh.AddU64(data, marshalEndian)
        elif type & MSG_TYPE_MASK == MSG_TYPE_UTF16:
            fullLen = (len(data) + 1) * 2
            if fullLen <= 255:
                type &= ~MSG_TYPE_MODIFIER_SIZE_32
                self.m_marsh.AddU8(type)
                self.m_marsh.AddU32(key, marshalEndian)
                self.m_marsh.AddU8(fullLen)
            else:
                type |= MSG_TYPE_MODIFIER_SIZE_32
                self.m_marsh.AddU8(type)
                self.m_marsh.AddU32(key, marshalEndian)
                self.m_marsh.AddU32(fullLen, marshalEndian)
            for c in data:
                self.m_marsh.AddU16(ord(c), marshalEndian)

            self.m_marsh.AddU16(0)
        elif type & MSG_TYPE_MASK == MSG_TYPE_UTF8:
            fullLen = len(data) + 1
            if fullLen <= 255:
                type &= ~MSG_TYPE_MODIFIER_SIZE_32
                self.m_marsh.AddU8(type)
                self.m_marsh.AddU32(key, marshalEndian)
                self.m_marsh.AddU8(fullLen)
            else:
                type |= MSG_TYPE_MODIFIER_SIZE_32
                self.m_marsh.AddU8(type)
                self.m_marsh.AddU32(key, marshalEndian)
                self.m_marsh.AddU32(fullLen, marshalEndian)
            for c in data:
                self.m_marsh.AddU8(ord(c))

            self.m_marsh.AddU8(0)
        elif type & MSG_TYPE_MASK == MSG_TYPE_BINARY or type & MSG_TYPE_MASK == MSG_TYPE_UTF8 or type & MSG_TYPE_MASK == MSG_TYPE_MSG:
            if len(data) <= 255:
                type &= ~MSG_TYPE_MODIFIER_SIZE_32
                self.m_marsh.AddU8(type)
                self.m_marsh.AddU32(key, marshalEndian)
                self.m_marsh.AddU8(len(data))
                self.m_marsh.AddData(data, includeSize=False)
            else:
                type |= MSG_TYPE_MODIFIER_SIZE_32
                self.m_marsh.AddU8(type)
                self.m_marsh.AddU32(key, marshalEndian)
                self.m_marsh.AddU32(len(data), marshalEndian)
                self.m_marsh.AddData(data, includeSize=False)
        else:
            raise RuntimeError('Unsupported message type (%u)' % type)

    def AddBool(self, key, data, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        if data != False:
            data = True
        self.Add(MSG_TYPE_BOOL, key, data, endianess)

    def AddData(self, key, data, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        self.Add(MSG_TYPE_BINARY, key, data, endianess)

    def AddError(self, key, moduleError, osError, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        if IsBigEndian(endianess):
            marshalEndian = self.m_marsh.BIG_ENDIAN
        else:
            marshalEndian = self.m_marsh.LITTLE_ENDIAN
        from mcl.object.Marshaler import Marshaler
        marsh = Marshaler()
        marsh.AddError(moduleError, osError, marshalEndian)
        self.Add(MSG_TYPE_BINARY, key, marsh.GetData(), endianess)

    def AddIpAddr(self, key, addr, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        if IsBigEndian(endianess):
            marshalEndian = self.m_marsh.BIG_ENDIAN
        else:
            marshalEndian = self.m_marsh.LITTLE_ENDIAN
        from mcl.object.Marshaler import Marshaler
        marsh = Marshaler()
        marsh.AddIpAddr(addr, marshalEndian)
        self.Add(MSG_TYPE_BINARY, key, marsh.GetData(), endianess)

    def AddMessage(self, key, msg, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        self.Add(MSG_TYPE_MSG, key, msg.Serialize(), endianess)

    def AddStringUtf8(self, key, str, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        if str == None:
            self.Add(MSG_TYPE_UTF8, key, '', endianess)
        else:
            self.Add(MSG_TYPE_UTF8, key, str, endianess)
        return

    def AddStringUtf16(self, key, str, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        if str == None:
            self.Add(MSG_TYPE_UTF16, key, '', endianess)
        else:
            self.Add(MSG_TYPE_UTF16, key, str, endianess)
        return

    def AddS8(self, key, data, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        self.Add(MSG_TYPE_S8, key, data, endianess)

    def AddS16(self, key, data, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        self.Add(MSG_TYPE_S16, key, data, endianess)

    def AddS32(self, key, data, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        self.Add(MSG_TYPE_S32, key, data, endianess)

    def AddS64(self, key, data, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        self.Add(MSG_TYPE_S64, key, data, endianess)

    def AddTime(self, key, t, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        if IsBigEndian(endianess):
            marshalEndian = self.m_marsh.BIG_ENDIAN
        else:
            marshalEndian = self.m_marsh.LITTLE_ENDIAN
        from mcl.object.Marshaler import Marshaler
        marsh = Marshaler()
        marsh.AddTime(t, marshalEndian)
        self.Add(MSG_TYPE_BINARY, key, marsh.GetData(), endianess)

    def AddU8(self, key, data, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        self.Add(MSG_TYPE_U8, key, data, endianess)

    def AddU16(self, key, data, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        self.Add(MSG_TYPE_U16, key, data, endianess)

    def AddU32(self, key, data, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        self.Add(MSG_TYPE_U32, key, data, endianess)

    def AddU64(self, key, data, endianess=MSG_TYPE_MODIFIER_NATIVE_ENDIAN):
        self.Add(MSG_TYPE_U64, key, data, endianess)

    def Clear(self):
        self.m_marsh.Clear()

    def GetSize(self):
        return self.m_marsh.GetSize()

    def Serialize(self):
        return self.m_marsh.GetData()