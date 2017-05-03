# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: handlers.py
"""
Additional handlers for the logging package for Python. The core package is
based on PEP 282 and comments thereto in comp.lang.python, and influenced by
Apache's log4j system.

Copyright (C) 2001-2010 Vinay Sajip. All Rights Reserved.

To use, simply 'import logging.handlers' and log away!
"""
import logging
import socket
import os
import cPickle
import struct
import time
import re
from stat import ST_DEV, ST_INO, ST_MTIME
try:
    import codecs
except ImportError:
    codecs = None

try:
    unicode
    _unicode = True
except NameError:
    _unicode = False

DEFAULT_TCP_LOGGING_PORT = 9020
DEFAULT_UDP_LOGGING_PORT = 9021
DEFAULT_HTTP_LOGGING_PORT = 9022
DEFAULT_SOAP_LOGGING_PORT = 9023
SYSLOG_UDP_PORT = 514
SYSLOG_TCP_PORT = 514
_MIDNIGHT = 86400

class BaseRotatingHandler(logging.FileHandler):
    """
    Base class for handlers that rotate log files at a certain point.
    Not meant to be instantiated directly.  Instead, use RotatingFileHandler
    or TimedRotatingFileHandler.
    """

    def __init__(self, filename, mode, encoding=None, delay=0):
        """
        Use the specified filename for streamed logging
        """
        if codecs is None:
            encoding = None
        logging.FileHandler.__init__(self, filename, mode, encoding, delay)
        self.mode = mode
        self.encoding = encoding
        return

    def emit(self, record):
        """
        Emit a record.
        
        Output the record to the file, catering for rollover as described
        in doRollover().
        """
        try:
            if self.shouldRollover(record):
                self.doRollover()
            logging.FileHandler.emit(self, record)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


class RotatingFileHandler(BaseRotatingHandler):
    """
    Handler for logging to a set of files, which switches from one file
    to the next when the current file reaches a certain size.
    """

    def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=0):
        """
        Open the specified file and use it as the stream for logging.
        
        By default, the file grows indefinitely. You can specify particular
        values of maxBytes and backupCount to allow the file to rollover at
        a predetermined size.
        
        Rollover occurs whenever the current log file is nearly maxBytes in
        length. If backupCount is >= 1, the system will successively create
        new files with the same pathname as the base file, but with extensions
        ".1", ".2" etc. appended to it. For example, with a backupCount of 5
        and a base file name of "app.log", you would get "app.log",
        "app.log.1", "app.log.2", ... through to "app.log.5". The file being
        written to is always "app.log" - when it gets filled up, it is closed
        and renamed to "app.log.1", and if files "app.log.1", "app.log.2" etc.
        exist, then they are renamed to "app.log.2", "app.log.3" etc.
        respectively.
        
        If maxBytes is zero, rollover never occurs.
        """
        if maxBytes > 0:
            mode = 'a'
        BaseRotatingHandler.__init__(self, filename, mode, encoding, delay)
        self.maxBytes = maxBytes
        self.backupCount = backupCount

    def doRollover(self):
        """
        Do a rollover, as described in __init__().
        """
        if self.stream:
            self.stream.close()
            self.stream = None
        if self.backupCount > 0:
            for i in range(self.backupCount - 1, 0, -1):
                sfn = '%s.%d' % (self.baseFilename, i)
                dfn = '%s.%d' % (self.baseFilename, i + 1)
                if os.path.exists(sfn):
                    if os.path.exists(dfn):
                        os.remove(dfn)
                    os.rename(sfn, dfn)

            dfn = self.baseFilename + '.1'
            if os.path.exists(dfn):
                os.remove(dfn)
            os.rename(self.baseFilename, dfn)
        self.mode = 'w'
        self.stream = self._open()
        return

    def shouldRollover(self, record):
        """
        Determine if rollover should occur.
        
        Basically, see if the supplied record would cause the file to exceed
        the size limit we have.
        """
        if self.stream is None:
            self.stream = self._open()
        if self.maxBytes > 0:
            msg = '%s\n' % self.format(record)
            self.stream.seek(0, 2)
            if self.stream.tell() + len(msg) >= self.maxBytes:
                return 1
        return 0


class TimedRotatingFileHandler(BaseRotatingHandler):
    """
    Handler for logging to a file, rotating the log file at certain timed
    intervals.
    
    If backupCount is > 0, when rollover is done, no more than backupCount
    files are kept - the oldest ones are deleted.
    """

    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False):
        BaseRotatingHandler.__init__(self, filename, 'a', encoding, delay)
        self.when = when.upper()
        self.backupCount = backupCount
        self.utc = utc
        if self.when == 'S':
            self.interval = 1
            self.suffix = '%Y-%m-%d_%H-%M-%S'
            self.extMatch = '^\\d{4}-\\d{2}-\\d{2}_\\d{2}-\\d{2}-\\d{2}$'
        elif self.when == 'M':
            self.interval = 60
            self.suffix = '%Y-%m-%d_%H-%M'
            self.extMatch = '^\\d{4}-\\d{2}-\\d{2}_\\d{2}-\\d{2}$'
        elif self.when == 'H':
            self.interval = 3600
            self.suffix = '%Y-%m-%d_%H'
            self.extMatch = '^\\d{4}-\\d{2}-\\d{2}_\\d{2}$'
        elif self.when == 'D' or self.when == 'MIDNIGHT':
            self.interval = 86400
            self.suffix = '%Y-%m-%d'
            self.extMatch = '^\\d{4}-\\d{2}-\\d{2}$'
        elif self.when.startswith('W'):
            self.interval = 604800
            if len(self.when) != 2:
                raise ValueError('You must specify a day for weekly rollover from 0 to 6 (0 is Monday): %s' % self.when)
            if self.when[1] < '0' or self.when[1] > '6':
                raise ValueError('Invalid day specified for weekly rollover: %s' % self.when)
            self.dayOfWeek = int(self.when[1])
            self.suffix = '%Y-%m-%d'
            self.extMatch = '^\\d{4}-\\d{2}-\\d{2}$'
        else:
            raise ValueError('Invalid rollover interval specified: %s' % self.when)
        self.extMatch = re.compile(self.extMatch)
        self.interval = self.interval * interval
        if os.path.exists(filename):
            t = os.stat(filename)[ST_MTIME]
        else:
            t = int(time.time())
        self.rolloverAt = self.computeRollover(t)

    def computeRollover(self, currentTime):
        """
        Work out the rollover time based on the specified time.
        """
        result = currentTime + self.interval
        if self.when == 'MIDNIGHT' or self.when.startswith('W'):
            if self.utc:
                t = time.gmtime(currentTime)
            else:
                t = time.localtime(currentTime)
            currentHour = t[3]
            currentMinute = t[4]
            currentSecond = t[5]
            r = _MIDNIGHT - ((currentHour * 60 + currentMinute) * 60 + currentSecond)
            result = currentTime + r
            if self.when.startswith('W'):
                day = t[6]
                if day != self.dayOfWeek:
                    if day < self.dayOfWeek:
                        daysToWait = self.dayOfWeek - day
                    else:
                        daysToWait = 6 - day + self.dayOfWeek + 1
                    newRolloverAt = result + daysToWait * 86400
                    if not self.utc:
                        dstNow = t[-1]
                        dstAtRollover = time.localtime(newRolloverAt)[-1]
                        if dstNow != dstAtRollover:
                            if not dstNow:
                                newRolloverAt = newRolloverAt - 3600
                            else:
                                newRolloverAt = newRolloverAt + 3600
                    result = newRolloverAt
        return result

    def shouldRollover(self, record):
        """
        Determine if rollover should occur.
        
        record is not used, as we are just comparing times, but it is needed so
        the method signatures are the same
        """
        t = int(time.time())
        if t >= self.rolloverAt:
            return 1
        return 0

    def getFilesToDelete(self):
        """
        Determine the files to delete when rolling over.
        
        More specific than the earlier method, which just used glob.glob().
        """
        dirName, baseName = os.path.split(self.baseFilename)
        fileNames = os.listdir(dirName)
        result = []
        prefix = baseName + '.'
        plen = len(prefix)
        for fileName in fileNames:
            if fileName[:plen] == prefix:
                suffix = fileName[plen:]
                if self.extMatch.match(suffix):
                    result.append(os.path.join(dirName, fileName))

        result.sort()
        if len(result) < self.backupCount:
            result = []
        else:
            result = result[:len(result) - self.backupCount]
        return result

    def doRollover(self):
        """
        do a rollover; in this case, a date/time stamp is appended to the filename
        when the rollover happens.  However, you want the file to be named for the
        start of the interval, not the current time.  If there is a backup count,
        then we have to get a list of matching filenames, sort them and remove
        the one with the oldest suffix.
        """
        if self.stream:
            self.stream.close()
            self.stream = None
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
        dfn = self.baseFilename + '.' + time.strftime(self.suffix, timeTuple)
        if os.path.exists(dfn):
            os.remove(dfn)
        os.rename(self.baseFilename, dfn)
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)

        self.mode = 'w'
        self.stream = self._open()
        currentTime = int(time.time())
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval

        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstNow = time.localtime(currentTime)[-1]
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:
                    newRolloverAt = newRolloverAt - 3600
                else:
                    newRolloverAt = newRolloverAt + 3600
        self.rolloverAt = newRolloverAt
        return


class WatchedFileHandler(logging.FileHandler):
    """
    A handler for logging to a file, which watches the file
    to see if it has changed while in use. This can happen because of
    usage of programs such as newsyslog and logrotate which perform
    log file rotation. This handler, intended for use under Unix,
    watches the file to see if it has changed since the last emit.
    (A file has changed if its device or inode have changed.)
    If it has changed, the old file stream is closed, and the file
    opened to get a new stream.
    
    This handler is not appropriate for use under Windows, because
    under Windows open files cannot be moved or renamed - logging
    opens the files with exclusive locks - and so there is no need
    for such a handler. Furthermore, ST_INO is not supported under
    Windows; stat always returns zero for this value.
    
    This handler is based on a suggestion and patch by Chad J.
    Schroeder.
    """

    def __init__(self, filename, mode='a', encoding=None, delay=0):
        logging.FileHandler.__init__(self, filename, mode, encoding, delay)
        if not os.path.exists(self.baseFilename):
            self.dev, self.ino = (-1, -1)
        else:
            stat = os.stat(self.baseFilename)
            self.dev, self.ino = stat[ST_DEV], stat[ST_INO]

    def emit(self, record):
        """
        Emit a record.
        
        First check if the underlying file has changed, and if it
        has, close the old stream and reopen the file to get the
        current stream.
        """
        if not os.path.exists(self.baseFilename):
            stat = None
            changed = 1
        else:
            stat = os.stat(self.baseFilename)
            changed = stat[ST_DEV] != self.dev or stat[ST_INO] != self.ino
        if changed and self.stream is not None:
            self.stream.flush()
            self.stream.close()
            self.stream = self._open()
            if stat is None:
                stat = os.stat(self.baseFilename)
            self.dev, self.ino = stat[ST_DEV], stat[ST_INO]
        logging.FileHandler.emit(self, record)
        return


class SocketHandler(logging.Handler):
    """
    A handler class which writes logging records, in pickle format, to
    a streaming socket. The socket is kept open across logging calls.
    If the peer resets it, an attempt is made to reconnect on the next call.
    The pickle which is sent is that of the LogRecord's attribute dictionary
    (__dict__), so that the receiver does not need to have the logging module
    installed in order to process the logging event.
    
    To unpickle the record at the receiving end into a LogRecord, use the
    makeLogRecord function.
    """

    def __init__(self, host, port):
        """
        Initializes the handler with a specific host address and port.
        
        The attribute 'closeOnError' is set to 1 - which means that if
        a socket error occurs, the socket is silently closed and then
        reopened on the next logging call.
        """
        logging.Handler.__init__(self)
        self.host = host
        self.port = port
        self.sock = None
        self.closeOnError = 0
        self.retryTime = None
        self.retryStart = 1.0
        self.retryMax = 30.0
        self.retryFactor = 2.0
        return

    def makeSocket(self, timeout=1):
        """
        A factory method which allows subclasses to define the precise
        type of socket they want.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if hasattr(s, 'settimeout'):
            s.settimeout(timeout)
        s.connect((self.host, self.port))
        return s

    def createSocket(self):
        """
        Try to create a socket, using an exponential backoff with
        a max retry time. Thanks to Robert Olson for the original patch
        (SF #815911) which has been slightly refactored.
        """
        now = time.time()
        if self.retryTime is None:
            attempt = 1
        else:
            attempt = now >= self.retryTime
        if attempt:
            try:
                self.sock = self.makeSocket()
                self.retryTime = None
            except socket.error:
                if self.retryTime is None:
                    self.retryPeriod = self.retryStart
                else:
                    self.retryPeriod = self.retryPeriod * self.retryFactor
                    if self.retryPeriod > self.retryMax:
                        self.retryPeriod = self.retryMax
                self.retryTime = now + self.retryPeriod

        return

    def send(self, s):
        """
        Send a pickled string to the socket.
        
        This function allows for partial sends which can happen when the
        network is busy.
        """
        if self.sock is None:
            self.createSocket()
        if self.sock:
            try:
                if hasattr(self.sock, 'sendall'):
                    self.sock.sendall(s)
                else:
                    sentsofar = 0
                    left = len(s)
                    while left > 0:
                        sent = self.sock.send(s[sentsofar:])
                        sentsofar = sentsofar + sent
                        left = left - sent

            except socket.error:
                self.sock.close()
                self.sock = None

        return

    def makePickle(self, record):
        """
        Pickles the record in binary format with a length prefix, and
        returns it ready for transmission across the socket.
        """
        ei = record.exc_info
        if ei:
            dummy = self.format(record)
            record.exc_info = None
        s = cPickle.dumps(record.__dict__, 1)
        if ei:
            record.exc_info = ei
        slen = struct.pack('>L', len(s))
        return slen + s

    def handleError(self, record):
        """
        Handle an error during logging.
        
        An error has occurred during logging. Most likely cause -
        connection lost. Close the socket so that we can retry on the
        next event.
        """
        if self.closeOnError and self.sock:
            self.sock.close()
            self.sock = None
        else:
            logging.Handler.handleError(self, record)
        return

    def emit(self, record):
        """
        Emit a record.
        
        Pickles the record and writes it to the socket in binary format.
        If there is an error with the socket, silently drop the packet.
        If there was a problem with the socket, re-establishes the
        socket.
        """
        try:
            s = self.makePickle(record)
            self.send(s)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def close(self):
        """
        Closes the socket.
        """
        if self.sock:
            self.sock.close()
            self.sock = None
        logging.Handler.close(self)
        return


class DatagramHandler(SocketHandler):
    """
    A handler class which writes logging records, in pickle format, to
    a datagram socket.  The pickle which is sent is that of the LogRecord's
    attribute dictionary (__dict__), so that the receiver does not need to
    have the logging module installed in order to process the logging event.
    
    To unpickle the record at the receiving end into a LogRecord, use the
    makeLogRecord function.
    
    """

    def __init__(self, host, port):
        """
        Initializes the handler with a specific host address and port.
        """
        SocketHandler.__init__(self, host, port)
        self.closeOnError = 0

    def makeSocket(self):
        """
        The factory method of SocketHandler is here overridden to create
        a UDP socket (SOCK_DGRAM).
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return s

    def send(self, s):
        """
        Send a pickled string to a socket.
        
        This function no longer allows for partial sends which can happen
        when the network is busy - UDP does not guarantee delivery and
        can deliver packets out of sequence.
        """
        if self.sock is None:
            self.createSocket()
        self.sock.sendto(s, (self.host, self.port))
        return


class SysLogHandler(logging.Handler):
    """
    A handler class which sends formatted logging records to a syslog
    server. Based on Sam Rushing's syslog module:
    http://www.nightmare.com/squirl/python-ext/misc/syslog.py
    Contributed by Nicolas Untz (after which minor refactoring changes
    have been made).
    """
    LOG_EMERG = 0
    LOG_ALERT = 1
    LOG_CRIT = 2
    LOG_ERR = 3
    LOG_WARNING = 4
    LOG_NOTICE = 5
    LOG_INFO = 6
    LOG_DEBUG = 7
    LOG_KERN = 0
    LOG_USER = 1
    LOG_MAIL = 2
    LOG_DAEMON = 3
    LOG_AUTH = 4
    LOG_SYSLOG = 5
    LOG_LPR = 6
    LOG_NEWS = 7
    LOG_UUCP = 8
    LOG_CRON = 9
    LOG_AUTHPRIV = 10
    LOG_FTP = 11
    LOG_LOCAL0 = 16
    LOG_LOCAL1 = 17
    LOG_LOCAL2 = 18
    LOG_LOCAL3 = 19
    LOG_LOCAL4 = 20
    LOG_LOCAL5 = 21
    LOG_LOCAL6 = 22
    LOG_LOCAL7 = 23
    priority_names = {'alert': LOG_ALERT,
       'crit': LOG_CRIT,
       'critical': LOG_CRIT,
       'debug': LOG_DEBUG,
       'emerg': LOG_EMERG,
       'err': LOG_ERR,
       'error': LOG_ERR,
       'info': LOG_INFO,
       'notice': LOG_NOTICE,
       'panic': LOG_EMERG,
       'warn': LOG_WARNING,
       'warning': LOG_WARNING
       }
    facility_names = {'auth': LOG_AUTH,
       'authpriv': LOG_AUTHPRIV,
       'cron': LOG_CRON,
       'daemon': LOG_DAEMON,
       'ftp': LOG_FTP,
       'kern': LOG_KERN,
       'lpr': LOG_LPR,
       'mail': LOG_MAIL,
       'news': LOG_NEWS,
       'security': LOG_AUTH,
       'syslog': LOG_SYSLOG,
       'user': LOG_USER,
       'uucp': LOG_UUCP,
       'local0': LOG_LOCAL0,
       'local1': LOG_LOCAL1,
       'local2': LOG_LOCAL2,
       'local3': LOG_LOCAL3,
       'local4': LOG_LOCAL4,
       'local5': LOG_LOCAL5,
       'local6': LOG_LOCAL6,
       'local7': LOG_LOCAL7
       }
    priority_map = {'DEBUG': 'debug',
       'INFO': 'info',
       'WARNING': 'warning',
       'ERROR': 'error',
       'CRITICAL': 'critical'
       }

    def __init__(self, address=(
 'localhost', SYSLOG_UDP_PORT), facility=LOG_USER, socktype=socket.SOCK_DGRAM):
        """
        Initialize a handler.
        
        If address is specified as a string, a UNIX socket is used. To log to a
        local syslogd, "SysLogHandler(address="/dev/log")" can be used.
        If facility is not specified, LOG_USER is used.
        """
        logging.Handler.__init__(self)
        self.address = address
        self.facility = facility
        self.socktype = socktype
        if isinstance(address, basestring):
            self.unixsocket = 1
            self._connect_unixsocket(address)
        else:
            self.unixsocket = 0
            self.socket = socket.socket(socket.AF_INET, socktype)
            if socktype == socket.SOCK_STREAM:
                self.socket.connect(address)
        self.formatter = None
        return

    def _connect_unixsocket(self, address):
        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        try:
            self.socket.connect(address)
        except socket.error:
            self.socket.close()
            self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            self.socket.connect(address)

    log_format_string = '<%d>%s\x00'

    def encodePriority(self, facility, priority):
        """
        Encode the facility and priority. You can pass in strings or
        integers - if strings are passed, the facility_names and
        priority_names mapping dictionaries are used to convert them to
        integers.
        """
        if isinstance(facility, basestring):
            facility = self.facility_names[facility]
        if isinstance(priority, basestring):
            priority = self.priority_names[priority]
        return facility << 3 | priority

    def close(self):
        """
        Closes the socket.
        """
        if self.unixsocket:
            self.socket.close()
        logging.Handler.close(self)

    def mapPriority(self, levelName):
        """
        Map a logging level name to a key in the priority_names map.
        This is useful in two scenarios: when custom levels are being
        used, and in the case where you can't do a straightforward
        mapping by lowercasing the logging level name because of locale-
        specific issues (see SF #1524081).
        """
        return self.priority_map.get(levelName, 'warning')

    def emit(self, record):
        """
        Emit a record.
        
        The record is formatted, and then sent to the syslog server. If
        exception information is present, it is NOT sent to the server.
        """
        msg = self.format(record) + '\x00'
        prio = '<%d>' % self.encodePriority(self.facility, self.mapPriority(record.levelname))
        if type(msg) is unicode:
            msg = msg.encode('utf-8')
            if codecs:
                msg = codecs.BOM_UTF8 + msg
        msg = prio + msg
        try:
            if self.unixsocket:
                try:
                    self.socket.send(msg)
                except socket.error:
                    self._connect_unixsocket(self.address)
                    self.socket.send(msg)

            elif self.socktype == socket.SOCK_DGRAM:
                self.socket.sendto(msg, self.address)
            else:
                self.socket.sendall(msg)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


class SMTPHandler(logging.Handler):
    """
    A handler class which sends an SMTP email for each logging event.
    """

    def __init__(self, mailhost, fromaddr, toaddrs, subject, credentials=None, secure=None):
        """
        Initialize the handler.
        
        Initialize the instance with the from and to addresses and subject
        line of the email. To specify a non-standard SMTP port, use the
        (host, port) tuple format for the mailhost argument. To specify
        authentication credentials, supply a (username, password) tuple
        for the credentials argument. To specify the use of a secure
        protocol (TLS), pass in a tuple for the secure argument. This will
        only be used when authentication credentials are supplied. The tuple
        will be either an empty tuple, or a single-value tuple with the name
        of a keyfile, or a 2-value tuple with the names of the keyfile and
        certificate file. (This tuple is passed to the `starttls` method).
        """
        logging.Handler.__init__(self)
        if isinstance(mailhost, tuple):
            self.mailhost, self.mailport = mailhost
        else:
            self.mailhost, self.mailport = mailhost, None
        if isinstance(credentials, tuple):
            self.username, self.password = credentials
        else:
            self.username = None
        self.fromaddr = fromaddr
        if isinstance(toaddrs, basestring):
            toaddrs = [
             toaddrs]
        self.toaddrs = toaddrs
        self.subject = subject
        self.secure = secure
        return

    def getSubject(self, record):
        """
        Determine the subject for the email.
        
        If you want to specify a subject line which is record-dependent,
        override this method.
        """
        return self.subject

    def emit(self, record):
        """
        Emit a record.
        
        Format the record and send it to the specified addressees.
        """
        try:
            import smtplib
            from email.utils import formatdate
            port = self.mailport
            if not port:
                port = smtplib.SMTP_PORT
            smtp = smtplib.SMTP(self.mailhost, port)
            msg = self.format(record)
            msg = 'From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s' % (
             self.fromaddr,
             ','.join(self.toaddrs),
             self.getSubject(record),
             formatdate(), msg)
            if self.username:
                if self.secure is not None:
                    smtp.ehlo()
                    smtp.starttls(*self.secure)
                    smtp.ehlo()
                smtp.login(self.username, self.password)
            smtp.sendmail(self.fromaddr, self.toaddrs, msg)
            smtp.quit()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

        return


class NTEventLogHandler(logging.Handler):
    """
    A handler class which sends events to the NT Event Log. Adds a
    registry entry for the specified application name. If no dllname is
    provided, win32service.pyd (which contains some basic message
    placeholders) is used. Note that use of these placeholders will make
    your event logs big, as the entire message source is held in the log.
    If you want slimmer logs, you have to pass in the name of your own DLL
    which contains the message definitions you want to use in the event log.
    """

    def __init__(self, appname, dllname=None, logtype='Application'):
        logging.Handler.__init__(self)
        try:
            import win32evtlogutil
            import win32evtlog
            self.appname = appname
            self._welu = win32evtlogutil
            if not dllname:
                dllname = os.path.split(self._welu.__file__)
                dllname = os.path.split(dllname[0])
                dllname = os.path.join(dllname[0], 'win32service.pyd')
            self.dllname = dllname
            self.logtype = logtype
            self._welu.AddSourceToRegistry(appname, dllname, logtype)
            self.deftype = win32evtlog.EVENTLOG_ERROR_TYPE
            self.typemap = {logging.DEBUG: win32evtlog.EVENTLOG_INFORMATION_TYPE,
               logging.INFO: win32evtlog.EVENTLOG_INFORMATION_TYPE,
               logging.WARNING: win32evtlog.EVENTLOG_WARNING_TYPE,
               logging.ERROR: win32evtlog.EVENTLOG_ERROR_TYPE,
               logging.CRITICAL: win32evtlog.EVENTLOG_ERROR_TYPE
               }
        except ImportError:
            print 'The Python Win32 extensions for NT (service, event logging) appear not to be available.'
            self._welu = None

        return

    def getMessageID(self, record):
        """
        Return the message ID for the event record. If you are using your
        own messages, you could do this by having the msg passed to the
        logger being an ID rather than a formatting string. Then, in here,
        you could use a dictionary lookup to get the message ID. This
        version returns 1, which is the base message ID in win32service.pyd.
        """
        return 1

    def getEventCategory(self, record):
        """
        Return the event category for the record.
        
        Override this if you want to specify your own categories. This version
        returns 0.
        """
        return 0

    def getEventType(self, record):
        """
        Return the event type for the record.
        
        Override this if you want to specify your own types. This version does
        a mapping using the handler's typemap attribute, which is set up in
        __init__() to a dictionary which contains mappings for DEBUG, INFO,
        WARNING, ERROR and CRITICAL. If you are using your own levels you will
        either need to override this method or place a suitable dictionary in
        the handler's typemap attribute.
        """
        return self.typemap.get(record.levelno, self.deftype)

    def emit(self, record):
        """
        Emit a record.
        
        Determine the message ID, event category and event type. Then
        log the message in the NT event log.
        """
        if self._welu:
            try:
                id = self.getMessageID(record)
                cat = self.getEventCategory(record)
                type = self.getEventType(record)
                msg = self.format(record)
                self._welu.ReportEvent(self.appname, id, cat, type, [msg])
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                self.handleError(record)

    def close(self):
        """
        Clean up this handler.
        
        You can remove the application name from the registry as a
        source of event log entries. However, if you do this, you will
        not be able to see the events as you intended in the Event Log
        Viewer - it needs to be able to access the registry to get the
        DLL name.
        """
        logging.Handler.close(self)


class HTTPHandler(logging.Handler):
    """
    A class which sends records to a Web server, using either GET or
    POST semantics.
    """

    def __init__(self, host, url, method='GET'):
        """
        Initialize the instance with the host, the request URL, and the method
        ("GET" or "POST")
        """
        logging.Handler.__init__(self)
        method = method.upper()
        if method not in ('GET', 'POST'):
            raise ValueError('method must be GET or POST')
        self.host = host
        self.url = url
        self.method = method

    def mapLogRecord(self, record):
        """
        Default implementation of mapping the log record into a dict
        that is sent as the CGI data. Overwrite in your class.
        Contributed by Franz  Glasner.
        """
        return record.__dict__

    def emit(self, record):
        """
        Emit a record.
        
        Send the record to the Web server as a percent-encoded dictionary
        """
        try:
            import httplib
            import urllib
            host = self.host
            h = httplib.HTTP(host)
            url = self.url
            data = urllib.urlencode(self.mapLogRecord(record))
            if self.method == 'GET':
                if url.find('?') >= 0:
                    sep = '&'
                else:
                    sep = '?'
                url = url + '%c%s' % (sep, data)
            h.putrequest(self.method, url)
            i = host.find(':')
            if i >= 0:
                host = host[:i]
            h.putheader('Host', host)
            if self.method == 'POST':
                h.putheader('Content-type', 'application/x-www-form-urlencoded')
                h.putheader('Content-length', str(len(data)))
            h.endheaders(data if self.method == 'POST' else None)
            h.getreply()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

        return


class BufferingHandler(logging.Handler):
    """
    A handler class which buffers logging records in memory. Whenever each
    record is added to the buffer, a check is made to see if the buffer should
    be flushed. If it should, then flush() is expected to do what's needed.
      """

    def __init__(self, capacity):
        """
        Initialize the handler with the buffer size.
        """
        logging.Handler.__init__(self)
        self.capacity = capacity
        self.buffer = []

    def shouldFlush(self, record):
        """
        Should the handler flush its buffer?
        
        Returns true if the buffer is up to capacity. This method can be
        overridden to implement custom flushing strategies.
        """
        return len(self.buffer) >= self.capacity

    def emit(self, record):
        """
        Emit a record.
        
        Append the record. If shouldFlush() tells us to, call flush() to process
        the buffer.
        """
        self.buffer.append(record)
        if self.shouldFlush(record):
            self.flush()

    def flush(self):
        """
        Override to implement custom flushing behaviour.
        
        This version just zaps the buffer to empty.
        """
        self.buffer = []

    def close(self):
        """
        Close the handler.
        
        This version just flushes and chains to the parent class' close().
        """
        self.flush()
        logging.Handler.close(self)


class MemoryHandler(BufferingHandler):
    """
    A handler class which buffers logging records in memory, periodically
    flushing them to a target handler. Flushing occurs whenever the buffer
    is full, or when an event of a certain severity or greater is seen.
    """

    def __init__(self, capacity, flushLevel=logging.ERROR, target=None):
        """
        Initialize the handler with the buffer size, the level at which
        flushing should occur and an optional target.
        
        Note that without a target being set either here or via setTarget(),
        a MemoryHandler is no use to anyone!
        """
        BufferingHandler.__init__(self, capacity)
        self.flushLevel = flushLevel
        self.target = target

    def shouldFlush(self, record):
        """
        Check for buffer full or a record at the flushLevel or higher.
        """
        return len(self.buffer) >= self.capacity or record.levelno >= self.flushLevel

    def setTarget(self, target):
        """
        Set the target handler for this handler.
        """
        self.target = target

    def flush(self):
        """
        For a MemoryHandler, flushing means just sending the buffered
        records to the target, if there is one. Override if you want
        different behaviour.
        """
        if self.target:
            for record in self.buffer:
                self.target.handle(record)

            self.buffer = []

    def close(self):
        """
        Flush, set the target to None and lose the buffer.
        """
        self.flush()
        self.target = None
        BufferingHandler.close(self)
        return