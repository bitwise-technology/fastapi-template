from abc import abstractmethod

from pydantic import BaseModel

from src.domain.usecases.usecase import UseCase
from src.services.helpers.http import HttpResponse


class HelloParams(BaseModel):
    hello: str


class HelloWorld(UseCase):
    @abstractmethod
    def handle(self, hello: HelloParams) -> HttpResponse:
        raise NotImplementedError()
