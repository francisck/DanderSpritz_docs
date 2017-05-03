# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: main.py
"""Unittest main program"""
import sys
import os
import types
from . import loader, runner
from .signals import installHandler
__unittest = True
FAILFAST = '  -f, --failfast   Stop on first failure\n'
CATCHBREAK = '  -c, --catch      Catch control-C and display results\n'
BUFFEROUTPUT = '  -b, --buffer     Buffer stdout and stderr during test runs\n'
USAGE_AS_MAIN = "Usage: %(progName)s [options] [tests]\n\nOptions:\n  -h, --help       Show this message\n  -v, --verbose    Verbose output\n  -q, --quiet      Minimal output\n%(failfast)s%(catchbreak)s%(buffer)s\nExamples:\n  %(progName)s test_module               - run tests from test_module\n  %(progName)s module.TestClass          - run tests from module.TestClass\n  %(progName)s module.Class.test_method  - run specified test method\n\n[tests] can be a list of any number of test modules, classes and test\nmethods.\n\nAlternative Usage: %(progName)s discover [options]\n\nOptions:\n  -v, --verbose    Verbose output\n%(failfast)s%(catchbreak)s%(buffer)s  -s directory     Directory to start discovery ('.' default)\n  -p pattern       Pattern to match test files ('test*.py' default)\n  -t directory     Top level directory of project (default to\n                   start directory)\n\nFor test discovery all test modules must be importable from the top\nlevel directory of the project.\n"
USAGE_FROM_MODULE = "Usage: %(progName)s [options] [test] [...]\n\nOptions:\n  -h, --help       Show this message\n  -v, --verbose    Verbose output\n  -q, --quiet      Minimal output\n%(failfast)s%(catchbreak)s%(buffer)s\nExamples:\n  %(progName)s                               - run default set of tests\n  %(progName)s MyTestSuite                   - run suite 'MyTestSuite'\n  %(progName)s MyTestCase.testSomething      - run MyTestCase.testSomething\n  %(progName)s MyTestCase                    - run all 'test*' test methods\n                                               in MyTestCase\n"

class TestProgram(object):
    """A command-line program that runs a set of tests; this is primarily
       for making test modules conveniently executable.
    """
    USAGE = USAGE_FROM_MODULE
    failfast = catchbreak = buffer = progName = None

    def __init__(self, module='__main__', defaultTest=None, argv=None, testRunner=None, testLoader=loader.defaultTestLoader, exit=True, verbosity=1, failfast=None, catchbreak=None, buffer=None):
        if isinstance(module, basestring):
            self.module = __import__(module)
            for part in module.split('.')[1:]:
                self.module = getattr(self.module, part)

        else:
            self.module = module
        if argv is None:
            argv = sys.argv
        self.exit = exit
        self.failfast = failfast
        self.catchbreak = catchbreak
        self.verbosity = verbosity
        self.buffer = buffer
        self.defaultTest = defaultTest
        self.testRunner = testRunner
        self.testLoader = testLoader
        self.progName = os.path.basename(argv[0])
        self.parseArgs(argv)
        self.runTests()
        return

    def usageExit(self, msg=None):
        if msg:
            print msg
        usage = {'progName': self.progName,'catchbreak': '','failfast': '','buffer': ''}
        if self.failfast != False:
            usage['failfast'] = FAILFAST
        if self.catchbreak != False:
            usage['catchbreak'] = CATCHBREAK
        if self.buffer != False:
            usage['buffer'] = BUFFEROUTPUT
        print self.USAGE % usage
        sys.exit(2)

    def parseArgs(self, argv):
        if len(argv) > 1 and argv[1].lower() == 'discover':
            self._do_discovery(argv[2:])
            return
        else:
            import getopt
            long_opts = [
             'help', 'verbose', 'quiet', 'failfast', 'catch', 'buffer']
            try:
                options, args = getopt.getopt(argv[1:], 'hHvqfcb', long_opts)
                for opt, value in options:
                    if opt in ('-h', '-H', '--help'):
                        self.usageExit()
                    if opt in ('-q', '--quiet'):
                        self.verbosity = 0
                    if opt in ('-v', '--verbose'):
                        self.verbosity = 2
                    if opt in ('-f', '--failfast'):
                        if self.failfast is None:
                            self.failfast = True
                    if opt in ('-c', '--catch'):
                        if self.catchbreak is None:
                            self.catchbreak = True
                    if opt in ('-b', '--buffer'):
                        if self.buffer is None:
                            self.buffer = True

                if len(args) == 0 and self.defaultTest is None:
                    self.testNames = None
                elif len(args) > 0:
                    self.testNames = args
                    if __name__ == '__main__':
                        self.module = None
                else:
                    self.testNames = (
                     self.defaultTest,)
                self.createTests()
            except getopt.error as msg:
                self.usageExit(msg)

            return

    def createTests(self):
        if self.testNames is None:
            self.test = self.testLoader.loadTestsFromModule(self.module)
        else:
            self.test = self.testLoader.loadTestsFromNames(self.testNames, self.module)
        return

    def _do_discovery(self, argv, Loader=loader.TestLoader):
        self.progName = '%s discover' % self.progName
        import optparse
        parser = optparse.OptionParser()
        parser.prog = self.progName
        parser.add_option('-v', '--verbose', dest='verbose', default=False, help='Verbose output', action='store_true')
        if self.failfast != False:
            parser.add_option('-f', '--failfast', dest='failfast', default=False, help='Stop on first fail or error', action='store_true')
        if self.catchbreak != False:
            parser.add_option('-c', '--catch', dest='catchbreak', default=False, help='Catch ctrl-C and display results so far', action='store_true')
        if self.buffer != False:
            parser.add_option('-b', '--buffer', dest='buffer', default=False, help='Buffer stdout and stderr during tests', action='store_true')
        parser.add_option('-s', '--start-directory', dest='start', default='.', help="Directory to start discovery ('.' default)")
        parser.add_option('-p', '--pattern', dest='pattern', default='test*.py', help="Pattern to match tests ('test*.py' default)")
        parser.add_option('-t', '--top-level-directory', dest='top', default=None, help='Top level directory of project (defaults to start directory)')
        options, args = parser.parse_args(argv)
        if len(args) > 3:
            self.usageExit()
        for name, value in zip(('start', 'pattern', 'top'), args):
            setattr(options, name, value)

        if self.failfast is None:
            self.failfast = options.failfast
        if self.catchbreak is None:
            self.catchbreak = options.catchbreak
        if self.buffer is None:
            self.buffer = options.buffer
        if options.verbose:
            self.verbosity = 2
        start_dir = options.start
        pattern = options.pattern
        top_level_dir = options.top
        loader = Loader()
        self.test = loader.discover(start_dir, pattern, top_level_dir)
        return

    def runTests(self):
        if self.catchbreak:
            installHandler()
        if self.testRunner is None:
            self.testRunner = runner.TextTestRunner
        if isinstance(self.testRunner, (type, types.ClassType)):
            try:
                testRunner = self.testRunner(verbosity=self.verbosity, failfast=self.failfast, buffer=self.buffer)
            except TypeError:
                testRunner = self.testRunner()

        else:
            testRunner = self.testRunner
        self.result = testRunner.run(self.test)
        if self.exit:
            sys.exit(not self.result.wasSuccessful())
        return


main = TestProgram