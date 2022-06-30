from enum import Enum

from types import HelloService, SeverityEnum, ByeService, Logger


class App:

    def __init__(self, hello_service: HelloService,
                 goodbye_service: ByeService):
        self.__goodbye_service = goodbye_service
        self.__hello_service = hello_service

    def run(self):
        self.__hello_service.hello()
        self.__goodbye_service.bye()


class LogHelloService:

    def __init__(self, logger: Logger):
        self.__logger = logger

    def hello(self):
        self.__logger.log("hello guys", severity=SeverityEnum.INFO)


class LogByeService:

    def __init__(self, logger: Logger):
        self.__logger = logger

    def bye(self):
        self.__logger.log("bye guys", severity=SeverityEnum.INFO)


class ConsoleLogger:

    def log(self, message: str, severity: SeverityEnum):
        print(f"severity: <{severity.name}> message: <{message}>")
