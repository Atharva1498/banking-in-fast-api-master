from tortoise import fields, models
from core.CreditorDebitor.enum import CreditorType, DebitorType, PaymentStatus


class Creditor(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255) 
    amount = fields.FloatField()  
    received_date = fields.DateField() 
    rate_of_interest = fields.FloatField() 
    return_on_investment = fields.FloatField()
    retail_promise = fields.CharField(max_length=255) 
    remark = fields.TextField(null=True) 
    creditor_type = fields.CharEnumField(CreditorType, max_length=20)
    payment_status = fields.CharEnumField(PaymentStatus, max_length=20) 

    class Meta:
        table = "creditor"


class Debitor(models.Model):
    id = fields.IntField(pk=True) 
    name = fields.CharField(max_length=255) 
    amount = fields.FloatField()  
    received_date = fields.DateField() 
    rate_of_interest = fields.FloatField()  
    return_on_investment = fields.FloatField()  
    retail_promise = fields.CharField(max_length=255) 
    remark = fields.TextField(null=True) 
    debitor_type = fields.CharEnumField(DebitorType, max_length=20) 
    payment_status = fields.CharEnumField(PaymentStatus, max_length=20) 

    class Meta:
        table = "debitor" 
