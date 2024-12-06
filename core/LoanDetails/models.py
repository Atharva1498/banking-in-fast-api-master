from tortoise import fields
from tortoise.models import Model
from core.LoanDetails.enum import LoanType


class LoanDetails(Model):
    id = fields.IntField(pk=True)
    borrower_name = fields.CharField(max_length=100)  
    sanction_date = fields.DateField() 
    loan_amount = fields.DecimalField(max_digits=12, decimal_places=2) 
    loan_tenure = fields.IntField()
    repayment_frequency = fields.CharField(max_length=20)  
    no_of_emi = fields.IntField()  
    emi_amount = fields.FloatField()
    loan_type = fields.CharEnumField(LoanType, max_length=50)
    current_pending_amount = fields.FloatField()
    date_of_emi = fields.DateField() 
    start_date = fields.DateField() 
    end_date = fields.DateField() 
    updated_at = fields.DatetimeField(auto_now=True)

    # Relations
    bank_detail = fields.ForeignKeyField(
        "models.BankDetails", related_name="loans"
    ) 
    person = fields.ForeignKeyField(
        "models.Person", related_name="loans", null=True
    ) 

    class Meta:
        table = "loan_details"
