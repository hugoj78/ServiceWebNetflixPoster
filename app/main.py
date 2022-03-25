from fastapi import FastAPI
from src.routes.posters import router as poster
from src.routes.health import router as health
from config.openapi import tags_metadata
import os

app = FastAPI(
    title="Web Services Poster",
    description="a REST API using python and mysql",
    version="0.0.1",
)

app.include_router(poster)
app.include_router(health)
