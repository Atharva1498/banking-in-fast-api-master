from tortoise.models import Model
from tortoise import fields
from core.LoanDetails.enum import LoanType


class LoanDetails(Model):
    id = fields.IntField(pk=True)
    borrower_name = fields.CharField(max_length=100)  # Name of the person who took the loan
    sanction_date = fields.DateField()  # Sanction date of the loan
    loan_amount = fields.DecimalField(max_digits=12, decimal_places=2)  # Amount of the loan
    loan_tenure = fields.IntField()  # Loan tenure in months
    
    repayment_frequency = fields.CharField(max_length=20)  # Frequency of repayment (e.g., Monthly, Quarterly)
    no_of_emi = fields.IntField()  # Number of EMIs
    emi_amount = fields.FloatField()  # EMI amount
    loan_type = fields.CharEnumField(LoanType, max_length=50)  # Loan type (Enum)
    current_pending_amount = fields.FloatField()  # Current pending loan amount
    date_of_emi = fields.DateField()  # Date of EMI payment
    start_date = fields.DateField()  # Start date of the loan
    end_date = fields.DateField()  # End date of the loan
    updated_at = fields.DatetimeField(auto_now=True) 

    # Relations
    bank_detail = fields.ForeignKeyField(
        "models.BankDetails", related_name="loans"
    )  # Link to the bank
    person = fields.ForeignKeyField(
        "models.Person", related_name="loans", null=True
    )  # Link to the person (optional)

    class Meta:
        table = "loan_details"

    
    
    