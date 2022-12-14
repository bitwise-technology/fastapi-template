from http import HTTPStatus

from src.services.usecases.hello_world import HelloWorld

sut = HelloWorld()


def test_should_return_200_when_hello_world():
    result = sut.handle(None)

    assert result.status_code == HTTPStatus.OK
    assert result.body == "Hello World"
