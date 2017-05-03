# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: MclTime.py


class MclTime:
    MCL_TIME_TYPE_NOT_A_TIME = 0
    MCL_TIME_TYPE_INVALID = 0
    MCL_TIME_TYPE_DELTA = 1
    MCL_TIME_TYPE_GMT = 2
    MCL_TIME_TYPE_LOCAL = 3

    def __init__(self, seconds=0, nanoseconds=0, type=MCL_TIME_TYPE_NOT_A_TIME):
        self.m_seconds = seconds
        self.m_nanoseconds = nanoseconds
        self.m_type = type

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        import datetime
        if self.m_type == MclTime.MCL_TIME_TYPE_DELTA:
            delta = datetime.timedelta(seconds=self.m_seconds, microseconds=self.m_nanoseconds / 1000)
            return '%s' % delta
        else:
            if self.m_type == MclTime.MCL_TIME_TYPE_GMT:
                try:
                    t = datetime.datetime.utcfromtimestamp(self.m_seconds)
                except:
                    t = datetime.datetime.utcfromtimestamp(0)

                return '%s GMT' % t
            if self.m_type == MclTime.MCL_TIME_TYPE_LOCAL:
                try:
                    t = datetime.datetime.utcfromtimestamp(self.m_seconds)
                except:
                    t = datetime.datetime.utcfromtimestamp(0)

                return '%s LOCAL' % t
            return 'seconds=%u nanoseconds=%u type=%u' % (self.m_seconds, self.m_nanoseconds, self.m_type)

    def __copy__(self):
        x = MclTime()
        x.m_seconds = self.m_seconds
        x.m_nanoseconds = self.m_nanoseconds
        x.m_type = self.m_type
        return x

    def __deepcopy__(self, memo):
        x = MclTime()
        x.m_seconds = self.m_seconds
        x.m_nanoseconds = self.m_nanoseconds
        x.m_type = self.m_type
        return x

    def GetNanoseconds(self):
        return self.m_nanoseconds

    def GetSeconds(self):
        return self.m_seconds

    def GetTimeType(self):
        return self.m_type

    def GetTimeTypeStr(self):
        if self.m_type == 0:
            return 'MCL_TIME_TYPE_NO_A_TIME'
        else:
            if self.m_type == MclTime.MCL_TIME_TYPE_DELTA:
                return 'MCL_TIME_TYPE_DELTA'
            if self.m_type == MclTime.MCL_TIME_TYPE_GMT:
                return 'MCL_TIME_TYPE_GMT'
            if self.m_type == MclTime.MCL_TIME_TYPE_LOCAL:
                return 'MCL_TIME_TYPE_LOCAL'
            return 'UNKNOWN'