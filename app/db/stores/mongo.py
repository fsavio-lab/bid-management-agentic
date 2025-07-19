from beanie import init_beanie, Document
from app.db.models import DOCUMENT_MODELS
from motor.motor_asyncio import AsyncIOMotorClient
from app import LOGGER, SETTINGS


class MongoDatabase:
    def __init__(self):
        self.client: AsyncIOMotorClient | None = None

    async def connect(self):
        self.client = AsyncIOMotorClient(SETTINGS.MONGO_URI)
        await init_beanie(
            database=self.client[SETTINGS.MONGO_DB],
            document_models=DOCUMENT_MODELS,
        )
        for model in DOCUMENT_MODELS:
            if (
                model.get_settings().name
                not in await self.client[SETTINGS.MONGO_DB].list_collection_names()
            ):
                await self.client[SETTINGS.MONGO_DB].create_collection(
                    model.get_settings().name
                )
        LOGGER.info("MongoDB connection initialized")

    async def disconnect(self):
        if self.client:
            self.client.close()
            LOGGER.info("MongoDB connection closed")


MONGO_STORE = MongoDatabase()
