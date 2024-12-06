from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from core.LoanDetails.models import LoanDetails
from core.LoanDetails.schemas import LoanDetailCreate, LoanDetailUpdate, LoanDetailResponse
from core.bank.models import BankDetails
from core.Person.models import Person

loan_routes = APIRouter()


### CREATE LOAN ###

@loan_routes.post("/loans", response_model=LoanDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_loan(loan_data: LoanDetailCreate):
    # Validate BankDetails
    bank = await BankDetails.get_or_none(id=loan_data.bank_id)
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")

    # Validate Person (optional)
    person = None
    if loan_data.person_id:
        person = await Person.get_or_none(id=loan_data.person_id)
        if not person:
            raise HTTPException(status_code=404, detail="Person not found")

    # Create Loan
    new_loan = await LoanDetails.create(
        borrower_name=loan_data.borrower_name,
        sanction_date=loan_data.sanction_date,
        loan_amount=loan_data.loan_amount,
        loan_tenure=loan_data.loan_tenure,
        repayment_frequency=loan_data.repayment_frequency,
        no_of_emi=loan_data.no_of_emi,
        emi_amount=loan_data.emi_amount,
        loan_type=loan_data.loan_type,
        current_pending_amount=loan_data.current_pending_amount,
        date_of_emi=loan_data.date_of_emi,
        start_date=loan_data.start_date,
        end_date=loan_data.end_date,
        bank_detail=bank,
        person=person,
    )
    return new_loan


### GET ALL LOANS ###

@loan_routes.get("/loans", response_model=List[LoanDetailResponse])
async def get_all_loans():
    return await LoanDetails.all()


### GET LOAN BY ID ###

@loan_routes.get("/loans/{loan_id}", response_model=LoanDetailResponse)
async def get_loan(loan_id: int):
    loan = await LoanDetails.get_or_none(id=loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan


### GET LOANS BY BANK ###

@loan_routes.get("/bank/{bank_id}/loans", response_model=List[LoanDetailResponse])
async def get_loans_by_bank(bank_id: int):
    bank = await BankDetails.get_or_none(id=bank_id)
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")
    loans = await LoanDetails.filter(bank_detail=bank).all()
    return loans


### GET LOANS BY PERSON ###

@loan_routes.get("/person/{person_id}/loans", response_model=List[LoanDetailResponse])
async def get_loans_by_person(person_id: int):
    person = await Person.get_or_none(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    loans = await LoanDetails.filter(person=person).all()
    return loans


### UPDATE LOAN ###

@loan_routes.put("/loans/{loan_id}", response_model=LoanDetailResponse)
async def update_loan(loan_id: int, loan_data: LoanDetailUpdate):
    loan = await LoanDetails.get_or_none(id=loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")

    # Update loan details
    await loan.update_from_dict(loan_data.dict(exclude_unset=True)).save()
    return loan


### DELETE LOAN ###

@loan_routes.delete("/loans/{loan_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_loan(loan_id: int):
    loan = await LoanDetails.get_or_none(id=loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    await loan.delete()
