import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

# FastAPI uygulaması
app = FastAPI()

# CORS middleware ekle
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Environment variable'dan MongoDB Atlas URL'ini al
mongo_url = os.getenv("MONGODB_ATLAS_URL")

if not mongo_url:
    raise ValueError("MONGODB_ATLAS_URL environment variable not set!")

# MongoDB bağlantısı
try:
    client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
    # Bağlantıyı test et
    client.admin.command('ping')
    db = client["tarim_web"]
    print("✓ MongoDB bağlantısı başarılı!")
except ServerSelectionTimeoutError:
    print("✗ MongoDB bağlantısı başarısız!")
    db = None
except Exception as e:
    print(f"✗ Hata: {e}")
    db = None

# Basit test endpoint
@app.get("/")
def read_root():
    return {"message": "Backend çalışıyor!", "status": "ok"}

# Items koleksiyonundan veri çekme
@app.get("/items")
def get_items():
    try:
        if not db:
            return {"error": "Database connection failed", "data": []}
        items = list(db["items"].find({}, {"_id": 0}))
        return {"data": items, "count": len(items)}
    except Exception as e:
        return {"error": str(e), "data": []}

# Urunler koleksiyonundan veri çekme
@app.get("/urunler")
def get_urunler():
    try:
        if not db:
            return {"error": "Database connection failed", "data": []}
        urunler = list(db["urunler"].find({}, {"_id": 0}))
        return {"data": urunler, "count": len(urunler)}
    except Exception as e:
        return {"error": str(e), "data": []}

# Health check
@app.get("/health")
def health():
    return {"status": "healthy"}

