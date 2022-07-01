from datetime import datetime

from punq import Container, Scope

from implementation import ConsoleLogger, App, LogHelloService, LogByeService, ConsoleUserInputService, RequestState
from _types import Logger, HelloService, ByeService, UserInputService

container = Container()

container.register(App)
container.register(RequestState, scope=Scope.singleton)
container.register(Logger, ConsoleLogger)
container.register(UserInputService, ConsoleUserInputService)
container.register(HelloService, LogHelloService)
container.register(ByeService, LogByeService)
while True:
    container.resolve(App).run()
