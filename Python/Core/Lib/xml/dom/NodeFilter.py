# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: NodeFilter.py


class NodeFilter:
    """
    This is the DOM2 NodeFilter interface. It contains only constants.
    """
    FILTER_ACCEPT = 1
    FILTER_REJECT = 2
    FILTER_SKIP = 3
    SHOW_ALL = 4294967295L
    SHOW_ELEMENT = 1
    SHOW_ATTRIBUTE = 2
    SHOW_TEXT = 4
    SHOW_CDATA_SECTION = 8
    SHOW_ENTITY_REFERENCE = 16
    SHOW_ENTITY = 32
    SHOW_PROCESSING_INSTRUCTION = 64
    SHOW_COMMENT = 128
    SHOW_DOCUMENT = 256
    SHOW_DOCUMENT_TYPE = 512
    SHOW_DOCUMENT_FRAGMENT = 1024
    SHOW_NOTATION = 2048

    def acceptNode(self, node):
        raise NotImplementedError