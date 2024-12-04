from fastapi import APIRouter, HTTPException, status
from typing import List
from core.GoldDetails.models import GoldDetails
from core.GoldDetails.schemas import GoldDetailsCreate, GoldDetailsResponse
from core.Person.models import Person

router = APIRouter()

# Route for creating new gold details
@router.post("/gold-details", response_model=GoldDetailsResponse, status_code=status.HTTP_201_CREATED)
async def create_gold_details(data: GoldDetailsCreate):
    person = await Person.get_or_none(id=data.person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    gold_details = await GoldDetails.create(**data.dict())
    return gold_details

# Route for getting all gold details
@router.get("/gold-details", response_model=List[GoldDetailsResponse])
async def get_gold_details():
    return await GoldDetails.all()

# Route for getting a specific gold detail by ID
@router.get("/gold-details/{gold_details_id}", response_model=GoldDetailsResponse)
async def get_gold_detail(gold_details_id: int):
    gold_details = await GoldDetails.filter(id=gold_details_id).first()
    if not gold_details:
        raise HTTPException(status_code=404, detail="GoldDetails not found")
    return gold_details

# Route for getting gold details by person_id
@router.get("/person/{person_id}/gold-details", response_model=List[GoldDetailsResponse])
async def get_gold_details_by_person(person_id: int):
    person = await Person.get_or_none(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    gold_details = await GoldDetails.filter(person=person).all()
    if not gold_details:
        raise HTTPException(status_code=404, detail="No gold details found for this person")
    return gold_details

# Route for updating a gold detail by ID
@router.put("/gold-details/{gold_details_id}", response_model=GoldDetailsResponse)
async def update_gold_detail(gold_details_id: int, data: GoldDetailsCreate):
    gold_details = await GoldDetails.filter(id=gold_details_id).first()
    if not gold_details:
        raise HTTPException(status_code=404, detail="GoldDetails not found")

    person = await Person.get_or_none(id=data.person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    await gold_details.update_from_dict(data.dict()).save()
    return gold_details

# Route for deleting a gold detail by ID
@router.delete("/gold-details/{gold_details_id}")
async def delete_gold_detail(gold_details_id: int):
    gold_details = await GoldDetails.filter(id=gold_details_id).first()
    if not gold_details:
        raise HTTPException(status_code=404, detail="GoldDetails not found")
    await gold_details.delete()
    return {"message": "GoldDetails deleted successfully"}
