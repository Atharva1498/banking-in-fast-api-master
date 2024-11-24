from enum import Enum

# Enum for the type of fixed deposit (e.g., Standard, Tax-saving, etc.)
class DepositType(str, Enum):
    STANDARD = "standard"
    TAX_SAVING = "tax_saving"
    RECURRING = "recurring"

# Enum for the status of the fixed deposit (e.g., Active, Matured, Closed, etc.)
class DepositStatus(str, Enum):
    ACTIVE = "active"
    MATURED = "matured"
    CLOSED = "closed"

