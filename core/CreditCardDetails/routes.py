from fastapi import APIRouter, HTTPException
from typing import List
from core.CreditCardDetails.models import CreditCardDetails
from core.CreditCardDetails.schemas import CreditCardCreate, CreditCardResponse

router = APIRouter()

@router.post("/credit-cards", response_model=CreditCardResponse)
async def create_credit_card(data: CreditCardCreate):
    try:
        card = await CreditCardDetails.create(**data.dict())
        return card
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/credit-cards", response_model=List[CreditCardResponse])
async def list_credit_cards():
    try:
        cards = await CreditCardDetails.all()
        return cards
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/credit-cards/{card_id}", response_model=CreditCardResponse)
async def get_credit_card(card_id: int):
    card = await CreditCardDetails.filter(id=card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Credit card not found")
    return card

@router.put("/credit-cards/{card_id}", response_model=CreditCardResponse)
async def update_credit_card(card_id: int, data: CreditCardCreate):
    card = await CreditCardDetails.filter(id=card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Credit card not found")
    await card.update_from_dict(data.dict()).save()
    return card

@router.delete("/credit-cards/{card_id}")
async def delete_credit_card(card_id: int):
    card = await CreditCardDetails.filter(id=card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Credit card not found")
    await card.delete()
    return {"message": "Credit card deleted successfully"}
