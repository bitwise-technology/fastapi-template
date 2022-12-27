from typing import Any, Union

from app.domain.usecases import UseCase
from app.services.helpers.http import HttpResponse


def fast_api_adapter(request: Union[Any, None], usecase: UseCase) -> HttpResponse:
    """Adapts a FastAPI request to a usecase

    Args:
        request (Any or None): Request to be adapted
        usecase (Usecase): Usecase to be adapted

    Returns:
        HttpResponse: Response from the usecase
    """
    return usecase.handle(request)
