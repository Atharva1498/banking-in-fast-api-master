from pydantic import BaseModel, EmailStr
from datetime import date
from core.enum import DepositType, DepositStatus

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
    deposit_type: DepositType  # Type of Fixed Deposit (e.g., standard, tax_saving)
    deposit_status: DepositStatus  # Status of the FD (e.g., active, matured)
    start_date: date  # Start date of the FD
    maturity_date: date  # Maturity date of the FD

class FixedDepositResponse(BaseModel):
    id: int  # Fixed Deposit ID
    depositor_name: str  # Name of the depositor
    person_id: int  # Person's unique ID
    bank_id: int  # Bank's unique ID
    fixed_deposit_id: str  # Unique Fixed Deposit ID
    amount_invested: float  # Amount invested
    fixed_deposit_number: str  # Fixed Deposit number
    investment_duration: int  # Duration in months or years
    rate_of_interest: float  # Rate of interest
    maturity_amount: float  # Maturity amount
    nominee_details: str  # Nominee details
    nominee_percentage: float  # Nominee's share in FD
    deposit_type: DepositType  # Type of Fixed Deposit
    deposit_status: DepositStatus  # Status of the FD
    start_date: date  # Start date of the FD
    maturity_date: date  # Maturity date of the FD

    class Config:
        orm_mode = True  # Ensure compatibility with Tortoise ORM models
