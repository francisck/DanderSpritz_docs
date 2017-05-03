# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Scheduler_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.status.cmd.scheduler', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Scheduler', 'scheduler', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        if input.GetMessageType() == mcl.msgtype.SCHEDULER_ADD:
            return _handleSchedulerAdd(output, msg)
        if input.GetMessageType() == mcl.msgtype.SCHEDULER_DELETE:
            return _handleSchedulerDelete(output, msg)
        if input.GetMessageType() == mcl.msgtype.SCHEDULER_QUERY:
            return _handleSchedulerQuery(output, msg)
        output.RecordError('Unhandled message type (%u)' % input.GetMessageType())
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return False


def _handleSchedulerAdd(output, msg):
    if msg.GetCount() == 0:
        output.RecordError('No data returned')
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return True
    results = ResultAdd()
    results.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('NewJob')
    try:
        jobId = int(results.jobId)
    except:
        jobId = 0

    xml.AddAttribute('id', '%u' % jobId)
    xml.AddAttribute('name', results.jobId)
    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _handleSchedulerDelete(output, msg):
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Deleted')
    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _handleSchedulerQuery(output, msg):
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Jobs')
    rtn = True
    for entry in msg:
        if entry['key'] == MSG_KEY_RESULT_ATJOB:
            rtn = _printATQuery(output, msg, xml)
        elif entry['key'] == MSG_KEY_RESULT_NETJOB:
            rtn = _printIEQuery(output, msg, xml)
        elif entry['key'] == MSG_KEY_RESULT_TASKSERVICE_FOLDER:
            rtn = _printTaskServiceQuery(output, msg, xml)
        else:
            output.RecordError('Invalid scheduler key (0x%08x) returned' % entry['key'])
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return True

    output.RecordXml(xml)
    if not rtn:
        output.EndWithStatus(mcl.target.CALL_FAILED)
    else:
        output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _printATQuery(output, msg, xml):
    xml.AddSubElement('AtHeader')
    netmsg = msg.FindMessage(MSG_KEY_RESULT_ATJOB)
    while netmsg.GetNumRetrieved() < netmsg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        job = ResultAtJob()
        job.Demarshal(netmsg)
        sub = xml.AddSubElement('AtJob')
        sub.AddAttribute('id', '%u' % job.jobId)
        sub.AddSubElementWithText('CommandText', job.cmd)
        sub.AddTimeElement('Time', job.jobTime)
        days = ''
        sub2 = sub.AddSubElement('Weekday')
        sub2.AddAttribute('mask', '0x%x' % job.daysOfWeek)
        if job.daysOfWeek & 1:
            days = days + 'M '
        if job.daysOfWeek & 2:
            days = days + 'Tu '
        if job.daysOfWeek & 4:
            days = days + 'W '
        if job.daysOfWeek & 8:
            days = days + 'Th '
        if job.daysOfWeek & 16:
            days = days + 'F '
        if job.daysOfWeek & 32:
            days = days + 'Sa '
        if job.daysOfWeek & 64:
            days = days + 'Su '
        sub2.AddAttribute('days', days)
        sub2 = sub.AddSubElement('Monthday')
        sub2.AddAttribute('mask', '0x%x' % job.daysOfMonth)
        days = ''
        x = 0
        while x < 32:
            if 1 << x & job.daysOfMonth:
                days = days + '%u ' % (x + 1)
            x = x + 1

        sub2.AddAttribute('days', days)
        sub2 = sub.AddSubElement('Flags')
        sub2.AddAttribute('mask', '0x%x' % job.flags)
        if job.flags & RESULT_ATJOB_FLAG_NONINTERACTIVE:
            sub2.AddSubElement('JobNonInteractive')
        if job.flags & RESULT_ATJOB_FLAG_RUNS_TODAY:
            sub2.AddSubElement('JobRunsToday')
        if job.flags & RESULT_ATJOB_FLAG_EXEC_ERROR:
            sub2.AddSubElement('JobExecError')
        if job.flags & RESULT_ATJOB_FLAG_RUN_PERIODICALLY:
            sub2.AddSubElement('JobRunPeriodically')
        if job.flags & RESULT_ATJOB_FLAG_ADD_CURRENT_DATE:
            sub2.AddSubElement('JobAddCurrentDate')

    return True


def _printIEQuery(output, msg, xml):
    netmsg = msg.FindMessage(MSG_KEY_RESULT_NETJOB)
    while netmsg.GetNumRetrieved() < netmsg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        job = ResultNetJob()
        job.Demarshal(netmsg)
        sub = xml.AddSubElement('NetJob')
        sub.AddAttribute('exitcode', '%d' % job.exitCode)
        sub.AddTimeElement('NextRun', job.nextRun)
        sub.AddSubElementWithText('JobName', job.jobName)
        sub.AddSubElementWithText('Application', job.displayName)
        sub.AddSubElementWithText('Parameters', job.params)
        sub.AddSubElementWithText('Account', job.accountName)
        sub2 = sub.AddSubElement('Flags')
        sub2.AddAttribute('mask', '0x%x' % job.flags)
        sub2 = sub.AddSubElement('Triggers')
        x = 0
        while x < job.numTriggers:
            trigger = netmsg.FindString(MSG_KEY_RESULT_NETJOB_TRIGGER)
            sub2.AddSubElementWithText('Trigger', trigger)
            x = x + 1

    return True


def _printTaskServiceQuery(output, msg, xml):
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        fmsg = msg.FindMessage(MSG_KEY_RESULT_TASKSERVICE_FOLDER)
        folder = ResultTaskServiceFolder()
        folder.Demarshal(fmsg)
        folderSub = xml.AddSubElement('TaskServiceFolder')
        folderSub.AddAttribute('name', folder.name)
        folderSub.AddAttribute('path', folder.path)
        while fmsg.GetNumRetrieved() < fmsg.GetCount():
            if mcl.CheckForStop():
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            jobmsg = fmsg.FindMessage(MSG_KEY_RESULT_TASKSERVICEJOB)
            job = ResultTaskServiceJob()
            job.Demarshal(jobmsg)
            jobSub = folderSub.AddSubElement('Job')
            jobSub.AddAttribute('name', job.name)
            jobSub.AddAttribute('path', job.path)
            _printTaskServiceQuery_flags(jobSub.AddSubElement('Flags'), job.flags)
            jobSub.AddAttribute('lastRunResult', '0x%08x' % job.lastRunResult)
            jobSub.AddAttribute('numMissedRuns', '%u' % job.numMissedRuns)
            jobSub.AddTimeElement('NextRunTime', job.nextRunTime)
            jobSub.AddTimeElement('LastRunTime', job.lastRunTime)
            jobSub.AddSubElementWithText('Xml', job.xml)
            if job.state == RESULT_TASKSERVICEJOB_STATE_UNKNOWN:
                stateStr = 'UNKNOWN'
            elif job.state == RESULT_TASKSERVICEJOB_STATE_DISABLED:
                stateStr = 'DISABLED'
            elif job.state == RESULT_TASKSERVICEJOB_STATE_QUEUED:
                stateStr = 'QUEUED'
            elif job.state == RESULT_TASKSERVICEJOB_STATE_READY:
                stateStr = 'READY'
            elif job.state == RESULT_TASKSERVICEJOB_STATE_RUNNING:
                stateStr = 'RUNNING'
            else:
                stateStr = 'UNKNOWN'
            jobSub.AddAttribute('state', stateStr)
            if job.state == RESULT_TASKSERVICEJOB_COMPAT_UNKNOWN:
                compatStr = 'UNKNOWN'
            elif job.state == RESULT_TASKSERVICEJOB_COMPAT_AT:
                compatStr = 'AT'
            elif job.state == RESULT_TASKSERVICEJOB_COMPAT_V1:
                compatStr = 'V1'
            elif job.state == RESULT_TASKSERVICEJOB_COMPAT_V2:
                compatStr = 'V2'
            else:
                compatStr = 'UNKNOWN'
            jobSub.AddAttribute('compatibility', compatStr)
            _printTaskServiceQuery_Actions(output, jobmsg, jobSub)
            _printTaskServiceQuery_Principal(output, jobmsg, jobSub)
            _printTaskServiceQuery_Triggers(output, jobmsg, jobSub)

    return True


def _printTaskServiceQuery_flags(xml, flags):
    flagMap = {RESULT_TASKSERVICEJOB_FLAG_ENABLED: 'FlagEnabled',
       RESULT_TASKSERVICEJOB_FLAG_ALLOW_DEMAND_START: 'FlagAllowDemandStart',
       RESULT_TASKSERVICEJOB_FLAG_ALLOW_HARD_TERMINATE: 'FlagAllowHardTerminate',
       RESULT_TASKSERVICEJOB_FLAG_DISALLOW_START_IF_ON_BATTERIES: 'FlagDisallowStartIfOnBatteries',
       RESULT_TASKSERVICEJOB_FLAG_HIDDEN: 'FlagHidden',
       RESULT_TASKSERVICEJOB_FLAG_REQUIRE_NETWORK: 'FlagRequireNetwork',
       RESULT_TASKSERVICEJOB_FLAG_START_WHEN_AVAILABLE: 'FlagStartWhenAvailable',
       RESULT_TASKSERVICEJOB_FLAG_STOP_IF_GOING_ON_BATTERIES: 'FlagStopIfGoingOnBatteries',
       RESULT_TASKSERVICEJOB_FLAG_WAKE_TO_RUN: 'FlagWakeToRun'
       }
    for key in flagMap.keys():
        if flags & key == key:
            xml.AddSubElement(flagMap[key])


def _printTaskServiceQuery_Actions(output, msg, xml):
    while msg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION) != None:
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        actionMsg = msg.FindMessage(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION)
        action = ResultTaskServiceAction()
        action.Demarshal(actionMsg)
        actionSub = xml.AddSubElement('Action')
        actionSub.AddSubElementWithText('Id', action.id)
        if action.type == RESULT_TASKSERVICEJOB_ACTION_TYPE_UNKNOWN:
            actionStr = 'UNKNOWN'
        elif action.type == RESULT_TASKSERVICEJOB_ACTION_TYPE_EXEC:
            actionStr = 'EXEC'
            if actionMsg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_EXEC) != None:
                execAction = ResultTaskServiceActionExec()
                execAction.Demarshal(actionMsg)
                execSub = actionSub.AddSubElement('Exec')
                execSub.AddSubElementWithText('Path', execAction.path)
                execSub.AddSubElementWithText('Arguments', execAction.arguments)
                execSub.AddSubElementWithText('WorkingDir', execAction.workingDir)
        elif action.type == RESULT_TASKSERVICEJOB_ACTION_TYPE_COM_HANDLER:
            actionStr = 'COM'
            if actionMsg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_COM) != None:
                comAction = ResultTaskServiceActionCom()
                comAction.Demarshal(actionMsg)
                comSub = actionSub.AddSubElement('COM')
                comSub.AddSubElementWithText('ClassId', comAction.classId)
                comSub.AddSubElementWithText('Data', comAction.data)
        elif action.type == RESULT_TASKSERVICEJOB_ACTION_TYPE_SEND_EMAIL:
            actionStr = 'EMAIL'
        elif action.type == RESULT_TASKSERVICEJOB_ACTION_TYPE_SHOW_MESSAGE:
            actionStr = 'MESSAGE'
        else:
            actionStr = 'UNKNOWN'
        actionSub.AddAttribute('type', actionStr)

    return


def _printTaskServiceQuery_Principal(output, msg, xml):
    if msg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL) != None:
        principal = ResultTaskServicePrincipal()
        principal.Demarshal(msg)
        principalSub = xml.AddSubElement('Principal')
        principalSub.AddSubElementWithText('DisplayName', principal.displayName)
        principalSub.AddSubElementWithText('GroupId', principal.groupId)
        principalSub.AddSubElementWithText('Id', principal.id)
        principalSub.AddSubElementWithText('UserId', principal.userId)
        if principal.logonType == RESULT_TASKSERVICEJOB_LOGONTYPE_UNKNOWN:
            logonTypeStr = 'UNKNOWN'
        elif principal.logonType == RESULT_TASKSERVICEJOB_LOGONTYPE_NONE:
            logonTypeStr = 'NONE'
        elif principal.logonType == RESULT_TASKSERVICEJOB_LOGONTYPE_PASSWORD:
            logonTypeStr = 'PASSWORD'
        elif principal.logonType == RESULT_TASKSERVICEJOB_LOGONTYPE_S4U:
            logonTypeStr = 'S4U'
        elif principal.logonType == RESULT_TASKSERVICEJOB_LOGONTYPE_INTERACTIVE_TOKEN:
            logonTypeStr = 'INTERACTIVE'
        elif principal.logonType == RESULT_TASKSERVICEJOB_LOGONTYPE_GROUP:
            logonTypeStr = 'GROUP'
        elif principal.logonType == RESULT_TASKSERVICEJOB_LOGONTYPE_SERVICE_ACCOUNT:
            logonTypeStr = 'SERVICE'
        elif principal.logonType == RESULT_TASKSERVICEJOB_LOGONTYPE_INTERACTIVE_TOKEN_OR_PASSWORD:
            logonTypeStr = 'INTERACTIVE_OR_PASSWORD'
        else:
            logonTypeStr = 'UNKNOWN'
        principalSub.AddAttribute('logonType', logonTypeStr)
        if principal.runLevel == RESULT_TASKSERVICEJOB_RUNLEVEL_UNKNOWN:
            runLevelStr = 'UNKNOWN'
        elif principal.runLevel == RESULT_TASKSERVICEJOB_RUNLEVEL_LEAST:
            runLevelStr = 'LEAST'
        elif principal.runLevel == RESULT_TASKSERVICEJOB_RUNLEVEL_HIGHEST:
            runLevelStr = 'HIGHEST'
        else:
            runLevelStr = 'UNKNOWN'
        principalSub.AddAttribute('runLevel', runLevelStr)
    return


def _printTaskServiceQuery_Triggers(output, msg, xml):
    while msg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER) != None:
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        triggerMsg = msg.FindMessage(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER)
        trigger = ResultTaskServiceTrigger()
        trigger.Demarshal(triggerMsg)
        triggerSub = xml.AddSubElement('Trigger')
        if trigger.enabled:
            triggerSub.AddAttribute('enabled', 'true')
        else:
            triggerSub.AddAttribute('enabled', 'false')
        triggerSub.AddSubElementWithText('Id', trigger.id)
        triggerSub.AddSubElementWithText('StartBoundary', trigger.startBoundary)
        triggerSub.AddSubElementWithText('EndBoundary', trigger.endBoundary)
        triggerSub.AddSubElementWithText('ExecTimeLimit', trigger.execTimeLimit)
        repSub = triggerSub.AddSubElement('Repetition')
        if trigger.repetition.stopAtDurationEnd:
            repSub.AddAttribute('stopAtDurationEnd', 'true')
        else:
            repSub.AddAttribute('stopAtDurationEnd', 'false')
        repSub.AddSubElementWithText('Duration', trigger.repetition.duration)
        repSub.AddSubElementWithText('Interval', trigger.repetition.interval)
        if trigger.type == RESULT_TASKSERVICEJOB_TRIGGER_TYPE_UNKNOWN:
            triggerStr = 'UNKNOWN'
        elif trigger.type == RESULT_TASKSERVICEJOB_TRIGGER_TYPE_EVENT:
            triggerStr = 'EVENT'
            if triggerMsg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_EVENT) != None:
                eventTrigger = ResultTaskServiceTriggerEvent()
                eventTrigger.Demarshal(triggerMsg)
                eventSub = triggerSub.AddSubElement('EventTrigger')
                eventSub.AddSubElementWithText('Subscription', eventTrigger.subscription)
        elif trigger.type == RESULT_TASKSERVICEJOB_TRIGGER_TYPE_TIME:
            triggerStr = 'TIME'
            if triggerMsg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_TIME) != None:
                timeTrigger = ResultTaskServiceTriggerTime()
                timeTrigger.Demarshal(triggerMsg)
                timeSub = triggerSub.AddSubElement('TimeTrigger')
                timeSub.AddSubElementWithText('RandomDelay', timeTrigger.randomDelay)
        elif trigger.type == RESULT_TASKSERVICEJOB_TRIGGER_TYPE_DAILY:
            triggerStr = 'DAILY'
            if triggerMsg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_DAILY) != None:
                dailyTrigger = ResultTaskServiceTriggerDaily()
                dailyTrigger.Demarshal(triggerMsg)
                dailySub = triggerSub.AddSubElement('DailyTrigger')
                dailySub.AddSubElementWithText('RandomDelay', dailyTrigger.randomDelay)
                dailySub.AddSubElementWithText('DaysInterval', '%u' % dailyTrigger.daysInterval)
        elif trigger.type == RESULT_TASKSERVICEJOB_TRIGGER_TYPE_WEEKLY:
            triggerStr = 'WEEKLY'
            if triggerMsg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_WEEKLY) != None:
                weeklyTrigger = ResultTaskServiceTriggerWeekly()
                weeklyTrigger.Demarshal(triggerMsg)
                weeklySub = triggerSub.AddSubElement('WeeklyTrigger')
                weeklySub.AddSubElementWithText('RandomDelay', weeklyTrigger.randomDelay)
                dowSub = weeklySub.AddSubElement('DaysOfWeek')
                dowSub.AddAttribute('value', '0x%04x' % weeklyTrigger.daysOfWeek)
                if weeklyTrigger.daysOfWeek & 1:
                    dowSub.AddSubElement('Sunday')
                if weeklyTrigger.daysOfWeek & 2:
                    dowSub.AddSubElement('Monday')
                if weeklyTrigger.daysOfWeek & 4:
                    dowSub.AddSubElement('Tuesday')
                if weeklyTrigger.daysOfWeek & 8:
                    dowSub.AddSubElement('Wednesday')
                if weeklyTrigger.daysOfWeek & 16:
                    dowSub.AddSubElement('Thursday')
                if weeklyTrigger.daysOfWeek & 32:
                    dowSub.AddSubElement('Friday')
                if weeklyTrigger.daysOfWeek & 64:
                    dowSub.AddSubElement('Saturday')
        elif trigger.type == RESULT_TASKSERVICEJOB_TRIGGER_TYPE_MONTHLY:
            triggerStr = 'MONTHLY'
            if triggerMsg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY) != None:
                monthlyTrigger = ResultTaskServiceTriggerMonthly()
                monthlyTrigger.Demarshal(triggerMsg)
                monthlySub = triggerSub.AddSubElement('MonthlyTrigger')
                monthlySub.AddSubElementWithText('RandomDelay', monthlyTrigger.randomDelay)
                if monthlyTrigger.runOnLastDayOfMonth:
                    monthlySub.AddAttribute('runOnLastDayOfMonth', 'true')
                else:
                    monthlySub.AddAttribute('runOnLastDayOfMonth', 'false')
                domSub = monthlySub.AddSubElement('DaysOfMonth')
                domSub.AddAttribute('value', '0x%08x' % monthlyTrigger.daysOfMonth)
                i = 1
                while i <= 31:
                    if monthlyTrigger.daysOfMonth & 1 << i - 1:
                        domSub.AddSubElementWithText('Day', '%u' % i)
                    i = i + 1

                if monthlyTrigger.daysOfMonth & 2147483648L:
                    domSub.AddSubElement('Last')
                moySub = monthlySub.AddSubElement('MonthsOfYear')
                moySub.AddAttribute('value', '0x%04x' % monthlyTrigger.monthsOfYear)
                if monthlyTrigger.monthsOfYear & 1:
                    moySub.AddSubElement('January')
                if monthlyTrigger.monthsOfYear & 2:
                    moySub.AddSubElement('February')
                if monthlyTrigger.monthsOfYear & 4:
                    moySub.AddSubElement('March')
                if monthlyTrigger.monthsOfYear & 8:
                    moySub.AddSubElement('April')
                if monthlyTrigger.monthsOfYear & 16:
                    moySub.AddSubElement('May')
                if monthlyTrigger.monthsOfYear & 32:
                    moySub.AddSubElement('June')
                if monthlyTrigger.monthsOfYear & 64:
                    moySub.AddSubElement('July')
                if monthlyTrigger.monthsOfYear & 128:
                    moySub.AddSubElement('August')
                if monthlyTrigger.monthsOfYear & 256:
                    moySub.AddSubElement('September')
                if monthlyTrigger.monthsOfYear & 512:
                    moySub.AddSubElement('October')
                if monthlyTrigger.monthsOfYear & 1024:
                    moySub.AddSubElement('November')
                if monthlyTrigger.monthsOfYear & 2048:
                    moySub.AddSubElement('December')
        elif trigger.type == RESULT_TASKSERVICEJOB_TRIGGER_TYPE_MONTHLYDOW:
            triggerStr = 'MONTHLYDOW'
            if triggerMsg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW) != None:
                monthlyTrigger = ResultTaskServiceTriggerMonthlyDOW()
                monthlyTrigger.Demarshal(triggerMsg)
                monthlySub = triggerSub.AddSubElement('MonthlyDOWTrigger')
                monthlySub.AddSubElementWithText('RandomDelay', monthlyTrigger.randomDelay)
                if monthlyTrigger.runOnLastWeekOfMonth:
                    monthlySub.AddAttribute('runOnLastWeekOfMonth', 'true')
                else:
                    monthlySub.AddAttribute('runOnLastWeekOfMonth', 'false')
                dowSub = monthlySub.AddSubElement('DaysOfWeek')
                dowSub.AddAttribute('value', '0x%04x' % monthlyTrigger.daysOfWeek)
                if monthlyTrigger.daysOfWeek & 1:
                    dowSub.AddSubElement('Sunday')
                if monthlyTrigger.daysOfWeek & 2:
                    dowSub.AddSubElement('Monday')
                if monthlyTrigger.daysOfWeek & 4:
                    dowSub.AddSubElement('Tuesday')
                if monthlyTrigger.daysOfWeek & 8:
                    dowSub.AddSubElement('Wednesday')
                if monthlyTrigger.daysOfWeek & 16:
                    dowSub.AddSubElement('Thursday')
                if monthlyTrigger.daysOfWeek & 32:
                    dowSub.AddSubElement('Friday')
                if monthlyTrigger.daysOfWeek & 64:
                    dowSub.AddSubElement('Saturday')
                moySub = monthlySub.AddSubElement('MonthsOfYear')
                moySub.AddAttribute('value', '0x%04x' % monthlyTrigger.monthsOfYear)
                if monthlyTrigger.monthsOfYear & 1:
                    moySub.AddSubElement('January')
                if monthlyTrigger.monthsOfYear & 2:
                    moySub.AddSubElement('February')
                if monthlyTrigger.monthsOfYear & 4:
                    moySub.AddSubElement('March')
                if monthlyTrigger.monthsOfYear & 8:
                    moySub.AddSubElement('April')
                if monthlyTrigger.monthsOfYear & 16:
                    moySub.AddSubElement('May')
                if monthlyTrigger.monthsOfYear & 32:
                    moySub.AddSubElement('June')
                if monthlyTrigger.monthsOfYear & 64:
                    moySub.AddSubElement('July')
                if monthlyTrigger.monthsOfYear & 128:
                    moySub.AddSubElement('August')
                if monthlyTrigger.monthsOfYear & 256:
                    moySub.AddSubElement('September')
                if monthlyTrigger.monthsOfYear & 512:
                    moySub.AddSubElement('October')
                if monthlyTrigger.monthsOfYear & 1024:
                    moySub.AddSubElement('November')
                if monthlyTrigger.monthsOfYear & 2048:
                    moySub.AddSubElement('December')
                womSub = monthlySub.AddSubElement('WeeksOfMonth')
                womSub.AddAttribute('value', '0x%04x' % monthlyTrigger.weeksOfMonth)
                if monthlyTrigger.weeksOfMonth & 1:
                    womSub.AddSubElement('First')
                if monthlyTrigger.weeksOfMonth & 2:
                    womSub.AddSubElement('Second')
                if monthlyTrigger.weeksOfMonth & 4:
                    womSub.AddSubElement('Third')
                if monthlyTrigger.weeksOfMonth & 8:
                    womSub.AddSubElement('Fourth')
                if monthlyTrigger.weeksOfMonth & 16:
                    womSub.AddSubElement('Fifth')
                if monthlyTrigger.weeksOfMonth & 32:
                    womSub.AddSubElement('Last')
        elif trigger.type == RESULT_TASKSERVICEJOB_TRIGGER_TYPE_IDLE:
            triggerStr = 'IDLE'
        elif trigger.type == RESULT_TASKSERVICEJOB_TRIGGER_TYPE_REGISTRATION:
            triggerStr = 'REGISTRATION'
            if triggerMsg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_REGISTRATION) != None:
                regTrigger = ResultTaskServiceTriggerRegistration()
                regTrigger.Demarshal(triggerMsg)
                regSub = triggerSub.AddSubElement('RegistrationTrigger')
                regSub.AddSubElementWithText('Delay', regTrigger.delay)
        elif trigger.type == RESULT_TASKSERVICEJOB_TRIGGER_TYPE_BOOT:
            triggerStr = 'BOOT'
            if triggerMsg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_BOOT) != None:
                bootTrigger = ResultTaskServiceTriggerBoot()
                bootTrigger.Demarshal(triggerMsg)
                bootSub = triggerSub.AddSubElement('BootTrigger')
                bootSub.AddSubElementWithText('Delay', bootTrigger.delay)
        elif trigger.type == RESULT_TASKSERVICEJOB_TRIGGER_TYPE_LOGON:
            triggerStr = 'LOGON'
            if triggerMsg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_LOGON) != None:
                logonTrigger = ResultTaskServiceTriggerLogon()
                logonTrigger.Demarshal(triggerMsg)
                logonSub = triggerSub.AddSubElement('LogonTrigger')
                logonSub.AddSubElementWithText('Delay', logonTrigger.delay)
                logonSub.AddSubElementWithText('UserId', logonTrigger.userId)
        elif trigger.type == RESULT_TASKSERVICEJOB_TRIGGER_TYPE_SESSION_STATE_CHANGE:
            triggerStr = 'SESSION_STATE_CHANGE'
            if triggerMsg.PeekByKey(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_SESSION_STATE_CHANGE) != None:
                sscTrigger = ResultTaskServiceTriggerSessionStateChange()
                sscTrigger.Demarshal(triggerMsg)
                sscSub = triggerSub.AddSubElement('SessionStateChangeTrigger')
                sscSub.AddSubElementWithText('Delay', sscTrigger.delay)
                sscSub.AddSubElementWithText('UserId', sscTrigger.userId)
                if sscTrigger.change == RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_UNKNOWN:
                    changeStr = 'UNKNOWN'
                elif sscTrigger.change == RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_CONSOLE_CONNECT:
                    changeStr = 'CONSOLE_CONNECT'
                elif sscTrigger.change == RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_CONSOLE_DISCONNECT:
                    changeStr = 'CONSOLE_DISCONNECT'
                elif sscTrigger.change == RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_REMOTE_CONNECT:
                    changeStr = 'REMOTE_CONNECT'
                elif sscTrigger.change == RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_REMOTE_DISCONNECT:
                    changeStr = 'REMOTE_DISCONNECT'
                elif sscTrigger.change == RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_SESSION_LOCK:
                    changeStr = 'SESSION_LOCK'
                elif sscTrigger.change == RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_SESSION_UNLOCK:
                    changeStr = 'SESSION_UNLOCK'
                else:
                    changeStr = 'UNKNOWN'
                sscSub.AddAttribute('change', changeStr)
        else:
            triggerStr = 'UNKNOWN'
        triggerSub.AddAttribute('type', triggerStr)

    return


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)