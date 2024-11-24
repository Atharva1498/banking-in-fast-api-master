from tortoise import fields, models
from core.PersonBankDepositorConnection.enum import ConnectionType, ConnectionStatus  # Import enums

class PersonBankDepositorConnection(models.Model):
    id = fields.IntField(pk=True)  # Primary key
    person_id = fields.ForeignKeyField(
        "models.PersonDetails", related_name="person_connections"
    )  # Foreign key to PersonDetails
    bank_id = fields.ForeignKeyField(
        "models.BankDetails", related_name="bank_connections"
    )  # Foreign key to BankDetails
    depositor_id = fields.ForeignKeyField(
        "models.DepositorDetails", related_name="depositor_connections"
    )  # Foreign key to DepositorDetails
    connection_type = fields.CharEnumField(ConnectionType, max_length=20)  # Connection type
    connection_status = fields.CharEnumField(ConnectionStatus, max_length=20)  # Connection status
    created_at = fields.DatetimeField(auto_now_add=True)  # Record creation timestamp
    updated_at = fields.DatetimeField(auto_now=True)  # Record update timestamp

    class Meta:
        table = "person_bank_depositor_connection"
