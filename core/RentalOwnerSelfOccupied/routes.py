from fastapi import APIRouter, HTTPException
from typing import List
from core.RentalOwnerSelfOccupied.models import RentalOwnerSelfOccupied
from core.RentalOwnerSelfOccupied.schemas import RentalOwnerSelfOccupiedCreate, RentalOwnerSelfOccupiedResponse

router = APIRouter()

# Route for creating new property details
@router.post("/rental-owner-self-occupied", response_model=RentalOwnerSelfOccupiedResponse)
async def create_rental_owner_self_occupied(data: RentalOwnerSelfOccupiedCreate):
    property_details = await RentalOwnerSelfOccupied.create(**data.dict())
    return property_details

# Route for getting all property details
@router.get("/rental-owner-self-occupied", response_model=List[RentalOwnerSelfOccupiedResponse])
async def get_all_property_details():
    return await RentalOwnerSelfOccupied.all()

# Route for getting a specific property detail by ID
@router.get("/rental-owner-self-occupied/{property_id}", response_model=RentalOwnerSelfOccupiedResponse)
async def get_property_details(property_id: int):
    property_details = await RentalOwnerSelfOccupied.filter(id=property_id).first()
    if not property_details:
        raise HTTPException(status_code=404, detail="Property not found")
    return property_details

# Route for updating a property detail by ID
@router.put("/rental-owner-self-occupied/{property_id}", response_model=RentalOwnerSelfOccupiedResponse)
async def update_property_details(property_id: int, data: RentalOwnerSelfOccupiedCreate):
    property_details = await RentalOwnerSelfOccupied.filter(id=property_id).first()
    if not property_details:
        raise HTTPException(status_code=404, detail="Property not found")
    await property_details.update_from_dict(data.dict()).save()
    return property_details

# Route for deleting a property detail by ID
@router.delete("/rental-owner-self-occupied/{property_id}")
async def delete_property_details(property_id: int):
    property_details = await RentalOwnerSelfOccupied.filter(id=property_id).first()
    if not property_details:
        raise HTTPException(status_code=404, detail="Property not found")
    await property_details.delete()
    return {"message": "Property details deleted successfully"}
