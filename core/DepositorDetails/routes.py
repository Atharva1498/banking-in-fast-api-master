from fastapi import APIRouter, HTTPException, status
from typing import List
from core.DepositorDetails.models import DepositorDetails
from core.DepositorDetails.schemas import DepositorCreate, DepositorResponse
from core.bank.models import BankDetails
from core.Person.models import Person

router = APIRouter()

# Create a new depositor
@router.post("/depositors", response_model=DepositorResponse)
async def create_depositor(data: DepositorCreate):
    # Validate the person
    person = await Person.get_or_none(id=data.person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    
    # Validate the bank
    bank = await BankDetails.get_or_none(id=data.bank_id)
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")

    # Create the depositor record
    depositor = await DepositorDetails.create(**data.dict())
    return depositor

# Get list of all depositors
@router.get("/depositors", response_model=List[DepositorResponse])
async def list_depositors():
    return await DepositorDetails.all()

# Get a specific depositor by ID
@router.get("/depositors/{depositor_id}", response_model=DepositorResponse)
async def get_depositor(depositor_id: int):
    depositor = await DepositorDetails.filter(id=depositor_id).first()
    if not depositor:
        raise HTTPException(status_code=404, detail="Depositor not found")
    return depositor

# Get all depositors by person_id
@router.get("/person/{person_id}/depositors", response_model=List[DepositorResponse])
async def get_depositors_by_person(person_id: int):
    person = await Person.get_or_none(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    depositors = await DepositorDetails.filter(person_id=person_id).all()
    if not depositors:
        raise HTTPException(status_code=404, detail="No depositors found for this person")
    
    return depositors

# Get all depositors by bank_id
@router.get("/bank/{bank_id}/depositors", response_model=List[DepositorResponse])
async def get_depositors_by_bank(bank_id: int):
    bank = await BankDetails.get_or_none(id=bank_id)
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")

    depositors = await DepositorDetails.filter(bank_id=bank_id).all()
    if not depositors:
        raise HTTPException(status_code=404, detail="No depositors found for this bank")
    
    return depositors

# Update a specific depositor by ID
@router.put("/depositors/{depositor_id}", response_model=DepositorResponse)
async def update_depositor(depositor_id: int, data: DepositorCreate):
    depositor = await DepositorDetails.filter(id=depositor_id).first()
    if not depositor:
        raise HTTPException(status_code=404, detail="Depositor not found")
    
    # Update depositor details
    await depositor.update_from_dict(data.dict()).save()
    return depositor

# Delete a specific depositor by ID
@router.delete("/depositors/{depositor_id}")
async def delete_depositor(depositor_id: int):
    depositor = await DepositorDetails.filter(id=depositor_id).first()
    if not depositor:
        raise HTTPException(status_code=404, detail="Depositor not found")
    
    await depositor.delete()
    return {"message": "Depositor deleted successfully"}
