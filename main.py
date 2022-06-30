from punq import Container

from implementation import ConsoleLogger, App, LogHelloService, LogByeService
from _types import Logger, HelloService, ByeService

container = Container()

container.register(App)
container.register(Logger, ConsoleLogger)
container.register(HelloService, LogHelloService)
container.register(ByeService, LogByeService)

container.resolve(App).run()
