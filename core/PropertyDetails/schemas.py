from pydantic import BaseModel
from datetime import date
from typing import Optional
from core.PropertyDetails.enum import PropertyLandType, PropertyMortgageStatus  # Import enums

class PropertyDetailsCreate(BaseModel):
    property_owner_name: str
    area: float
    land_type: PropertyLandType
    registration_number: str
    purchase_cost: float
    broker_name: str
    broker_mobile: str
    broker_email: str
    mortgage_status: PropertyMortgageStatus
    bank_name: Optional[str] = None
    loan_amount: Optional[float] = None
    bank_valuation: Optional[float] = None
    property_tax_last_payment: Optional[date] = None
    property_nominee: str

class PropertyDetailsResponse(PropertyDetailsCreate):
    id: int

    class Config:
        orm_mode = True
