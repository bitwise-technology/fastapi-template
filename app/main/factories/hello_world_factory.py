from app.domain.usecases.usecase import UseCase
from app.services.usecases.hello_world import HelloWorld


def hello_world_factory() -> UseCase:
    return HelloWorld()
