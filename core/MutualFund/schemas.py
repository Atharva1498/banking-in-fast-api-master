from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

# Create Schema for Mutual Fund
class MutualFundCreate(BaseModel):
    deposit_holder_name: str
    mutual_fund_company: str
    amount: float
    scheme_name: str
    folio_number: str
    fund_type: str
    payment_options: str
    sip_or_lumpsum: str
    sip_tenure: int  # In months
    maturity_date: date
    customer_portal_login_id: str
    nominee_name: str
    agent_cellphone_number: str
    company_contract_number: str
    company_helpdesk_number: str
    company_helpdesk_email: str
    person_id: int 

# Response 
class MutualFundResponse(MutualFundCreate):
    id: int

    class Config:
        orm_mode = True
