from tortoise import fields, models
from core.CreditorDebitor.enum import CreditorType, DebitorType, PaymentStatus


class Creditor(models.Model):
    id = fields.IntField(pk=True)  # Primary key
    name = fields.CharField(max_length=255)  # Name of the creditor
    amount = fields.FloatField()  # Amount given
    received_date = fields.DateField()  # Date the amount was received
    rate_of_interest = fields.FloatField()  # Interest rate
    return_on_investment = fields.FloatField()  # Return on investment
    retail_promise = fields.CharField(max_length=255)  # Retail promise description
    remark = fields.TextField(null=True)  # Any additional remarks
    creditor_type = fields.CharEnumField(CreditorType, max_length=20)  # Creditor type
    payment_status = fields.CharEnumField(PaymentStatus, max_length=20)  # Payment status

    class Meta:
        table = "creditor"  # Table name in the database


class Debitor(models.Model):
    id = fields.IntField(pk=True)  # Primary key
    name = fields.CharField(max_length=255)  # Name of the debitor
    amount = fields.FloatField()  # Amount borrowed
    received_date = fields.DateField()  # Date the amount was borrowed
    rate_of_interest = fields.FloatField()  # Interest rate
    return_on_investment = fields.FloatField()  # Return on investment
    retail_promise = fields.CharField(max_length=255)  # Retail promise description
    remark = fields.TextField(null=True)  # Any additional remarks
    debitor_type = fields.CharEnumField(DebitorType, max_length=20)  # Debitor type
    payment_status = fields.CharEnumField(PaymentStatus, max_length=20)  # Payment status

    class Meta:
        table = "debitor"  # Table name in the database
