from enum import Enum

# Optional enum for share types (Equity, Preferred, etc.)
class ShareType(str, Enum):
    EQUITY = "Equity"
    PREFERRED = "Preferred"
    PREFERENCE = "Preference"
