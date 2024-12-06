from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"


class AddressType(str, Enum):
    permanent = "permanent"
    temporary = "temporary"
