from tortoise import fields, models
from core.FixedDepositDetails.enum import DepositType, DepositStatus  # Import enums

class FixedDepositDetails(models.Model):
    id = fields.IntField(pk=True)  # Primary key for Fixed Deposit
    depositor_name = fields.CharField(max_length=100)  # Name of the depositor
    person_id = fields.IntField()  # Person's unique ID
    bank_id = fields.IntField()  # Bank's unique ID
    fixed_deposit_id = fields.CharField(max_length=20, unique=True)  # Unique Fixed Deposit ID
    amount_invested = fields.FloatField()  # Amount invested in the fixed deposit
    fixed_deposit_number = fields.CharField(max_length=20, unique=True)  # Unique FD number
    investment_duration = fields.IntField()  # Duration in months or years
    rate_of_interest = fields.FloatField()  # Rate of interest
    maturity_amount = fields.FloatField()  # Amount at maturity
    nominee_details = fields.CharField(max_length=255)  # Nominee details
    nominee_percentage = fields.FloatField()  # Percentage of FD the nominee can own
    deposit_type = fields.CharEnumField(DepositType, max_length=20)  # Type of Fixed Deposit
    deposit_status = fields.CharEnumField(DepositStatus, max_length=20)  # Status (Active, Matured, Closed)
    start_date = fields.DateField()  # Start date of the FD
    maturity_date = fields.DateField()  # Maturity date of the FD

    class Meta:
        table = "fixed_deposit_details"

