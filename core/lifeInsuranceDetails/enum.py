# core/insurance/enum.py

from enum import Enum

class LifeInsuranceType(str, Enum):
    TERM = "term"
    WHOLE_LIFE = "whole_life"
    UNIVERSAL_LIFE = "universal_life"
    VARIABLE_LIFE = "variable_life"
    FINAL_EXPENSE = "final_expense"
    GROUP_LIFE = "group_life"

class BeneficiaryRelation(str, Enum):
    SPOUSE = "spouse"
    CHILD = "child"
    PARENT = "parent"
    SIBLING = "sibling"
    OTHER = "other"
