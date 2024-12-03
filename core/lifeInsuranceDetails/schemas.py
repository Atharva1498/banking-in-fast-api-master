from pydantic import BaseModel
from datetime import date


class LifeInsuranceCreate(BaseModel):
    policy_number: str
    policy_type: str
    coverage_amount: float
    start_date: date
    end_date: date
    beneficiary_name: str
    person_id: int  # Associate the life insurance with a person


class LifeInsuranceResponse(BaseModel):
    id: int
    policy_number: str
    policy_type: str
    coverage_amount: float
    start_date: date
    end_date: date
    beneficiary_name: str
    person_id: int  # Include person_id in the response

    class Config:
        orm_mode = True
