from pydantic import BaseModel, Field, EmailStr
from datetime import date
from typing import List, Optional
from core.Person.enum import Gender, AddressType


# Address Schemas
class AddressCreate(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    address_type: AddressType


class AddressResponse(AddressCreate):
    id: int

    class Config:
        orm_mode = True


# Family Details Schemas
class FamilyDetailsCreate(BaseModel):
    first_name: str
    last_name: str
    relationship: str
    birthdate: date
    gender: Gender


class FamilyDetailsResponse(FamilyDetailsCreate):
    id: int

    class Config:
        orm_mode = True


# Person Schemas
class PersonCreate(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    dob: date
    phone_number: str
    email: Optional[EmailStr] = None
    aadhar_card_number: Optional[str] = Field(max_length=12, pattern=r"^\d{12}$")
    pan_card_number: Optional[str] = Field(max_length=10, pattern=r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$") 

    # Nested data
    addresses: List[AddressCreate]
    family_members: List[FamilyDetailsCreate]


class PersonResponse(PersonCreate):
    id: int
    addresses: List[AddressResponse]
    family_members: List[FamilyDetailsResponse]

    class Config:
        orm_mode = True
