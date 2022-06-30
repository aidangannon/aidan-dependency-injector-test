from enum import Enum


class HelloService:

    def hello(self):
        ...


class ByeService:

    def bye(self):
        ...


class SeverityEnum(Enum):
    DEBUG = "DEBUG",
    INFO = "INFO",
    ERROR = "ERROR"


class Logger:

    def log(self, message: str, severity: SeverityEnum):
        ...
