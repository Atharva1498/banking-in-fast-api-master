from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from core.auth.models import User
from core.bank.models import BankDetails, CreditCardDetails, DebitCardDetails
from core.bank.schemas import (
    BankDetailsCreate,
    BankDetailsResponse,
    CreditCardCreate,
    CreditCardResponse,
    DebitCardCreate,
    DebitCardResponse,
)
from core.shared.auth import get_current_user
from core.bank.enum import AccountType, AddressType, CardType, RelationshipType
from core.Person.models import Person

bank_routes = APIRouter()


### BANK DETAILS ###

# Create a new BankDetail
@bank_routes.post("/bank-details", response_model=BankDetailsResponse, status_code=status.HTTP_201_CREATED)
async def create_bank_detail(bank_details: BankDetailsCreate, user: User = Depends(get_current_user)):
    try:
        new_bank_detail = await BankDetails.create(**bank_details.dict(), user=user)
        return new_bank_detail
    except Exception as e:
        raise HTTPException(status_code=400, detail="Account creation failed.")


# Retrieve all BankDetails for the user
@bank_routes.get("/bank-details", response_model=List[BankDetailsResponse])
async def get_all_bank_details(user: User = Depends(get_current_user)):
    return await BankDetails.filter(user=user).all()


# Retrieve a specific BankDetail by ID
@bank_routes.get("/bank-details/{bank_id}", response_model=BankDetailsResponse)
async def get_bank_detail(bank_id: int, user: User = Depends(get_current_user)):
    bank_detail = await BankDetails.get_or_none(id=bank_id, user=user)
    if not bank_detail:
        raise HTTPException(status_code=404, detail="Bank detail not found.")
    return bank_detail


# Update a BankDetail
@bank_routes.put("/bank-details/{bank_id}", response_model=BankDetailsResponse)
async def update_bank_detail(bank_id: int, bank_details: BankDetailsCreate, user: User = Depends(get_current_user)):
    bank_detail = await BankDetails.get_or_none(id=bank_id, user=user)
    if not bank_detail:
        raise HTTPException(status_code=404, detail="Bank detail not found.")
    await bank_detail.update_from_dict(bank_details.dict()).save()
    return bank_detail


# Delete a BankDetail
@bank_routes.delete("/bank-details/{bank_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bank_detail(bank_id: int, user: User = Depends(get_current_user)):
    deleted_count = await BankDetails.filter(id=bank_id, user=user).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="Bank detail not found.")


### CREDIT CARD DETAILS ###

# Add a Credit Card to a BankDetail
@bank_routes.post("/bank-details/{bank_id}/credit-cards", response_model=CreditCardResponse)
async def add_credit_card(bank_id: int, card: CreditCardCreate):
    bank_detail = await BankDetails.get_or_none(id=bank_id)
    if not bank_detail:
        raise HTTPException(status_code=404, detail="Bank detail not found.")
    new_card = await CreditCardDetails.create(**card.dict(), bank_detail=bank_detail)
    return new_card


# Retrieve all Credit Cards for a BankDetail
@bank_routes.get("/bank-details/{bank_id}/credit-cards", response_model=List[CreditCardResponse])
async def get_credit_cards(bank_id: int):
    bank_detail = await BankDetails.get_or_none(id=bank_id)
    if not bank_detail:
        raise HTTPException(status_code=404, detail="Bank detail not found.")
    return await CreditCardDetails.filter(bank_detail=bank_detail).all()


# Update a Credit Card
@bank_routes.put("/credit-cards/{card_id}", response_model=CreditCardResponse)
async def update_credit_card(card_id: int, card: CreditCardCreate):
    credit_card = await CreditCardDetails.get_or_none(id=card_id)
    if not credit_card:
        raise HTTPException(status_code=404, detail="Credit card not found.")
    await credit_card.update_from_dict(card.dict()).save()
    return credit_card


# Delete a Credit Card
@bank_routes.delete("/credit-cards/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_credit_card(card_id: int):
    deleted_count = await CreditCardDetails.filter(id=card_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="Credit card not found.")


### DEBIT CARD DETAILS ###

# Add a Debit Card to a BankDetail
@bank_routes.post("/bank-details/{bank_id}/debit-cards", response_model=DebitCardResponse)
async def add_debit_card(bank_id: int, card: DebitCardCreate):
    bank_detail = await BankDetails.get_or_none(id=bank_id)
    if not bank_detail:
        raise HTTPException(status_code=404, detail="Bank detail not found.")
    new_card = await DebitCardDetails.create(**card.dict(), bank_detail=bank_detail)
    return new_card


# Retrieve all Debit Cards for a BankDetail
@bank_routes.get("/bank-details/{bank_id}/debit-cards", response_model=List[DebitCardResponse])
async def get_debit_cards(bank_id: int):
    bank_detail = await BankDetails.get_or_none(id=bank_id)
    if not bank_detail:
        raise HTTPException(status_code=404, detail="Bank detail not found.")
    return await DebitCardDetails.filter(bank_detail=bank_detail).all()


# Update a Debit Card
@bank_routes.put("/debit-cards/{card_id}", response_model=DebitCardResponse)
async def update_debit_card(card_id: int, card: DebitCardCreate):
    debit_card = await DebitCardDetails.get_or_none(id=card_id)
    if not debit_card:
        raise HTTPException(status_code=404, detail="Debit card not found.")
    await debit_card.update_from_dict(card.dict()).save()
    return debit_card


# Delete a Debit Card
@bank_routes.delete("/debit-cards/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_debit_card(card_id: int):
    deleted_count = await DebitCardDetails.filter(id=card_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="Debit card not found.")


### NEW ROUTE FOR PERSON'S BANK DETAILS ###

# Get all BankDetails for a person by person_id
@bank_routes.get("/person/{person_id}/bank-details", response_model=List[BankDetailsResponse])
async def get_bank_details_by_person_id(person_id: int):
    # Ensure the person exists
    person = await Person.get_or_none(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    
    # Fetch all bank details related to the person
    bank_details = await BankDetails.filter(person_id=person_id).all()
    
    # If no bank details are found
    if not bank_details:
        raise HTTPException(status_code=404, detail="No bank details found for this person")
    
    return bank_details
