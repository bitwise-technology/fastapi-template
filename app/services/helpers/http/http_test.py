from http import HTTPStatus

from faker import Faker

from app.services.helpers.http.http import HttpStatus


sut = HttpStatus()
fake = Faker()


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
