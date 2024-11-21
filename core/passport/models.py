from tortoise import fields
from tortoise.models import Model

class PassportDetails(Model):
    id = fields.IntField(pk=True)
    passport_number = fields.CharField(max_length=20, unique=True)
    date_of_issue = fields.DateField()
    date_of_expiry = fields.DateField()
    place_of_issue = fields.CharField(max_length=255)
    user = fields.ForeignKeyField("models.User", related_name="passports")

    class Meta:
        table = "passport_details"
