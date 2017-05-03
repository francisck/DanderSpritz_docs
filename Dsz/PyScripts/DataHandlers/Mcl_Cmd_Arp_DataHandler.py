# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Arp_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.network.cmd.arp', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Arp', 'arp', [])
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
            output.EndWithStatus(input.GetStatus())
            return True
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        initialResult = Result()
        initialResult.Demarshal(msg)
        moreData = initialResult.moreData
        xml.Start('ArpEntries')
        if initialResult.listType == RESULT_INITIAL_LIST:
            xml.AddSubElement('ArpHeader')
        _addArpEntry(xml, initialResult)
        while msg.GetNumRetrieved() < msg.GetCount():
            if mcl.CheckForStop():
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            result = Result()
            result.Demarshal(msg)
            moreData = result.moreData
            _addArpEntry(xml, result)

        output.RecordXml(xml)
        if moreData:
            if initialResult.listType == RESULT_INITIAL_LIST:
                output.GoToBackground()
            output.End()
            return True
        output.SetTaskStatus(mcl.target.CALL_SUCCEEDED)
        output.End()
        return True


def _addArpEntry(xml, entry):
    sub = xml.AddSubElement('ArpEntry')
    sub.AddAddressIP('IP', entry.ipAddr)
    sub.AddAddressPhysical('Physical', entry.physicalAddr, entry.physicalAddrLen)
    if entry.type != RESULT_ENTRY_TYPE_NO_TYPE:
        sub.AddAttribute('type', _getEntryType(entry.type))
    if len(entry.adapter) > 0:
        sub.AddAttribute('adapter', entry.adapter)
    if entry.flags & RESULT_FLAGS_IS_ROUTER:
        sub.AddSubElement('FlagIsRouter')
    if entry.flags & RESULT_FLAGS_IS_UNREACHABLE:
        sub.AddSubElement('FlagIsUnreachable')
    if entry.state != RESULT_STATE_UNKNOWN:
        sub.AddAttribute('state', _getStateType(entry.state))


def _getEntryType(type):
    if type == RESULT_ENTRY_TYPE_STATIC:
        return 'Static'
    else:
        if type == RESULT_ENTRY_TYPE_DYNAMIC:
            return 'Dynamic'
        if type == RESULT_ENTRY_TYPE_INVALID:
            return 'Invalid'
        if type == RESULT_ENTRY_TYPE_OTHER:
            return 'Other'
        return 'Unknown'


def _getStateType(state):
    if state == RESULT_STATE_UNREACHABLE:
        return 'UNREACHABLE'
    else:
        if state == RESULT_STATE_INCOMPLETE:
            return 'INCOMPLETE'
        if state == RESULT_STATE_PROBE:
            return 'PROBE'
        if state == RESULT_STATE_DELAY:
            return 'DELAY'
        if state == RESULT_STATE_STALE:
            return 'STALE'
        if state == RESULT_STATE_REACHABLE:
            return 'REACHABLE'
        if state == RESULT_STATE_PERMANENT:
            return 'PERMANENT'
        return 'Unknown'


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)