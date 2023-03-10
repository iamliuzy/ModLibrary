import datetime
from os import linesep

import constants

logfile = open("latest.log", mode="w", encoding="utf-8")
debug_logfile = open("latest_debug.log", mode="w", encoding="utf-8")


class LogLevel:
    debug = "DEBUG"
    info = "INFO"
    warn = "WARN"
    error = "ERROR"
    critical = "CRITICAL"


def log(s: str, level=LogLevel.info):
    time = datetime.datetime.today().strftime("%c")
    result = ""
    result = result + "[" + time + "]" + "(" + level + ")"
    result = result + " " + s
    if (not level == LogLevel.debug) or constants.DEBUG:
        print(result)
    logfile.write(result + linesep)
    debug_logfile.write(result + linesep)


def debug(s: str):
    log(s, LogLevel.debug)


def info(s: str):
    log(s, LogLevel.info)


def warn(s: str):
    log(s, LogLevel.warn)


def error(s: str):
    log(s, LogLevel.error)


def critical(s: str):
    log(s, LogLevel.critical)
