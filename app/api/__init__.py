from fastapi.routing import APIRouter
from fastapi import Response
from .v1 import router as v1_router

async def health_check() -> Response:
    Response("Status: OK", status_code=200)

router = APIRouter(prefix="/api")
router.include_router(v1_router)
router.add_api_route(
    "/health-check",
    health_check,
    tags=["Health Check"],
)

