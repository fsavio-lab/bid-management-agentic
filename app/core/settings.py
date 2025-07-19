from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")
    MONGO_URI = os.getenv("MONGO_URI","")
    MONGO_DB = os.getenv("MONGO_DB","app")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL","")


SETTINGS = Settings()
