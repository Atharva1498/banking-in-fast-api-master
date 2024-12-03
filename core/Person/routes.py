from fastapi import APIRouter, HTTPException, status
from typing import List
from core.Person.models import Person, Address, FamilyDetails
from core.Person.schema import PersonCreate, PersonResponse
from tortoise.transactions import in_transaction

person_router = APIRouter()


@person_router.post("/person", response_model=PersonResponse, status_code=status.HTTP_201_CREATED)
async def create_person(person_data: PersonCreate):
    async with in_transaction():
        # Create the person
        person = await Person.create(
            first_name=person_data.first_name,
            middle_name=person_data.middle_name,
            last_name=person_data.last_name,
            dob=person_data.dob,
            phone_number=person_data.phone_number,
            email=person_data.email,
        )

        # Create addresses
        for address_data in person_data.addresses:
            await Address.create(person=person, **address_data.dict())

        # Create family members
        for family_data in person_data.family_members:
            await FamilyDetails.create(person=person, **family_data.dict())

        return await Person.get(id=person.id).prefetch_related("addresses", "family_members")


@person_router.get("/person/{person_id}", response_model=PersonResponse)
async def get_person(person_id: int):
    person = await Person.get_or_none(id=person_id).prefetch_related("addresses", "family_members")
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person


@person_router.put("/person/{person_id}", response_model=PersonResponse)
async def update_person(person_id: int, person_data: PersonCreate):
    person = await Person.get_or_none(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    # Update person details
    await person.update_from_dict(person_data.dict(exclude={"addresses", "family_members"})).save()

    # Update addresses
    await Address.filter(person=person).delete()
    for address_data in person_data.addresses:
        await Address.create(person=person, **address_data.dict())

    # Update family members
    await FamilyDetails.filter(person=person).delete()
    for family_data in person_data.family_members:
        await FamilyDetails.create(person=person, **family_data.dict())

    return await Person.get(id=person.id).prefetch_related("addresses", "family_members")


@person_router.delete("/person/{person_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_person(person_id: int):
    person = await Person.get_or_none(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    await person.delete()
