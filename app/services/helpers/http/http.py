from http import HTTPStatus
from typing import Any


class HttpResponse:
    def __init__(self, status_code: int, body: Any=None):
        self.status_code = status_code
        self.body = body

    def __repr__(self):
        return f"HttpResponse (status_code={self.status_code}, body={self.body})"


class HttpStatus:
    """Status code and body for HTTP responses, following the https://http.cat

    Returns:
        HttpResponse: status_code and body
    """
    @staticmethod
    def ok_200(body: Any) -> HttpResponse:
        return HttpResponse(HTTPStatus.OK, body)

    @staticmethod
    def created_201(body: Any) -> HttpResponse:
        return HttpResponse(HTTPStatus.CREATED, body)
