from pydantic import BaseModel
from datetime import date
from typing import Optional
from core.ShareAndHoldings.enum import ShareType  # Import ShareType enum

class ShareAndHoldingsCreate(BaseModel):
    company_name: str  # Company name
    total_shares: int  # Total number of shares
    shares_owned: int  # Number of shares owned
    purchase_date: date  # Date of purchase
    purchase_rate: float  # Purchase rate per share
    purchase_cost: float  # Total cost of purchase
    demat_account_number: str  # Demat account number
    current_market_cost: float  # Current market cost per share
    share_type: Optional[ShareType] = None  # Optional: Type of share

class ShareAndHoldingsResponse(ShareAndHoldingsCreate):
    id: int  # ID of the share holding details

    class Config:
        orm_mode = True  # To allow ORM (Tortoise) to serialize the model
