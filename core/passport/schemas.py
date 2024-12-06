from pydantic import BaseModel, Field
from datetime import date


class PassportCreate(BaseModel):
    passport_number: str = Field(max_length=20)
    date_of_issue: date
    date_of_expiry: date

    # Place of issue fields
    country: str = Field(max_length=100)
    state: str = Field(max_length=100)
    city: str = Field(max_length=100)
    zip_code: str = Field(max_length=20)
    person_id: int


class PassportResponse(PassportCreate):
    id: int

    class Config:
        orm_mode = True
