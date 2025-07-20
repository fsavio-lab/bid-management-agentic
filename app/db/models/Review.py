from beanie import Document, before_event, Insert, Link, BackLink
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, TYPE_CHECKING
from datetime import datetime, timezone
from app.db.utils.events import create_identifier


class ReviewSet(Document):
    reviews: List[BackLink["Review"]] = Field(default_factory=list, original_field="review_set")
    bid: Link["Bid"]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "review-set"

    @before_event(Insert)
    async def generate_id(self):
        return await create_identifier(self)



class Review(Document):
    alert: Literal["Error", "Warning", "Good", "Critical"]
    title: str
    reason: str = Field(description="Reason for the alert")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    review_set: Link["ReviewSet"]
    class Settings:
        name = "review"

    @before_event(Insert)
    async def generate_id(self):
        return await create_identifier(self)

from app.db.models.Bid import Bid
ReviewSet.model_rebuild()