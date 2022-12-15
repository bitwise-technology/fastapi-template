from http import HTTPStatus

from faker import Faker

from app.services.helpers.http.http import HttpStatus, HttpRequest, HttpResponse


sut = HttpStatus()
fake = Faker()


def test_should_make_http_request_instance():
    header = { fake.word(): fake.word() }
    body = fake.json()
    query = { fake.word(): fake.word() }

    http_request = HttpRequest(
        header=header,
        body=body,
        query=query
    )

    assert http_request.header == header
    assert http_request.body == body
    assert http_request.query == query
    assert repr(http_request) == f"HttpRequest (header={header}, body={body}, query={query})"


def test_should_make_http_response_instance():
    status_code = fake.random_int()
    body = fake.json()

    http_response = HttpResponse(
        status_code=status_code,
        body=body
    )

    assert http_response.status_code == status_code
    assert http_response.body == body
    assert repr(http_response) == f"HttpResponse (status_code={status_code}, body={body})"


def test_should_return_ok_200_status_code_and_body():
    body = fake.json()
    result = sut.ok_200(body)

    assert result.status_code == HTTPStatus.OK
    assert result.body == body


def test_should_return_created_201_status_code_and_body():
    body = fake.json()
    result = sut.created_201(body)

    assert result.status_code == HTTPStatus.CREATED
    assert result.body == body
