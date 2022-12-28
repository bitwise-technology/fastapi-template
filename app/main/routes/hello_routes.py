from typing import Union

from fastapi import APIRouter, Response

from app.domain.usecases.hello_world import HelloParams
from app.main.adapters import fast_api_adapter
from app.main.factories import hello_world_factory

HelloWorld = APIRouter(prefix="/hello", tags=["Hello World"])


@HelloWorld.get("/")
def hello_world(body: HelloParams, response: Response):
    result = fast_api_adapter(body, hello_world_factory())
    response.status_code = result.status_code
    return result.body
