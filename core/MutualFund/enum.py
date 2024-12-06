from enum import Enum

class FundType(str, Enum):
    EQUITY = "equity"
    DEBT = "debt"
    HYBRID = "hybrid"
    ETF = "ETF"

class SIPOrLumpsum(str, Enum):
    SIP = "sip"
    LUMPSUM = "lumpsum"
