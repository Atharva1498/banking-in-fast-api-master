from fastapi import APIRouter, HTTPException, Depends
from typing import List
from tortoise.exceptions import IntegrityError
from core.auth.models import User
from core.shared.auth import get_current_user
from core.passport.models import PassportDetails
from core.passport.schemas import PassportCreate, PassportResponse

passport_router = APIRouter()

@passport_router.post(
    "/passport",
    response_model=PassportResponse,
    dependencies=[Depends(get_current_user)],
)
async def create_passport_details(
    passport_data: PassportCreate, user: User = Depends(get_current_user)
):
    try:
        new_passport = await PassportDetails.create(
            user=user,
            **passport_data.dict()
        )
        return new_passport
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail="Passport number must be unique.")

@passport_router.get(
    "/passport",
    response_model=List[PassportResponse],
    dependencies=[Depends(get_current_user)],
)
async def get_passport_details(user: User = Depends(get_current_user)):
    return await PassportDetails.filter(user=user).all()

@passport_router.put(
    "/passport/{passport_id}",
    response_model=PassportResponse,
    dependencies=[Depends(get_current_user)],
)
async def update_passport_details(
    passport_id: int,
    passport_data: PassportCreate,
    user: User = Depends(get_current_user),
):
    passport = await PassportDetails.get_or_none(id=passport_id, user=user)
    if not passport:
        raise HTTPException(status_code=404, detail="Passport not found.")
    await passport.update_from_dict(passport_data.dict()).save()
    return passport

@passport_router.delete(
    "/passport/{passport_id}",
    dependencies=[Depends(get_current_user)],
)
async def delete_passport_details(passport_id: int, user: User = Depends(get_current_user)):
    passport = await PassportDetails.get_or_none(id=passport_id, user=user)
    if not passport:
        raise HTTPException(status_code=404, detail="Passport not found.")
    await passport.delete()
    return {"detail": "Passport deleted successfully"}

