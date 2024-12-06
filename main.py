from contextlib import asynccontextmanager
from typing import AsyncIterator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from core.shared.db import init_db
from core.shared.conf import settings
from core.auth.routes import auth_router
from core.Person.routes import person_router
from core.bank.routes import bank_routes
from core.lifeInsuranceDetails.routes import life_insurance_router
from core.passport.routes import passport_router
from core.LoanDetails.routes import loan_routes
from core.CreditCardDetails.routes import router as credit_card_router
from core.FixedDepositDetails.routes import router as fixed_deposit_router
from core.DepositorDetails.routes import router as depositor_router
from core.CreditorDebitor.routes import router as creditor_debitor_router 
from core.GoldDetails.routes import router as gold_details_router
from core.PropertyDetails.routes import router as property_details_router
from core.RentalOwnerSelfOccupied.routes import router as rental_owner_self_occupied_router
from core.MutualFund.routes import router as mutual_fund_router
from core.ShareAndHoldings.routes import router as share_and_holdings_router






SERVER_PREFIX = "/api"

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await init_db()
    yield
    await Tortoise.close_connections()

app = FastAPI(
    title="DUMMY PROJECT",
    version="1.0.0",
    openapi_url=f"{SERVER_PREFIX}/openapi.json",
    docs_url=f"{SERVER_PREFIX}/docs",
    redoc_url=f"{SERVER_PREFIX}/redoc",
    debug=True,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
app.include_router(person_router, prefix="/api", tags=["Person & Address"])
app.include_router(bank_routes, prefix=f"{SERVER_PREFIX}/bank", tags=["Bank"])
app.include_router(life_insurance_router, prefix=f"{SERVER_PREFIX}/lifeInsuranceDetails", tags=["Life Insurance"])
app.include_router(passport_router, prefix=f"{SERVER_PREFIX}/passport", tags=["Passport"])
app.include_router(loan_routes, prefix=f"{SERVER_PREFIX}/loans", tags=["Loan Details"])
app.include_router(credit_card_router, prefix=f"{SERVER_PREFIX}/credit-cards", tags=["Credit Cards"])
app.include_router(fixed_deposit_router, prefix=f"{SERVER_PREFIX}/fixed-deposits", tags=["Fixed Deposits"])
app.include_router(depositor_router, prefix=f"{SERVER_PREFIX}/depositors", tags=["Depositors"])
app.include_router(creditor_debitor_router, prefix=f"{SERVER_PREFIX}/creditor-debitor", tags=["Creditor & Debitor"])
app.include_router(gold_details_router, prefix="/api/gold-details", tags=["Gold Details"])
app.include_router(property_details_router, prefix="/api/property-details", tags=["Property Details"])
app.include_router(rental_owner_self_occupied_router, prefix="/api/rental-owner-self-occupied", tags=["RentalOwnerSelfOccupied"])
app.include_router(mutual_fund_router, prefix="/api/mutual-fund", tags=["Mutual Fund"])
app.include_router(share_and_holdings_router, prefix="/api/share-and-holdings", tags=["Share and Holdings"])


@app.get("/")
def root():
    return {"message": "API is running!"}
