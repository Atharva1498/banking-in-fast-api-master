from enum import Enum

class LoanType(str, Enum):
    PERSONAL = "personal"
    HOME = "home"
    AUTO = "auto"
    EDUCATION = "education"
    BUSINESS = "business"
    GOLD = "gold"
    AGRICULTURAL = "agricultural"

class RepaymentFrequency(str, Enum):
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    ANNUALLY = "annually"
    ONE_TIME = "one_time"

class LoanStatus(str, Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    DEFAULTED = "defaulted"
    PENDING_APPROVAL = "pending_approval"
    REJECTED = "rejected"


