# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py


def Echo(str):
    import mcl_platform.tasking
    mcl_platform.tasking.Echo(str)


def EchoError(str):
    import mcl_platform.tasking
    mcl_platform.tasking.EchoError(str)


def EchoGood(str):
    import mcl_platform.tasking
    mcl_platform.tasking.EchoGood(str)


def EchoWarning(str):
    import mcl_platform.tasking
    mcl_platform.tasking.EchoWarning(str)


def GetContext():
    import mcl_platform.tasking
    return mcl_platform.tasking.GetContext()


def GetParameters():
    import mcl_platform.tasking
    return mcl_platform.tasking.GetParameters()


def GetProcedureNumber():
    import mcl_platform.tasking
    return mcl_platform.tasking.GetProcedureNumber()


def OutputError(str):
    import mcl_platform.tasking
    mcl_platform.tasking.OutputError(str)


def OutputXml(xml):
    import mcl_platform.tasking
    mcl_platform.tasking.OutputXml(xml)


def RecordModuleError(moduleError, osError, errorStrings={}, translateOsError=True, osErrorStrings=None, translateMclStatusError=True):
    import mcl_platform.tasking
    mcl_platform.tasking.RecordModuleError(moduleError, osError, errorStrings, translateOsError, osErrorStrings, translateMclStatusError)


def RpcPerformCall(rpcInfo, wait=False):
    import mcl_platform.tasking
    return mcl_platform.tasking.RpcPerformCall(rpcInfo, wait)


def TaskGoToBackground():
    import mcl_platform.tasking
    mcl_platform.tasking.TaskGoToBackground()


def TaskSetStatus(status):
    import mcl_platform.tasking
    mcl_platform.tasking.TaskSetStatus(status)


class RpcInfo:

    def __init__(self, framework, apiValues=[]):
        self.framework = framework
        self.apiValues = list(apiValues)
        self.data = None
        self.dest = None
        self.taskInfo_disable = False
        self.messagingType = 'Raw'
        return

    def SetData(self, data):
        self.data = data

    def SetDestination(self, dest):
        self.dest = dest

    def TaskInfoDisable(self):
        self.taskInfo_disable = True

    def SetMessagingType(self, msgType):
        self.messagingType = msgType


class Tasking:

    def __init__(self):
        import mcl.object.XmlOutput
        self.m_xml = mcl.object.XmlOutput.XmlOutput()
        self.m_xml.Start('TaskingInfo')

    def AddProvider(self, providerName, providerId):
        sub = self.m_xml.AddSubElement('Provider')
        sub.AddAttribute('name', '%s' % providerName)
        sub.AddAttribute('id', '%u' % providerId)

    def AddSearchMask(self, mask):
        self.m_xml.AddSubElementWithText('SearchMask', '%s' % mask)

    def AddSearchParam(self, param):
        self.m_xml.AddSubElementWithText('SearchParam', '%s' % param)

    def AddSearchPath(self, path):
        self.m_xml.AddSubElementWithText('SearchPath', '%s' % path)

    def Clear(self):
        self.m_xml.Clear()
        self.m_xml.Start('TaskingInfo')

    def GetXmlObject(self):
        return self.m_xml

    def SetMaxMatches(self, maxMatches):
        self.m_xml.AddSubElementWithText('SearchMaxMatches', '%u' % maxMatches)

    def SetRecursive(self, depth=0):
        if depth != 0:
            self.m_xml.AddSubElementWithText('SearchRecursive', '%u' % depth)
        else:
            self.m_xml.AddSubElement('SearchRecursive')

    def SetSearchTimeAfter(self, after):
        if after != None:
            from mcl.object.MclTime import MclTime
            if after.GetTimeType() != MclTime.MCL_TIME_TYPE_NOT_A_TIME:
                if after.GetTimeType() == MclTime.MCL_TIME_TYPE_DELTA:
                    raise RuntimeError('After time cannot be of type DELTA')
                self.m_xml.AddTimeElement('SearchAfterDate', after)
        return

    def SetSearchTimeAge(self, age):
        if age != None:
            from mcl.object.MclTime import MclTime
            if age.GetTimeType() != MclTime.MCL_TIME_TYPE_NOT_A_TIME:
                if age.GetTimeType() != MclTime.MCL_TIME_TYPE_DELTA:
                    raise RuntimeError('Age must be of type DELTA')
                self.m_xml.AddTimeElement('SearchAge', age)
        return

    def SetSearchTimeBefore(self, before):
        if before != None:
            from mcl.object.MclTime import MclTime
            if before.GetTimeType() != MclTime.MCL_TIME_TYPE_NOT_A_TIME:
                if before.GetTimeType() == MclTime.MCL_TIME_TYPE_DELTA:
                    raise RuntimeError('Before time cannot be of type DELTA')
                self.m_xml.AddTimeElement('SearchBeforeDate', before)
        return

    def SetTargetLocal(self):
        sub = self.m_xml.AddSubElement('CommandTarget')
        sub.AddAttribute('type', 'local')

    def SetTargetRemote(self, name):
        sub = self.m_xml.AddSubElement('CommandTarget')
        sub.AddAttribute('type', 'remote')
        sub.SetText('%s' % name)

    def SetType(self, type):
        self.m_xml.AddSubElementWithText('TaskType', '%s' % type)