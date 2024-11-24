from tortoise import fields, models
from core.DepositorDetails.enum import DepositType  # Import DepositType enum

class DepositorDetails(models.Model):
    id = fields.IntField(pk=True)  # Unique Depositor ID
    depositor_name = fields.CharField(max_length=100)  # Name of the depositor
    person_id = fields.ForeignKeyField(
        "models.PersonDetails", related_name="depositors"
    )  # Foreign key to PersonDetails model
    contact_number = fields.CharField(max_length=15)  # Contact number
    email = fields.CharField(max_length=100)  # Email address
    address = fields.TextField()  # Address of the depositor
    amount_invested = fields.FloatField()  # Amount invested
    roi = fields.FloatField()  # Rate of Interest in percentage
    deposit_type = fields.CharEnumField(DepositType, max_length=20)  # Deposit type
    invested_date = fields.DateField()  # Date of investment
    maturity_date = fields.DateField()  # Date of maturity
    created_at = fields.DatetimeField(auto_now_add=True)  # Record creation timestamp
    updated_at = fields.DatetimeField(auto_now=True)  # Record update timestamp

    class Meta:
        table = "depositor_details"




