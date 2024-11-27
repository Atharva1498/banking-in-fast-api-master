from pydantic import BaseModel
from datetime import date
from typing import Optional
from core.RentalOwnerSelfOccupied.enum import PropertyStatus

class RentalOwnerSelfOccupiedCreate(BaseModel):
    property_status: PropertyStatus  # Rent, Owned, Self-Occupied
    rent_per_month: Optional[float] = None  # Rent per month (if rented)
    rented_person_name: Optional[str] = None  # Rented person's name (if rented)
    rented_person_email: Optional[str] = None  # Rented person's email (if rented)
    rented_person_mobile: Optional[str] = None  # Rented person's mobile number
    bank_ifsc_code: Optional[str] = None  # Bank IFSC code (if rented)
    bank_account_number: Optional[str] = None  # Bank account number (if rented)
    rent_agreement_details: Optional[str] = None  # Rent agreement details (if rented)
    rent_deposit: Optional[float] = None  # Rent deposit (if rented)
    owner_name: Optional[str] = None  # Name of the property owner (if owned/self-occupied)
    self_occupied_details: Optional[str] = None  # Self-occupied property details (if self-occupied)

class RentalOwnerSelfOccupiedResponse(RentalOwnerSelfOccupiedCreate):
    id: int  # ID of the property details

    class Config:
        orm_mode = True
