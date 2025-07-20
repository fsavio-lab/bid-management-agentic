from fastapi import APIRouter, Depends, Query, HTTPException, Body
from typing import List, Optional, Any, Dict
from beanie import PydanticObjectId
from app.db.models.Tender import Tender, TenderUpdate
from app.db.utils.filters import parse_operator_filter, parse_text_filter
from app.db.utils.pagination import (
    paginate_queryset,
    pagination_params,
    PaginationParams,
)

router = APIRouter(prefix="/tenders", tags=["Tenders"])


@router.get("/", response_model=Dict[str, Any])
async def list_tenders(
    title: Optional[str] = Query(None, description="Text filter for title"),
    estimated_value: Optional[str] = Query(
        None, description='Operator filter (e.g. ["<", 10000])'
    ),
    pagination: PaginationParams = Depends(pagination_params),
):
    filters: Dict[str, Any] = {}

    # Apply text filters
    filters.update(parse_text_filter("title", title))

    # Apply numeric filters
    filters.update(parse_operator_filter("estimated_value_inr", estimated_value))

    # Query with filters
    total = await Tender.find(filters).count()
    skip = (pagination.page - 1) * pagination.size
    results = await Tender.find(filters).skip(skip).limit(pagination.size).to_list()

    return await paginate_queryset(results, total, pagination)


@router.get("/{tender_id}", response_model=Tender)
async def get_tender(tender_id: PydanticObjectId):
    tender = await Tender.get(tender_id)
    if not tender:
        raise HTTPException(status_code=404, detail="Tender not found")
    return tender


@router.post("/", response_model=Tender)
async def create_tender(tender: Tender):
    await tender.insert()
    return tender


@router.put("/{tender_id}", response_model=Tender)
async def update_tender(tender_id: PydanticObjectId, data: Tender):
    existing = await Tender.get(tender_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Tender not found")

    update_data = data.model_dump(exclude_unset=True)
    await existing.set(update_data)
    return await Tender.get(tender_id)


@router.delete("/{tender_id}")
async def delete_tender(tender_id: PydanticObjectId):
    tender = await Tender.get(tender_id)
    if not tender:
        raise HTTPException(status_code=404, detail="Tender not found")
    await tender.delete()
    return {"message": "Tender deleted successfully"}


@router.patch("/{tender_id}", response_model=Tender)
async def patch_tender(
    tender_id: PydanticObjectId,
    data: TenderUpdate = Body(
        ..., example={"title": "Updated Title", "status": "Open"}
    ),
):
    tender = await Tender.get(tender_id)
    if not tender:
        raise HTTPException(status_code=404, detail="Tender not found")

    try:
        await tender.set(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return await Tender.get(tender_id)
