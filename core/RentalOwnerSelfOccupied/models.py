from tortoise import fields, models
from core.RentalOwnerSelfOccupied.enum import PropertyStatus

class RentalOwnerSelfOccupied(models.Model):
    id = fields.IntField(pk=True)  # Primary key
    property_status = fields.CharEnumField(PropertyStatus, max_length=50)  # Rent, Owned, Self-Occupied
    rent_per_month = fields.FloatField(null=True)  # Rent per month (if rented)
    rented_person_name = fields.CharField(max_length=255, null=True)  # Name of rented person (if rented)
    rented_person_email = fields.CharField(max_length=255, null=True)  # Email of rented person
    rented_person_mobile = fields.CharField(max_length=15, null=True)  # Mobile number of rented person
    bank_ifsc_code = fields.CharField(max_length=11, null=True)  # Bank IFSC code (if rented)
    bank_account_number = fields.CharField(max_length=20, null=True)  # Bank account number (if rented)
    rent_agreement_details = fields.TextField(null=True)  # Rent agreement details (if rented)
    rent_deposit = fields.FloatField(null=True)  # Rent deposit (if rented)
    owner_name = fields.CharField(max_length=255)  # Name of the property owner (if owned/self-occupied)
    self_occupied_details = fields.TextField(null=True)  # Self-occupied property details (if self-occupied)
    
    class Meta:
        table = "rental_owner_self_occupied"  # Table name in the database
