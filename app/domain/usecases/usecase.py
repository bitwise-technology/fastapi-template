from abc import ABC, abstractmethod
from typing import Any

from app.services.helpers.http import HttpResponse


class UseCase(ABC):
    @abstractmethod
    def handle(self, *args: Any) -> HttpResponse:
        raise NotImplementedError("This contract method must be implemented")
