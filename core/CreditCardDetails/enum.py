from enum import Enum

class CardType(str, Enum):
    CREDIT = "credit"
    DEBIT = "debit"

class CardStatus(str, Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    EXPIRED = "expired"