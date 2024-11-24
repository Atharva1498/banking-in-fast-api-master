from tortoise import fields, models

class LoanDetails(models.Model):
    loan_id = fields.CharField(max_length=20, unique=True)  # Unique identifier for the loan
    borrower_name = fields.CharField(max_length=100)  # Name of the person who took the loan
    loan_type = fields.CharField(max_length=50)  # Type of loan (e.g., Home, Personal, Auto)
    loan_amount = fields.DecimalField(max_digits=12, decimal_places=2)  # Amount of the loan
    interest_rate = fields.DecimalField(max_digits=5, decimal_places=2)  # Interest rate in percentage
    tenure = fields.IntField()  # Tenure of the loan in months
    repayment_frequency = fields.CharField(max_length=20)  # Frequency of repayment (e.g., Monthly, Quarterly)
    loan_status = fields.CharField(max_length=20)  # Status of the loan (e.g., Active, Closed, Defaulted)
    start_date = fields.DateField()  # Start date of the loan
    end_date = fields.DateField()  # End date of the loan
    created_at = fields.DatetimeField(auto_now_add=True)  # Auto-generated creation timestamp
    updated_at = fields.DatetimeField(auto_now=True)  # Auto-generated update timestamp
