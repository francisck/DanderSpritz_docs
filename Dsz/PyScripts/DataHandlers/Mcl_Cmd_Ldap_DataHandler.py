# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Ldap_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.survey.cmd.ldap', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Ldap', 'ldap', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        if msg.GetCount() == 0:
            output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
            return True
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('LdapEntries')
        sub = None
        done = False
        for entry in msg:
            if mcl.CheckForStop():
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            submsg = msg.FindMessage(MSG_KEY_RESULT)
            results = Result()
            results.Demarshal(submsg)
            if results.numAttributes == -1:
                done = True
            else:
                if results.numAttributes == 0:
                    sub = xml.AddSubElement('LdapEntry')
                sub2 = sub.AddSubElement('Attribute')
                sub2.AddAttribute('attNum', '%i' % results.numAttributes)
                sub2.AddAttribute('dataType', '%u' % results.osDataType)
                sub2.AddSubElementWithText('Type', results.attrType)
                if results.dataType == RESULT_TYPE_BOOL:
                    boolVal = submsg.FindBool(MSG_KEY_RESULT_DATA)
                    if boolVal:
                        sub2.AddSubElementWithText('Value', 'true')
                    else:
                        sub2.AddSubElementWithText('Value', 'false')
                elif results.dataType == RESULT_TYPE_INT:
                    intVal = submsg.FindS32(MSG_KEY_RESULT_DATA)
                    sub2.AddSubElementWithText('Value', '%d' % intVal)
                elif results.dataType == RESULT_TYPE_STR:
                    strVal = submsg.FindString(MSG_KEY_RESULT_DATA)
                    sub2.AddSubElementWithText('Value', strVal)
                elif results.dataType == RESULT_TYPE_TIME:
                    timeVal = submsg.FindTime(MSG_KEY_RESULT_DATA)
                    sub2.AddTimeElement('Value', timeVal)
                elif results.dataType == RESULT_TYPE_HEX:
                    strVal = submsg.FindString(MSG_KEY_RESULT_DATA)
                    sub2.AddSubElementWithText('Value', strVal)
                elif results.dataType == RESULT_TYPE_LARGEINT:
                    intVal = submsg.FindS64(MSG_KEY_RESULT_DATA)
                    sub2.AddSubElementWithText('Value', '%d' % intVal)
                elif results.dataType == RESULT_TYPE_UNKNOWN:
                    strVal = submsg.FindString(MSG_KEY_RESULT_DATA)
                    sub2.AddSubElementWithText('Value', 'Unhandled data type (%s)' % strVal)
                elif results.dataType == RESULT_TYPE_EXCEPTION:
                    strVal = submsg.FindString(MSG_KEY_RESULT_DATA)
                    sub2.AddSubElementWithText('Value', 'Exception handling data type (%s)' % strVal)
                else:
                    output.RecordError('Unhandled type (%u)' % results.dataType)
                    output.EndWithStatus(mcl.target.CALL_FAILED)
                    return True

        output.RecordXml(xml)
        if not done:
            output.End()
        else:
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