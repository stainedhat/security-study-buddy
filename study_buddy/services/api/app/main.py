from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from data.db import database
from routers import question_router_v1


def create_app():
    _app = FastAPI()

    # Setup the /questions endpoints
    _app.include_router(question_router_v1.router)
    _app.include_router(question_router_v1.router, prefix="/v1")
    _app.include_router(question_router_v1.router, prefix="/latest")

    return _app


app = create_app()

allowed_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost",
    "http://127.0.0.1"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
