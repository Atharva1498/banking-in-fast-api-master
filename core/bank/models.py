from tortoise.models import Model
from tortoise import fields
from core.bank.enum import AccountType


class Person(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)


class BankDetails(Model):
    id = fields.IntField(pk=True)
    bank_name = fields.CharField(max_length=255)
    branch_address = fields.TextField(null=True)
    account_holder_name = fields.CharField(max_length=100)  # Added Account Holder Name
    account_number = fields.CharField(max_length=50)
    account_type = fields.CharEnumField(AccountType)
    branch_ifsc_code = fields.CharField(max_length=20, null=True)
    bank_micr_code = fields.CharField(max_length=20, null=True)
    cheque_book_issued_date = fields.DateField(null=True)
    netbanking_id = fields.CharField(max_length=100, null=True)
    registered_email = fields.CharField(max_length=100, null=True)
    registered_mobile = fields.CharField(max_length=15, null=True)
    bank_helpline_number = fields.CharField(max_length=15, null=True)
    bank_helpline_email = fields.CharField(max_length=100, null=True)
    relationship_manager_name = fields.CharField(max_length=100, null=True)
    relationship_manager_email = fields.CharField(max_length=100, null=True)
    relationship_manager_mobile = fields.CharField(max_length=15, null=True)

    # Relations
    user = fields.ForeignKeyField("models.User", related_name="bank_details")
    person = fields.ForeignKeyField("models.Person", related_name="bank_details", null=True)  # Foreign key to Person

    class Meta:
        unique_together = (("account_number", "user"),)


class CreditCardDetails(Model):
    id = fields.IntField(pk=True)
    card_number = fields.CharField(max_length=16, unique=True)  # Card Number
    expiry_date = fields.DateField()  # Expiry Date
    cardholder_name = fields.CharField(max_length=100)  # Name on Card
    bank_detail = fields.ForeignKeyField("models.BankDetails", related_name="credit_cards")  # Relation to Bank Details


class DebitCardDetails(Model):
    id = fields.IntField(pk=True)
    card_number = fields.CharField(max_length=16, unique=True)  # Card Number
    expiry_date = fields.DateField()  # Expiry Date
    cardholder_name = fields.CharField(max_length=100)  # Name on Card
    bank_detail = fields.ForeignKeyField("models.BankDetails", related_name="debit_cards")  # Relation to Bank Details
