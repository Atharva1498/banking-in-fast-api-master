from fastapi import APIRouter, HTTPException
from typing import List
from core.ShareAndHoldings.models import ShareAndHoldings
from core.ShareAndHoldings.schemas import ShareAndHoldingsCreate, ShareAndHoldingsResponse

router = APIRouter()

# Route for creating new share holding details
@router.post("/share-and-holdings", response_model=ShareAndHoldingsResponse)
async def create_share_and_holdings(data: ShareAndHoldingsCreate):
    share_details = await ShareAndHoldings.create(**data.dict())
    return share_details

# Route for getting all share holding details
@router.get("/share-and-holdings", response_model=List[ShareAndHoldingsResponse])
async def get_all_share_and_holdings():
    return await ShareAndHoldings.all()

# Route for getting a specific share holding detail by ID
@router.get("/share-and-holdings/{share_id}", response_model=ShareAndHoldingsResponse)
async def get_share_and_holding_detail(share_id: int):
    share_details = await ShareAndHoldings.filter(id=share_id).first()
    if not share_details:
        raise HTTPException(status_code=404, detail="Share and Holding not found")
    return share_details

# Route for updating a share holding detail by ID
@router.put("/share-and-holdings/{share_id}", response_model=ShareAndHoldingsResponse)
async def update_share_and_holding_detail(share_id: int, data: ShareAndHoldingsCreate):
    share_details = await ShareAndHoldings.filter(id=share_id).first()
    if not share_details:
        raise HTTPException(status_code=404, detail="Share and Holding not found")
    await share_details.update_from_dict(data.dict()).save()
    return share_details

# Route for deleting a share holding detail by ID
@router.delete("/share-and-holdings/{share_id}")
async def delete_share_and_holding_detail(share_id: int):
    share_details = await ShareAndHoldings.filter(id=share_id).first()
    if not share_details:
        raise HTTPException(status_code=404, detail="Share and Holding not found")
    await share_details.delete()
    return {"message": "Share and Holding details deleted successfully"}
