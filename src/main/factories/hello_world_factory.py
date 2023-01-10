from src.domain.usecases.usecase import UseCase
from src.services.usecases.hello_world import HelloWorld


def hello_world_factory() -> UseCase:
    return HelloWorld()
