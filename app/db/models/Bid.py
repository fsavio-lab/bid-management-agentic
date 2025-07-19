from beanie import Document, before_event, Insert, Link
from pydantic import BaseModel, Field
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime, timezone
from app.db.utils.events import create_identifier


if TYPE_CHECKING:
    from app.db.models import Tender, File

class Bid(Document):
    tender: Link["Tender"]
    bidder_company: str
    bidder_contact: str | None = None
    bid_value_inr: float
    message: str | None = None
    attachments: List[Link["File"]] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "bid"
    
    @before_event(Insert)
    async def generate_id(self):
        return await create_identifier(self)
