from enum import Enum


class UserInputService:

    def read(self) -> str:
        """blocking call"""
        ...


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


class ChoiceEnum(Enum):
    HELLO = "HELLO",
    BYE = "BYE"


class Logger:

    def log(self, message: str, severity: SeverityEnum):
        ...
