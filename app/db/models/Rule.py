from __future__ import annotations
from beanie import Document, before_event, Insert, Link
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, TYPE_CHECKING
from datetime import datetime, timezone
from app.db.utils.events import create_identifier
if TYPE_CHECKING:
    from app.db.models import File, Tender

SUPPORTED_FILE_TYPES = ["pdf", "docx", "xlsx", "csv"]

class Rule(Document):
    content: str
    source: Link["File"]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "rule"

    @before_event(Insert)
    async def generate_id(self):
        return await create_identifier(self)

class RuleSet(Document):
    tender: Link["Tender"]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "rule_set"

    @before_event(Insert)
    async def generate_id(self):
        return await create_identifier(self)