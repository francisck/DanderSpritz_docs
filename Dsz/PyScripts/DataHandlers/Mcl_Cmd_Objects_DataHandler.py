# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Objects_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.status.cmd.objects', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Objects', 'objects', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('Objects')
        gotValidDir = False
        objectList = list()
        sub = None
        while msg.GetNumRetrieved() < msg.GetCount():
            if mcl.CheckForStop():
                output.RecordXml(xml)
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            result = Result()
            try:
                result.Demarshal(msg)
            except:
                output.RecordXml(xml)
                raise

            if result.flags & RESULT_FLAG_DIR_START:
                _dumpObjects(sub, objectList)
                _deleteObjects(objectList)
                sub = xml.AddSubElement('ObjectDirectory')
                sub.AddAttribute('name', result.name)
                if result.status != 0:
                    errorStr = output.TranslateOsError(result.status)
                    sub.AddSubElementWithText('QueryFailure', errorStr)
                else:
                    gotValidDir = True
            elif sub != None:
                _addObject(objectList, result)

        _dumpObjects(sub, objectList)
        _deleteObjects(objectList)
        output.RecordXml(xml)
        if gotValidDir:
            output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
        else:
            output.EndWithStatus(mcl.target.CALL_FAILED)
        return True


def _addObject(objectList, result):
    i = 0
    while i < len(objectList):
        if result.type < objectList[i].type:
            objectList.insert(i, result)
            return
        if result.type == objectList[i].type:
            if result.name < objectList[i].name:
                objectList.insert(i, result)
                return
        i = i + 1

    objectList.append(result)


def _deleteObjects(objectList):
    del objectList[0:len(objectList) - 1]


def _dumpObjects(xml, objectList):
    for obj in objectList:
        sub = xml.AddSubElement('Object')
        sub.AddAttribute('name', obj.name)
        sub.AddAttribute('type', obj.type)


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)