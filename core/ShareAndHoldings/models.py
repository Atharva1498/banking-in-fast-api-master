from tortoise import fields, models
from core.ShareAndHoldings.enum import ShareType  # Import enum if needed

class ShareAndHoldings(models.Model):
    id = fields.IntField(pk=True)  # Primary key
    company_name = fields.CharField(max_length=255)  # Company name
    total_shares = fields.IntField()  # Total number of shares
    shares_owned = fields.IntField()  # Number of shares owned
    purchase_date = fields.DateField()  # Date of purchase
    purchase_rate = fields.FloatField()  # Purchase rate per share
    purchase_cost = fields.FloatField()  # Total cost of purchase
    demat_account_number = fields.CharField(max_length=255)  # Demat account number
    current_market_cost = fields.FloatField()  # Current market cost per share
    share_type = fields.CharEnumField(ShareType, max_length=50, null=True)  # Optional: Type of share

    class Meta:
        table = "share_and_holdings"  # Table name in the database
