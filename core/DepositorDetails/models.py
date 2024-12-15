from tortoise import fields, models
from core.DepositorDetails.enum import DepositType
from core.bank.models import BankDetails  # Import BankDetails model
from core.Person.models import Person  # Import Person model

class DepositorDetails(models.Model):
    id = fields.IntField(pk=True)
    depositor_name = fields.CharField(max_length=100)
    person = fields.ForeignKeyField("models.Person", related_name="depositors")  
    contact_number = fields.CharField(max_length=15)
    email = fields.CharField(max_length=100)
    address = fields.TextField()
    amount_invested = fields.FloatField()
    roi = fields.FloatField()
    deposit_type = fields.CharEnumField(DepositType, max_length=20)
    invested_date = fields.DateField()
    maturity_date = fields.DateField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "depositor_details"
