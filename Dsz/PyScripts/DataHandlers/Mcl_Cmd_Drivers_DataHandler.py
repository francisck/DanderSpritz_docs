# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Drivers_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.survey.cmd.drivers', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Drivers', 'drivers', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    if input.GetMessageType() == mcl.msgtype.DRIVER_LIST:
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('Drivers')
        while msg.GetNumRetrieved() < msg.GetCount():
            if mcl.CheckForStop():
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            result = Result()
            result.Demarshal(msg)
            sub = xml.AddSubElement('Driver')
            if result.imageBase >> 32 == 0:
                base = result.imageBase & 4294967295L
                sub.AddAttribute('base', '0x%08x' % base)
            else:
                sub.AddAttribute('base', '0x%016x' % result.imageBase)
            sub.AddAttribute('size', '%u' % result.size)
            sub.AddAttribute('flags', '0x%08x' % result.flags)
            sub.AddAttribute('loadCount', '%u' % result.loadCount)
            if result.buildDate.GetTimeType() != result.buildDate.MCL_TIME_TYPE_INVALID:
                sub.AddTimeElement('BuildDate', result.buildDate)
            sub.AddSubElementWithText('Name', result.imageName)
            sub.AddSubElementWithText('Author', result.author)
            sub.AddSubElementWithText('License', result.license)
            sub.AddSubElementWithText('Version', result.version)
            sub.AddSubElementWithText('Description', result.description)
            sub.AddSubElementWithText('Comments', result.comments)
            sub.AddSubElementWithText('InternalName', result.internalName)
            sub.AddSubElementWithText('OriginalName', result.originalName)
            sub.AddSubElementWithText('ProductName', result.productName)
            sub.AddSubElementWithText('Trademark', result.trademarks)
            if result.itemFlags & RESULT_ITEM_FLAG_SIGNED:
                sub.AddSubElement('Signed')
            elif result.itemFlags & RESULT_ITEM_FLAG_UNSIGNED:
                sub.AddSubElement('Unsigned')

        output.RecordXml(xml)
    elif input.GetMessageType() == mcl.msgtype.DRIVER_LOAD:
        pass
    elif input.GetMessageType() == mcl.msgtype.DRIVER_UNLOAD:
        pass
    else:
        output.RecordError('Unhandled message type (%u)' % input.GetMessageType())
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return True
    output.EndWithStatus(input.GetStatus())
    return True


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)