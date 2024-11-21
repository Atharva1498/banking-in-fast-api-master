from tortoise import fields, models

class DrivingLicense(models.Model):
    id = fields.IntField(pk=True)
    license_number = fields.CharField(max_length=20, unique=True)
    name = fields.CharField(max_length=100)
    date_of_issue = fields.DateField()
    date_of_expiry = fields.DateField()
    dob = fields.DateField()  # Date of Birth of the license holder
    address = fields.TextField()
    vehicle_class = fields.CharField(max_length=50)  # Vehicle class/category

    class Meta:
        table = "driving_licenses"