from typing import Any, Union

from app.domain.usecases import UseCase
from app.services.helpers.http import HttpResponse


def fast_api_adapter(
    factory: UseCase,
    body: Union[Any, None] = None,
    query: Union[Any, None] = None,
    path: Union[Any, None] = None,
) -> HttpResponse:
    """Adapter that passes the factory parameters passed
    to the use case and returns the status code and response body.

    Args:
        factory (UseCase): Factory UseCases
        body (Union[Any, None], optional): Request Body Params. Defaults to None.
        query (Union[Any, None], optional): Request Query Params. Defaults to None.
        path (Union[Any, None], optional): Request Path Params. Defaults to None.

    Returns:
        HttpResponse: Object with status_code and body
    """
    return factory.handle(body, query, path)
