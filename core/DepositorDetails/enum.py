from enum import Enum

class DepositType(str, Enum):
    SAVINGS = "savings"
    FIXED_DEPOSIT = "fixed_deposit"
    RECURRING = "recurring"
    CURRENT = "current"
