from enum import Enum

class FundType(str, Enum):
    EQUITY = "Equity"
    DEBT = "Debt"
    HYBRID = "Hybrid"
    LIQUID = "Liquid"
    ETF = "ETF"

class PaymentOptions(str, Enum):
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    ANNUAL = "Annual"

class SipOrLumpsum(str, Enum):
    SIP = "SIP"
    LUMPSUM = "Lumpsum"
