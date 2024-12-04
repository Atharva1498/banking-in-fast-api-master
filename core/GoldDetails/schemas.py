from pydantic import BaseModel
from datetime import date
from typing import Optional
from core.GoldDetails.enum import JewelryType, GoldType  # Import enums

class GoldDetailsCreate(BaseModel):
    jewelry_type: JewelryType
    gold_type: GoldType
    weight: float
    purchase_date: date
    purchase_price: float
    purchase_shop: str
    person_id: int  # Link to the person

class GoldDetailsResponse(GoldDetailsCreate):
    id: int  # The ID of the gold details record

    class Config:
        orm_mode = True  # To allow ORM (Tortoise) to serialize the model
