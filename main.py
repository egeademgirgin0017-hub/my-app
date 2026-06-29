import os
from fastapi import FastAPI
from pymongo import MongoClient

# FastAPI uygulaması
app = FastAPI()

# Environment variable'dan MongoDB Atlas URL'ini al
mongo_url = os.getenv("MONGODB_ATLAS_URL")

# MongoDB bağlantısı
client = MongoClient(mongo_url)
db = client["tarim_web"]   # senin database adın

# Basit test endpoint
@app.get("/")
def read_root():
    return {"message": "Backend çalışıyor!"}

# Items koleksiyonundan veri çekme
@app.get("/items")
def get_items():
    items = list(db["items"].find({}, {"_id": 0}))
    return {"data": items}

# Urunler koleksiyonundan veri çekme
@app.get("/urunler")
def get_urunler():
    urunler = list(db["urunler"].find({}, {"_id": 0}))
    return {"data": urunler}
