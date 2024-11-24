from pydantic import BaseModel
from datetime import date
from core.enum import LoanType, LoanStatus, RepaymentFrequency
from core.models import LoanDetails


class LoanDetailCreate(BaseModel):
    loan_type: LoanType
    amount: float
    interest_rate: float
    tenure: int
    repayment_frequency: RepaymentFrequency
    issued_date: date
    due_date: date

class LoanDetailResponse(BaseModel):
    id: int
    loan_type: LoanType
    amount: float
    interest_rate: float
    tenure: int
    status: LoanStatus
    repayment_frequency: RepaymentFrequency
    issued_date: date
    due_date: date

    class Config:
        orm_mode = True
