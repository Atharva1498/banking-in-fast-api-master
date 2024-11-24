from fastapi import APIRouter, HTTPException
from typing import List
from core.FixedDepositDetails.models import FixedDepositDetails
from core.FixedDepositDetails.schemas import FixedDepositCreate, FixedDepositResponse

router = APIRouter()

# Create a new fixed deposit
@router.post("/fixed-deposits", response_model=FixedDepositResponse)
async def create_fixed_deposit(data: FixedDepositCreate):
    try:
        # Create a new fixed deposit entry in the database
        deposit = await FixedDepositDetails.create(**data.dict())
        return deposit
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Get list of all fixed deposits
@router.get("/fixed-deposits", response_model=List[FixedDepositResponse])
async def list_fixed_deposits():
    try:
        deposits = await FixedDepositDetails.all()  # Fetch all fixed deposit records
        return deposits
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get a specific fixed deposit by ID
@router.get("/fixed-deposits/{deposit_id}", response_model=FixedDepositResponse)
async def get_fixed_deposit(deposit_id: int):
    deposit = await FixedDepositDetails.filter(id=deposit_id).first()  # Fetch by ID
    if not deposit:
        raise HTTPException(status_code=404, detail="Fixed Deposit not found")
    return deposit

# Update a specific fixed deposit by ID
@router.put("/fixed-deposits/{deposit_id}", response_model=FixedDepositResponse)
async def update_fixed_deposit(deposit_id: int, data: FixedDepositCreate):
    deposit = await FixedDepositDetails.filter(id=deposit_id).first()  # Fetch by ID
    if not deposit:
        raise HTTPException(status_code=404, detail="Fixed Deposit not found")
    
    # Update deposit details
    await deposit.update_from_dict(data.dict()).save()
    return deposit

# Delete a specific fixed deposit by ID
@router.delete("/fixed-deposits/{deposit_id}")
async def delete_fixed_deposit(deposit_id: int):
    deposit = await FixedDepositDetails.filter(id=deposit_id).first()  # Fetch by ID
    if not deposit:
        raise HTTPException(status_code=404, detail="Fixed Deposit not found")
    
    await deposit.delete()  # Delete the deposit
    return {"message": "Fixed Deposit deleted successfully"}
