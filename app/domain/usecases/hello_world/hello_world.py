from abc import abstractmethod

from app.domain.usecases.usecase import UseCase
from app.services.helpers.http import HttpResponse


class HelloWorld(UseCase):
    @abstractmethod
    def handle(self) -> HttpResponse:
        raise NotImplementedError()
