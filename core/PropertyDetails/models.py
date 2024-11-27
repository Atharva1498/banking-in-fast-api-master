from tortoise import fields, models
from core.PropertyDetails.enum import PropertyLandType, PropertyMortgageStatus  # Import enums

class PropertyDetails(models.Model):
    id = fields.IntField(pk=True)  # Primary key
    property_owner_name = fields.CharField(max_length=255)  # Name of property owner
    area = fields.FloatField()  # Area of the property in square meters
    land_type = fields.CharEnumField(PropertyLandType, max_length=50)  # Type of land
    registration_number = fields.CharField(max_length=255)  # Registration number of land
    purchase_cost = fields.FloatField()  # Cost of purchasing the land
    broker_name = fields.CharField(max_length=255)  # Broker's name
    broker_mobile = fields.CharField(max_length=15)  # Broker's mobile number
    broker_email = fields.CharField(max_length=255)  # Broker's email address
    mortgage_status = fields.CharEnumField(PropertyMortgageStatus, max_length=20)  # Whether property is mortgaged
    bank_name = fields.CharField(max_length=255, null=True)  # Bank name (if mortgaged)
    loan_amount = fields.FloatField(null=True)  # Loan amount (if mortgaged)
    bank_valuation = fields.FloatField(null=True)  # Property valuation by bank
    property_tax_last_payment = fields.DateField(null=True)  # Last payment date of property tax
    property_nominee = fields.CharField(max_length=255)  # Nominee name

    class Meta:
        table = "property_details"  # Table name in the database
