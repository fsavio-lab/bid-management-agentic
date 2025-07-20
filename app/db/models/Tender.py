from beanie import Document, before_event, Insert, Link, BackLink, PydanticObjectId
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, timezone
from app.db.utils.events import create_identifier
from enum import Enum
from app.db.models.File import File


class TenderType(str, Enum):
    GOODS = "Goods"
    SERVICES = "Services"
    WORKS = "Works"
    CONSULTANCY = "Consultancy"
    OTHERS = "Others"


class TenderStatus(str, Enum):
    OPEN = "Open"
    CLOSED = "Closed"
    CANCELLED = "Cancelled"
    AWARDED = "Awarded"
    DRAFT = "Draft"


class Tender(Document):
    # General Information
    title: str
    description: Optional[str] = None
    tender_type: TenderType = TenderType.GOODS
    category: Optional[str] = None
    organization_name: str
    department: Optional[str] = None

    # Financials
    estimated_value_inr: Optional[float] = None
    emd_amount_inr: Optional[float] = None  # Earnest Money Deposit
    tender_fee_inr: Optional[float] = None

    # Dates
    publication_date: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    submission_deadline: datetime
    opening_date: Optional[datetime] = None

    # Tender Status
    status: TenderStatus = TenderStatus.DRAFT

    # Metadata
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    # Attachments
    attachments: Optional[List[Link["File"]]] = []

    # Queries
    queries: List[BackLink["Query"]] = Field(
        default_factory=list, original_field="tender"
    )
    # Queries
    review_sets: List[BackLink["ReviewSet"]] = Field(
        default_factory=list, original_field="tender"
    )

    class Settings:
        name = "tender"

    @before_event(Insert)
    async def generate_id(self):
        return await create_identifier(self)


class TenderUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    tender_type: Optional[TenderType] = None
    category: Optional[str] = None
    organization_name: Optional[str] = None
    department: Optional[str] = None

    estimated_value_inr: Optional[float] = None
    emd_amount_inr: Optional[float] = None
    tender_fee_inr: Optional[float] = None

    publication_date: Optional[datetime] = None
    submission_deadline: Optional[datetime] = None
    opening_date: Optional[datetime] = None

    status: Optional[TenderStatus] = None

    attachments: Optional[List[PydanticObjectId]] = None


from app.db.models.Review import ReviewSet
from app.db.models.Query import Query

Tender.model_rebuild()
