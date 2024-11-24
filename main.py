from contextlib import asynccontextmanager
from typing import AsyncIterator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
from core.shared.db import init_db
from core.shared.conf import settings
from core.auth.routes import auth_route
from core.family.routes import family_router
from core.bank.routes import bank_routes
from core.lifeInsuranceDetails.routes import life_insurance_router
from core.passport.routes import passport_router
from tortoise import Tortoise, run_async
from core.LoanDetails.routes import loan_details_router
from core.CreditCardDetails.routes import router as credit_card_router
from core.FixedDepositDetails.routes import router as fixed_deposit_router
from core.DepositorDetails.routes import router as depositor_router
from core.PersonBankDepositorConnection.routes import router as connection_router  # Import connection router


# from core.shared.middleware import JWTBearer, JWTMiddleware

SERVER_PREFIX = "/api"

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # Startup event
    await init_db()
    yield
    # Shutdown event
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

# Uncomment and configure JWT Middleware if required
# app.add_middleware(JWTMiddleware)

register_tortoise(
    app,
    db_url=settings.DATABASE,
    modules={"models": ["core.shared.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(auth_route, prefix=f"{SERVER_PREFIX}/auth", tags=["auth"])
app.include_router(family_router, prefix=f"{SERVER_PREFIX}/family", tags=["family"])
app.include_router(bank_routes, prefix=f"{SERVER_PREFIX}/bank", tags=["bank"])
app.include_router(life_insurance_router, prefix=f"{SERVER_PREFIX}/lifeInsuranceDetails", tags=["lifeInsuranceDetails"])
app.include_router(passport_router, prefix=f"{SERVER_PREFIX}/passport", tags=["passport"])
app.include_router(loan_details_router, prefix="/api", tags=["Loan Details"])
app.include_router(credit_card_router, prefix=f"{SERVER_PREFIX}/credit-cards", tags=["Credit Cards"])
app.include_router(fixed_deposit_router, prefix="/api/fixed-deposits", tags=["Fixed Deposits"])
app.include_router(depositor_router, prefix="/api/depositors", tags=["Depositors"])
app.include_router(connection_router, prefix="/api/connections", tags=["Connections"])



