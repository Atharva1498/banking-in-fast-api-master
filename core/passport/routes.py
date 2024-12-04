from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from core.passport.models import PassportDetails
from core.passport.schemas import PassportCreate, PassportResponse
from core.Person.models import Person

passport_router = APIRouter()

# Create a new Passport
@passport_router.post("/passport", response_model=PassportResponse, status_code=status.HTTP_201_CREATED)
async def create_passport(passport_data: PassportCreate):
    # Verify the person exists
    person = await Person.get_or_none(id=passport_data.person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    # Create the passport
    new_passport = await PassportDetails.create(
        passport_number=passport_data.passport_number,
        date_of_issue=passport_data.date_of_issue,
        date_of_expiry=passport_data.date_of_expiry,
        country=passport_data.country,
        state=passport_data.state,
        city=passport_data.city,
        zip_code=passport_data.zip_code,
        person=person
    )
    return new_passport


# Get all Passports for a Person
@passport_router.get("/person/{person_id}/passports", response_model=List[PassportResponse])
async def get_passports_by_person(person_id: int):
    # Verify the person exists
    person = await Person.get_or_none(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    # Retrieve all passports linked to the person
    passports = await PassportDetails.filter(person=person).all()
    if not passports:
        raise HTTPException(status_code=404, detail="No passports found for this person")

    return passports


# Get a specific Passport by ID
@passport_router.get("/passport/{passport_id}", response_model=PassportResponse)
async def get_passport(passport_id: int):
    passport = await PassportDetails.get_or_none(id=passport_id)
    if not passport:
        raise HTTPException(status_code=404, detail="Passport not found")
    return passport


# Update a Passport
@passport_router.put("/passport/{passport_id}", response_model=PassportResponse)
async def update_passport(passport_id: int, passport_data: PassportCreate):
    passport = await PassportDetails.get_or_none(id=passport_id)
    if not passport:
        raise HTTPException(status_code=404, detail="Passport not found")

    # Update passport details
    await passport.update_from_dict(passport_data.dict(exclude={"person_id"})).save()
    return passport


# Delete a Passport
@passport_router.delete("/passport/{passport_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_passport(passport_id: int):
    passport = await PassportDetails.get_or_none(id=passport_id)
    if not passport:
        raise HTTPException(status_code=404, detail="Passport not found")
    await passport.delete()
