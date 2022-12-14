from abc import abstractmethod

from app.domain.usecases.usecase import Usecase
from app.services.helpers.http import HttpResponse


class HelloWorld(Usecase):
    @abstractmethod
    def execute(self) -> HttpResponse:
        raise NotImplementedError()
