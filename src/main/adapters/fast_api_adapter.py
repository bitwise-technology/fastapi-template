from typing import Any

from src.domain.usecases import UseCase
from src.services.helpers.http import HttpResponse


def fast_api_adapter(
    factory: UseCase,
    body: Any | None = None,
    query: Any | None = None,
    path: Any | None = None,
) -> HttpResponse:
    """Adapter that passes the factory parameters passed
    to the use case and returns the status code and response body.

    Args:
        factory (UseCase): Factory UseCases
        body (Any | None, optional): Request Body Params. Defaults to None.
        query (Any | None, optional): Request Query Params. Defaults to None.
        path (Any | None, optional): Request Path Params. Defaults to None.

    Returns:
        HttpResponse: Object with status_code and body
    """
    return factory.handle(body, query, path)
