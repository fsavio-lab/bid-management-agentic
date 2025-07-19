from fastapi import APIRouter
from .health_check import router as health_router

router = APIRouter("/v1")
router.include_router(health_check)
