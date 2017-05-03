# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _UserAssist.py
import dsz
import dsz.lp
import dsz.user
import datetime
import socket
import sys

def main():
    params = dsz.lp.cmdline.ParseCommandLine(sys.argv, '_UserAssist.txt')
    if len(params) == 0:
        return False
    try:
        verbose = False
        if 'verbose' in params:
            verbose = True
        if params['type'][0].lower() == 'current':
            if not GetUserInfo('C', '', verbose):
                return False
        elif params['type'][0].lower() == 'all':
            dsz.control.echo.Off()
            if not dsz.cmd.Run('registryquery -hive U', dsz.RUN_FLAG_RECORD):
                dsz.control.echo.On()
                raise RuntimeError, 'Error querying users'
            dsz.control.echo.On()
            users = dsz.cmd.data.Get('Key::Subkey::Name', dsz.TYPE_STRING)
            for user in users:
                GetUserInfo('U', '%s' % user, verbose)

        elif params['type'][0].lower() == 'user':
            if 'user' not in params:
                dsz.ui.Echo('-user option must be specified', dsz.ERROR)
                return False
            if not GetUserInfo('U', '%s' % params['user'][0], verbose):
                return False
        else:
            dsz.ui.Echo('Unknown type')
            return False
    except RuntimeError as err:
        dsz.ui.Echo('%s' % err, dsz.ERROR)

    return True


def GetUserInfo(hive, user='', verbose=False):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if user == '':
        userName = dsz.user.GetCurrent()
    else:
        userName = user
        try:
            if dsz.cmd.Run('sidlookup -name %s' % user, dsz.RUN_FLAG_RECORD):
                userName = dsz.cmd.data.Get('Sid::Name', dsz.TYPE_STRING)[0]
        except:
            pass

    win7 = dsz.version.checks.windows.Is7OrGreater()
    if user == '':
        fullkey = 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\UserAssist'
    else:
        fullkey = '%s\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\UserAssist' % user
    if not dsz.cmd.Run('registryquery -hive %s -key "%s" -recursive' % (hive, fullkey), dsz.RUN_FLAG_RECORD):
        return False
    subkeys = dsz.cmd.data.Get('Key[0]::Subkey::Name', dsz.TYPE_STRING)
    allkeys = dsz.cmd.data.Get('Key::Name', dsz.TYPE_STRING)
    dsz.ui.Echo('------------------------------------------------------------------')
    dsz.ui.Echo('User: %s' % userName)
    dsz.ui.Echo('------------------------------------------------------------------')
    dsz.script.data.Start('User')
    dsz.script.data.Add('Name', userName, dsz.TYPE_STRING)
    for guid in subkeys:
        dsz.script.CheckStop()
        i = 0
        while i < len(allkeys):
            dsz.script.CheckStop()
            if allkeys[i] != '%s\\%s\\Count' % (fullkey, guid):
                i += 1
                continue
            values = dsz.cmd.data.Get('Key[%u]::Value' % i, dsz.TYPE_OBJECT)
            if win7:
                DecodeWin7(values, verbose)
            else:
                DecodePreWin7(values, verbose)
            i += 1

    dsz.script.data.Store()
    return True


def DecodePreWin7(values, verbose=False):
    ignoreTypes = list()
    if not verbose:
        ignoreTypes.append('UEME_UITOOLBAR')
        ignoreTypes.append('UEME_UIHOTKEY')
        ignoreTypes.append('UEME_RUNWMCMD')
        ignoreTypes.append('UEME_UISCUT')
        ignoreTypes.append('UEME_UIQCUT')
        ignoreTypes.append('UEME_CTLSESSION')
        ignoreTypes.append('UEME_CTLCUACount')
    i = 0
    while i < len(values):
        dsz.script.CheckStop()
        try:
            name = dsz.cmd.data.ObjectGet(values[i], 'Name', dsz.TYPE_STRING)
            value = dsz.cmd.data.ObjectGet(values[i], 'Value', dsz.TYPE_STRING)
            type = dsz.cmd.data.ObjectGet(values[i], 'Type', dsz.TYPE_STRING)
            j = 0
            while j < len(name):
                decodedName = rot13decode(name[j])
                nameParts = decodedName.split(':', 1)
                ignore = False
                for ignored in ignoreTypes:
                    if nameParts[0] == ignored:
                        ignore = True
                        break

                dsz.script.data.Start('Value')
                dsz.script.data.Add('Type', nameParts[0], dsz.TYPE_STRING)
                if len(nameParts) > 1:
                    dsz.script.data.Add('Data', nameParts[1], dsz.TYPE_STRING)
                if not ignore:
                    dsz.ui.Echo('%s' % nameParts[0])
                    if len(nameParts) > 1:
                        dsz.ui.Echo('      Data : %s' % nameParts[1])
                if type[j] == 'REG_BINARY':
                    if len(value[j]) == 32:
                        session = socket.ntohl(int(value[j][0:8], 16))
                        count = socket.ntohl(int(value[j][8:16], 16))
                        timestamp2 = socket.ntohl(int(value[j][16:24], 16))
                        timestamp1 = socket.ntohl(int(value[j][24:32], 16))
                        timestamp = long('%08x%08x' % (timestamp1, timestamp2), 16)
                        if nameParts[0] == 'UEME_RUNPATH':
                            count -= 5
                        dsz.script.data.Add('Session', '%u' % session, dsz.TYPE_INT)
                        dsz.script.data.Add('Count', '%u' % count, dsz.TYPE_INT)
                        if not ignore:
                            if verbose:
                                dsz.ui.Echo('   Session : %u' % session)
                            dsz.ui.Echo('     Count : %u' % count)
                        if timestamp > 0:
                            timestamp /= 10000000
                            timestamp -= 11644473600L
                            t = datetime.datetime.fromtimestamp(timestamp)
                            dsz.script.data.Add('Timestamp', t.ctime(), dsz.TYPE_STRING)
                            if not ignore:
                                dsz.ui.Echo(' Last Used : %s' % t.ctime())
                dsz.script.data.End()
                j += 1

        except:
            pass

        i += 1

    return True


def DecodeWin7(values, verbose=False):
    ignoreTypes = list()
    if not verbose:
        ignoreTypes.append('UEME_CTLSESSION')
        ignoreTypes.append('UEME_CTLCUACount')
    i = 0
    while i < len(values):
        dsz.script.CheckStop()
        try:
            name = dsz.cmd.data.ObjectGet(values[i], 'Name', dsz.TYPE_STRING)
            value = dsz.cmd.data.ObjectGet(values[i], 'Value', dsz.TYPE_STRING)
            type = dsz.cmd.data.ObjectGet(values[i], 'Type', dsz.TYPE_STRING)
            j = 0
            while j < len(name):
                decodedName = rot13decode(name[j])
                if decodedName.startswith('UEME_'):
                    nameParts = decodedName.split(':', 1)
                else:
                    nameParts = [
                     'UEME_RUNPATH', decodedName]
                ignore = False
                for ignored in ignoreTypes:
                    if nameParts[0] == ignored:
                        ignore = True
                        break

                dsz.script.data.Start('Value')
                dsz.script.data.Add('Type', nameParts[0], dsz.TYPE_STRING)
                if len(nameParts) > 1:
                    nameParts[1] = translateKnownFolders(nameParts[1])
                    dsz.script.data.Add('Data', nameParts[1], dsz.TYPE_STRING)
                if not ignore:
                    dsz.ui.Echo('%s' % nameParts[0])
                    if len(nameParts) > 1:
                        dsz.ui.Echo('      Data : %s' % nameParts[1])
                if type[j] == 'REG_BINARY':
                    if len(value[j]) == 144:
                        count = socket.ntohl(int(value[j][8:16], 16))
                        timestamp2 = socket.ntohl(int(value[j][120:128], 16))
                        timestamp1 = socket.ntohl(int(value[j][128:136], 16))
                        timestamp = long('%08x%08x' % (timestamp1, timestamp2), 16)
                        dsz.script.data.Add('Count', '%u' % count, dsz.TYPE_INT)
                        if not ignore:
                            dsz.ui.Echo('     Count : %u' % count)
                        if timestamp > 0:
                            timestamp /= 10000000
                            timestamp -= 11644473600L
                            t = datetime.datetime.utcfromtimestamp(timestamp)
                            dsz.script.data.Add('Timestamp', t.ctime(), dsz.TYPE_STRING)
                            if not ignore:
                                dsz.ui.Echo(' Last Used : %s' % t.ctime())
                dsz.script.data.End()
                j += 1

        except:
            pass

        i += 1

    return True


def rot13decode(text):
    rtnText = ''
    for x in range(len(text)):
        dsz.script.CheckStop()
        byte = ord(text[x])
        cap = byte & 32
        byte = byte & ~cap
        if byte >= ord('A') and byte <= ord('Z'):
            byte = (byte - ord('A') + 13) % 26 + ord('A')
        byte = byte | cap
        rtnText = rtnText + chr(byte)

    return rtnText


def translateKnownFolders(folder):
    folder = folder.replace('{D20BEEC4-5CA8-4905-AE3B-BF251EA09B53}', '%Network%')
    folder = folder.replace('{0AC0837C-BBF8-452A-850D-79D08E667CA7}', '%ComputerFolder%')
    folder = folder.replace('{4D9F7874-4E0C-4904-967B-40B0D20C3E4B}', '%InternetFolder%')
    folder = folder.replace('{82A74AEB-AEB4-465C-A014-D097EE346D63}', '%ControlPanelFolder%')
    folder = folder.replace('{76FC4E2D-D6AD-4519-A663-37BD56068185}', '%PrintersFolder%')
    folder = folder.replace('{43668BF8-C14E-49B2-97C9-747784D784B7}', '%SyncManagerFolder%')
    folder = folder.replace('{0F214138-B1D3-4a90-BBA9-27CBC0C5389A}', '%SyncSetupFolder%')
    folder = folder.replace('{4bfefb45-347d-4006-a5be-ac0cb0567192}', '%ConflictFolder%')
    folder = folder.replace('{289a9a43-be44-4057-a41b-587a76d7e7f9}', '%SyncResultsFolder%')
    folder = folder.replace('{B7534046-3ECB-4C18-BE4E-64CD4CB7D6AC}', '%RecycleBinFolder%')
    folder = folder.replace('{6F0CD92B-2E97-45D1-88FF-B0D186B8DEDD}', '%ConnectionsFolder%')
    folder = folder.replace('{FD228CB7-AE11-4AE3-864C-16F3910AB8FE}', '%Fonts%')
    folder = folder.replace('{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}', '%Desktop%')
    folder = folder.replace('{B97D20BB-F46A-4C97-BA10-5E3608430854}', '%Startup%')
    folder = folder.replace('{A77F5D77-2E2B-44C3-A6A2-ABA601054A51}', '%Programs%')
    folder = folder.replace('{625B53C3-AB48-4EC1-BA1F-A1EF4146FC19}', '%StartMenu%')
    folder = folder.replace('{AE50C081-EBD2-438A-8655-8A092E34987A}', '%Recent%')
    folder = folder.replace('{8983036C-27C0-404B-8F08-102D10DCFD74}', '%SendTo%')
    folder = folder.replace('{FDD39AD0-238F-46AF-ADB4-6C85480369C7}', '%Documents%')
    folder = folder.replace('{1777F761-68AD-4D8A-87BD-30B759FA33DD}', '%Favorites%')
    folder = folder.replace('{C5ABBF53-E17F-4121-8900-86626FC2C973}', '%NetHood%')
    folder = folder.replace('{9274BD8D-CFD1-41C3-B35E-B13F55A758F4}', '%PrintHood%')
    folder = folder.replace('{A63293E8-664E-48DB-A079-DF759E0509F7}', '%Templates%')
    folder = folder.replace('{82A5EA35-D9CD-47C5-9629-E15D2F714E6E}', '%CommonStartup%')
    folder = folder.replace('{0139D44E-6AFE-49F2-8690-3DAFCAE6FFB8}', '%CommonPrograms%')
    folder = folder.replace('{A4115719-D62E-491D-AA7C-E74B8BE3B067}', '%CommonStartMenu%')
    folder = folder.replace('{C4AA340D-F20F-4863-AFEF-F87EF2E6BA25}', '%PublicDesktop%')
    folder = folder.replace('{62AB5D82-FDC1-4DC3-A9DD-070D1D495D97}', '%ProgramData%')
    folder = folder.replace('{B94237E7-57AC-4347-9151-B08C6C32D1F7}', '%CommonTemplates%')
    folder = folder.replace('{ED4824AF-DCE4-45A8-81E2-FC7965083634}', '%PublicDocuments%')
    folder = folder.replace('{3EB685DB-65F9-4CF6-A03A-E3EF65729F3D}', '%RoamingAppData%')
    folder = folder.replace('{F1B32785-6FBA-4FCF-9D55-7B8E7F157091}', '%LocalAppData%')
    folder = folder.replace('{A520A1A4-1780-4FF6-BD18-167343C5AF16}', '%LocalAppDataLow%')
    folder = folder.replace('{352481E8-33BE-4251-BA85-6007CAEDCF9D}', '%InternetCache%')
    folder = folder.replace('{2B0F765D-C0E9-4171-908E-08A611B84FF6}', '%Cookies%')
    folder = folder.replace('{D9DC8A3B-B784-432E-A781-5A1130A75963}', '%History%')
    folder = folder.replace('{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}', '%System%')
    folder = folder.replace('{D65231B0-B2F1-4857-A4CE-A8E7C6EA7D27}', '%SystemX86%')
    folder = folder.replace('{F38BF404-1D43-42F2-9305-67DE0B28FC23}', '%Windows%')
    folder = folder.replace('{5E6C858F-0E22-4760-9AFE-EA3317B67173}', '%Profile%')
    folder = folder.replace('{33E28130-4E1E-4676-835A-98395C3BC3BB}', '%Pictures%')
    folder = folder.replace('{7C5A40EF-A0FB-4BFC-874A-C0F2E0B9FA8E}', '%ProgramFilesX86%')
    folder = folder.replace('{DE974D24-D9C6-4D3E-BF91-F4455120B917}', '%ProgramFilesCommonX86%')
    folder = folder.replace('{6D809377-6AF0-444b-8957-A3773F02200E}', '%ProgramFilesX64%')
    folder = folder.replace('{6365D5A7-0F0D-45e5-87F6-0DA56B6A4F7D}', '%ProgramFilesCommonX64%')
    folder = folder.replace('{905e63b6-c1bf-494e-b29c-65b732d3d21a}', '%ProgramFiles%')
    folder = folder.replace('{F7F1ED05-9F6D-47A2-AAAE-29D317C6F066}', '%ProgramFilesCommon%')
    folder = folder.replace('{724EF170-A42D-4FEF-9F26-B60E846FBA4F}', '%AdminTools%')
    folder = folder.replace('{D0384E7D-BAC3-4797-8F14-CBA229B392B5}', '%CommonAdminTools%')
    folder = folder.replace('{4BD8D571-6D19-48D3-BE97-422220080E43}', '%Music%')
    folder = folder.replace('{18989B1D-99B5-455B-841C-AB7C74E4DDFC}', '%Videos%')
    folder = folder.replace('{B6EBFB86-6907-413C-9AF7-4FC2ABF07CC5}', '%PublicPictures%')
    folder = folder.replace('{3214FAB5-9757-4298-BB61-92A9DEAA44FF}', '%PublicMusic%')
    folder = folder.replace('{2400183A-6185-49FB-A2D8-4A392A602BA3}', '%PublicVideos%')
    folder = folder.replace('{8AD10C31-2ADB-4296-A8F7-E4701232C972}', '%ResourceDir%')
    folder = folder.replace('{2A00375E-224C-49DE-B8D1-440DF7EF3DDC}', '%LocalizedResourcesDir%')
    folder = folder.replace('{C1BAE2D0-10DF-4334-BEDD-7AA20B227A9D}', '%CommonOEMLinks%')
    folder = folder.replace('{9E52AB10-F80D-49DF-ACB8-4330F5687855}', '%CDBurning%')
    folder = folder.replace('{0762D272-C50A-4BB0-A382-697DCD729B80}', '%UserProfiles%')
    folder = folder.replace('{DE92C1C7-837F-4F69-A3BB-86E631204A23}', '%Playlists%')
    folder = folder.replace('{15CA69B3-30EE-49C1-ACE1-6B5EC372AFB5}', '%SamplePlaylists%')
    folder = folder.replace('{B250C668-F57D-4EE1-A63C-290EE7D1AA1F}', '%SampleMusic%')
    folder = folder.replace('{C4900540-2379-4C75-844B-64E6FAF8716B}', '%SamplePictures%')
    folder = folder.replace('{859EAD94-2E85-48AD-A71A-0969CB56A6CD}', '%SampleVideos%')
    folder = folder.replace('{69D2CF90-FC33-4FB7-9A0C-EBB0F0FCB43C}', '%PhotoAlbums%')
    folder = folder.replace('{DFDF76A2-C82A-4D63-906A-5644AC457385}', '%Public%')
    folder = folder.replace('{df7266ac-9274-4867-8d55-3bd661de872d}', '%ChangeRemovePrograms%')
    folder = folder.replace('{a305ce99-f527-492b-8b1a-7e76fa98d6e4}', '%AppUpdates%')
    folder = folder.replace('{de61d971-5ebc-4f02-a3a9-6c82895e5c04}', '%AddNewPrograms%')
    folder = folder.replace('{374DE290-123F-4565-9164-39C4925E467B}', '%Downloads%')
    folder = folder.replace('{3D644C9B-1FB8-4f30-9B45-F670235F79C0}', '%PublicDownloads%')
    folder = folder.replace('{7d1d3a04-debb-4115-95cf-2f29da2920da}', '%SavedSearches%')
    folder = folder.replace('{52a4f021-7b75-48a9-9f6b-4b87a210bc8f}', '%QuickLaunch%')
    folder = folder.replace('{56784854-C6CB-462b-8169-88E350ACB882}', '%Contacts%')
    folder = folder.replace('{A75D362E-50FC-4fb7-AC2C-A8BEAA314493}', '%SidebarParts%')
    folder = folder.replace('{7B396E54-9EC5-4300-BE0A-2482EBAE1A26}', '%SidebarDefaultParts%')
    folder = folder.replace('{5b3749ad-b49f-49c1-83eb-15370fbd4882}', '%TreeProperties%')
    folder = folder.replace('{DEBF2536-E1A8-4c59-B6A2-414586476AEA}', '%PublicGameTasks%')
    folder = folder.replace('{054FAE61-4DD8-4787-80B6-090220C4B700}', '%GameTasks%')
    folder = folder.replace('{4C5C32FF-BB9D-43b0-B5B4-2D72E54EAAA4}', '%SavedGames%')
    folder = folder.replace('{CAC52C1A-B53D-4edc-92D7-6B2E8AC19434}', '%Games%')
    folder = folder.replace('{bd85e001-112e-431e-983b-7b15ac09fff1}', '%RecordedTV%')
    folder = folder.replace('{98ec0e18-2098-4d44-8644-66979315a281}', '%SEARCH_MAPI%')
    folder = folder.replace('{ee32e446-31ca-4aba-814f-a5ebd2fd6d5e}', '%SEARCH_CSC%')
    folder = folder.replace('{bfb9d5e0-c6a9-404c-b2b2-ae6db6af4968}', '%Links%')
    folder = folder.replace('{f3ce0f7c-4901-4acc-8648-d5d44b04ef8f}', '%UsersFiles%')
    folder = folder.replace('{190337d1-b8ca-4121-a639-6d472d16972a}', '%SearchHome%')
    folder = folder.replace('{2C36C0AA-5812-4b87-BFD0-4CD0DFB19B39}', '%OriginalImages%')
    folder = folder.replace('{9E3995AB-1F9C-4F13-B827-48B24B6C7174}', '%UserPinned%')
    folder = folder.replace('{ED228FDF-9EA8-4870-83B1-96B02CFE0D52}', '%Games%')
    folder = folder.replace('{00D8862B-6453-4957-A821-3D98D74C76BE}', '%Solitaire%')
    folder = folder.replace('{1FE520E6-95FE-48A6-9956-D7FBC347A472}', '%Backgammon%')
    folder = folder.replace('{205286E5-F5F2-4306-BDB1-864245E33227}', '%Chess%')
    folder = folder.replace('{3022722E-3A23-4839-AA85-348FC79C7686}', '%Checkers%')
    folder = folder.replace('{5FA410C1-1DD5-4238-833E-4DF9974FBC9C}', '%Spades%')
    folder = folder.replace('{6C815596-821F-40B3-8A84-643B73A8EB16}', '%Freecell%')
    folder = folder.replace('{91CA4D38-EA2B-4F3C-94DE-36C1386182FC}', '%PurblePlace%')
    folder = folder.replace('{AF698A5B-24D6-4F78-AE95-204B09EDC7B6}', '%Mahjong%')
    folder = folder.replace('{AFA7FF39-1DDF-4F70-A2D5-23FCFFF02E5F}', '%SpiderSolitaire%')
    folder = folder.replace('{D1A7F7E0-D4E9-49E8-BF2C-CEAA01D2E670}', '%Hearts%')
    folder = folder.replace('{E91579C0-4EA9-4A2A-A9B2-04BEF1D6DC29}', '%MineSweeper%')
    folder = folder.replace('{FC96B68C-09EF-4251-A598-19E4BE1B76A9}', '%MoreGames%')
    return folder


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)