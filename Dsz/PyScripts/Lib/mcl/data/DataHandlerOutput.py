# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: DataHandlerOutput.py


class DataHandlerOutput:

    def __init__(self, input):
        pass

    def CreateLogFile(self, prefix, suffix, subDir=None, utf8=True):
        raise RuntimeError('DataHandlerOutput.CreateLogFile must be overriden')

    def End(self):
        raise RuntimeError('DataHandlerOutput.End must be overriden')

    def EndWithStatus(self, status):
        self.SetTaskStatus(status)
        self.End()

    def GoToBackground(self):
        pass

    def RecordError(self, errorStr):
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('ErrorString')
        xml.SetText(errorStr)
        self.RecordXml(xml)

    def RecordModuleError(self, moduleError, osError, modErrorStrings={}, translateOsError=True, osErrorStrings=None, translateMclStatusError=True):
        import mcl.status
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('Errors')
        if modErrorStrings.has_key(moduleError):
            modErrorStr = modErrorStrings[moduleError]
        elif translateMclStatusError and mcl.status.errorStrings.has_key(moduleError):
            modErrorStr = mcl.status.errorStrings[moduleError]
        else:
            modErrorStr = '0x%08x' % moduleError
        haveErrorData = False
        if len(modErrorStr) > 0:
            sub = xml.AddSubElement('ModuleError')
            sub.AddAttribute('value', '%u' % moduleError)
            sub.SetText(modErrorStr)
            haveErrorData = True
        if osError != 0:
            try:
                if translateOsError and osErrorStrings == None:
                    osErrorStr = self.TranslateOsError(osError)
                elif translateOsError and osErrorStrings != None and osErrorStrings.has_key(osError):
                    osErrorStr = osErrorStrings[osError]
                else:
                    osErrorStr = 'Additional Error: %d (0x%x)' % (osError, osError)
            except:
                osErrorStr = 'Unknown Error: %u (0x%x)' % (osError, osError)

            sub = xml.AddSubElement('OsError')
            sub.AddAttribute('value', '%u' % osError)
            sub.SetText(osErrorStr)
            haveErrorData = True
        if haveErrorData == True:
            self.RecordXml(xml)
        return

    def RecordXml(self, xml):
        raise RuntimeError('DataHandlerOutput.RecordXml must be overriden')

    def SetTaskStatus(self, status):
        raise RuntimeError('DataHandlerOutput.SetTaskStatus must be overriden')

    def Start(self, elementName, namespace, attributes):
        raise RuntimeError('DataHandlerOutput.Start must be overriden')

    def TranslateOsError(self, osError):
        raise RuntimeError('DataHandlerOutput.TranslateOsError must be overriden')