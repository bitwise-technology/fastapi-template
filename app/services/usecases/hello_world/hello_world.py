from typing import Union
from app.domain.usecases.hello_world import HelloWorld as HelloWorldContract
from app.domain.usecases.hello_world import HelloParams
from app.services.helpers.http.http import HttpResponse, HttpStatus


class HelloWorld(HelloWorldContract):
    def handle(self, hello: Union[HelloParams, None]) -> HttpResponse:
        return HttpStatus.ok_200("Hello World")
