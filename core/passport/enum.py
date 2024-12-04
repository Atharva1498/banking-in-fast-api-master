from enum import Enum


class Country(str, Enum):
    INDIA = "India"
    USA = "USA"
    UK = "UK"
    CANADA = "Canada"
    AUSTRALIA = "Australia"
    RUSSIA ="Russia

class State(str, Enum):
    MAHARASHTRA = "Maharashtra"
    GUJARAT = "Gujarat"
    CALIFORNIA = "California"
    TEXAS = "Texas"

class City(str, Enum):
    MUMBAI = "Mumbai"
    PUNE = "Pune"
    NEW_YORK = "New York"
    LOS_ANGELES = "Los Angeles"
