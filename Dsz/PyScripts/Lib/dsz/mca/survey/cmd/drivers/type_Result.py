# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime
RESULT_ITEM_FLAG_SIGNED = 1
RESULT_ITEM_FLAG_UNSIGNED = 2

class Result:

    def __init__(self):
        self.__dict__['imageBase'] = 0
        self.__dict__['size'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['loadCount'] = 0
        self.__dict__['itemFlags'] = 0
        self.__dict__['buildDate'] = mcl.object.MclTime.MclTime()
        self.__dict__['imageName'] = ''
        self.__dict__['author'] = ''
        self.__dict__['license'] = ''
        self.__dict__['version'] = ''
        self.__dict__['description'] = ''
        self.__dict__['comments'] = ''
        self.__dict__['internalName'] = ''
        self.__dict__['originalName'] = ''
        self.__dict__['productName'] = ''
        self.__dict__['trademarks'] = ''

    def __getattr__(self, name):
        if name == 'imageBase':
            return self.__dict__['imageBase']
        if name == 'size':
            return self.__dict__['size']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'loadCount':
            return self.__dict__['loadCount']
        if name == 'itemFlags':
            return self.__dict__['itemFlags']
        if name == 'buildDate':
            return self.__dict__['buildDate']
        if name == 'imageName':
            return self.__dict__['imageName']
        if name == 'author':
            return self.__dict__['author']
        if name == 'license':
            return self.__dict__['license']
        if name == 'version':
            return self.__dict__['version']
        if name == 'description':
            return self.__dict__['description']
        if name == 'comments':
            return self.__dict__['comments']
        if name == 'internalName':
            return self.__dict__['internalName']
        if name == 'originalName':
            return self.__dict__['originalName']
        if name == 'productName':
            return self.__dict__['productName']
        if name == 'trademarks':
            return self.__dict__['trademarks']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'imageBase':
            self.__dict__['imageBase'] = value
        elif name == 'size':
            self.__dict__['size'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'loadCount':
            self.__dict__['loadCount'] = value
        elif name == 'itemFlags':
            self.__dict__['itemFlags'] = value
        elif name == 'buildDate':
            self.__dict__['buildDate'] = value
        elif name == 'imageName':
            self.__dict__['imageName'] = value
        elif name == 'author':
            self.__dict__['author'] = value
        elif name == 'license':
            self.__dict__['license'] = value
        elif name == 'version':
            self.__dict__['version'] = value
        elif name == 'description':
            self.__dict__['description'] = value
        elif name == 'comments':
            self.__dict__['comments'] = value
        elif name == 'internalName':
            self.__dict__['internalName'] = value
        elif name == 'originalName':
            self.__dict__['originalName'] = value
        elif name == 'productName':
            self.__dict__['productName'] = value
        elif name == 'trademarks':
            self.__dict__['trademarks'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_IMAGE_BASE, self.__dict__['imageBase'])
        submsg.AddU32(MSG_KEY_RESULT_SIZE, self.__dict__['size'])
        submsg.AddU32(MSG_KEY_RESULT_FLAGS, self.__dict__['flags'])
        submsg.AddU16(MSG_KEY_RESULT_LOAD_COUNT, self.__dict__['loadCount'])
        submsg.AddU32(MSG_KEY_RESULT_ITEM_FLAGS, self.__dict__['itemFlags'])
        submsg.AddTime(MSG_KEY_RESULT_BUILD_DATE, self.__dict__['buildDate'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_IMAGE_NAME, self.__dict__['imageName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_AUTHOR, self.__dict__['author'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_LICENSE, self.__dict__['license'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_VERSION, self.__dict__['version'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DESCRIPTION, self.__dict__['description'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_COMMENTS, self.__dict__['comments'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_INTERNAL_NAME, self.__dict__['internalName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_ORIGINAL_NAME, self.__dict__['originalName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_PRODUCT_NAME, self.__dict__['productName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TRADEMARKS, self.__dict__['trademarks'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['imageBase'] = submsg.FindU64(MSG_KEY_RESULT_IMAGE_BASE)
        self.__dict__['size'] = submsg.FindU32(MSG_KEY_RESULT_SIZE)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_FLAGS)
        self.__dict__['loadCount'] = submsg.FindU16(MSG_KEY_RESULT_LOAD_COUNT)
        self.__dict__['itemFlags'] = submsg.FindU32(MSG_KEY_RESULT_ITEM_FLAGS)
        self.__dict__['buildDate'] = submsg.FindTime(MSG_KEY_RESULT_BUILD_DATE)
        self.__dict__['imageName'] = submsg.FindString(MSG_KEY_RESULT_IMAGE_NAME)
        self.__dict__['author'] = submsg.FindString(MSG_KEY_RESULT_AUTHOR)
        self.__dict__['license'] = submsg.FindString(MSG_KEY_RESULT_LICENSE)
        self.__dict__['version'] = submsg.FindString(MSG_KEY_RESULT_VERSION)
        self.__dict__['description'] = submsg.FindString(MSG_KEY_RESULT_DESCRIPTION)
        self.__dict__['comments'] = submsg.FindString(MSG_KEY_RESULT_COMMENTS)
        self.__dict__['internalName'] = submsg.FindString(MSG_KEY_RESULT_INTERNAL_NAME)
        self.__dict__['originalName'] = submsg.FindString(MSG_KEY_RESULT_ORIGINAL_NAME)
        self.__dict__['productName'] = submsg.FindString(MSG_KEY_RESULT_PRODUCT_NAME)
        self.__dict__['trademarks'] = submsg.FindString(MSG_KEY_RESULT_TRADEMARKS)