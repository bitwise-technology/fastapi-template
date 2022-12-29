from fastapi import FastAPI

from app.main.config.environment import get_environment_variables
from app.main.routes import HelloWorld

env = get_environment_variables()

app = FastAPI(title=env.SERVICE_NAME, version=env.APP_VERSION)

app.include_router(HelloWorld)
