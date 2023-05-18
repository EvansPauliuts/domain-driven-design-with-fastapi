from fastapi import FastAPI

from src.core.config import env_settings
from src.metadata.tags import tags
from src.models.base import init
from src.routers.v1.books import router as book_router

settings = env_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    openapi_tags=tags,
)

app.include_router(book_router)


@app.get('/')
async def root():
    return {'message': 'Run FastAPI!!!'}


init()
