from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.posters import router as poster
from src.routes.health import router as health
from config.openapi import tags_metadata
import os

app = FastAPI(
    title="WebServiceNetflix - Poster",
    description="a REST API using python and mysql",
    version="0.0.1",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(poster)
app.include_router(health)
