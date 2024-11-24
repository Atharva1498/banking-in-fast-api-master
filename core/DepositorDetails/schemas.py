from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from core.DepositorDetails.enum import DepositType  # Import DepositType enum

class DepositorCreate(BaseModel):
    depositor_name: str
    person_id: int
    contact_number: str
    email: EmailStr
    address: str
    amount_invested: float
    roi: float  # Rate of Interest in percentage
    deposit_type: DepositType  # Enum for Deposit Type
    invested_date: date
    maturity_date: date

class DepositorResponse(BaseModel):
    id: int
    depositor_name: str
    person_id: int
    contact_number: str
    email: EmailStr
    address: str
    amount_invested: float
    roi: float
    deposit_type: DepositType
    invested_date: date
    maturity_date: date
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
