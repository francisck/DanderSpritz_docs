# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_MINIMIZED = mcl.status.framework.ERR_START + 2
ERR_GPA_FAILED = mcl.status.framework.ERR_START + 3
ERR_LOAD_LIBRARY_FAILED = mcl.status.framework.ERR_START + 4
ERR_OPEN_WINSTA_FAILED = mcl.status.framework.ERR_START + 5
ERR_GET_INDEX_FAILED = mcl.status.framework.ERR_START + 6
ERR_OPEN_DESKTOP_FAILED = mcl.status.framework.ERR_START + 7
ERR_LIST_ENUM = mcl.status.framework.ERR_START + 8
ERR_POSTMESSAGE_FAILED = mcl.status.framework.ERR_START + 9
ERR_HANDLE_IS_NOT_WINDOW = mcl.status.framework.ERR_START + 10
ERR_BUTTON_NOT_FOUND = mcl.status.framework.ERR_START + 11
ERR_EXCEPTION = mcl.status.framework.ERR_START + 12
ERR_SCREENSHOT_FORMAT_NOT_SUPPORTED = mcl.status.framework.ERR_START + 13
ERR_CREATE_DC_ERROR = mcl.status.framework.ERR_START + 14
ERR_GET_RESOLUTION_FAILED = mcl.status.framework.ERR_START + 15
ERR_CREATE_BMP_ERROR = mcl.status.framework.ERR_START + 16
ERR_SELECT_OBJECT_ERROR = mcl.status.framework.ERR_START + 17
ERR_BIT_TRANSFER_FAILED = mcl.status.framework.ERR_START + 18
ERR_GET_OBJECT_ERROR = mcl.status.framework.ERR_START + 19
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 20
ERR_GET_DIB_ERROR = mcl.status.framework.ERR_START + 21
ERR_SCREENSHOT_CANNOT_GET_ENCODER = mcl.status.framework.ERR_START + 22
ERR_OPEN_DATA_PIPE_FAILED = mcl.status.framework.ERR_START + 23
ERR_GET_API_FAILED = mcl.status.framework.ERR_START + 24
ERR_INJECT_SETUP_FAILED = mcl.status.framework.ERR_START + 25
ERR_CONNECT_PIPE_FAILED = mcl.status.framework.ERR_START + 26
ERR_READ_PIPE_FAILED = mcl.status.framework.ERR_START + 27
ERR_SEND_IMAGE = mcl.status.framework.ERR_START + 28
ERR_INJECT_FAILED = mcl.status.framework.ERR_START + 29
ERR_INJECT_EXCEPTION = mcl.status.framework.ERR_START + 30
ERR_GET_EXIT_CODE_FAILED = mcl.status.framework.ERR_START + 31
ERR_INJECT_THREAD_ENDED = mcl.status.framework.ERR_START + 32
ERR_INJECT_WRITE_FAILED = mcl.status.framework.ERR_START + 33
ERR_INJECT_INPUT_DESKTOP_ERROR = mcl.status.framework.ERR_START + 34
ERR_INJECT_ALLOC_FAILED = mcl.status.framework.ERR_START + 35
ERR_INJECT_OPEN_PIPE_FAILED = mcl.status.framework.ERR_START + 36
ERR_WINDOW_PLACEMENT_ERROR = mcl.status.framework.ERR_START + 37
ERR_WINDOW_IS_NOT_VISIBLE = mcl.status.framework.ERR_START + 38
ERR_INJECT_UNKNOWN = mcl.status.framework.ERR_START + 39
ERR_GET_SAFEPOINT_FAILED = mcl.status.framework.ERR_START + 40
ERR_INJECTION_REQUIRED = mcl.status.framework.ERR_START + 41
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_MINIMIZED: 'Window is minimized, capturing requires dangerous behavior',
   ERR_GPA_FAILED: 'Failed to get required procedure address',
   ERR_LOAD_LIBRARY_FAILED: 'Failed to load required library',
   ERR_OPEN_WINSTA_FAILED: 'Open of Window station failed',
   ERR_GET_INDEX_FAILED: 'Failed to get index NtUserOpenDesktop',
   ERR_OPEN_DESKTOP_FAILED: 'Failed to open desktop',
   ERR_LIST_ENUM: 'Failed to enumerate objects',
   ERR_POSTMESSAGE_FAILED: 'Failed to send message to window',
   ERR_HANDLE_IS_NOT_WINDOW: 'Value is not a valid window handle',
   ERR_BUTTON_NOT_FOUND: 'Button not found',
   ERR_EXCEPTION: 'An exception occurred',
   ERR_SCREENSHOT_FORMAT_NOT_SUPPORTED: 'Screenshot format not supported',
   ERR_CREATE_DC_ERROR: 'Failed to create device context',
   ERR_GET_RESOLUTION_FAILED: 'Failed to get screen resolution',
   ERR_CREATE_BMP_ERROR: 'Failed to create bitmap',
   ERR_SELECT_OBJECT_ERROR: 'Failed to set the display object',
   ERR_BIT_TRANSFER_FAILED: 'Transfer of bit data failed',
   ERR_GET_OBJECT_ERROR: 'Failed to get bitmap object',
   ERR_ALLOC_FAILED: 'Memory allocation failed',
   ERR_GET_DIB_ERROR: 'Failed to get DIB bits',
   ERR_SCREENSHOT_CANNOT_GET_ENCODER: 'Could not get screenshot encoder',
   ERR_OPEN_DATA_PIPE_FAILED: 'Open of data pipe for transfer failed',
   ERR_GET_API_FAILED: 'Failed to get required API',
   ERR_INJECT_SETUP_FAILED: 'Injection setup failed',
   ERR_CONNECT_PIPE_FAILED: 'Connect to data pipe failed',
   ERR_READ_PIPE_FAILED: 'Read from data pipe failed',
   ERR_SEND_IMAGE: 'Image sent',
   ERR_INJECT_FAILED: 'Injection into process failed',
   ERR_INJECT_EXCEPTION: 'InjectThread: Exception encountered',
   ERR_GET_EXIT_CODE_FAILED: 'Get of injected thread exit code failed',
   ERR_INJECT_THREAD_ENDED: 'Injected thread has closed abnormally',
   ERR_INJECT_WRITE_FAILED: 'InjectThread: Write of data to pipe failed',
   ERR_INJECT_INPUT_DESKTOP_ERROR: 'InjectThread: Process is not in a visible desktop',
   ERR_INJECT_ALLOC_FAILED: 'InjectThread: Memory allocation failed',
   ERR_INJECT_OPEN_PIPE_FAILED: 'InjectThread: Open of data pipe failed',
   ERR_WINDOW_PLACEMENT_ERROR: 'Failed to modify window placement',
   ERR_WINDOW_IS_NOT_VISIBLE: 'Window is not visible',
   ERR_INJECT_UNKNOWN: 'Unknown error returned from injection routine',
   ERR_GET_SAFEPOINT_FAILED: 'Failed to find safe point at which to maximize window',
   ERR_INJECTION_REQUIRED: 'Injection required in this environment'
   }