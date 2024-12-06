from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
from core.LoanDetails.enum import LoanType


class LoanDetailCreate(BaseModel):
    borrower_name: str = Field(max_length=100)  # Name of the borrower
    sanction_date: date  # Sanction date of the loan
    loan_amount: float  # Total loan amount
    loan_tenure: int  # Loan tenure in months
    repayment_frequency: str = Field(max_length=20)  # Repayment frequency (e.g., Monthly, Quarterly)
    no_of_emi: int  # Number of EMIs
    emi_amount: float  # EMI amount
    loan_type: LoanType  # Type of loan
    current_pending_amount: float  # Current pending amount
    date_of_emi: date  # Date of EMI payment
    start_date: date  # Start date of the loan
    end_date: date  # End date of the loan
    bank_id: int  # ID of the bank associated with the loan
    person_id: Optional[int] = None  # ID of the person (optional)


class LoanDetailUpdate(BaseModel):
    borrower_name: Optional[str] = None
    sanction_date: Optional[date] = None
    loan_amount: Optional[float] = None
    loan_tenure: Optional[int] = None
    repayment_frequency: Optional[str] = None
    no_of_emi: Optional[int] = None
    emi_amount: Optional[float] = None
    loan_type: Optional[LoanType] = None
    current_pending_amount: Optional[float] = None
    date_of_emi: Optional[date] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    bank_id: Optional[int] = None
    person_id: Optional[int] = None


class LoanDetailResponse(BaseModel):
    id: int
    borrower_name: str
    sanction_date: date
    loan_amount: float
    loan_tenure: int
    repayment_frequency: str
    no_of_emi: int
    emi_amount: float
    loan_type: LoanType
    current_pending_amount: float
    date_of_emi: date
    start_date: date
    end_date: date
    bank_id: int  # Bank ID for the loan
    person_id: Optional[int] = None  # Person ID (optional)

    class Config:
        orm_mode = True
