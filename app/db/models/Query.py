from beanie import Document, before_event, Insert, Link
from pydantic import BaseModel, Field
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime, timezone
from app.db.utils.events import create_identifier

if TYPE_CHECKING:
    from app.db.models.Tender import Tender


class Query(Document):
    tender: Link["Tender"]
    sender_company: str
    sender_department: Optional[str] = None
    question: str
    answer: Optional[str] = None
    answered_at: Optional[datetime] = None

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "query"

    @before_event(Insert)
    async def generate_id(self):
        return await create_identifier(self)


from app.db.models.Tender import Tender
Query.model_rebuild()
