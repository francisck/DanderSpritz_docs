# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Performance_DataHandler.py
PERF_SIZE_DWORD = 0
PERF_SIZE_LARGE = 256
PERF_SIZE_ZERO = 512
PERF_SIZE_VARIABLE_LEN = 768
PERF_TYPE_NUMBER = 0
PERF_TYPE_COUNTER = 1024
PERF_TYPE_TEXT = 2048
PERF_TYPE_ZERO = 3072
PERF_NUMBER_HEX = 0
PERF_NUMBER_DECIMAL = 65536
PERF_NUMBER_DEC_1000 = 131072
PERF_COUNTER_VALUE = 0
PERF_COUNTER_RATE = 65536
PERF_COUNTER_FRACTION = 131072
PERF_COUNTER_BASE = 196608
PERF_COUNTER_ELAPSED = 262144
PERF_COUNTER_QUEUELEN = 327680
PERF_COUNTER_HISTOGRAM = 393216
PERF_COUNTER_PRECISION = 458752
PERF_TEXT_UNICODE = 0
PERF_TEXT_ASCII = 65536
PERF_TIMER_TICK = 0
PERF_TIMER_100NS = 1048576
PERF_OBJECT_TIMER = 2097152
PERF_DELTA_COUNTER = 4194304
PERF_DELTA_BASE = 8388608
PERF_INVERSE_COUNTER = 16777216
PERF_MULTI_COUNTER = 33554432
PERF_DISPLAY_NO_SUFFIX = 0
PERF_DISPLAY_PER_SEC = 268435456
PERF_DISPLAY_PERCENT = 536870912
PERF_DISPLAY_SECONDS = 805306368
PERF_DISPLAY_NOSHOW = 1073741824
PERF_COUNTER_COUNTER = PERF_SIZE_DWORD | PERF_TYPE_COUNTER | PERF_COUNTER_RATE | PERF_TIMER_TICK | PERF_DELTA_COUNTER | PERF_DISPLAY_PER_SEC
PERF_COUNTER_TIMER = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_RATE | PERF_TIMER_TICK | PERF_DELTA_COUNTER | PERF_DISPLAY_PERCENT
PERF_COUNTER_QUEUELEN_TYPE = PERF_SIZE_DWORD | PERF_TYPE_COUNTER | PERF_COUNTER_QUEUELEN | PERF_TIMER_TICK | PERF_DELTA_COUNTER | PERF_DISPLAY_NO_SUFFIX
PERF_COUNTER_LARGE_QUEUELEN_TYPE = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_QUEUELEN | PERF_TIMER_TICK | PERF_DELTA_COUNTER | PERF_DISPLAY_NO_SUFFIX
PERF_COUNTER_100NS_QUEUELEN_TYPE = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_QUEUELEN | PERF_TIMER_100NS | PERF_DELTA_COUNTER | PERF_DISPLAY_NO_SUFFIX
PERF_COUNTER_OBJ_TIME_QUEUELEN_TYPE = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_QUEUELEN | PERF_OBJECT_TIMER | PERF_DELTA_COUNTER | PERF_DISPLAY_NO_SUFFIX
PERF_COUNTER_BULK_COUNT = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_RATE | PERF_TIMER_TICK | PERF_DELTA_COUNTER | PERF_DISPLAY_PER_SEC
PERF_COUNTER_TEXT = PERF_SIZE_VARIABLE_LEN | PERF_TYPE_TEXT | PERF_TEXT_UNICODE | PERF_DISPLAY_NO_SUFFIX
PERF_COUNTER_RAWCOUNT = PERF_SIZE_DWORD | PERF_TYPE_NUMBER | PERF_NUMBER_DECIMAL | PERF_DISPLAY_NO_SUFFIX
PERF_COUNTER_LARGE_RAWCOUNT = PERF_SIZE_LARGE | PERF_TYPE_NUMBER | PERF_NUMBER_DECIMAL | PERF_DISPLAY_NO_SUFFIX
PERF_COUNTER_RAWCOUNT_HEX = PERF_SIZE_DWORD | PERF_TYPE_NUMBER | PERF_NUMBER_HEX | PERF_DISPLAY_NO_SUFFIX
PERF_COUNTER_LARGE_RAWCOUNT_HEX = PERF_SIZE_LARGE | PERF_TYPE_NUMBER | PERF_NUMBER_HEX | PERF_DISPLAY_NO_SUFFIX
PERF_SAMPLE_FRACTION = PERF_SIZE_DWORD | PERF_TYPE_COUNTER | PERF_COUNTER_FRACTION | PERF_DELTA_COUNTER | PERF_DELTA_BASE | PERF_DISPLAY_PERCENT
PERF_SAMPLE_COUNTER = PERF_SIZE_DWORD | PERF_TYPE_COUNTER | PERF_COUNTER_RATE | PERF_TIMER_TICK | PERF_DELTA_COUNTER | PERF_DISPLAY_NO_SUFFIX
PERF_COUNTER_NODATA = PERF_SIZE_ZERO | PERF_DISPLAY_NOSHOW
PERF_COUNTER_TIMER_INV = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_RATE | PERF_TIMER_TICK | PERF_DELTA_COUNTER | PERF_INVERSE_COUNTER | PERF_DISPLAY_PERCENT
PERF_SAMPLE_BASE = PERF_SIZE_DWORD | PERF_TYPE_COUNTER | PERF_COUNTER_BASE | PERF_DISPLAY_NOSHOW | 1
PERF_AVERAGE_TIMER = PERF_SIZE_DWORD | PERF_TYPE_COUNTER | PERF_COUNTER_FRACTION | PERF_DISPLAY_SECONDS
PERF_AVERAGE_BASE = PERF_SIZE_DWORD | PERF_TYPE_COUNTER | PERF_COUNTER_BASE | PERF_DISPLAY_NOSHOW | 2
PERF_AVERAGE_BULK = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_FRACTION | PERF_DISPLAY_NOSHOW
PERF_OBJ_TIME_TIMER = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_RATE | PERF_OBJECT_TIMER | PERF_DELTA_COUNTER | PERF_DISPLAY_PERCENT
PERF_100NSEC_TIMER = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_RATE | PERF_TIMER_100NS | PERF_DELTA_COUNTER | PERF_DISPLAY_PERCENT
PERF_100NSEC_TIMER_INV = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_RATE | PERF_TIMER_100NS | PERF_DELTA_COUNTER | PERF_INVERSE_COUNTER | PERF_DISPLAY_PERCENT
PERF_COUNTER_MULTI_TIMER = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_RATE | PERF_DELTA_COUNTER | PERF_TIMER_TICK | PERF_MULTI_COUNTER | PERF_DISPLAY_PERCENT
PERF_COUNTER_MULTI_TIMER_INV = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_RATE | PERF_DELTA_COUNTER | PERF_MULTI_COUNTER | PERF_TIMER_TICK | PERF_INVERSE_COUNTER | PERF_DISPLAY_PERCENT
PERF_COUNTER_MULTI_BASE = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_BASE | PERF_MULTI_COUNTER | PERF_DISPLAY_NOSHOW
PERF_100NSEC_MULTI_TIMER = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_DELTA_COUNTER | PERF_COUNTER_RATE | PERF_TIMER_100NS | PERF_MULTI_COUNTER | PERF_DISPLAY_PERCENT
PERF_100NSEC_MULTI_TIMER_INV = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_DELTA_COUNTER | PERF_COUNTER_RATE | PERF_TIMER_100NS | PERF_MULTI_COUNTER | PERF_INVERSE_COUNTER | PERF_DISPLAY_PERCENT
PERF_RAW_FRACTION = PERF_SIZE_DWORD | PERF_TYPE_COUNTER | PERF_COUNTER_FRACTION | PERF_DISPLAY_PERCENT
PERF_LARGE_RAW_FRACTION = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_FRACTION | PERF_DISPLAY_PERCENT
PERF_RAW_BASE = PERF_SIZE_DWORD | PERF_TYPE_COUNTER | PERF_COUNTER_BASE | PERF_DISPLAY_NOSHOW | 3
PERF_LARGE_RAW_BASE = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_BASE | PERF_DISPLAY_NOSHOW
PERF_ELAPSED_TIME = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_ELAPSED | PERF_OBJECT_TIMER | PERF_DISPLAY_SECONDS
PERF_COUNTER_DELTA = PERF_SIZE_DWORD | PERF_TYPE_COUNTER | PERF_COUNTER_VALUE | PERF_DELTA_COUNTER | PERF_DISPLAY_NO_SUFFIX
PERF_COUNTER_LARGE_DELTA = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_VALUE | PERF_DELTA_COUNTER | PERF_DISPLAY_NO_SUFFIX
PERF_PRECISION_SYSTEM_TIMER = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_PRECISION | PERF_TIMER_TICK | PERF_DELTA_COUNTER | PERF_DISPLAY_PERCENT
PERF_PRECISION_100NS_TIMER = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_PRECISION | PERF_TIMER_100NS | PERF_DELTA_COUNTER | PERF_DISPLAY_PERCENT
PERF_PRECISION_OBJECT_TIMER = PERF_SIZE_LARGE | PERF_TYPE_COUNTER | PERF_COUNTER_PRECISION | PERF_OBJECT_TIMER | PERF_DELTA_COUNTER | PERF_DISPLAY_PERCENT
PERF_PRECISION_TIMESTAMP = PERF_LARGE_RAW_BASE

def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.status.cmd.performance', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Performance', 'performance', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    strings = {}
    if not _processMessage(output, xml, msg, strings):
        return True
    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _processMessage(output, root, msg, strings):
    parent = root
    lastParent = None
    lastWasInstance = False
    for entry in msg:
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        if entry['key'] == MSG_KEY_RESULT_HEADER:
            hdr = ResultHeader()
            hdr.Demarshal(msg)
            root.Start('PerformanceHeader')
            root.AddAttribute('systemName', hdr.sysName)
            root.AddAttribute('perfCount', '%u' % hdr.perfCount)
            root.AddAttribute('perfCountsPerSecond', '%u' % hdr.perfCountsPerSecond)
            root.AddAttribute('perfTime100nSec', '%u' % hdr.perfTime100nSec)
            parent = root
            lastParent = None
            lastWasInstance = False
        elif entry['key'] == MSG_KEY_RESULT_OBJECT_HEADER:
            objHdr = ResultObjectHeader()
            objHdr.Demarshal(msg)
            parent = root
            lastParent = None
            lastWasInstance = False
            sub = parent.AddSubElement('ObjectHeader')
            sub.AddAttribute('helpIndex', '%u' % objHdr.helpTitleIndex)
            sub.AddAttribute('nameIndex', '%u' % objHdr.nameTitleIndex)
            if strings.has_key(objHdr.helpTitleIndex):
                sub.AddSubElementWithText('Help', strings[objHdr.helpTitleIndex])
            else:
                sub.AddSubElementWithText('Help', '%u' % objHdr.helpTitleIndex)
            if strings.has_key(objHdr.nameTitleIndex):
                sub.AddSubElementWithText('Name', strings[objHdr.nameTitleIndex])
            else:
                sub.AddSubElementWithText('Name', '%u' % objHdr.nameTitleIndex)
            lastParent = parent
            parent = sub
        elif entry['key'] == MSG_KEY_RESULT_INSTANCE:
            inst = ResultInstance()
            inst.Demarshal(msg)
            if lastWasInstance and lastParent != None:
                parent = lastParent
                lastParent = None
            sub = parent.AddSubElement('Instance')
            sub.AddAttribute('id', '%u' % inst.id)
            sub.AddAttribute('parent', '%u' % inst.parent)
            sub.AddAttribute('name', inst.name)
            lastParent = parent
            parent = sub
            lastWasInstance = True
        elif entry['key'] == MSG_KEY_RESULT_COUNT:
            counter = ResultCount()
            counter.Demarshal(msg)
            sub = parent.AddSubElement('Counter')
            sub.AddAttribute('helpIndex', '%u' % counter.helpIndex)
            sub.AddAttribute('nameIndex', '%u' % counter.nameIndex)
            if strings.has_key(counter.helpIndex):
                sub.AddSubElementWithText('Help', strings[counter.helpIndex])
            else:
                sub.AddSubElementWithText('Help', '%u' % counter.helpIndex)
            if strings.has_key(counter.nameIndex):
                sub.AddSubElementWithText('Name', strings[counter.nameIndex])
            else:
                sub.AddSubElementWithText('Name', '%u' % counter.nameIndex)
            sub.AddAttribute('type', '0x%08x' % counter.type)
            value = sub.AddSubElement('Value')
            if len(counter.valueStr) > 0:
                value.SetText(counter.valueStr)
            elif counter.type & PERF_SIZE_ZERO == PERF_SIZE_ZERO:
                pass
            elif counter.type & PERF_NUMBER_DEC_1000 == PERF_NUMBER_DEC_1000:
                value.SetText('%u' % (counter.value / 1000))
            else:
                value.SetText('%u' % counter.value)
            _getPerfInfo(value, counter.type)
        elif entry['key'] == MSG_KEY_RESULT_STRING:
            str = ResultString()
            str.Demarshal(msg)
            strings[str.id] = str.str
        elif entry['key'] == MSG_KEY_RESULT_OBJECT_GROUP:
            submsg = msg.FindMessage(MSG_KEY_RESULT_OBJECT_GROUP)
            if not _processMessage(output, parent, submsg, strings):
                return False
        else:
            output.RecordError('Unhandled data key (0x%08x)' % entry['key'])
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False

    return True


def _getPerfInfo(value, type):
    if type == PERF_COUNTER_COUNTER:
        value.AddAttribute('suffix', '/sec')
        value.AddAttribute('type', 'PERF_COUNTER_COUNTER')
    elif type == PERF_COUNTER_TIMER:
        value.AddAttribute('suffix', '%%')
        value.AddAttribute('type', 'PERF_COUNTER_TIMER')
    elif type == PERF_COUNTER_QUEUELEN_TYPE:
        value.AddAttribute('type', 'PERF_COUNTER_QUEUELEN_TYPE')
    elif type == PERF_COUNTER_LARGE_QUEUELEN_TYPE:
        value.AddAttribute('type', 'PERF_COUNTER_LARGE_QUEUELEN_TYPE')
    elif type == PERF_COUNTER_100NS_QUEUELEN_TYPE:
        value.AddAttribute('type', 'PERF_COUNTER_100NS_QUEUELEN_TYPE')
    elif type == PERF_COUNTER_OBJ_TIME_QUEUELEN_TYPE:
        value.AddAttribute('type', 'PERF_COUNTER_OBJ_TIME_QUEUELEN_TYPE')
    elif type == PERF_COUNTER_BULK_COUNT:
        value.AddAttribute('suffix', '/sec')
        value.AddAttribute('type', 'PERF_COUNTER_BULK_COUNT')
    elif type == PERF_COUNTER_TEXT:
        value.AddAttribute('type', 'PERF_COUNTER_TEXT')
    elif type == PERF_COUNTER_RAWCOUNT:
        value.AddAttribute('type', 'PERF_COUNTER_RAWCOUNT')
    elif type == PERF_COUNTER_LARGE_RAWCOUNT:
        value.AddAttribute('type', 'PERF_COUNTER_LARGE_RAWCOUNT')
    elif type == PERF_COUNTER_RAWCOUNT_HEX:
        value.AddAttribute('type', 'PERF_COUNTER_RAWCOUNT_HEX')
    elif type == PERF_COUNTER_LARGE_RAWCOUNT_HEX:
        value.AddAttribute('type', 'PERF_COUNTER_LARGE_RAWCOUNT_HEX')
    elif type == PERF_SAMPLE_FRACTION:
        value.AddAttribute('suffix', '%%')
        value.AddAttribute('type', 'PERF_SAMPLE_FRACTION')
    elif type == PERF_SAMPLE_COUNTER:
        value.AddAttribute('suffix', '%%')
        value.AddAttribute('type', 'PERF_SAMPLE_COUNTER')
    elif type == PERF_COUNTER_NODATA:
        pass
    elif type == PERF_COUNTER_TIMER_INV:
        value.AddAttribute('suffix', '%%')
        value.AddAttribute('type', 'PERF_COUNTER_TIMER_INV')
    elif type == PERF_SAMPLE_BASE:
        value.AddAttribute('type', 'PERF_SAMPLE_BASE')
    elif type == PERF_AVERAGE_TIMER:
        value.AddAttribute('suffix', '%%')
        value.AddAttribute('type', 'PERF_AVERAGE_TIMER')
    elif type == PERF_AVERAGE_BASE:
        value.AddAttribute('type', 'PERF_AVERAGE_BASE')
    elif type == PERF_AVERAGE_BULK:
        value.AddAttribute('type', 'PERF_AVERAGE_BULK')
    elif type == PERF_OBJ_TIME_TIMER:
        value.AddAttribute('suffix', '%%')
        value.AddAttribute('type', 'PERF_OBJ_TIME_TIMER')
    elif type == PERF_100NSEC_TIMER:
        value.AddAttribute('suffix', '%%')
        value.AddAttribute('type', 'PERF_100NSEC_TIMER')
    elif type == PERF_100NSEC_TIMER_INV:
        value.AddAttribute('suffix', '%%')
        value.AddAttribute('type', 'PERF_100NSEC_TIMER_INV')
    elif type == PERF_COUNTER_MULTI_TIMER:
        value.AddAttribute('suffix', '%%')
        value.AddAttribute('type', 'PERF_COUNTER_MULTI_TIMER')
    elif type == PERF_COUNTER_MULTI_TIMER_INV:
        value.AddAttribute('suffix', '%%')
        value.AddAttribute('type', 'PERF_COUNTER_MULTI_TIMER_INV')
    elif type == PERF_COUNTER_MULTI_BASE:
        pass
    elif type == PERF_100NSEC_MULTI_TIMER:
        value.AddAttribute('suffix', '%%')
        value.AddAttribute('type', 'PERF_100NSEC_MULTI_TIMER')
    elif type == PERF_RAW_FRACTION:
        value.AddAttribute('suffix', '%%')
        value.AddAttribute('type', 'PERF_RAW_FRACTION')
    elif type == PERF_LARGE_RAW_FRACTION:
        value.AddAttribute('suffix', '%%')
        value.AddAttribute('type', 'PERF_LARGE_RAW_FRACTION')
    elif type == PERF_RAW_BASE:
        value.AddAttribute('type', 'PERF_RAW_BASE')
    elif type == PERF_LARGE_RAW_BASE:
        value.AddAttribute('type', 'PERF_LARGE_RAW_BASE')
    elif type == PERF_ELAPSED_TIME:
        value.AddAttribute('suffix', '%%')
        value.AddAttribute('type', 'PERF_ELAPSED_TIME')
    elif type == PERF_COUNTER_DELTA:
        value.AddAttribute('type', 'PERF_COUNTER_DELTA')
    elif type == PERF_COUNTER_LARGE_DELTA:
        value.AddAttribute('type', 'PERF_COUNTER_LARGE_DELTA')
    elif type == PERF_PRECISION_SYSTEM_TIMER:
        value.AddAttribute('type', 'PERF_PRECISION_SYSTEM_TIMER')
    elif type == PERF_PRECISION_100NS_TIMER:
        value.AddAttribute('type', 'PERF_PRECISION_100NS_TIMER')
    elif type == PERF_PRECISION_OBJECT_TIMER:
        value.AddAttribute('type', 'PERF_PRECISION_OBJECT_TIMER')


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)