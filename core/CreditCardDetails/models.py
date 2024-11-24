from tortoise import fields, models
from core.CreditCardDetails.enum import CardType, CardStatus

class CreditCardDetails(models.Model):
    id = fields.IntField(pk=True)
    credit_card_number = fields.CharField(max_length=16, unique=True)  # Unique card number
    cardholder_name = fields.CharField(max_length=100)
    expiry_date = fields.DateField()
    card_type = fields.CharEnumField(CardType, max_length=20)  # Credit or Debit
    card_status = fields.CharEnumField(CardStatus, max_length=20)  # Active, Blocked, Expired
    credit_limit = fields.FloatField()
    available_credit = fields.FloatField()
    credit_card_amount = fields.FloatField()  # Outstanding amount on the credit card
    type_of_credit_card = fields.CharField(max_length=50)  # E.g., Platinum, Gold, Basic
    issue_bank_name = fields.CharField(max_length=100)  # Bank that issued the card
    linked_bank_account_number = fields.CharField(max_length=20)  # Associated bank account
    registered_mobile_number = fields.CharField(max_length=15)  # Mobile number linked to the card
    registered_email = fields.CharField(max_length=100)  # Email linked to the card
    date_of_payment = fields.DateField()  # Payment due date
    date_of_bill_generation = fields.DateField()  # Bill generation date

    class Meta:
        table = "credit_card_details"
