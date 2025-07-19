from fastapi.routing import APIRouter
from fastapi import Response

router = APIRouter(prefix="/health-check", tags=["Health Check"])

@router.get("/")
async def health_check():
    return Response("Status: OK", status_code=200)
