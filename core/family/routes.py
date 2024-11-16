from fastapi import APIRouter, Depends, HTTPException, status
from core.auth.models import User
from core.shared.auth import get_current_user
from .models import Address, FamilyMember
from .schema import AddressCreate, AddressResponse, FamilyMemberCreate, FamilyMemberResponse
from core.shared.middleware import JWTBearer
from core.family.models import Person
from core.family.schema import PersonCreate, PersonUpdate, PersonResponse
from tortoise.contrib.pydantic import pydantic_model_creator


family_router = APIRouter()


@family_router.post("/addresses", response_model=AddressResponse, dependencies=[Depends(JWTBearer())])
async def create_address(address: AddressCreate, user: User = Depends(get_current_user) ):
    address_data = address.model_dump()
    address_data["user"] = user
    address_obj = await Address.create(**address_data)
    return address_obj

@family_router.post("/family-members", response_model=FamilyMemberResponse, dependencies=[Depends(JWTBearer())])
async def create_family_member(family_member: FamilyMemberCreate, user: User = Depends(get_current_user)):
    family_data = family_member.model_dump()
    family_data["user_id"] = user.id
    family_member_obj = await FamilyMember.create(**family_data)
    return family_member_obj

# Tortoise model to Pydantic model
Person_Pydantic = pydantic_model_creator(Person, name="Person")

@family_router.post("/personalDetails", response_model=PersonResponse)
async def create_person(person: PersonCreate):
    new_person = await Person.create(**person.dict())
    return await Person_Pydantic.from_tortoise_orm(new_person)

@family_router.get("/personalDetails/{person_id}", response_model=PersonResponse)
async def read_person(person_id: int):
    person = await Person.get(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return await Person_Pydantic.from_tortoise_orm(person)

@family_router.put("/personalDetails/{person_id}", response_model=PersonResponse)
async def update_person(person_id: int, person: PersonUpdate):
    person_obj = await Person.get(id=person_id)
    if not person_obj:
        raise HTTPException(status_code=404, detail="Person not found")
    await person_obj.update_from_dict(person.dict()).save()
    return await Person_Pydantic.from_tortoise_orm(person_obj)

@family_router.delete("/personalDetails/{person_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_person(person_id: int):
    deleted_count = await Person.filter(id=person_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="Person not found")