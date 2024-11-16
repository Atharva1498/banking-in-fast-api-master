from typing import Optional
from pydantic import BaseModel, Field, validator
from datetime import date

class LifeInsuranceCreate(BaseModel):
    policy_number: str = Field(max_length=50)
    policy_type: str = Field(max_length=100)
    coverage_amount: float
    start_date: date
    end_date: date
    beneficiary_name: str = Field(max_length=100)
    insured_member: Optional[int] = None

    @validator('policy_number')
    def policy_number_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Policy number must not be empty')
        return v

    @validator('policy_type')
    def policy_type_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Policy type must not be empty')
        return v

    @validator('coverage_amount')
    def coverage_amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Coverage amount must be a positive number')
        return v

    @validator('end_date')
    def end_date_must_be_after_start_date(cls, v, values):
        start_date = values.get('start_date')
        if start_date and v <= start_date:
            raise ValueError('End date must be after the start date')
        return v

class LifeInsuranceResponse(BaseModel):
    id: int
    policy_number: str
    policy_type: str
    coverage_amount: float
    start_date: date
    end_date: date
    beneficiary_name: str
    insured_member: Optional[int] = None

    class Config:
        from_attributes = True
