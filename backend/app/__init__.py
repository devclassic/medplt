from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise
from app.handlers import router

app = FastAPI()

register_tortoise(
    app=app,
    config={
        "connections": {"default": "sqlite://data.db"},
        "apps": {
            "models": {
                "models": ["app.mods"],
                "default_connection": "default",
            },
        },
    },
    generate_schemas=True,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.add_middleware(
    SessionMiddleware,
    secret_key="woaiwhr001",
)

app.include_router(router)

app.mount("/", StaticFiles(directory="public", html=True))
