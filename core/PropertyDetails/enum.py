from enum import Enum

class PropertyLandType(str, Enum):
    AGRICULTURAL = "Agricultural"
    COMMERCIAL = "Commercial"
    RESIDENTIAL = "Residential"
    INDUSTRIAL = "Industrial"

class PropertyMortgageStatus(str, Enum):
    MORTGAGED = "Mortgaged"
    NOT_MORTGAGED = "Not Mortgaged"
