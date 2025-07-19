from beanie import Document, before_event, Insert, Link
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime, timezone
from app.db.utils.events import create_identifier


class Review(Document):
    alert: Literal["Error", "Warning", "Good", "Critical"]
    title: str
    reason: str = Field(description="Reason for the alert")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "review"

    @before_event(Insert)
    async def generate_id(self):
        return await create_identifier(self)


class ReviewSet(Document):
    reviews: List[Link[Review]]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "review-set"

    @before_event(Insert)
    async def generate_id(self):
        return await create_identifier(self)
