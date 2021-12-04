import uvicorn
from fastapi import FastAPI

from server.api import default, users
from server.db.db import engine
from server.models import Users
from server.settings.settings import API_ROUTE, API_HOST, API_PORT, API_NAME

Users.Base.metadata.create_all(bind=engine)

app = FastAPI(title=API_NAME, version="1.0")


if __name__ == '__main__':
    app.include_router(default.router, prefix=API_ROUTE)
    app.include_router(users.router, prefix=API_ROUTE + "/users", tags=["Users"])

    uvicorn.run(app, host=API_HOST, port=API_PORT)
