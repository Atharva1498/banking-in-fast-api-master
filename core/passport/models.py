from tortoise import fields
from tortoise.models import Model


class PassportDetails(Model):
    id = fields.IntField(pk=True)
    passport_number = fields.CharField(max_length=20, unique=True)
    date_of_issue = fields.DateField()
    date_of_expiry = fields.DateField()

    # Place_of_issue
    country = fields.CharField(max_length=100)
    state = fields.CharField(max_length=100)
    city = fields.CharField(max_length=100)
    zip_code = fields.CharField(max_length=20)

    person = fields.ForeignKeyField("models.Person", related_name="passports")

    class Meta:
        table = "passport_details"
