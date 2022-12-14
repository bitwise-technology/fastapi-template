from app.domain.usecases.hello_world import HelloWorld as HelloWorldContract
from app.services.helpers.http.http import HttpResponse, HttpStatus


class HelloWorld(HelloWorldContract):
    def execute(self) -> HttpResponse:
        return HttpStatus.ok_200("Hello World")
