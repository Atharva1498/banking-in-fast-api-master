from fastapi import APIRouter, HTTPException, Depends
from tortoise.exceptions import IntegrityError
from typing import List, Optional

from core.auth.models import User
from core.lifeInsuranceDetails.models import LifeInsurance
from core.lifeInsuranceDetails.schemas import LifeInsuranceCreate, LifeInsuranceResponse
from core.shared.auth import get_current_user
from core.Person.models import Person

life_insurance_router = APIRouter()


### CRUD with `person_id` ###

# Create a new life insurance policy linked to a person
@life_insurance_router.post("/life-insurance", response_model=LifeInsuranceResponse)
async def create_life_insurance(data: LifeInsuranceCreate):
    person = await Person.get_or_none(id=data.person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    try:
        new_policy = await LifeInsurance.create(
            **data.dict(exclude={"person_id"}), person=person
        )
        return new_policy
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Get all life insurance policies for a person
@life_insurance_router.get("/person/{person_id}/life-insurance", response_model=List[LifeInsuranceResponse])
async def get_life_insurance_by_person(person_id: int):
    person = await Person.get_or_none(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    policies = await LifeInsurance.filter(person=person).all()
    if not policies:
        raise HTTPException(status_code=404, detail="No life insurance policies found")
    return policies


### CRUD with user authentication ###

# Create a life insurance policy (with JWT authentication)
@life_insurance_router.post("/auth-life-insurance", response_model=LifeInsuranceResponse, dependencies=[Depends(get_current_user)])
async def create_life_insurance_auth(
    life_insurance: LifeInsuranceCreate, user: User = Depends(get_current_user)
):
    try:
        new_policy = await LifeInsurance.create(
            **life_insurance.dict(), user=user
        )
        return new_policy
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Get all life insurance policies associated with the user
@life_insurance_router.get("/auth-life-insurance", response_model=List[LifeInsuranceResponse], dependencies=[Depends(get_current_user)])
async def get_life_insurance_policies(user: User = Depends(get_current_user)):
    policies = await LifeInsurance.filter(user=user).all()
    return policies


# Get a specific life insurance policy by policy ID
@life_insurance_router.get("/auth-life-insurance/{policy_id}", response_model=LifeInsuranceResponse, dependencies=[Depends(get_current_user)])
async def get_life_insurance_policy(policy_id: int, user: User = Depends(get_current_user)):
    policy = await LifeInsurance.get_or_none(id=policy_id, user=user)
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    return policy


# Update a life insurance policy
@life_insurance_router.put("/auth-life-insurance/{policy_id}", response_model=LifeInsuranceResponse, dependencies=[Depends(get_current_user)])
async def update_life_insurance_policy(
    policy_id: int,
    life_insurance_update: LifeInsuranceCreate,
    user: User = Depends(get_current_user),
):
    policy = await LifeInsurance.get_or_none(id=policy_id, user=user)
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    await policy.update_from_dict(life_insurance_update.dict()).save()
    return policy


# Delete a life insurance policy
@life_insurance_router.delete("/auth-life-insurance/{policy_id}", response_model=dict, dependencies=[Depends(get_current_user)])
async def delete_life_insurance_policy(policy_id: int, user: User = Depends(get_current_user)):
    policy = await LifeInsurance.get_or_none(id=policy_id, user=user)
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    await policy.delete()
    return {"detail": "Policy deleted successfully"}
