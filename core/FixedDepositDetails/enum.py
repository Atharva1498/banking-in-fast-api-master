from enum import Enum

class DepositType(str, Enum):
    RECURRING = "recurring"
    FIXED = "fixed"

class DepositStatus(str, Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    PENDING = "pending"

