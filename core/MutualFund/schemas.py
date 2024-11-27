from pydantic import BaseModel
from datetime import date
from typing import Optional
from core.MutualFund.enum import FundType, PaymentOptions, SipOrLumpsum  # Import enums

class MutualFundCreate(BaseModel):
    deposit_holder_name: str
    mutual_fund_company: str
    amount: float
    scheme_name: str
    folio_number: str
    fund_type: FundType
    payment_option: PaymentOptions
    sip_or_lumpsum: SipOrLumpsum
    sip_tenure: Optional[int] = None  # SIP tenure (if SIP is chosen)
    maturity_date: date
    bank_details: str  # Bank details for ECS/SI
    customer_portal_login_id: str
    nominee_name: str
    agent_cellphone_number: str
    company_contract_number: str
    company_helpdesk_number: str
    company_helpdesk_email: str

class MutualFundResponse(MutualFundCreate):
    id: int  # ID of the mutual fund details

    class Config:
        orm_mode = True  # To allow ORM (Tortoise) to serialize the model
