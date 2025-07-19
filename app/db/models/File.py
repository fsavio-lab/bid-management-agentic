from beanie import Document, before_event, Insert
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime, timezone
from app.db.utils.events import create_identifier

SUPPORTED_FILE_TYPES = ["pdf", "docx", "xlsx", "csv"]

class File(Document):
    name: str
    url: str
    type: Literal["pdf", "docx", "xlsx", "csv"]
    size_kb: Optional[float] = None
    uploaded_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "file"

    @before_event(Insert)
    async def generate_id(self):
        return await create_identifier(self)
