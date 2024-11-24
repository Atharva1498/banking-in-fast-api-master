from pydantic import BaseModel
from datetime import datetime
from core.PersonBankDepositorConnection.enum import ConnectionType, ConnectionStatus  # Import enums

class ConnectionCreate(BaseModel):
    person_id: int
    bank_id: int
    depositor_id: int
    connection_type: ConnectionType  # Enum for Connection Type
    connection_status: ConnectionStatus  # Enum for Connection Status

class ConnectionResponse(BaseModel):
    id: int
    person_id: int
    bank_id: int
    depositor_id: int
    connection_type: ConnectionType
    connection_status: ConnectionStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
