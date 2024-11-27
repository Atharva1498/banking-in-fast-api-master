from enum import Enum


class CreditorType(str, Enum):
    INDIVIDUAL = "individual"  # Creditor is an individual
    BUSINESS = "business"  # Creditor is a business entity
    OTHER = "other"  # Other types of creditors


class DebitorType(str, Enum):
    INDIVIDUAL = "individual"  # Debitor is an individual
    BUSINESS = "business"  # Debitor is a business entity
    OTHER = "other"  # Other types of debitors


class PaymentStatus(str, Enum):
    PENDING = "pending"  # Payment is pending
    COMPLETED = "completed"  # Payment is completed
    DEFAULTED = "defaulted"  # Payment is defaulted
