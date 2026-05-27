from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.v1.api import api_router
from app.core.config import get_settings
from app.core.exceptions import (
    BusinessError,
    ForbiddenError,
    NotFoundError,
    UnauthorizedError,
)

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description="Todo List API với Services, Workers (Celery) và business logic",
    version="2.0.0",
)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)


@app.exception_handler(BusinessError)
async def business_error_handler(request: Request, exc: BusinessError):
    return JSONResponse(status_code=400, content={"detail": exc.message})


@app.exception_handler(NotFoundError)
async def not_found_error_handler(request: Request, exc: NotFoundError):
    return JSONResponse(status_code=404, content={"detail": exc.message})


@app.exception_handler(UnauthorizedError)
async def unauthorized_error_handler(request: Request, exc: UnauthorizedError):
    return JSONResponse(
        status_code=401,
        content={"detail": exc.message},
        headers={"WWW-Authenticate": "Bearer"},
    )


@app.exception_handler(ForbiddenError)
async def forbidden_error_handler(request: Request, exc: ForbiddenError):
    return JSONResponse(status_code=403, content={"detail": exc.message})


@app.get("/")
async def root():
    return {
        "message": settings.APP_NAME,
        "docs": "/docs",
        "api_v1": settings.API_V1_PREFIX,
        "workers": "celery -A app.core.celery_app worker --loglevel=info",
    }
