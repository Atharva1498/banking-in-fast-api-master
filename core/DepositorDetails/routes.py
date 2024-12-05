from fastapi import APIRouter, HTTPException
from typing import List
from core.DepositorDetails.models import DepositorDetails
from core.DepositorDetails.schemas import DepositorCreate
from core.Person.models import Person

router = APIRouter()

# Create a new depositor for a person
@router.post("/person/depositors/{person_id}", response_model=DepositorCreate)
async def create_depositor(person_id: int, data: DepositorCreate):
    # Validate the person
    person = await Person.get_or_none(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    # Create the depositor record
    depositor = await DepositorDetails.create(
        depositor_name=data.depositor_name,
        person_id=person_id,  
        contact_number=data.contact_number,
        email=data.email,
        address=data.address,
        amount_invested=data.amount_invested,
        roi=data.roi,
        deposit_type=data.deposit_type,
        invested_date=data.invested_date,
        maturity_date=data.maturity_date,
    )
    return depositor

# Get all depositors for a person
@router.get("/person/depositors/{person_id}", response_model=List[DepositorCreate])
async def get_depositors_by_person(person_id: int):
    person = await Person.get_or_none(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    depositors = await DepositorDetails.filter(person_id=person_id).all()
    if not depositors:
        raise HTTPException(status_code=404, detail="No depositors found for this person")
    
    return depositors

# Update a depositor for a person
@router.put("/person/depositors/{person_id}", response_model=DepositorCreate)
async def update_depositor(person_id: int, data: DepositorCreate):
    depositor = await DepositorDetails.filter(person_id=person_id).first()
    if not depositor:
        raise HTTPException(status_code=404, detail="Depositor not found")
    
    # Update depositor details
    await depositor.update_from_dict(
        {
            "depositor_name": data.depositor_name,
            "person_id": person_id,  # Ensure the person_id remains the same
            "contact_number": data.contact_number,
            "email": data.email,
            "address": data.address,
            "amount_invested": data.amount_invested,
            "roi": data.roi,
            "deposit_type": data.deposit_type,
            "invested_date": data.invested_date,
            "maturity_date": data.maturity_date,
        }
    ).save()
    return depositor

# Delete all depositors for a person
@router.delete("/person/depositors/{person_id}")
async def delete_all_depositors_by_person(person_id: int):
    person = await Person.get_or_none(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    
    deleted_count = await DepositorDetails.filter(person_id=person_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="No depositors found for this person")
    
    return {"message": f"{deleted_count} depositors deleted successfully"}
