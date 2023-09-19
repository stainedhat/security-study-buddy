from typing import Union

from fastapi import FastAPI
from routers import question_router_v1
from data.db import database


def create_app():
    _app = FastAPI()

    # Setup the /questions endpoints
    _app.include_router(question_router_v1.router)
    _app.include_router(question_router_v1.router, prefix="/v1")
    _app.include_router(question_router_v1.router, prefix="/latest")

    return _app


app = create_app()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
