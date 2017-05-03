# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 2
ERR_GET_VERSION_FAILED = mcl.status.framework.ERR_START + 3
ERR_LOAD_LIB_FAILED = mcl.status.framework.ERR_START + 4
ERR_GET_PROC_FAILED = mcl.status.framework.ERR_START + 5
ERR_QUERY_FAILED = mcl.status.framework.ERR_START + 6
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 7
ERR_UNAME_FAILED = mcl.status.framework.ERR_START + 8
ERR_SSCANF_FAILED = mcl.status.framework.ERR_START + 9
ERR_KSYMS_OPEN_FAILED = mcl.status.framework.ERR_START + 10
ERR_ELFLIB_OUTOFDATE = mcl.status.framework.ERR_START + 11
ERR_NO_ELF_DESCRIPTOR = mcl.status.framework.ERR_START + 12
ERR_EXCEPTION = mcl.status.framework.ERR_START + 13
errorStrings = {ERR_INVALID_PARAM: 'Invalid Parameter(s)',
   ERR_MARSHAL_FAILED: 'Data marshal failed',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_GET_VERSION_FAILED: 'OS GetVersion failed',
   ERR_LOAD_LIB_FAILED: 'Error loading library',
   ERR_GET_PROC_FAILED: 'Failed to get procedure',
   ERR_QUERY_FAILED: 'NetServerGetInfo error',
   ERR_ALLOC_FAILED: 'Memory allocation fails',
   ERR_UNAME_FAILED: 'OS uname() system call failed',
   ERR_SSCANF_FAILED: 'OS sscanf() for version numbers failed',
   ERR_KSYMS_OPEN_FAILED: 'Could not open /dev/ksyms',
   ERR_ELFLIB_OUTOFDATE: 'ELF library version probably out of date',
   ERR_NO_ELF_DESCRIPTOR: 'Could not get ELF descriptor',
   ERR_EXCEPTION: 'Exception caught'
   }