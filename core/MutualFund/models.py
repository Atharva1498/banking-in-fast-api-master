from tortoise import fields, models
from core.MutualFund.enum import FundType, PaymentOptions, SipOrLumpsum  # Import enums

class MutualFund(models.Model):
    id = fields.IntField(pk=True)  # Primary key
    deposit_holder_name = fields.CharField(max_length=255)  # Deposit holder's name
    mutual_fund_company = fields.CharField(max_length=255)  # Mutual fund company
    amount = fields.FloatField()  # Amount invested
    scheme_name = fields.CharField(max_length=255)  # Scheme name
    folio_number = fields.CharField(max_length=50)  # Folio number
    fund_type = fields.CharEnumField(FundType, max_length=50)  # Fund type (Equity, Debt, etc.)
    payment_option = fields.CharEnumField(PaymentOptions, max_length=20)  # Payment options (Monthly, Quarterly, etc.)
    sip_or_lumpsum = fields.CharEnumField(SipOrLumpsum, max_length=20)  # SIP or Lump Sum
    sip_tenure = fields.IntField(null=True)  # SIP tenure (if SIP is chosen)
    maturity_date = fields.DateField()  # Maturity date
    bank_details = fields.TextField()  # Bank details for ECS/SI
    customer_portal_login_id = fields.CharField(max_length=255)  # Customer portal login ID
    nominee_name = fields.CharField(max_length=255)  # Nominee name
    agent_cellphone_number = fields.CharField(max_length=15)  # Agent's cellphone number
    company_contract_number = fields.CharField(max_length=50)  # Company contract number
    company_helpdesk_number = fields.CharField(max_length=15)  # Company help desk number
    company_helpdesk_email = fields.CharField(max_length=255)  # Company help desk email

    class Meta:
        table = "mutual_fund_details"  # Table name in the database
