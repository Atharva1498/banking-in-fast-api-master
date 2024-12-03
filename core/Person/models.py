from tortoise.models import Model
from tortoise import fields
from core.Person.enum import Gender, AddressType

class Person(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50)
    middle_name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50)
    dob = fields.DateField()
    phone_number = fields.CharField(max_length=15, unique=True)
    email = fields.CharField(max_length=100, unique=True, null=True)
    aadhar_card_number = fields.CharField(max_length=12, unique=True, null=True)
    pan_card_number = fields.CharField(max_length=10, unique=True, null=True)

    # Relations
    addresses = fields.ReverseRelation["Address"]
    family_members = fields.ReverseRelation["FamilyDetails"]

    class Meta:
        table = "person"

class Address(Model):
    id = fields.IntField(pk=True)
    street = fields.CharField(max_length=255)
    city = fields.CharField(max_length=100)
    state = fields.CharField(max_length=100)
    zip_code = fields.CharField(max_length=20)
    address_type = fields.CharEnumField(AddressType)  # Permanent/Temporary

    # Foreign key relation
    person = fields.ForeignKeyField("models.Person", related_name="addresses")

    class Meta:
        table = "address"

class FamilyDetails(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    relationship = fields.CharField(max_length=50)
    birthdate = fields.DateField()
    gender = fields.CharEnumField(Gender)
    phone_number = fields.CharField(max_length=15, unique=True)
    email = fields.CharField(max_length=100, unique=True, null=True)
    # Foreign key relation
    person = fields.ForeignKeyField("models.Person", related_name="family_members")

    class Meta:
        table = "family_details"
