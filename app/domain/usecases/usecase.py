from abc import ABC, abstractmethod
from typing import Any

from app.services.helpers.http import HttpResponse


class Usecase(ABC):
    @abstractmethod
    def execute(self, *args: Any|None) -> HttpResponse:
        raise NotImplementedError("This contract method must be implemented")
