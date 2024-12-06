from tortoise import fields, models


class LifeInsurance(models.Model):
    policy_number = fields.CharField(max_length=20, unique=True)
    policy_type = fields.CharField(max_length=50)
    coverage_amount = fields.DecimalField(max_digits=10, decimal_places=2)
    start_date = fields.DateField()
    end_date = fields.DateField()
    beneficiary_name = fields.CharField(max_length=100)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    # New foreign key to Person
    person = fields.ForeignKeyField("models.Person", related_name="life_insurance_policies", null=True)
