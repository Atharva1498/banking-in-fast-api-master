from pydantic import BaseModel, Field
from datetime import date

class PassportCreate(BaseModel):
    passport_number: str = Field(max_length=20)
    date_of_issue: date
    date_of_expiry: date
    place_of_issue: str = Field(max_length=255)

class PassportResponse(PassportCreate):
    id: int
    user: int

    class Config:
        from_attributes = True
