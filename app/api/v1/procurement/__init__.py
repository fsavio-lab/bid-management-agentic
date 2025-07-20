from fastapi import APIRouter
from .tender import router as tender_router
from .query import router as query_router
from .bid import router as bid_router

router = APIRouter(prefix="/procurement")
router.include_router(tender_router)
router.include_router(query_router)
router.include_router(bid_router)
