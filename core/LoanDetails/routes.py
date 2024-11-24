from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist
from core.LoanDetails.models import LoanDetails  # Import LoanDetails from core.models
from pydantic import BaseModel
from typing import List

# Create an instance of the APIRouter
loan_details_router = APIRouter()

# Pydantic schema for creating and reading LoanDetails
class LoanDetailsCreate(BaseModel):
    loan_amount: float
    loan_type: str
    interest_rate: float
    tenure: int  # Loan tenure in years

class LoanDetailsOut(LoanDetailsCreate):
    id: int
    created_at: str  # You can add created_at or any other fields returned from the DB

    class Config:
        orm_mode = True  # This allows Pydantic to work with Tortoise models


# Route to create a new LoanDetails entry
@loan_details_router.post("/loan-details/", response_model=LoanDetailsOut)
async def create_loan_details(loan_details: LoanDetailsCreate):
    # Create a new LoanDetails entry in the database
    new_loan = await LoanDetails.create(**loan_details.dict())
    return new_loan


# Route to get all LoanDetails entries
@loan_details_router.get("/loan-details/", response_model=List[LoanDetailsOut])
async def get_all_loan_details():
    # Get all loan details from the database
    loans = await LoanDetails.all()
    return loans


# Route to get a specific LoanDetails entry by ID
@loan_details_router.get("/loan-details/{loan_id}", response_model=LoanDetailsOut)
async def get_loan_details(loan_id: int):
    try:
        # Try to fetch the loan details by ID
        loan = await LoanDetails.get(id=loan_id)
        return loan
    except DoesNotExist:
        # If not found, raise a 404 error
        raise HTTPException(status_code=404, detail="Loan not found")


# Route to update a specific LoanDetails entry by ID
@loan_details_router.put("/loan-details/{loan_id}", response_model=LoanDetailsOut)
async def update_loan_details(loan_id: int, loan_details: LoanDetailsCreate):
    try:
        # Try to fetch and update the loan details
        loan = await LoanDetails.get(id=loan_id)
        loan.loan_amount = loan_details.loan_amount
        loan.loan_type = loan_details.loan_type
        loan.interest_rate = loan_details.interest_rate
        loan.tenure = loan_details.tenure
        await loan.save()
        return loan
    except DoesNotExist:
        # If not found, raise a 404 error
        raise HTTPException(status_code=404, detail="Loan not found")


# Route to delete a specific LoanDetails entry by ID
@loan_details_router.delete("/loan-details/{loan_id}")
async def delete_loan_details(loan_id: int):
    try:
        # Try to fetch and delete the loan details
        loan = await LoanDetails.get(id=loan_id)
        await loan.delete()
        return {"message": "Loan details deleted successfully"}
    except DoesNotExist:
        # If not found, raise a 404 error
        raise HTTPException(status_code=404, detail="Loan not found")
