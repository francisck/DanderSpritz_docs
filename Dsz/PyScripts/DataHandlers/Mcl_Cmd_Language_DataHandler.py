# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Language_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.survey.cmd.language', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Language', 'language', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    results = Result()
    results.Demarshal(msg)
    localeLangEnglish = _translateLanguageId(results.locale.languageValue)
    if len(localeLangEnglish) == 0:
        localeLangEnglish = results.locale.language
    uiLangEnglish = _translateLanguageId(results.ui.languageValue)
    if len(uiLangEnglish) == 0:
        uiLangEnglish = results.ui.language
    installedLangEnglish = _translateLanguageId(results.installed.languageValue)
    if len(installedLangEnglish) == 0:
        installedLangEnglish = results.installed.language
    rtn = mcl.target.CALL_SUCCEEDED
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Languages')
    sub = xml.AddSubElement('LocaleLanguage')
    sub.AddAttribute('value', '0x%08x' % results.locale.languageValue)
    sub.AddSubElementWithText('English', localeLangEnglish)
    sub.AddSubElementWithText('Native', results.locale.language)
    sub = xml.AddSubElement('UILanguage')
    sub.AddAttribute('value', '0x%08x' % results.ui.languageValue)
    sub.AddSubElementWithText('English', uiLangEnglish)
    sub.AddSubElementWithText('Native', results.ui.language)
    sub = xml.AddSubElement('InstalledLanguage')
    sub.AddAttribute('value', '0x%08x' % results.installed.languageValue)
    sub.AddSubElementWithText('English', installedLangEnglish)
    sub.AddSubElementWithText('Native', results.installed.language)
    sub = xml.AddSubElement('OSLanguages')
    sub.AddAttribute('osFile', results.osFile)
    sub.AddAttribute('availableLanguages', '%u' % results.numAvailLanguages)
    if results.fileCode != 0:
        rtn = mcl.target.CALL_FAILED
        error = output.TranslateOsError(results.fileCode)
        sub.AddSubElementWithText('QueryError', error)
    i = 0
    while i < results.numReturned:
        info = ResultLanguageInfo()
        info.Demarshal(msg)
        eng = _translateLanguageId(info.languageValue)
        if len(eng) == 0:
            eng = info.language
        sub2 = sub.AddSubElement('OSLanguage')
        sub2.AddAttribute('value', '0x%08x' % info.languageValue)
        sub2.AddSubElementWithText('English', eng)
        sub2.AddSubElementWithText('Native', info.language)
        i = i + 1

    output.RecordXml(xml)
    output.EndWithStatus(rtn)
    return True


def _translateLanguageId(id):
    primaryId = id & 1023
    secondaryId = id >> 10 & 63
    primary = ''
    sub = ''
    if primaryId == 54:
        primary = 'Afrikaans'
        if secondaryId == 1:
            sub = 'South Africa'
    elif primaryId == 28:
        primary = 'Albanian'
        if secondaryId == 1:
            sub = 'Albania'
    elif primaryId == 132:
        primary = 'Alsatian'
        if secondaryId == 1:
            sub = 'France'
    elif primaryId == 94:
        primary = 'Amharic'
        if secondaryId == 1:
            sub = 'Ethiopia'
    elif primaryId == 1:
        primary = 'Arabic'
        if secondaryId == 1:
            sub = 'Saudi Arabia'
        elif secondaryId == 2:
            sub = 'Iraq'
        elif secondaryId == 3:
            sub = 'Egypt'
        elif secondaryId == 4:
            sub = 'Libya'
        elif secondaryId == 5:
            sub = 'Algeria'
        elif secondaryId == 6:
            sub = 'Morocco'
        elif secondaryId == 7:
            sub = 'Tunisia'
        elif secondaryId == 8:
            sub = 'Oman'
        elif secondaryId == 9:
            sub = 'Yemen'
        elif secondaryId == 10:
            sub = 'Syria'
        elif secondaryId == 11:
            sub = 'Jordan'
        elif secondaryId == 12:
            sub = 'Lebanon'
        elif secondaryId == 13:
            sub = 'Kuwait'
        elif secondaryId == 14:
            sub = 'U.A.E'
        elif secondaryId == 15:
            sub = 'Bahrain'
        elif secondaryId == 16:
            sub = 'Qatar'
    elif primaryId == 43:
        primary = 'Armenian'
        if secondaryId == 1:
            sub = 'Armenia'
    elif primaryId == 77:
        primary = 'Assamese'
        if secondaryId == 1:
            sub = 'India'
    elif primaryId == 44:
        primary = 'Azeri'
        if secondaryId == 1:
            sub = 'Latin'
        elif secondaryId == 2:
            sub = 'Cyrillic'
    elif primaryId == 109:
        primary = 'Bashkir'
        if secondaryId == 1:
            sub = 'Russia'
    elif primaryId == 45:
        primary = 'Basque'
        if secondaryId == 1:
            sub = 'Basque'
    elif primaryId == 35:
        primary = 'Belarusian'
        if secondaryId == 1:
            sub = 'Belarus'
    elif primaryId == 69:
        primary = 'Bengali'
        if secondaryId == 1:
            sub = 'India'
        elif secondaryId == 2:
            sub = 'Bangladesh'
    elif primaryId == 126:
        primary = 'Breton'
        if secondaryId == 1:
            sub = 'France'
    elif primaryId == 2:
        primary = 'Bulgarian'
        if secondaryId == 1:
            sub = 'Bulgaria'
    elif primaryId == 3:
        primary = 'Catalan'
        if secondaryId == 1:
            sub = 'Catalan'
    elif primaryId == 4:
        primary = 'Chinese'
        if secondaryId == 1:
            sub = 'Taiwan'
        elif secondaryId == 2:
            sub = 'PR China'
        elif secondaryId == 3:
            sub = 'Hong Kong S.A.R., P.R.C.'
        elif secondaryId == 4:
            sub = 'Singapore'
        elif secondaryId == 5:
            sub = 'Macau S.A.R.'
    elif primaryId == 131:
        primary = 'Corsican'
        if secondaryId == 1:
            sub = 'France'
    elif primaryId == 5:
        primary = 'Czech'
        if secondaryId == 1:
            sub = 'Czech Republic'
    elif primaryId == 6:
        primary = 'Danish'
        if secondaryId == 1:
            sub = 'Denmark'
    elif primaryId == 140:
        primary = 'Dari'
        if secondaryId == 1:
            sub = 'Afghanistan'
    elif primaryId == 101:
        primary = 'Divehi'
        if secondaryId == 1:
            sub = 'Maldives'
    elif primaryId == 19:
        primary = 'Dutch'
        if secondaryId == 1:
            sub = ''
        elif secondaryId == 2:
            sub = 'Belgian'
    elif primaryId == 9:
        primary = 'English'
        if secondaryId == 1:
            sub = 'USA'
        elif secondaryId == 2:
            sub = 'UK'
        elif secondaryId == 3:
            sub = 'Australian'
        elif secondaryId == 4:
            sub = 'Canadian'
        elif secondaryId == 5:
            sub = 'New Zealand'
        elif secondaryId == 6:
            sub = 'Irish'
        elif secondaryId == 7:
            sub = 'South Africa'
        elif secondaryId == 8:
            sub = 'Jamaica'
        elif secondaryId == 9:
            sub = 'Caribbean'
        elif secondaryId == 10:
            sub = 'Belize'
        elif secondaryId == 11:
            sub = 'Trinidad'
        elif secondaryId == 12:
            sub = 'Zimbabwe'
        elif secondaryId == 13:
            sub = 'Philippines'
        elif secondaryId == 16:
            sub = 'India'
        elif secondaryId == 17:
            sub = 'Malaysia'
        elif secondaryId == 18:
            sub = 'Singapore'
    elif primaryId == 37:
        primary = 'Estonian'
        if secondaryId == 1:
            sub = 'Estonia'
    elif primaryId == 56:
        primary = 'Faeroese'
        if secondaryId == 1:
            sub = 'Faroe Islands'
    elif primaryId == 41:
        primary = 'Farsi'
        if secondaryId == 1:
            sub = 'Iran'
    elif primaryId == 100:
        primary = 'Filipino'
        if secondaryId == 1:
            sub = 'Philippines'
    elif primaryId == 11:
        primary = 'Finnish'
        if secondaryId == 1:
            sub = 'Finland'
    elif primaryId == 12:
        primary = 'French'
        if secondaryId == 1:
            sub = ''
        elif secondaryId == 2:
            sub = 'Belgian'
        elif secondaryId == 3:
            sub = 'Canadian'
        elif secondaryId == 4:
            sub = 'Swiss'
        elif secondaryId == 5:
            sub = 'Luxembourg'
        elif secondaryId == 6:
            sub = 'Monaco'
    elif primaryId == 98:
        primary = 'Frisian'
        if secondaryId == 1:
            sub = 'Netherlands'
    elif primaryId == 86:
        primary = 'Galician'
        if secondaryId == 1:
            sub = 'Galician'
    elif primaryId == 55:
        primary = 'Georgian'
        if secondaryId == 1:
            sub = 'Georgia'
    elif primaryId == 7:
        primary = 'German'
        if secondaryId == 1:
            sub = ''
        elif secondaryId == 2:
            sub = 'Swiss'
        elif secondaryId == 3:
            sub = 'Austrian'
        elif secondaryId == 4:
            sub = 'Luxembourg'
        elif secondaryId == 5:
            sub = 'Liechtenstein'
    elif primaryId == 8:
        primary = 'Greek'
        if secondaryId == 1:
            sub = 'Greece'
    elif primaryId == 111:
        primary = 'Greenlandic'
        if secondaryId == 1:
            sub = 'Greenland'
    elif primaryId == 71:
        primary = 'Gujarati'
        if secondaryId == 1:
            sub = 'India (Gujarati Script)'
    elif primaryId == 104:
        primary = 'Hausa'
        if secondaryId == 1:
            sub = 'Latin, Nigeria'
    elif primaryId == 13:
        primary = 'Hebrew'
        if secondaryId == 1:
            sub = 'Israel'
    elif primaryId == 57:
        primary = 'Hindi'
        if secondaryId == 1:
            sub = 'India'
    elif primaryId == 14:
        primary = 'Hungarian'
        if secondaryId == 1:
            sub = 'Hungary'
    elif primaryId == 15:
        primary = 'Icelandic'
        if secondaryId == 1:
            sub = 'Iceland'
    elif primaryId == 112:
        primary = 'Igbo'
        if secondaryId == 1:
            sub = 'Nigeria'
    elif primaryId == 33:
        primary = 'Indonesian'
        if secondaryId == 1:
            sub = 'Indonesia'
    elif primaryId == 93:
        primary = 'Inuktitut'
        if secondaryId == 1:
            sub = 'Canada - Syllabics'
        elif secondaryId == 2:
            sub = 'Canada - Latin'
    elif primaryId == 60:
        primary = 'Irish'
        if secondaryId == 2:
            sub = 'Ireland'
    elif primaryId == 16:
        primary = 'Italian'
        if secondaryId == 1:
            sub = ''
        elif secondaryId == 2:
            sub = 'Swiss'
    elif primaryId == 17:
        primary = 'Japanese'
        if secondaryId == 1:
            sub = 'Japan'
    elif primaryId == 75:
        primary = 'Kannada'
        if secondaryId == 1:
            sub = 'India (Kannada Script)'
    elif primaryId == 96:
        primary = 'Kashmiri'
        if secondaryId == 2:
            sub = 'South Asia'
    elif primaryId == 63:
        primary = 'Kazak'
        if secondaryId == 1:
            sub = 'Kazakhstan'
    elif primaryId == 83:
        primary = 'Khmer'
        if secondaryId == 1:
            sub = 'Cambodia'
    elif primaryId == 134:
        primary = 'Kiche'
        if secondaryId == 1:
            sub = 'Guatemala'
    elif primaryId == 135:
        primary = 'Kinyarwanda'
        if secondaryId == 1:
            sub = 'Rwanda'
    elif primaryId == 87:
        primary = 'Konkani'
        if secondaryId == 1:
            sub = 'India'
    elif primaryId == 18:
        primary = 'Korean'
        if secondaryId == 1:
            sub = 'Extended Wansung'
    elif primaryId == 64:
        primary = 'Kyrgyz'
        if secondaryId == 1:
            sub = 'Kyrgyzstan'
    elif primaryId == 84:
        primary = 'Lao'
        if secondaryId == 1:
            sub = 'Lao PDR'
    elif primaryId == 38:
        primary = 'Latvian'
        if secondaryId == 1:
            sub = 'Latvia'
    elif primaryId == 39:
        primary = 'Lithuanian'
    elif primaryId == 110:
        primary = 'Luxembourgish'
        if secondaryId == 1:
            sub = 'Luxembourg'
    elif primaryId == 47:
        primary = 'Macedonian'
        if secondaryId == 1:
            sub = 'Macedonia (FYROM)'
    elif primaryId == 62:
        primary = 'Malay'
        if secondaryId == 1:
            sub = 'Malaysia'
        elif secondaryId == 2:
            sub = 'Brunei Darussalam'
    elif primaryId == 76:
        primary = 'Malayalam'
        if secondaryId == 1:
            sub = 'India (Malayalam Script)'
    elif primaryId == 58:
        primary = 'Maltese'
        if secondaryId == 1:
            sub = 'Malta'
    elif primaryId == 88:
        primary = 'Manipuri'
    elif primaryId == 129:
        primary = 'Maori'
        if secondaryId == 1:
            sub = 'New Zealand'
    elif primaryId == 122:
        primary = 'Mapudungun'
        if secondaryId == 1:
            sub = 'Chile'
    elif primaryId == 78:
        primary = 'Marathi'
        if secondaryId == 1:
            sub = 'India'
    elif primaryId == 124:
        primary = 'Mohawk'
        if secondaryId == 1:
            sub = 'Mohawk'
    elif primaryId == 80:
        primary = 'Mongolian'
        if secondaryId == 1:
            sub = 'Cyrillic, Mongolia'
        elif secondaryId == 2:
            sub = 'PRC'
    elif primaryId == 97:
        primary = 'Nepali'
        if secondaryId == 1:
            sub = 'Nepal'
        elif secondaryId == 2:
            sub = 'India'
    elif primaryId == 20:
        primary = 'Norwegian'
        if secondaryId == 1:
            sub = 'Bokmal'
        elif secondaryId == 2:
            sub = 'Nynorsk'
    elif primaryId == 130:
        primary = 'Occitan'
        if secondaryId == 1:
            sub = 'France'
    elif primaryId == 72:
        primary = 'Oriya'
        if secondaryId == 1:
            sub = 'India (Oriya Script)'
    elif primaryId == 99:
        primary = 'Pashto'
        if secondaryId == 1:
            sub = 'Afghanistan'
    elif primaryId == 21:
        primary = 'Polish'
        if secondaryId == 1:
            sub = 'Poland'
    elif primaryId == 22:
        primary = 'Portuguese'
        if secondaryId == 1:
            sub = 'Brazilian'
        elif secondaryId == 2:
            sub = ''
    elif primaryId == 70:
        primary = 'Punjabi'
        if secondaryId == 1:
            sub = 'India (Gurmukhi Script)'
    elif primaryId == 107:
        primary = 'Quechua'
        if secondaryId == 1:
            sub = 'Bolivia'
        elif secondaryId == 2:
            sub = 'Ecuador'
        elif secondaryId == 3:
            sub = 'Peru'
    elif primaryId == 24:
        primary = 'Romanian'
        if secondaryId == 1:
            sub = 'Romania'
    elif primaryId == 23:
        primary = 'Romansh'
        if secondaryId == 1:
            sub = 'Switzerland'
    elif primaryId == 25:
        primary = 'Russian'
        if secondaryId == 1:
            sub = 'Russia'
    elif primaryId == 59:
        primary = 'Sami'
        if secondaryId == 1:
            sub = 'Northern Sami (Norway)'
        elif secondaryId == 2:
            sub = 'Northern Sami (Sweden)'
        elif secondaryId == 3:
            sub = 'Northern Sami (Finland)'
        elif secondaryId == 4:
            sub = 'Lule Sami (Norway)'
        elif secondaryId == 5:
            sub = 'Lule Sami (Sweden)'
        elif secondaryId == 6:
            sub = 'Southern Sami (Norway)'
        elif secondaryId == 7:
            sub = 'Southern Sami (Sweden)'
        elif secondaryId == 8:
            sub = 'Skolt Sami (Finland)'
        elif secondaryId == 9:
            sub = 'Inari Sami (Finland)'
    elif primaryId == 79:
        primary = 'Sanskrit'
        if secondaryId == 1:
            sub = 'India'
    elif primaryId == 26:
        primary = 'Serbian'
        if secondaryId == 1:
            sub = 'Croatian (Croatia)'
        elif secondaryId == 2:
            sub = 'Latin'
        elif secondaryId == 3:
            sub = 'Cyrillic'
        elif secondaryId == 4 or secondaryId == 5 or secondaryId == 6:
            sub = 'Bosnia and Herzegovina - Latin'
        elif secondaryId == 7 or secondaryId == 8:
            sub = 'Bosnia and Herzegovina - Cyrillic'
    elif primaryId == 89:
        primary = 'Sindhi'
        if secondaryId == 1:
            sub = 'India'
        elif secondaryId == 2:
            sub = 'Pakistan'
    elif primaryId == 91:
        primary = 'Sinhalese'
        if secondaryId == 1:
            sub = 'Sri Lanka'
    elif primaryId == 27:
        primary = 'Slovak'
        if secondaryId == 1:
            sub = 'Slovakia'
    elif primaryId == 36:
        primary = 'Slovenian'
        if secondaryId == 1:
            sub = 'Slovenia'
    elif primaryId == 46:
        primary = 'Sorbian'
        if secondaryId == 1:
            sub = 'Upper Sorbian (Germany)'
        elif secondaryId == 2:
            sub = 'Lower Sorbian (Germany)'
    elif primaryId == 108:
        primary = 'Sotho'
        if secondaryId == 1:
            sub = 'South Africa'
    elif primaryId == 10:
        primary = 'Spanish'
        if secondaryId == 1:
            sub = 'Castilian'
        elif secondaryId == 2:
            sub = 'Mexican'
        elif secondaryId == 3:
            sub = 'Modern'
        elif secondaryId == 4:
            sub = 'Guatemala'
        elif secondaryId == 5:
            sub = 'Costa Rica'
        elif secondaryId == 6:
            sub = 'Panama'
        elif secondaryId == 7:
            sub = 'Dominican Republic'
        elif secondaryId == 8:
            sub = 'Venezuela'
        elif secondaryId == 9:
            sub = 'Colombia'
        elif secondaryId == 10:
            sub = 'Peru'
        elif secondaryId == 11:
            sub = 'Argentina'
        elif secondaryId == 12:
            sub = 'Ecuador'
        elif secondaryId == 13:
            sub = 'Chile'
        elif secondaryId == 14:
            sub = 'Uruguay'
        elif secondaryId == 15:
            sub = 'Paraguay'
        elif secondaryId == 16:
            sub = 'Bolivia'
        elif secondaryId == 17:
            sub = 'El Salvador'
        elif secondaryId == 18:
            sub = 'Honduras'
        elif secondaryId == 19:
            sub = 'Nicaragua'
        elif secondaryId == 20:
            sub = 'Puerto Rico'
        elif secondaryId == 21:
            sub = 'United States'
    elif primaryId == 65:
        primary = 'Swahili'
        if secondaryId == 1:
            sub = 'Kenya'
    elif primaryId == 29:
        primary = 'Swedish'
        if secondaryId == 1:
            sub = ''
        elif secondaryId == 2:
            sub = 'Finland'
    elif primaryId == 90:
        primary = 'Syriac'
        if secondaryId == 1:
            sub = 'Syria'
    elif primaryId == 40:
        primary = 'Tajik'
        if secondaryId == 1:
            sub = 'Tajikistan'
    elif primaryId == 95:
        primary = 'Tamazight'
        if secondaryId == 1:
            sub = 'Latin, Algeria'
    elif primaryId == 73:
        primary = 'Tamil'
        if secondaryId == 1:
            sub = 'India'
    elif primaryId == 68:
        primary = 'Tatar'
        if secondaryId == 1:
            sub = 'Russia'
    elif primaryId == 74:
        primary = 'Telugu'
        if secondaryId == 1:
            sub = 'India (Telugu Script)'
    elif primaryId == 30:
        primary = 'Thai'
        if secondaryId == 1:
            sub = 'Thailand'
    elif primaryId == 81:
        primary = 'Tibetan'
        if secondaryId == 1:
            sub = 'PRC'
    elif primaryId == 115:
        primary = 'Tigrigna'
        if secondaryId == 1:
            sub = 'Eritrea'
    elif primaryId == 50:
        primary = 'Tswana'
        if secondaryId == 1:
            sub = 'Setswana / Tswana (South Africa)'
    elif primaryId == 31:
        primary = 'Turkish'
        if secondaryId == 1:
            sub = 'Turkey'
    elif primaryId == 66:
        primary = 'Turkmen'
        if secondaryId == 1:
            sub = 'Turkmenistan'
    elif primaryId == 128:
        primary = 'Uighur'
        if secondaryId == 1:
            sub = 'PRC'
    elif primaryId == 34:
        primary = 'Ukrainian'
        if secondaryId == 1:
            sub = 'Ukraine'
    elif primaryId == 32:
        primary = 'Urdu'
        if secondaryId == 1:
            sub = 'Pakistan'
        elif secondaryId == 2:
            sub = 'India'
    elif primaryId == 67:
        primary = 'Uzbek'
        if secondaryId == 1:
            sub = 'Latin'
        elif secondaryId == 2:
            sub = 'Cyrillic'
    elif primaryId == 42:
        primary = 'Vietnamese'
        if secondaryId == 1:
            sub = 'Vietnam'
    elif primaryId == 82:
        primary = 'Welsh'
        if secondaryId == 1:
            sub = 'United Kingdom'
    elif primaryId == 136:
        primary = 'Wolof'
        if secondaryId == 1:
            sub = 'Senegal'
    elif primaryId == 52:
        primary = 'Xhosa'
        if secondaryId == 1:
            sub = 'South Africa'
    elif primaryId == 133:
        primary = 'Yakut'
        if secondaryId == 1:
            sub = 'Russia'
    elif primaryId == 120:
        primary = 'Yi'
        if secondaryId == 1:
            sub = 'PRC'
    elif primaryId == 106:
        primary = 'Yoruba'
        if secondaryId == 1:
            sub = 'Nigeria'
    elif primaryId == 53:
        primary = 'Zulu'
        if secondaryId == 1:
            sub = 'South Africa'
    else:
        return ''
    if len(primary) > 0 and len(sub) > 0:
        return '%s (%s)' % (primary, sub)
    else:
        return primary


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)