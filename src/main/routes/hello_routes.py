from fastapi import APIRouter, Response

from src.domain.usecases.hello_world import HelloParams
from src.main.adapters import fast_api_adapter
from src.main.factories import hello_world_factory

HelloWorld = APIRouter(prefix="/hello", tags=["Hello World"])


@HelloWorld.get("/")
def hello_world(body: HelloParams, response: Response):
    result = fast_api_adapter(body, hello_world_factory())
    response.status_code = result.status_code
    return result.body
