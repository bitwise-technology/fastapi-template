from abc import ABC, abstractmethod
from typing import Any, Union

from src.services.helpers.http import HttpResponse


class UseCase(ABC):
    @abstractmethod
    def handle(self, *args: Union[Any, None]) -> HttpResponse:
        raise NotImplementedError("This contract method must be implemented")
