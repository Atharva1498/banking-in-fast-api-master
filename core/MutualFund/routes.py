from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from core.MutualFund.models import MutualFund
from core.MutualFund.schemas import MutualFundCreate, MutualFundResponse
from core.Person.models import Person
from core.shared.auth import get_current_user

router = APIRouter()

# Create a new Mutual Fund record
@router.post("/mutual-fund-details", response_model=MutualFundResponse, status_code=status.HTTP_201_CREATED)
async def create_mutual_fund(data: MutualFundCreate, user: Person = Depends(get_current_user)):
    # Ensure the person exists
    person = await Person.get_or_none(id=data.person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    # Create the mutual fund entry
    mutual_fund_details = await MutualFund.create(
        deposit_holder_name=data.deposit_holder_name,
        mutual_fund_company=data.mutual_fund_company,
        amount=data.amount,
        scheme_name=data.scheme_name,
        folio_number=data.folio_number,
        fund_type=data.fund_type,
        payment_options=data.payment_options,
        sip_or_lumpsum=data.sip_or_lumpsum,
        sip_tenure=data.sip_tenure,
        maturity_date=data.maturity_date,
        customer_portal_login_id=data.customer_portal_login_id,
        nominee_name=data.nominee_name,
        agent_cellphone_number=data.agent_cellphone_number,
        company_contract_number=data.company_contract_number,
        company_helpdesk_number=data.company_helpdesk_number,
        company_helpdesk_email=data.company_helpdesk_email,
        person=person  # Linking mutual fund to the person
    )
    return mutual_fund_details

# Get all Mutual Funds associated with a Person
@router.get("/person/{person_id}/mutual-funds", response_model=List[MutualFundResponse])
async def get_mutual_funds_by_person(person_id: int):
    person = await Person.get_or_none(id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    mutual_funds = await MutualFund.filter(person=person).all()
    if not mutual_funds:
        raise HTTPException(status_code=404, detail="No mutual funds found for this person")
    
    return mutual_funds

# Get all Mutual Fund details
@router.get("/mutual-fund-details", response_model=List[MutualFundResponse])
async def get_all_mutual_fund_details():
    return await MutualFund.all()

# Get a specific Mutual Fund detail by ID
@router.get("/mutual-fund-details/{mutual_fund_id}", response_model=MutualFundResponse)
async def get_mutual_fund_detail(mutual_fund_id: int):
    mutual_fund_details = await MutualFund.filter(id=mutual_fund_id).first()
    if not mutual_fund_details:
        raise HTTPException(status_code=404, detail="Mutual Fund Details not found")
    return mutual_fund_details

# Update a Mutual Fund detail by ID
@router.put("/mutual-fund-details/{mutual_fund_id}", response_model=MutualFundResponse)
async def update_mutual_fund_detail(mutual_fund_id: int, data: MutualFundCreate):
    mutual_fund_details = await MutualFund.filter(id=mutual_fund_id).first()
    if not mutual_fund_details:
        raise HTTPException(status_code=404, detail="Mutual Fund Details not found")
    
    # Update mutual fund details
    await mutual_fund_details.update_from_dict(data.dict()).save()
    return mutual_fund_details

# Delete a Mutual Fund detail by ID
@router.delete("/mutual-fund-details/{mutual_fund_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mutual_fund_detail(mutual_fund_id: int):
    mutual_fund_details = await MutualFund.filter(id=mutual_fund_id).first()
    if not mutual_fund_details:
        raise HTTPException(status_code=404, detail="Mutual Fund Details not found")
    
    await mutual_fund_details.delete()
    return {"detail": "Mutual Fund deleted successfully"}
