from _types import HelloService, SeverityEnum, ByeService, Logger, UserInputService, ChoiceEnum


class RequestState:

    def __init__(self, logger: Logger):
        self.__count: int = 0
        self.__logger = logger

        self.__logger.log(message="request state service constructed", severity=SeverityEnum.DEBUG)

    def increment(self):
        self.__count = self.__count + 1

    def get_count(self) -> int:
        return self.__count


class App:

    def __init__(self, hello_service: HelloService,
                 goodbye_service: ByeService,
                 user_input_service: UserInputService,
                 logger: Logger,
                 request_state: RequestState):
        self.__request_state = request_state
        self.__logger = logger
        self.__user_input_service = user_input_service
        self.__goodbye_service = goodbye_service
        self.__hello_service = hello_service

        self.__logger.log(message="app constructed", severity=SeverityEnum.DEBUG)

    def run(self):
        self.__request_state.increment()
        self.__logger.log(message=f"request state: {self.__request_state.get_count()}", severity=SeverityEnum.INFO)
        choice = self.__user_input_service.read()
        if choice == ChoiceEnum.BYE.name:
            self.__goodbye_service.bye()
        elif choice == ChoiceEnum.HELLO.name:
            self.__hello_service.hello()
        else:
            self.__logger.log(message=f"{choice} is not valid", severity=SeverityEnum.ERROR)


class LogHelloService:

    def __init__(self, logger: Logger):
        self.__logger = logger

        self.__logger.log(message="hello service constructed", severity=SeverityEnum.DEBUG)

    def hello(self):
        self.__logger.log("hello guys", severity=SeverityEnum.INFO)


class LogByeService:

    def __init__(self, logger: Logger):
        self.__logger = logger

        self.__logger.log(message="bye service constructed", severity=SeverityEnum.DEBUG)

    def bye(self):
        self.__logger.log("bye guys", severity=SeverityEnum.INFO)


class ConsoleUserInputService:

    def __init__(self, logger: Logger):
        self.__logger = logger

        self.__logger.log(message="console user input service constructed", severity=SeverityEnum.DEBUG)

    def read(self) -> str:
        return input()


class ConsoleLogger:

    def __init__(self):
        print(f"severity: <DEBUG> message: <console logger constructed>")

    def log(self, message: str, severity: SeverityEnum):
        print(f"severity: <{severity.name}> message: <{message}>")
