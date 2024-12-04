from fastapi import APIRouter, HTTPException, status
from typing import List
from core.FixedDepositDetails.models import FixedDepositDetails
from core.FixedDepositDetails.schemas import FixedDepositCreate, FixedDepositResponse
from core.bank.models import BankDetails
from core.Person.models import Person

router = APIRouter()

# Create a new fixed deposit
@router.post("/fixed-deposits", response_model=FixedDepositResponse)
async def create_fixed_deposit(data: FixedDepositCreate):
    # Validate the person
    person = await Person.get_or_none(id=data.person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    
    # Validate the bank
    bank = await BankDetails.get_or_none(id=data.bank_id)
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")

    # Create the fixed deposit entry
    deposit = await FixedDepositDetails.create(
        depositor_name=data.depositor_name,
        person=person,
        bank=bank,
        fixed_deposit_id=data.fixed_deposit_id,
        amount_invested=data.amount_invested,
        fixed_deposit_number=data.fixed_deposit_number,
        investment_duration=data.investment_duration,
        rate_of_interest=data.rate_of_interest,
        maturity_amount=data.maturity_amount,
        nominee_details=data.nominee_details,
        nominee_percentage=data.nominee_percentage,
        deposit_type=data.deposit_type,
        deposit_status=data.deposit_status,
        start_date=data.start_date,
        maturity_date=data.maturity_date,
    )
    return deposit

# Get all fixed deposits
@router.get("/fixed-deposits", response_model=List[FixedDepositResponse])
async def list_fixed_deposits():
    return await FixedDepositDetails.all()

# Get fixed deposits by person_id
@router.get("/person/{person_id}/fixed-deposits", response_model=List[FixedDepositResponse])
async def get_fixed_deposits_by_person(person_id: int):
    person = await Person.get_or_none(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    deposits = await FixedDepositDetails.filter(person=person).all()
    if not deposits:
        raise HTTPException(status_code=404, detail="No fixed deposits found for this person")
    return deposits

# Get fixed deposits by bank_id
@router.get("/bank/{bank_id}/fixed-deposits", response_model=List[FixedDepositResponse])
async def get_fixed_deposits_by_bank(bank_id: int):
    bank = await BankDetails.get_or_none(id=bank_id)
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")

    deposits = await FixedDepositDetails.filter(bank=bank).all()
    if not deposits:
        raise HTTPException(status_code=404, detail="No fixed deposits found for this bank")
    return deposits

# Update fixed deposit
@router.put("/fixed-deposits/{deposit_id}", response_model=FixedDepositResponse)
async def update_fixed_deposit(deposit_id: int, data: FixedDepositCreate):
    deposit = await FixedDepositDetails.get_or_none(id=deposit_id)
    if not deposit:
        raise HTTPException(status_code=404, detail="Fixed Deposit not found")

    # Update deposit details
    await deposit.update_from_dict(data.dict()).save()
    return deposit

# Delete fixed deposit
@router.delete("/fixed-deposits/{deposit_id}")
async def delete_fixed_deposit(deposit_id: int):
    deposit = await FixedDepositDetails.get_or_none(id=deposit_id)
    if not deposit:
        raise HTTPException(status_code=404, detail="Fixed Deposit not found")

    await deposit.delete()
    return {"message": "Fixed Deposit deleted successfully"}
