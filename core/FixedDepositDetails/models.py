from tortoise import fields, models
from core.FixedDepositDetails.enum import DepositType, DepositStatus
from core.bank.models import BankDetails  
from core.Person.models import Person  

class FixedDepositDetails(models.Model):
    id = fields.IntField(pk=True)
    depositor_name = fields.CharField(max_length=100)
    person = fields.ForeignKeyField("models.Person", related_name="fixed_deposits") 
    bank = fields.ForeignKeyField("models.BankDetails", related_name="fixed_deposits") 
    fixed_deposit_id = fields.CharField(max_length=20, unique=True)
    amount_invested = fields.FloatField()
    fixed_deposit_number = fields.CharField(max_length=20, unique=True)
    investment_duration = fields.IntField()
    rate_of_interest = fields.FloatField()
    maturity_amount = fields.FloatField()
    nominee_details = fields.CharField(max_length=255)
    nominee_percentage = fields.FloatField()
    deposit_type = fields.CharEnumField(DepositType, max_length=20)
    deposit_status = fields.CharEnumField(DepositStatus, max_length=20)
    start_date = fields.DateField()
    maturity_date = fields.DateField()

    class Meta:
        table = "fixed_deposit_details"
