from pydantic import BaseModel, EmailStr
from datetime import date
from core.CreditCardDetails.enum import CardType, CardStatus

class CreditCardCreate(BaseModel):
    credit_card_number: str
    cardholder_name: str
    expiry_date: date
    card_type: CardType
    card_status: CardStatus
    credit_limit: float
    available_credit: float
    credit_card_amount: float
    type_of_credit_card: str
    issue_bank_name: str
    linked_bank_account_number: str
    registered_mobile_number: str
    registered_email: EmailStr
    date_of_payment: date
    date_of_bill_generation: date

class CreditCardResponse(BaseModel):
    id: int
    credit_card_number: str
    cardholder_name: str
    expiry_date: date
    card_type: CardType
    card_status: CardStatus
    credit_limit: float
    available_credit: float
    credit_card_amount: float
    type_of_credit_card: str
    issue_bank_name: str
    linked_bank_account_number: str
    registered_mobile_number: str
    registered_email: EmailStr
    date_of_payment: date
    date_of_bill_generation: date

    class Config:
        orm_mode = True
