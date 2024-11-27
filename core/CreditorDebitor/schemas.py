from pydantic import BaseModel
from datetime import date
from typing import Optional
from core.CreditorDebitor.enum import CreditorType, DebitorType, PaymentStatus


class CreditorCreate(BaseModel):
    name: str
    amount: float
    received_date: date
    rate_of_interest: float
    return_on_investment: float
    retail_promise: str
    remark: Optional[str]
    creditor_type: CreditorType  # Creditor type enum
    payment_status: PaymentStatus  # Payment status enum


class CreditorResponse(CreditorCreate):
    id: int

    class Config:
        orm_mode = True


class DebitorCreate(BaseModel):
    name: str
    amount: float
    received_date: date
    rate_of_interest: float
    return_on_investment: float
    retail_promise: str
    remark: Optional[str]
    debitor_type: DebitorType  # Debitor type enum
    payment_status: PaymentStatus  # Payment status enum


class DebitorResponse(DebitorCreate):
    id: int

    class Config:
        orm_mode = True
