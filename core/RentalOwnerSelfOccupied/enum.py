from enum import Enum

class PropertyStatus(str, Enum):
    RENTED = "Rented"
    OWNED = "Owned"
    SELF_OCCUPIED = "Self-Occupied"
