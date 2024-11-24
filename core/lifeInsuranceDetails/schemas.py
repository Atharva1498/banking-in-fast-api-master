from pydantic import BaseModel
from datetime import date

class LifeInsuranceCreate(BaseModel):
    policy_number: str
    policy_type: str
    coverage_amount: float
    start_date: date
    end_date: date
    beneficiary_name: str
    insured_member: int = None  # Optional, can be None if not provided

class LifeInsuranceResponse(BaseModel):
    id: int
    policy_number: str
    policy_type: str
    coverage_amount: float
    start_date: date
    end_date: date
    beneficiary_name: str

    class Config:
        orm_mode = True
