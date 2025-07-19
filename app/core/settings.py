from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")
    MONGO_URI = os.getenv("MONGO_URI","mongodb://127.0.0.1:27017")
    MONGO_DB = os.getenv("MONGO_DB","app")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL","")
    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS","*").split(",")


SETTINGS = Settings()
