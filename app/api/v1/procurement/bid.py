from fastapi import APIRouter, HTTPException, Depends, Query as FastQuery, Body
from typing import List, Optional, Dict, Any
from beanie import PydanticObjectId
from app.db.models.Bid import Bid
from app.db.utils.pagination import (
    paginate_queryset,
    pagination_params,
    PaginationParams,
)
from app.db.utils.filters import parse_text_filter

router = APIRouter(prefix="/bid", tags=["Bid"])


@router.get("/", response_model=Dict[str, Any])
async def list_queries(
    sender_company: Optional[str] = FastQuery(
        None, description='Text filter like ["contains", "abc"]'
    ),
    pagination: PaginationParams = Depends(pagination_params),
):
    filters = {}
    filters.update(parse_text_filter("sender_company", sender_company))

    total = await Bid.find(filters).count()
    skip = (pagination.page - 1) * pagination.size
    items = await Bid.find(filters).skip(skip).limit(pagination.size).to_list()

    return await paginate_queryset(items, total, pagination)


@router.get("/{query_id}", response_model=Bid)
async def get_query(query_id: PydanticObjectId):
    query = await Bid.get(query_id)
    if not query:
        raise HTTPException(status_code=404, detail="Query not found")
    return query


@router.post("/", response_model=Bid)
async def create_query(query: Bid):
    await query.insert()
    return query


@router.put("/{query_id}", response_model=Bid)
async def update_query(query_id: PydanticObjectId, data: Bid):
    existing = await Bid.get(query_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Query not found")

    update_data = data.model_dump(exclude_unset=True)
    await existing.set(update_data)
    return await Bid.get(query_id)


@router.patch("/{query_id}", response_model=Bid)
async def patch_query(query_id: PydanticObjectId, data: Dict[str, Any] = Body(...)):
    query = await Bid.get(query_id)
    if not query:
        raise HTTPException(status_code=404, detail="Query not found")

    try:
        await query.set(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return await Bid.get(query_id)


@router.delete("/{query_id}")
async def delete_query(query_id: PydanticObjectId):
    query = await Bid.get(query_id)
    if not query:
        raise HTTPException(status_code=404, detail="Query not found")
    await query.delete()
    return {"message": "Query deleted successfully"}
