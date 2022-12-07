from fastapi import APIRouter

HelloWorld = APIRouter(prefix="/hello", tags=["Hello World"])


@HelloWorld.get("/")
def hello_world():
    return {"Hello": "World"}
