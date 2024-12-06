from tortoise import fields
from tortoise.models import Model
from core.Person.models import Person  
from core.bank.models import BankDetails  

class MutualFund(Model):
    id = fields.IntField(pk=True)
    deposit_holder_name = fields.CharField(max_length=255)
    mutual_fund_company = fields.CharField(max_length=255)
    amount = fields.DecimalField(max_digits=12, decimal_places=2)
    scheme_name = fields.CharField(max_length=255)
    folio_number = fields.CharField(max_length=50)
    fund_type = fields.CharField(max_length=100)
    payment_options = fields.CharField(max_length=50)
    sip_or_lumpsum = fields.CharField(max_length=50)
    sip_tenure = fields.IntField()  # In months
    maturity_date = fields.DateField()
    customer_portal_login_id = fields.CharField(max_length=100)
    nominee_name = fields.CharField(max_length=255)
    agent_cellphone_number = fields.CharField(max_length=15)
    company_contract_number = fields.CharField(max_length=50)
    company_helpdesk_number = fields.CharField(max_length=20)
    company_helpdesk_email = fields.CharField(max_length=100)

    # Relations
    person = fields.ForeignKeyField("models.Person", related_name="mutual_funds", null=True)
    bank_detail = fields.ForeignKeyField("models.BankDetails", related_name="mutual_funds", null=True)

    class Meta:
        table = "mutual_funds"
