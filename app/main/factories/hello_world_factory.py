from app.services.usecases.hello_world import HelloWorld
from app.domain.usecases.usecase import UseCase


def hello_world_factory() -> UseCase:
    return HelloWorld()
