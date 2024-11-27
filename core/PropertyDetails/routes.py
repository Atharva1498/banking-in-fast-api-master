from fastapi import APIRouter, HTTPException
from typing import List
from core.PropertyDetails.models import PropertyDetails
from core.PropertyDetails.schemas import PropertyDetailsCreate, PropertyDetailsResponse

router = APIRouter()

# Route for creating new property details
@router.post("/property-details", response_model=PropertyDetailsResponse)
async def create_property_details(data: PropertyDetailsCreate):
    property_details = await PropertyDetails.create(**data.dict())
    return property_details

# Route for getting all property details
@router.get("/property-details", response_model=List[PropertyDetailsResponse])
async def get_property_details():
    return await PropertyDetails.all()

# Route for getting a specific property detail by ID
@router.get("/property-details/{property_details_id}", response_model=PropertyDetailsResponse)
async def get_property_detail(property_details_id: int):
    property_details = await PropertyDetails.filter(id=property_details_id).first()
    if not property_details:
        raise HTTPException(status_code=404, detail="PropertyDetails not found")
    return property_details

# Route for updating a property detail by ID
@router.put("/property-details/{property_details_id}", response_model=PropertyDetailsResponse)
async def update_property_detail(property_details_id: int, data: PropertyDetailsCreate):
    property_details = await PropertyDetails.filter(id=property_details_id).first()
    if not property_details:
        raise HTTPException(status_code=404, detail="PropertyDetails not found")
    await property_details.update_from_dict(data.dict()).save()
    return property_details

# Route for deleting a property detail by ID
@router.delete("/property-details/{property_details_id}")
async def delete_property_detail(property_details_id: int):
    property_details = await PropertyDetails.filter(id=property_details_id).first()
    if not property_details:
        raise HTTPException(status_code=404, detail="PropertyDetails not found")
    await property_details.delete()
    return {"message": "PropertyDetails deleted successfully"}
