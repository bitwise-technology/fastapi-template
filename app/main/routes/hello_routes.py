from app.main.main import app


@app.get("/")
def hello_world():
    return {"Hello": "World"}
