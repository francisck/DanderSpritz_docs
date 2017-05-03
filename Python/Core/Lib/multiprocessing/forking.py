# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: forking.py
import os
import sys
import signal
from multiprocessing import util, process
__all__ = [
 'Popen', 'assert_spawning', 'exit', 'duplicate', 'close', 'ForkingPickler']

def assert_spawning(self):
    if not Popen.thread_is_spawning():
        raise RuntimeError('%s objects should only be shared between processes through inheritance' % type(self).__name__)


from pickle import Pickler

class ForkingPickler(Pickler):
    dispatch = Pickler.dispatch.copy()

    @classmethod
    def register(cls, type, reduce):

        def dispatcher(self, obj):
            rv = reduce(obj)
            self.save_reduce(obj=obj, *rv)

        cls.dispatch[type] = dispatcher


def _reduce_method(m):
    if m.im_self is None:
        return (getattr, (m.im_class, m.im_func.func_name))
    else:
        return (
         getattr, (m.im_self, m.im_func.func_name))
        return


ForkingPickler.register(type(ForkingPickler.save), _reduce_method)

def _reduce_method_descriptor(m):
    return (
     getattr, (m.__objclass__, m.__name__))


ForkingPickler.register(type(list.append), _reduce_method_descriptor)
ForkingPickler.register(type(int.__add__), _reduce_method_descriptor)
try:
    from functools import partial
except ImportError:
    pass
else:

    def _reduce_partial(p):
        return (_rebuild_partial, (p.func, p.args, p.keywords or {}))


    def _rebuild_partial(func, args, keywords):
        return partial(func, *args, **keywords)


    ForkingPickler.register(partial, _reduce_partial)

if sys.platform != 'win32':
    import time
    exit = os._exit
    duplicate = os.dup
    close = os.close

    class Popen(object):

        def __init__(self, process_obj):
            sys.stdout.flush()
            sys.stderr.flush()
            self.returncode = None
            self.pid = os.fork()
            if self.pid == 0:
                if 'random' in sys.modules:
                    import random
                    random.seed()
                code = process_obj._bootstrap()
                sys.stdout.flush()
                sys.stderr.flush()
                os._exit(code)
            return

        def poll(self, flag=os.WNOHANG):
            if self.returncode is None:
                try:
                    pid, sts = os.waitpid(self.pid, flag)
                except os.error:
                    return

                if pid == self.pid:
                    if os.WIFSIGNALED(sts):
                        self.returncode = -os.WTERMSIG(sts)
                    else:
                        self.returncode = os.WEXITSTATUS(sts)
            return self.returncode

        def wait(self, timeout=None):
            if timeout is None:
                return self.poll(0)
            else:
                deadline = time.time() + timeout
                delay = 0.0005
                while 1:
                    res = self.poll()
                    if res is not None:
                        break
                    remaining = deadline - time.time()
                    if remaining <= 0:
                        break
                    delay = min(delay * 2, remaining, 0.05)
                    time.sleep(delay)

                return res

        def terminate(self):
            if self.returncode is None:
                try:
                    os.kill(self.pid, signal.SIGTERM)
                except OSError as e:
                    if self.wait(timeout=0.1) is None:
                        raise

            return

        @staticmethod
        def thread_is_spawning():
            return False


else:
    import thread
    import msvcrt
    import _subprocess
    import time
    from _multiprocessing import win32, Connection, PipeConnection
    from .util import Finalize
    from pickle import load, HIGHEST_PROTOCOL

    def dump(obj, file, protocol=None):
        ForkingPickler(file, protocol).dump(obj)


    TERMINATE = 65536
    WINEXE = sys.platform == 'win32' and getattr(sys, 'frozen', False)
    WINSERVICE = sys.executable.lower().endswith('pythonservice.exe')
    exit = win32.ExitProcess
    close = win32.CloseHandle
    if WINSERVICE:
        _python_exe = os.path.join(sys.exec_prefix, 'python.exe')
    else:
        _python_exe = sys.executable

    def set_executable(exe):
        global _python_exe
        _python_exe = exe


    def duplicate(handle, target_process=None, inheritable=False):
        if target_process is None:
            target_process = _subprocess.GetCurrentProcess()
        return _subprocess.DuplicateHandle(_subprocess.GetCurrentProcess(), handle, target_process, 0, inheritable, _subprocess.DUPLICATE_SAME_ACCESS).Detach()


    class Popen(object):
        """
        Start a subprocess to run the code of a process object
        """
        _tls = thread._local()

        def __init__(self, process_obj):
            rfd, wfd = os.pipe()
            rhandle = duplicate(msvcrt.get_osfhandle(rfd), inheritable=True)
            os.close(rfd)
            cmd = get_command_line() + [rhandle]
            cmd = ' '.join(('"%s"' % x for x in cmd))
            hp, ht, pid, tid = _subprocess.CreateProcess(_python_exe, cmd, None, None, 1, 0, None, None, None)
            ht.Close()
            close(rhandle)
            self.pid = pid
            self.returncode = None
            self._handle = hp
            prep_data = get_preparation_data(process_obj._name)
            to_child = os.fdopen(wfd, 'wb')
            Popen._tls.process_handle = int(hp)
            try:
                dump(prep_data, to_child, HIGHEST_PROTOCOL)
                dump(process_obj, to_child, HIGHEST_PROTOCOL)
            finally:
                del Popen._tls.process_handle
                to_child.close()

            return

        @staticmethod
        def thread_is_spawning():
            return getattr(Popen._tls, 'process_handle', None) is not None

        @staticmethod
        def duplicate_for_child(handle):
            return duplicate(handle, Popen._tls.process_handle)

        def wait(self, timeout=None):
            if self.returncode is None:
                if timeout is None:
                    msecs = _subprocess.INFINITE
                else:
                    msecs = max(0, int(timeout * 1000 + 0.5))
                res = _subprocess.WaitForSingleObject(int(self._handle), msecs)
                if res == _subprocess.WAIT_OBJECT_0:
                    code = _subprocess.GetExitCodeProcess(self._handle)
                    if code == TERMINATE:
                        code = -signal.SIGTERM
                    self.returncode = code
            return self.returncode

        def poll(self):
            return self.wait(timeout=0)

        def terminate(self):
            if self.returncode is None:
                try:
                    _subprocess.TerminateProcess(int(self._handle), TERMINATE)
                except WindowsError:
                    if self.wait(timeout=0.1) is None:
                        raise

            return


    def is_forking(argv):
        """
        Return whether commandline indicates we are forking
        """
        if len(argv) >= 2 and argv[1] == '--multiprocessing-fork':
            return True
        else:
            return False


    def freeze_support():
        """
        Run code for process object if this in not the main process
        """
        if is_forking(sys.argv):
            main()
            sys.exit()


    def get_command_line():
        """
        Returns prefix of command line used for spawning a child process
        """
        if process.current_process()._identity == () and is_forking(sys.argv):
            raise RuntimeError('\n            Attempt to start a new process before the current process\n            has finished its bootstrapping phase.\n\n            This probably means that you are on Windows and you have\n            forgotten to use the proper idiom in the main module:\n\n                if __name__ == \'__main__\':\n                    freeze_support()\n                    ...\n\n            The "freeze_support()" line can be omitted if the program\n            is not going to be frozen to produce a Windows executable.')
        if getattr(sys, 'frozen', False):
            return [sys.executable, '--multiprocessing-fork']
        else:
            prog = 'from multiprocessing.forking import main; main()'
            return [
             _python_exe, '-c', prog, '--multiprocessing-fork']


    def main():
        """
        Run code specifed by data received over pipe
        """
        handle = int(sys.argv[-1])
        fd = msvcrt.open_osfhandle(handle, os.O_RDONLY)
        from_parent = os.fdopen(fd, 'rb')
        process.current_process()._inheriting = True
        preparation_data = load(from_parent)
        prepare(preparation_data)
        self = load(from_parent)
        process.current_process()._inheriting = False
        from_parent.close()
        exitcode = self._bootstrap()
        exit(exitcode)


    def get_preparation_data(name):
        """
        Return info about parent needed by child to unpickle process object
        """
        from .util import _logger, _log_to_stderr
        d = dict(name=name, sys_path=sys.path, sys_argv=sys.argv, log_to_stderr=_log_to_stderr, orig_dir=process.ORIGINAL_DIR, authkey=process.current_process().authkey)
        if _logger is not None:
            d['log_level'] = _logger.getEffectiveLevel()
        if not WINEXE and not WINSERVICE:
            main_path = getattr(sys.modules['__main__'], '__file__', None)
            if not main_path and sys.argv[0] not in ('', '-c'):
                main_path = sys.argv[0]
            if main_path is not None:
                if not os.path.isabs(main_path) and process.ORIGINAL_DIR is not None:
                    main_path = os.path.join(process.ORIGINAL_DIR, main_path)
                d['main_path'] = os.path.normpath(main_path)
        return d


    def reduce_connection(conn):
        if not Popen.thread_is_spawning():
            raise RuntimeError('By default %s objects can only be shared between processes\nusing inheritance' % type(conn).__name__)
        return (
         type(conn),
         (Popen.duplicate_for_child(conn.fileno()),
          conn.readable, conn.writable))


    ForkingPickler.register(Connection, reduce_connection)
    ForkingPickler.register(PipeConnection, reduce_connection)
old_main_modules = []

def prepare(data):
    """
    Try to get current process ready to unpickle process object
    """
    old_main_modules.append(sys.modules['__main__'])
    if 'name' in data:
        process.current_process().name = data['name']
    if 'authkey' in data:
        process.current_process()._authkey = data['authkey']
    if 'log_to_stderr' in data and data['log_to_stderr']:
        util.log_to_stderr()
    if 'log_level' in data:
        util.get_logger().setLevel(data['log_level'])
    if 'sys_path' in data:
        sys.path = data['sys_path']
    if 'sys_argv' in data:
        sys.argv = data['sys_argv']
    if 'dir' in data:
        os.chdir(data['dir'])
    if 'orig_dir' in data:
        process.ORIGINAL_DIR = data['orig_dir']
    if 'main_path' in data:
        main_path = data['main_path']
        main_name = os.path.splitext(os.path.basename(main_path))[0]
        if main_name == '__init__':
            main_name = os.path.basename(os.path.dirname(main_path))
        if main_name != 'ipython':
            import imp
            if main_path is None:
                dirs = None
            elif os.path.basename(main_path).startswith('__init__.py'):
                dirs = [
                 os.path.dirname(os.path.dirname(main_path))]
            else:
                dirs = [
                 os.path.dirname(main_path)]
            file, path_name, etc = imp.find_module(main_name, dirs)
            try:
                main_module = imp.load_module('__parents_main__', file, path_name, etc)
            finally:
                if file:
                    file.close()

            sys.modules['__main__'] = main_module
            main_module.__name__ = '__main__'
            for obj in main_module.__dict__.values():
                try:
                    if obj.__module__ == '__parents_main__':
                        obj.__module__ = '__main__'
                except Exception:
                    pass

    return