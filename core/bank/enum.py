from enum import Enum


class AccountType(str, Enum):
    SAVINGS = "Savings"
    CURRENT = "Current"
    RECURRING_DEPOSIT = "Recurring Deposit"


class AddressType(str, Enum):
    PERMANENT = "Permanent"
    TEMPORARY = "Temporary"


class CardType(str, Enum):
    DEBIT = "Debit"
    CREDIT = "Credit"


class RelationshipType(str, Enum):
    MANAGER = "Manager"
    EXECUTIVE = "Executive"
