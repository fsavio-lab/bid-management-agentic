from pydantic import BaseModel
from typing import Generic, TypeVar, List
from pydantic.generics import GenericModel
from fastapi import Query
from typing import Sequence
from math import ceil

T = TypeVar("T")


class PaginationParams(BaseModel):
    page: int = 1
    size: int = 10


class PageResponse(GenericModel, Generic[T]):
    data: List[T]
    page: int
    size: int
    total: int
    total_pages: int
    has_next: bool
    has_prev: bool



def pagination_params(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(10, ge=1, le=100, description="Items per page")
) -> PaginationParams:
    return PaginationParams(page=page, size=size)


async def paginate_queryset(
    items: Sequence,
    total: int,
    pagination: PaginationParams,
):
    page = pagination.page
    size = pagination.size
    total_pages = ceil(total / size) if total > 0 else 1

    return {
        "data": items,
        "page": page,
        "size": size,
        "total": total,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "has_prev": page > 1,
    }