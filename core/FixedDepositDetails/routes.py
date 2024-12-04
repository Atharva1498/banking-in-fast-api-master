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
    deposit = await FixedDepositDetails.create(**data.dict())
    return deposit

# Get list of all fixed deposits
@router.get("/fixed-deposits", response_model=List[FixedDepositResponse])
async def list_fixed_deposits():
    try:
        deposits = await FixedDepositDetails.all()  
        return deposits
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get a specific fixed deposit by ID
@router.get("/fixed-deposits/{deposit_id}", response_model=FixedDepositResponse)
async def get_fixed_deposit(deposit_id: int):
    deposit = await FixedDepositDetails.filter(id=deposit_id).first()  # Fetch by ID
    if not deposit:
        raise HTTPException(status_code=404, detail="Fixed Deposit not found")
    return deposit

# Get all fixed deposits by person_id
@router.get("/person/{person_id}/fixed-deposits", response_model=List[FixedDepositResponse])
async def get_fixed_deposits_by_person(person_id: int):
    person = await Person.get_or_none(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    
    deposits = await FixedDepositDetails.filter(person_id=person_id).all()
    if not deposits:
        raise HTTPException(status_code=404, detail="No fixed deposits found for this person")
    
    return deposits

# Get all fixed deposits by bank_id
@router.get("/bank/{bank_id}/fixed-deposits", response_model=List[FixedDepositResponse])
async def get_fixed_deposits_by_bank(bank_id: int):
    bank = await BankDetails.get_or_none(id=bank_id)
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")
    
    deposits = await FixedDepositDetails.filter(bank_id=bank_id).all()
    if not deposits:
        raise HTTPException(status_code=404, detail="No fixed deposits found for this bank")
    
    return deposits

# Update a specific fixed deposit by ID
@router.put("/fixed-deposits/{deposit_id}", response_model=FixedDepositResponse)
async def update_fixed_deposit(deposit_id: int, data: FixedDepositCreate):
    deposit = await FixedDepositDetails.filter(id=deposit_id).first()  
    if not deposit:
        raise HTTPException(status_code=404, detail="Fixed Deposit not found")
    
    # Update deposit details
    await deposit.update_from_dict(data.dict()).save()
    return deposit

# Delete a specific fixed deposit by ID
@router.delete("/fixed-deposits/{deposit_id}")
async def delete_fixed_deposit(deposit_id: int):
    deposit = await FixedDepositDetails.filter(id=deposit_id).first()
    if not deposit:
        raise HTTPException(status_code=404, detail="Fixed Deposit not found")
    
    await deposit.delete()  # Delete the deposit
    return {"message": "Fixed Deposit deleted successfully"}
