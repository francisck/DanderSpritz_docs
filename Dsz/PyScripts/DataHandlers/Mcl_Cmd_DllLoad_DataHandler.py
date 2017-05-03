# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_DllLoad_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.data.env
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.install.cmd.dllload', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('DllLoad', 'dllload', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        if msg[0]['key'] == MSG_KEY_RESULT_LOAD:
            results = ResultLoad()
            results.Demarshal(msg)
            from mcl.object.XmlOutput import XmlOutput
            xml = XmlOutput()
            xml.Start('DllLoad')
            if results.loadAddress > 4294967295L:
                xml.AddAttribute('loadAddress', '0x%016x' % results.loadAddress)
            else:
                xml.AddAttribute('loadAddress', '0x%08x' % results.loadAddress)
            output.RecordXml(xml)
            try:
                if mcl.data.env.IsTrue(LP_ENV_DLLU_NOWAIT):
                    output.GoToBackground()
            except:
                pass

            output.End()
            return True
        if msg[0]['key'] == MSG_KEY_RESULT_UNLOAD:
            results = ResultUnload()
            results.Demarshal(msg)
            from mcl.object.XmlOutput import XmlOutput
            xml = XmlOutput()
            xml.Start('DllUnload')
            if results.unloaded:
                xml.AddAttribute('unloaded', 'true')
            else:
                xml.AddAttribute('unloaded', 'false')
            output.RecordXml(xml)
            output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
            return True
        if msg[0]['key'] == MSG_KEY_RESULT_INJECTED:
            results = ResultInjected()
            results.Demarshal(msg)
            from mcl.object.XmlOutput import XmlOutput
            xml = XmlOutput()
            xml.Start('DllInjected')
            xml.AddAttribute('pid', '%u' % results.pid)
            if results.loadAddress > 4294967295L:
                xml.AddAttribute('loadAddress', '0x%016x' % results.loadAddress)
            else:
                xml.AddAttribute('loadAddress', '0x%08x' % results.loadAddress)
            if results.unloaded:
                xml.AddAttribute('unloaded', 'true')
            else:
                xml.AddAttribute('unloaded', 'false')
            output.RecordXml(xml)
            output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
            return True
        output.RecordError('Unhandled data key (0x%08x)' % msg[0]['key'])
        output.EndWithStatus(mcl.target.CALL_FAILED)
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