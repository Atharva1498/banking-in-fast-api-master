from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from enum import Enum


# BankDetails Schemas
class BankDetailsCreate(BaseModel):
    bank_name: str
    branch_address: Optional[str]
    account_number: str
    account_type: str
    branch_ifsc_code: Optional[str]
    bank_micr_code: Optional[str]
    cheque_book_issued_date: Optional[date]
    netbanking_id: Optional[str]
    registered_email: Optional[str]
    registered_mobile: Optional[str]
    bank_helpline_number: Optional[str]
    bank_helpline_email: Optional[str]
    relationship_manager_name: Optional[str]
    relationship_manager_email: Optional[str]
    relationship_manager_mobile: Optional[str]


# BankDetailsResponse extends BankDetailsCreate to include id and person_id
class BankDetailsResponse(BankDetailsCreate):
    id: int
    person_id: int  # Include person_id in the response

    class Config:
        orm_mode = True


# CreditCard Schemas
class CreditCardCreate(BaseModel):
    card_number: str
    expiry_date: date
    cardholder_name: str


class CreditCardResponse(CreditCardCreate):
    id: int

    class Config:
        orm_mode = True


# DebitCard Schemas
class DebitCardCreate(BaseModel):
    card_number: str
    expiry_date: date
    cardholder_name: str


class DebitCardResponse(DebitCardCreate):
    id: int

    class Config:
        orm_mode = True
