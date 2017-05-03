# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: mutex.py
import _dsz
import dsz
import dsz.lp
import sys

class Mutex:

    def __init__(self, name, maxTries=10000):
        self.name = '_MUTEX_%s' % name
        self.maxTries = maxTries

    def acquire(self, maxTries=10000):
        id = int(dsz.script.Env['script_command_id'])
        while True:
            if dsz.script.CheckStop():
                return False
            owner = self._GetMutexOwner()
            if id == owner:
                return True
            if owner == 0:
                dsz.env.Set(self.name, '%d' % id, 0, '')
            maxTries = maxTries - 1
            if maxTries == 0:
                return False
            dsz.Sleep(250)

    def release(self):
        id = int(dsz.script.Env['script_command_id'])
        owner = self._GetMutexOwner()
        if owner == id:
            return dsz.env.Delete(self.name, 0, '')
        return False

    def _GetMutexOwner(self):
        if not dsz.env.Check(self.name, 0, ''):
            return 0
        try:
            owner = int(dsz.env.Get(self.name, 0, ''))
            isRunning = dsz.cmd.data.Get('CommandMetaData::IsRunning', dsz.TYPE_BOOL, owner)
            if isRunning[0]:
                return owner
            return 0
        except:
            return -1

    def __enter__(self):
        if not self.acquire(self.maxTries):
            raise MutexException(self.name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
        return False


class MutexException(Exception):

    def __init__(self, name=None):
        self.MutexName = name

    def __str__(self):
        if self.MutexName:
            return 'Unable to acquire mutex %s' % self.MutexName
        else:
            return 'Unable to acquire a mutex'