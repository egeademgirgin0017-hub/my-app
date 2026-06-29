from pydantic import BaseModel

# Ürün modeli
class Urun(BaseModel):
    isim: str
    fiyat: int


