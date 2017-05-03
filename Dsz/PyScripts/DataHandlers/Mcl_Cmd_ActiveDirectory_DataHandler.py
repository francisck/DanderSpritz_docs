# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_ActiveDirectory_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.survey.cmd.activedirectory', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('ActiveDirectory', 'activedirectory', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    if msg.GetCount() == 0:
        output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
        return True
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('AdData')
    for entry in msg:
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        if entry['key'] == MSG_KEY_RESULT_MODE:
            results = ResultMode()
            results.Demarshal(msg)
            sub = xml.AddSubElement('AdMode')
            if results.isMixed:
                sub.AddAttribute('mixed', 'true')
            else:
                sub.AddAttribute('mixed', 'false')
            sub.AddAttribute('name', results.domainName)
        elif entry['key'] == MSG_KEY_RESULT_INFO:
            results = ResultInfo()
            results.Demarshal(msg)
            sub = xml.AddSubElement('AdEntry')
            sub.AddSubElementWithText('Category', results.category)
            sub.AddSubElementWithText('Name', results.name)
            sub.AddSubElementWithText('DistinguishedName', results.dn)
        elif entry['key'] == MSG_KEY_RESULT_USER:
            results = ResultUser()
            results.Demarshal(msg)
            sub = xml.AddSubElement('AdUser')
            sub2 = sub.AddSubElement('Flags')
            if results.AccountDisabled:
                sub2.AddSubElement('AccountDisabled')
            if results.IsAccountLocked:
                sub2.AddSubElement('IsAccountLocked')
            if results.PasswordRequired:
                sub2.AddSubElement('PasswordRequired')
            if results.RequireUniquePassword:
                sub2.AddSubElement('RequireUniquePassword')
            if results.AccountExpirationDate.GetTimeType() != results.AccountExpirationDate.MCL_TIME_TYPE_NOT_A_TIME:
                sub.AddTimeElement('AccountExpirationDate', results.AccountExpirationDate)
            if results.LastFailedLogin.GetTimeType() != results.LastFailedLogin.MCL_TIME_TYPE_NOT_A_TIME:
                sub.AddTimeElement('LastFailedLogin', results.LastFailedLogin)
            if results.LastLogin.GetTimeType() != results.LastLogin.MCL_TIME_TYPE_NOT_A_TIME:
                sub.AddTimeElement('LastLogin', results.LastLogin)
            if results.LastLogoff.GetTimeType() != results.LastLogoff.MCL_TIME_TYPE_NOT_A_TIME:
                sub.AddTimeElement('LastLogoff', results.LastLogoff)
            if results.PasswordExpirationDate.GetTimeType() != results.PasswordExpirationDate.MCL_TIME_TYPE_NOT_A_TIME:
                sub.AddTimeElement('PasswordExpirationDate', results.PasswordExpirationDate)
            if results.PasswordLastChanged.GetTimeType() != results.PasswordLastChanged.MCL_TIME_TYPE_NOT_A_TIME:
                sub.AddTimeElement('PasswordLastChanged', results.PasswordLastChanged)
            sub.AddAttribute('badLoginCount', '%u' % results.BadLoginCount)
            sub.AddAttribute('maxStorage', '%u' % results.MaxStorage)
            sub.AddAttribute('passwordMinimumLength', '%u' % results.PasswordMinimumLength)
            sub.AddSubElementWithText('Department', results.Department)
            sub.AddSubElementWithText('Description', results.Description)
            sub.AddSubElementWithText('EmailAddress', results.EmailAddress)
            sub.AddSubElementWithText('LastName', results.LastName)
            sub.AddSubElementWithText('FirstName', results.FirstName)
            sub.AddSubElementWithText('FullName', results.FullName)
            sub.AddSubElementWithText('HomeDirectory', results.HomeDirectory)
            sub.AddSubElementWithText('HomePage', results.HomePage)
            sub.AddSubElementWithText('LoginScript', results.LoginScript)
            sub.AddSubElementWithText('Manager', results.Manager)
            sub.AddSubElementWithText('TelephoneNumber', results.OfficeNumber)
            sub.AddSubElementWithText('TelephoneHome', results.HomeNumber)
            sub.AddSubElementWithText('TelephoneMobile', results.CellNumber)
            sub.AddSubElementWithText('TelephonePager', results.PagerNumber)
            sub.AddSubElementWithText('FaxNumber', results.FaxNumber)
            sub.AddSubElementWithText('OfficeLocations', results.OfficeLocation)
            sub.AddSubElementWithText('Name', results.UserName)
        else:
            output.RecordError('Unhandled key (%u) returned to callback' % entry['key'])
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return True

    output.RecordXml(xml)
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