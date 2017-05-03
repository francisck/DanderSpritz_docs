# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import mcl.status
ERR_RESERVED_MASK = 4026531840L
CALL_SUCCEEDED = mcl.status.MCL_SUCCESS
CALL_FAILED = 268435456
CALL_RUNNING = 268435457
ERR_UNKNOWN = 268435472
ERR_READ_FAILED = 268435473
ERR_WRITE_FAILED = 268435474
ERR_ALLOCATION_FAILED = 268435475
ERR_INVALID_DATA_HEADER = 268435476
ERR_NOT_ENOUGH_DATA = 268435477
ERR_DECOMPRESS_FAILED = 268435478
ERR_USER_NOT_SUPPORTED = 268435479
ERR_SET_USER_FAILED = 268435480
ERR_NOT_IMPLEMENTED = 268435481
ERR_DISABLE_WOW64_FAILED = 268435482
errorStrings = {CALL_FAILED: 'Mcl_Target: Call failed',
   CALL_RUNNING: 'Mcl_Target: Call running',
   ERR_UNKNOWN: 'Mcl_Target: Unknown error',
   ERR_READ_FAILED: 'Mcl_Target: Error reading data',
   ERR_WRITE_FAILED: 'Mcl_Target: Error writing data',
   ERR_ALLOCATION_FAILED: 'Mcl_Target: Error allocating necessary memory',
   ERR_INVALID_DATA_HEADER: 'Mcl_Target: Received data header is corrupt',
   ERR_NOT_ENOUGH_DATA: 'Mcl_Target: Not enough data in receive buffer',
   ERR_DECOMPRESS_FAILED: 'Mcl_Target: Decompression of data encountered an error',
   ERR_USER_NOT_SUPPORTED: 'Mcl_Target: Use of user prefix not supported on this platform',
   ERR_SET_USER_FAILED: 'Mcl_Target: Failed to set thread user',
   ERR_NOT_IMPLEMENTED: 'Mcl_Target: Not implemented on this platform',
   ERR_DISABLE_WOW64_FAILED: 'Mcl_Target: Failed to disable WOW64 redirection'
   }