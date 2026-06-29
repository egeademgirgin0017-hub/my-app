import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Ortam değişkeninden bağlantı stringini al
MONGO_URL = os.getenv("MONGO_URL")

# MongoDB Atlas istemcisi
client = AsyncIOMotorClient(MONGO_URL)

# Kullanılacak veritabanı
db = client["tarim_web"]
