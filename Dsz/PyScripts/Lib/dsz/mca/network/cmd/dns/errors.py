# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_INVALID_NAME = mcl.status.framework.ERR_START + 2
ERR_ERROR_CREATING_QUERY = mcl.status.framework.ERR_START + 3
ERR_ERROR_ALLOCATING_MEMORY = mcl.status.framework.ERR_START + 4
ERR_ERROR_SENDING_QUERY = mcl.status.framework.ERR_START + 5
ERR_NOT_SUPPORTED = mcl.status.framework.ERR_START + 6
ERR_ERROR_API_NOT_FOUND = mcl.status.framework.ERR_START + 7
ERR_ERROR_CACHE_QUERY_FAILED = mcl.status.framework.ERR_START + 8
ERR_ERROR_CACHE_FLUSH_FAILED = mcl.status.framework.ERR_START + 9
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_INVALID_NAME: 'Invalid name specified',
   ERR_ERROR_CREATING_QUERY: 'Error creating DNS query',
   ERR_ERROR_ALLOCATING_MEMORY: 'Unable to allocate space for query response',
   ERR_ERROR_SENDING_QUERY: 'Send or Recv of query failed',
   ERR_NOT_SUPPORTED: 'Operation not supported on this platform',
   ERR_ERROR_API_NOT_FOUND: 'Required OS API not found',
   ERR_ERROR_CACHE_QUERY_FAILED: 'Query of cache failed',
   ERR_ERROR_CACHE_FLUSH_FAILED: 'Flush of cache failed'
   }