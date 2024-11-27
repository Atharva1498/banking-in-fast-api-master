from tortoise import fields, models
from core.GoldDetails.enum import JewelryType, GoldType  # Import enums

class GoldDetails(models.Model):
    id = fields.IntField(pk=True)  # Primary key
    jewelry_type = fields.CharEnumField(JewelryType, max_length=50)  # Jewelry type (ring, necklace, etc.)
    gold_type = fields.CharEnumField(GoldType, max_length=50)  # Type of gold (24K, 22K, etc.)
    purchase_date = fields.DateField()  # Purchase date
    weight = fields.FloatField()  # Weight of the gold in grams
    purchase_price = fields.FloatField()  # Purchase price in local currency
    purchase_shop = fields.CharField(max_length=255)  # Name of the shop where purchased

    class Meta:
        table = "gold_details"  # Table name in the database
