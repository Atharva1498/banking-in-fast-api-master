from fastapi import APIRouter, HTTPException
from typing import List
from core.CreditorDebitor.models import Creditor, Debitor
from core.CreditorDebitor.enum import CreditorType, DebitorType, PaymentStatus

from core.CreditorDebitor.schemas import (
    CreditorCreate,
    CreditorResponse,
    DebitorCreate,
    DebitorResponse,
)

router = APIRouter()

# Routes for Creditor
@router.post("/creditors", response_model=CreditorResponse)
async def create_creditor(data: CreditorCreate):
    creditor = await Creditor.create(**data.dict())
    return creditor


@router.get("/creditors", response_model=List[CreditorResponse])
async def get_creditors():
    return await Creditor.all()


@router.get("/creditors/{creditor_id}", response_model=CreditorResponse)
async def get_creditor(creditor_id: int):
    creditor = await Creditor.filter(id=creditor_id).first()
    if not creditor:
        raise HTTPException(status_code=404, detail="Creditor not found")
    return creditor


@router.put("/creditors/{creditor_id}", response_model=CreditorResponse)
async def update_creditor(creditor_id: int, data: CreditorCreate):
    creditor = await Creditor.filter(id=creditor_id).first()
    if not creditor:
        raise HTTPException(status_code=404, detail="Creditor not found")
    await creditor.update_from_dict(data.dict()).save()
    return creditor


@router.delete("/creditors/{creditor_id}")
async def delete_creditor(creditor_id: int):
    creditor = await Creditor.filter(id=creditor_id).first()
    if not creditor:
        raise HTTPException(status_code=404, detail="Creditor not found")
    await creditor.delete()
    return {"message": "Creditor deleted successfully"}


# Routes for Debitor
@router.post("/debitors", response_model=DebitorResponse)
async def create_debitor(data: DebitorCreate):
    debitor = await Debitor.create(**data.dict())
    return debitor


@router.get("/debitors", response_model=List[DebitorResponse])
async def get_debitors():
    return await Debitor.all()


@router.get("/debitors/{debitor_id}", response_model=DebitorResponse)
async def get_debitor(debitor_id: int):
    debitor = await Debitor.filter(id=debitor_id).first()
    if not debitor:
        raise HTTPException(status_code=404, detail="Debitor not found")
    return debitor


@router.put("/debitors/{debitor_id}", response_model=DebitorResponse)
async def update_debitor(debitor_id: int, data: DebitorCreate):
    debitor = await Debitor.filter(id=debitor_id).first()
    if not debitor:
        raise HTTPException(status_code=404, detail="Debitor not found")
    await debitor.update_from_dict(data.dict()).save()
    return debitor


@router.delete("/debitors/{debitor_id}")
async def delete_debitor(debitor_id: int):
    debitor = await Debitor.filter(id=debitor_id).first()
    if not debitor:
        raise HTTPException(status_code=404, detail="Debitor not found")
    await debitor.delete()
    return {"message": "Debitor deleted successfully"}
