# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Item.py
from types import *
import mcl.object.MclTime

class ResultMode:

    def __init__(self):
        self.__dict__['isMixed'] = False
        self.__dict__['domainName'] = ''

    def __getattr__(self, name):
        if name == 'isMixed':
            return self.__dict__['isMixed']
        if name == 'domainName':
            return self.__dict__['domainName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'isMixed':
            self.__dict__['isMixed'] = value
        elif name == 'domainName':
            self.__dict__['domainName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_MODE_IS_MIXED, self.__dict__['isMixed'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_MODE_DOMAIN_NAME, self.__dict__['domainName'])
        mmsg.AddMessage(MSG_KEY_RESULT_MODE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MODE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['isMixed'] = submsg.FindBool(MSG_KEY_RESULT_MODE_IS_MIXED)
        self.__dict__['domainName'] = submsg.FindString(MSG_KEY_RESULT_MODE_DOMAIN_NAME)


class ResultInfo:

    def __init__(self):
        self.__dict__['category'] = ''
        self.__dict__['name'] = ''
        self.__dict__['dn'] = ''

    def __getattr__(self, name):
        if name == 'category':
            return self.__dict__['category']
        if name == 'name':
            return self.__dict__['name']
        if name == 'dn':
            return self.__dict__['dn']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'category':
            self.__dict__['category'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'dn':
            self.__dict__['dn'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_INFO_CATEGORY, self.__dict__['category'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_INFO_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_INFO_DN, self.__dict__['dn'])
        mmsg.AddMessage(MSG_KEY_RESULT_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['category'] = submsg.FindString(MSG_KEY_RESULT_INFO_CATEGORY)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_INFO_NAME)
        self.__dict__['dn'] = submsg.FindString(MSG_KEY_RESULT_INFO_DN)


class ResultUser:

    def __init__(self):
        self.__dict__['AccountDisabled'] = False
        self.__dict__['AccountExpirationDate'] = mcl.object.MclTime.MclTime()
        self.__dict__['BadLoginCount'] = 0
        self.__dict__['IsAccountLocked'] = False
        self.__dict__['LastFailedLogin'] = mcl.object.MclTime.MclTime()
        self.__dict__['LastLogin'] = mcl.object.MclTime.MclTime()
        self.__dict__['LastLogoff'] = mcl.object.MclTime.MclTime()
        self.__dict__['MaxStorage'] = 0
        self.__dict__['PasswordExpirationDate'] = mcl.object.MclTime.MclTime()
        self.__dict__['PasswordLastChanged'] = mcl.object.MclTime.MclTime()
        self.__dict__['PasswordMinimumLength'] = 0
        self.__dict__['PasswordRequired'] = False
        self.__dict__['RequireUniquePassword'] = False
        self.__dict__['Department'] = ''
        self.__dict__['Description'] = ''
        self.__dict__['EmailAddress'] = ''
        self.__dict__['LastName'] = ''
        self.__dict__['FirstName'] = ''
        self.__dict__['FullName'] = ''
        self.__dict__['HomeDirectory'] = ''
        self.__dict__['HomePage'] = ''
        self.__dict__['LoginScript'] = ''
        self.__dict__['Manager'] = ''
        self.__dict__['OfficeNumber'] = ''
        self.__dict__['HomeNumber'] = ''
        self.__dict__['CellNumber'] = ''
        self.__dict__['PagerNumber'] = ''
        self.__dict__['FaxNumber'] = ''
        self.__dict__['OfficeLocation'] = ''
        self.__dict__['UserName'] = ''

    def __getattr__(self, name):
        if name == 'AccountDisabled':
            return self.__dict__['AccountDisabled']
        if name == 'AccountExpirationDate':
            return self.__dict__['AccountExpirationDate']
        if name == 'BadLoginCount':
            return self.__dict__['BadLoginCount']
        if name == 'IsAccountLocked':
            return self.__dict__['IsAccountLocked']
        if name == 'LastFailedLogin':
            return self.__dict__['LastFailedLogin']
        if name == 'LastLogin':
            return self.__dict__['LastLogin']
        if name == 'LastLogoff':
            return self.__dict__['LastLogoff']
        if name == 'MaxStorage':
            return self.__dict__['MaxStorage']
        if name == 'PasswordExpirationDate':
            return self.__dict__['PasswordExpirationDate']
        if name == 'PasswordLastChanged':
            return self.__dict__['PasswordLastChanged']
        if name == 'PasswordMinimumLength':
            return self.__dict__['PasswordMinimumLength']
        if name == 'PasswordRequired':
            return self.__dict__['PasswordRequired']
        if name == 'RequireUniquePassword':
            return self.__dict__['RequireUniquePassword']
        if name == 'Department':
            return self.__dict__['Department']
        if name == 'Description':
            return self.__dict__['Description']
        if name == 'EmailAddress':
            return self.__dict__['EmailAddress']
        if name == 'LastName':
            return self.__dict__['LastName']
        if name == 'FirstName':
            return self.__dict__['FirstName']
        if name == 'FullName':
            return self.__dict__['FullName']
        if name == 'HomeDirectory':
            return self.__dict__['HomeDirectory']
        if name == 'HomePage':
            return self.__dict__['HomePage']
        if name == 'LoginScript':
            return self.__dict__['LoginScript']
        if name == 'Manager':
            return self.__dict__['Manager']
        if name == 'OfficeNumber':
            return self.__dict__['OfficeNumber']
        if name == 'HomeNumber':
            return self.__dict__['HomeNumber']
        if name == 'CellNumber':
            return self.__dict__['CellNumber']
        if name == 'PagerNumber':
            return self.__dict__['PagerNumber']
        if name == 'FaxNumber':
            return self.__dict__['FaxNumber']
        if name == 'OfficeLocation':
            return self.__dict__['OfficeLocation']
        if name == 'UserName':
            return self.__dict__['UserName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'AccountDisabled':
            self.__dict__['AccountDisabled'] = value
        elif name == 'AccountExpirationDate':
            self.__dict__['AccountExpirationDate'] = value
        elif name == 'BadLoginCount':
            self.__dict__['BadLoginCount'] = value
        elif name == 'IsAccountLocked':
            self.__dict__['IsAccountLocked'] = value
        elif name == 'LastFailedLogin':
            self.__dict__['LastFailedLogin'] = value
        elif name == 'LastLogin':
            self.__dict__['LastLogin'] = value
        elif name == 'LastLogoff':
            self.__dict__['LastLogoff'] = value
        elif name == 'MaxStorage':
            self.__dict__['MaxStorage'] = value
        elif name == 'PasswordExpirationDate':
            self.__dict__['PasswordExpirationDate'] = value
        elif name == 'PasswordLastChanged':
            self.__dict__['PasswordLastChanged'] = value
        elif name == 'PasswordMinimumLength':
            self.__dict__['PasswordMinimumLength'] = value
        elif name == 'PasswordRequired':
            self.__dict__['PasswordRequired'] = value
        elif name == 'RequireUniquePassword':
            self.__dict__['RequireUniquePassword'] = value
        elif name == 'Department':
            self.__dict__['Department'] = value
        elif name == 'Description':
            self.__dict__['Description'] = value
        elif name == 'EmailAddress':
            self.__dict__['EmailAddress'] = value
        elif name == 'LastName':
            self.__dict__['LastName'] = value
        elif name == 'FirstName':
            self.__dict__['FirstName'] = value
        elif name == 'FullName':
            self.__dict__['FullName'] = value
        elif name == 'HomeDirectory':
            self.__dict__['HomeDirectory'] = value
        elif name == 'HomePage':
            self.__dict__['HomePage'] = value
        elif name == 'LoginScript':
            self.__dict__['LoginScript'] = value
        elif name == 'Manager':
            self.__dict__['Manager'] = value
        elif name == 'OfficeNumber':
            self.__dict__['OfficeNumber'] = value
        elif name == 'HomeNumber':
            self.__dict__['HomeNumber'] = value
        elif name == 'CellNumber':
            self.__dict__['CellNumber'] = value
        elif name == 'PagerNumber':
            self.__dict__['PagerNumber'] = value
        elif name == 'FaxNumber':
            self.__dict__['FaxNumber'] = value
        elif name == 'OfficeLocation':
            self.__dict__['OfficeLocation'] = value
        elif name == 'UserName':
            self.__dict__['UserName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_USER_ACCOUNT_DISABLED, self.__dict__['AccountDisabled'])
        submsg.AddTime(MSG_KEY_RESULT_USER_ACCOUNT_EXPIRATION_DATE, self.__dict__['AccountExpirationDate'])
        submsg.AddU32(MSG_KEY_RESULT_USER_BAD_LOGIN_COUNT, self.__dict__['BadLoginCount'])
        submsg.AddBool(MSG_KEY_RESULT_USER_IS_ACCOUNT_LOCKED, self.__dict__['IsAccountLocked'])
        submsg.AddTime(MSG_KEY_RESULT_USER_LAST_FAILED_LOGIN, self.__dict__['LastFailedLogin'])
        submsg.AddTime(MSG_KEY_RESULT_USER_LAST_LOGIN, self.__dict__['LastLogin'])
        submsg.AddTime(MSG_KEY_RESULT_USER_LAST_LOGOFF, self.__dict__['LastLogoff'])
        submsg.AddU32(MSG_KEY_RESULT_USER_MAX_STORAGE, self.__dict__['MaxStorage'])
        submsg.AddTime(MSG_KEY_RESULT_USER_PASSWORD_EXPIRATION_DATE, self.__dict__['PasswordExpirationDate'])
        submsg.AddTime(MSG_KEY_RESULT_USER_PASSWORD_LAST_CHANGED, self.__dict__['PasswordLastChanged'])
        submsg.AddU32(MSG_KEY_RESULT_USER_PASSWORD_MINIMUM_LENGTH, self.__dict__['PasswordMinimumLength'])
        submsg.AddBool(MSG_KEY_RESULT_USER_PASSWORD_REQUIRED, self.__dict__['PasswordRequired'])
        submsg.AddBool(MSG_KEY_RESULT_USER_REQUIRE_UNIQUE_PASSWORD, self.__dict__['RequireUniquePassword'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_DEPARTMENT, self.__dict__['Department'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_DESCRIPTION, self.__dict__['Description'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_EMAIL_ADDRESS, self.__dict__['EmailAddress'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_LAST_NAME, self.__dict__['LastName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_FIRST_NAME, self.__dict__['FirstName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_FULL_NAME, self.__dict__['FullName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_HOME_DIRECTORY, self.__dict__['HomeDirectory'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_HOME_PAGE, self.__dict__['HomePage'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_LOGIN_SCRIPT, self.__dict__['LoginScript'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_MANAGER, self.__dict__['Manager'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_OFFICE_NUMBER, self.__dict__['OfficeNumber'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_HOME_NUMBER, self.__dict__['HomeNumber'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_CELL_NUMBER, self.__dict__['CellNumber'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_PAGER_NUMBER, self.__dict__['PagerNumber'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_FAX_NUMBER, self.__dict__['FaxNumber'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_OFFICE_LOCATION, self.__dict__['OfficeLocation'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_USER_NAME, self.__dict__['UserName'])
        mmsg.AddMessage(MSG_KEY_RESULT_USER, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_USER, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['AccountDisabled'] = submsg.FindBool(MSG_KEY_RESULT_USER_ACCOUNT_DISABLED)
        self.__dict__['AccountExpirationDate'] = submsg.FindTime(MSG_KEY_RESULT_USER_ACCOUNT_EXPIRATION_DATE)
        self.__dict__['BadLoginCount'] = submsg.FindU32(MSG_KEY_RESULT_USER_BAD_LOGIN_COUNT)
        self.__dict__['IsAccountLocked'] = submsg.FindBool(MSG_KEY_RESULT_USER_IS_ACCOUNT_LOCKED)
        self.__dict__['LastFailedLogin'] = submsg.FindTime(MSG_KEY_RESULT_USER_LAST_FAILED_LOGIN)
        self.__dict__['LastLogin'] = submsg.FindTime(MSG_KEY_RESULT_USER_LAST_LOGIN)
        self.__dict__['LastLogoff'] = submsg.FindTime(MSG_KEY_RESULT_USER_LAST_LOGOFF)
        self.__dict__['MaxStorage'] = submsg.FindU32(MSG_KEY_RESULT_USER_MAX_STORAGE)
        self.__dict__['PasswordExpirationDate'] = submsg.FindTime(MSG_KEY_RESULT_USER_PASSWORD_EXPIRATION_DATE)
        self.__dict__['PasswordLastChanged'] = submsg.FindTime(MSG_KEY_RESULT_USER_PASSWORD_LAST_CHANGED)
        self.__dict__['PasswordMinimumLength'] = submsg.FindU32(MSG_KEY_RESULT_USER_PASSWORD_MINIMUM_LENGTH)
        self.__dict__['PasswordRequired'] = submsg.FindBool(MSG_KEY_RESULT_USER_PASSWORD_REQUIRED)
        self.__dict__['RequireUniquePassword'] = submsg.FindBool(MSG_KEY_RESULT_USER_REQUIRE_UNIQUE_PASSWORD)
        self.__dict__['Department'] = submsg.FindString(MSG_KEY_RESULT_USER_DEPARTMENT)
        self.__dict__['Description'] = submsg.FindString(MSG_KEY_RESULT_USER_DESCRIPTION)
        self.__dict__['EmailAddress'] = submsg.FindString(MSG_KEY_RESULT_USER_EMAIL_ADDRESS)
        self.__dict__['LastName'] = submsg.FindString(MSG_KEY_RESULT_USER_LAST_NAME)
        self.__dict__['FirstName'] = submsg.FindString(MSG_KEY_RESULT_USER_FIRST_NAME)
        self.__dict__['FullName'] = submsg.FindString(MSG_KEY_RESULT_USER_FULL_NAME)
        self.__dict__['HomeDirectory'] = submsg.FindString(MSG_KEY_RESULT_USER_HOME_DIRECTORY)
        self.__dict__['HomePage'] = submsg.FindString(MSG_KEY_RESULT_USER_HOME_PAGE)
        self.__dict__['LoginScript'] = submsg.FindString(MSG_KEY_RESULT_USER_LOGIN_SCRIPT)
        self.__dict__['Manager'] = submsg.FindString(MSG_KEY_RESULT_USER_MANAGER)
        self.__dict__['OfficeNumber'] = submsg.FindString(MSG_KEY_RESULT_USER_OFFICE_NUMBER)
        self.__dict__['HomeNumber'] = submsg.FindString(MSG_KEY_RESULT_USER_HOME_NUMBER)
        self.__dict__['CellNumber'] = submsg.FindString(MSG_KEY_RESULT_USER_CELL_NUMBER)
        self.__dict__['PagerNumber'] = submsg.FindString(MSG_KEY_RESULT_USER_PAGER_NUMBER)
        self.__dict__['FaxNumber'] = submsg.FindString(MSG_KEY_RESULT_USER_FAX_NUMBER)
        self.__dict__['OfficeLocation'] = submsg.FindString(MSG_KEY_RESULT_USER_OFFICE_LOCATION)
        self.__dict__['UserName'] = submsg.FindString(MSG_KEY_RESULT_USER_USER_NAME)