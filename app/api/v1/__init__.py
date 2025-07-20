from fastapi import APIRouter
from .procurement import router as procurement_router

router = APIRouter(prefix="/v1")
router.include_router(procurement_router)
