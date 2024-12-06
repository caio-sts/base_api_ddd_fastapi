from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.di import DependencyContainer
from src.infra.databases.sqlalchemy.connection import init_database
from src.infra.http.routers import example


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_database()
    yield

def create_app() -> FastAPI:
    container = DependencyContainer()

    app = FastAPI(lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.container = container
    app.include_router(example.router)
    return app


app = create_app()
