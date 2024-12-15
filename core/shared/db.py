import os
from tortoise import Tortoise

# Get DATABASE_URL from environment or default to PostgreSQL service in Docker
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgres://admin:admin@postgres:5432/bank_dbname"  # Replace with your actual credentials
)

# Tortoise Configuration
DATABASE_CONFIG = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": [
                "core.Person",  # Add all your API models here
                "core.auth",
                "core.bank",
                "core.CreditCardDetails",
                "core.CreditorDebitor",
                "core.DepositorDetails",
                "core.FixedDepositDetails",
                "core.GoldDetails",
                "core.lifeInsuranceDetails",
                "core.LoanDetails",
                "core.MutualFund",
                "core.passport",
                "core.PropertyDetails",
                "core.RentalOwnerSelfOccupied",
                "core.ShareAndHoldings",
                "aerich.models",  # For migrations (if using Aerich)
            ],
            "default_connection": "default",
        }
    },
}

async def init_db():
    """Initialize the Tortoise database."""
    await Tortoise.init(config=DATABASE_CONFIG)
    await Tortoise.generate_schemas()

async def close_db():
    """Close the Tortoise database connections."""
    await Tortoise.close_connections()
