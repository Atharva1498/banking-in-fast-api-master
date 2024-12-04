from pydantic import BaseModel
from datetime import date
from core.FixedDepositDetails.enum import DepositType, DepositStatus

class FixedDepositCreate(BaseModel):
    depositor_name: str  # Name of the depositor
    person_id: int  # Person's unique ID
    bank_id: int  # Bank's unique ID
    fixed_deposit_id: str  # Unique Fixed Deposit ID
    amount_invested: float  # Amount invested in the fixed deposit
    fixed_deposit_number: str  # Unique FD number
    investment_duration: int  # Duration of the investment (in months)
    rate_of_interest: float  # Rate of interest
    maturity_amount: float  # Amount at maturity
    nominee_details: str  # Nominee details
    nominee_percentage: float  # Percentage of the FD the nominee is entitled to
    deposit_type: DepositType  # Type of Fixed Deposit
    deposit_status: DepositStatus  # Status of the FD
    start_date: date  # Start date of the FD
    maturity_date: date  # Maturity date of the FD

class FixedDepositResponse(BaseModel):
    id: int
    depositor_name: str
    person_id: int
    bank_id: int
    fixed_deposit_id: str
    amount_invested: float
    fixed_deposit_number: str
    investment_duration: int
    rate_of_interest: float
    maturity_amount: float
    nominee_details: str
    nominee_percentage: float
    deposit_type: DepositType
    deposit_status: DepositStatus
    start_date: date
    maturity_date: date

    class Config:
        orm_mode = True
