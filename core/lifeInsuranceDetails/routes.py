from fastapi import APIRouter, HTTPException, Depends
from tortoise.exceptions import IntegrityError
from typing import List, Optional

from core.auth.models import User
from core.lifeInsuranceDetails.models import LifeInsurance  # Replace with actual import path
from core.lifeInsuranceDetails.schemas import LifeInsuranceCreate, LifeInsuranceResponse
from core.shared.auth import get_current_user
from core.shared.middleware import JWTBearer

life_insurance_router = APIRouter()
# Assuming `bank_routes` is already defined as your router
@life_insurance_router.post(
    "/life-insurance",
    response_model=LifeInsuranceResponse,
    dependencies=[Depends(JWTBearer())],
)
async def create_life_insurance(
    life_insurance: LifeInsuranceCreate, user: User = Depends(get_current_user)
):
    try:
        # Check if a family member is associated, otherwise assign to the user
        insured_member_id = life_insurance.insured_member if life_insurance.insured_member else None

        # Create a new LifeInsurance instance
        new_life_insurance = await LifeInsurance.create(
            policy_number=life_insurance.policy_number,
            policy_type=life_insurance.policy_type,
            coverage_amount=life_insurance.coverage_amount,
            start_date=life_insurance.start_date,
            end_date=life_insurance.end_date,
            beneficiary_name=life_insurance.beneficiary_name,
            insured_member_id=insured_member_id,
            user=user,
        )
        return new_life_insurance
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=str(e))

@life_insurance_router.get(
    "/life-insurance",
    response_model=List[LifeInsuranceResponse],
    dependencies=[Depends(JWTBearer())],
)
async def get_life_insurance_policies(user: User = Depends(get_current_user)):
    try:
        # Fetch life insurance policies associated with the user and their family members
        life_insurance_policies = await LifeInsurance.filter(user=user).all()
        return life_insurance_policies
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@life_insurance_router.get(
    "/life-insurance/{policy_id}",
    response_model=LifeInsuranceResponse,
    dependencies=[Depends(JWTBearer())],
)
async def get_life_insurance_policy(policy_id: int, user: User = Depends(get_current_user)):
    try:
        # Retrieve a single life insurance policy by ID and ensure it belongs to the user
        policy = await LifeInsurance.get(id=policy_id, user=user)
        if not policy:
            raise HTTPException(status_code=404, detail="Policy not found")
        return policy
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@life_insurance_router.put(
    "/life-insurance/{policy_id}",
    response_model=LifeInsuranceResponse,
    dependencies=[Depends(JWTBearer())],
)
async def update_life_insurance_policy(
    policy_id: int,
    life_insurance_update: LifeInsuranceCreate,
    user: User = Depends(get_current_user),
):
    try:
        # Fetch the policy, ensure it exists and belongs to the user
        policy = await LifeInsurance.get(id=policy_id, user=user)
        if not policy:
            raise HTTPException(status_code=404, detail="Policy not found")

        # Update policy details
        policy.policy_number = life_insurance_update.policy_number
        policy.policy_type = life_insurance_update.policy_type
        policy.coverage_amount = life_insurance_update.coverage_amount
        policy.start_date = life_insurance_update.start_date
        policy.end_date = life_insurance_update.end_date
        policy.beneficiary_name = life_insurance_update.beneficiary_name
        policy.insured_member_id = life_insurance_update.insured_member or policy.insured_member_id
        await policy.save()
        return policy
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@life_insurance_router.delete(
    "/life-insurance/{policy_id}",
    response_model=dict,
    dependencies=[Depends(JWTBearer())],
)
async def delete_life_insurance_policy(policy_id: int, user: User = Depends(get_current_user)):
    try:
        # Find and delete the policy, ensuring it belongs to the user
        policy = await LifeInsurance.get(id=policy_id, user=user)
        if not policy:
            raise HTTPException(status_code=404, detail="Policy not found")
        await policy.delete()
        return {"detail": "Policy deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))