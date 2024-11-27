from fastapi import APIRouter, HTTPException
from typing import List
from core.MutualFund.models import MutualFund
from core.MutualFund.schemas import MutualFundCreate, MutualFundResponse

router = APIRouter()

# Route for creating new mutual fund details
@router.post("/mutual-fund-details", response_model=MutualFundResponse)
async def create_mutual_fund(data: MutualFundCreate):
    mutual_fund_details = await MutualFund.create(**data.dict())
    return mutual_fund_details

# Route for getting all mutual fund details
@router.get("/mutual-fund-details", response_model=List[MutualFundResponse])
async def get_all_mutual_fund_details():
    return await MutualFund.all()

# Route for getting a specific mutual fund detail by ID
@router.get("/mutual-fund-details/{mutual_fund_id}", response_model=MutualFundResponse)
async def get_mutual_fund_detail(mutual_fund_id: int):
    mutual_fund_details = await MutualFund.filter(id=mutual_fund_id).first()
    if not mutual_fund_details:
        raise HTTPException(status_code=404, detail="Mutual Fund Details not found")
    return mutual_fund_details

# Route for updating a mutual fund detail by ID
@router.put("/mutual-fund-details/{mutual_fund_id}", response_model=MutualFundResponse)
async def update_mutual_fund_detail(mutual_fund_id: int, data: MutualFundCreate):
    mutual_fund_details = await MutualFund.filter(id=mutual_fund_id).first()
    if not mutual_fund_details:
        raise HTTPException(status_code=404, detail="Mutual Fund Details not found")
    await mutual_fund_details.update_from_dict(data.dict()).save()
    return mutual_fund_details

# Route for deleting a mutual fund detail by ID
@router.delete("/mutual-fund-details/{mutual_fund_id}")
async def delete_mutual_fund_detail(mutual_fund_id: int):
    mutual_fund_details = await MutualFund.filter(id=mutual_fund_id).first()
    if not mutual_fund_details:
        raise HTTPException(status_code=404, detail="Mutual Fund Details not found")
    await mutual_fund_details.delete()
    return {"message": "Mutual Fund Details deleted successfully"}
