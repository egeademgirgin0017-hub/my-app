from fastapi import APIRouter, HTTPException
from bson import ObjectId
from database import db
from models import Urun

router = APIRouter()

@router.post("/urun")
async def urun_ekle(urun: Urun):
    result = await db.urunler.insert_one(urun.dict())
    return {"id": str(result.inserted_id), "message": "Ürün eklendi"}

@router.get("/urunler")
async def urunleri_listele():
    urunler = []
    async for urun in db.urunler.find():
        urun["_id"] = str(urun["_id"])
        urunler.append(urun)
    return urunler

@router.delete("/urun/{id}")
async def urun_sil(id: str):
    try:
        obj_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Geçersiz ID formatı")

    result = await db.urunler.delete_one({"_id": obj_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Ürün bulunamadı")
    return {"message": "Ürün silindi"}
