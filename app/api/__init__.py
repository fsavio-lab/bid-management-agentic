from fastapi.routing import APIRouter
from .v1 import router as v1_router

router = APIRouter(prefix="/api")