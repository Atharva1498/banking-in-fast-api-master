from pydantic import BaseModel
from datetime import date
from typing import Optional
from core.GoldDetails.enum import JewelryType, GoldType  # Import enums

class GoldDetailsCreate(BaseModel):
    jewelry_type: JewelryType  # Jewelry type (ring, necklace, etc.)
    gold_type: GoldType  # Type of gold (24K, 22K, etc.)
    purchase_date: date  # Purchase date
    weight: float  # Weight of the gold
    purchase_price: float  # Purchase price
    purchase_shop: str  # Name of the shop where the gold was purchased

class GoldDetailsResponse(GoldDetailsCreate):
    id: int  # The ID of the gold details record

    class Config:
        orm_mode = True  # To allow ORM (Tortoise) to serialize the model

