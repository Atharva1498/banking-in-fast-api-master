from fastapi import APIRouter, HTTPException
from typing import List
from core.DepositorDetails.models import DepositorDetails
from core.DepositorDetails.schemas import DepositorCreate, DepositorResponse

router = APIRouter()

# Create a new depositor
@router.post("/depositors", response_model=DepositorResponse)
async def create_depositor(data: DepositorCreate):
    try:
        depositor = await DepositorDetails.create(**data.dict())
        return depositor
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Get list of all depositors
@router.get("/depositors", response_model=List[DepositorResponse])
async def list_depositors():
    try:
        depositors = await DepositorDetails.all()
        return depositors
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get a specific depositor by ID
@router.get("/depositors/{depositor_id}", response_model=DepositorResponse)
async def get_depositor(depositor_id: int):
    depositor = await DepositorDetails.filter(id=depositor_id).first()
    if not depositor:
        raise HTTPException(status_code=404, detail="Depositor not found")
    return depositor

# Update a specific depositor by ID
@router.put("/depositors/{depositor_id}", response_model=DepositorResponse)
async def update_depositor(depositor_id: int, data: DepositorCreate):
    depositor = await DepositorDetails.filter(id=depositor_id).first()
    if not depositor:
        raise HTTPException(status_code=404, detail="Depositor not found")
    await depositor.update_from_dict(data.dict()).save()
    return depositor

# Delete a specific depositor by ID
@router.delete("/depositors/{depositor_id}")
async def delete_depositor(depositor_id: int):
    depositor = await DepositorDetails.filter(id=depositor_id).first()
    if not depositor:
        raise HTTPException(status_code=404, detail="Depositor not found")
    await depositor.delete()
    return {"message": "Depositor deleted successfully"}
