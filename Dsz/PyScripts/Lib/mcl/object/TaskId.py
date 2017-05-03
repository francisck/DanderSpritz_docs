# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: TaskId.py


class TaskId:

    def GenerateAsString():
        import uuid
        from md5 import md5
        simpleUuid = uuid.uuid1()
        finalUuid = uuid.UUID(md5(simpleUuid.bytes).hexdigest())
        return str(finalUuid)

    def StrToIntArray(origStr):
        import math
        v = filter(lambda c: c not in '-', origStr)
        l = 2
        listTaskId = [ v[i * l:(i + 1) * l] for i in range(int(math.ceil(len(v) / float(l)))) ]
        arrayTaskId = [ int(s, 16) for s in listTaskId ]
        return arrayTaskId

    GenerateAsString = staticmethod(GenerateAsString)
    StrToIntArray = staticmethod(StrToIntArray)