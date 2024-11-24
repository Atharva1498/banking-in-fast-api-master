from fastapi import APIRouter, HTTPException
from typing import List
from core.PersonBankDepositorConnection.models import PersonBankDepositorConnection
from core.PersonBankDepositorConnection.schemas import ConnectionCreate, ConnectionResponse

router = APIRouter()

# Create a new connection
@router.post("/connections", response_model=ConnectionResponse)
async def create_connection(data: ConnectionCreate):
    try:
        connection = await PersonBankDepositorConnection.create(**data.dict())
        return connection
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Get list of all connections
@router.get("/connections", response_model=List[ConnectionResponse])
async def list_connections():
    try:
        connections = await PersonBankDepositorConnection.all()
        return connections
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get a specific connection by ID
@router.get("/connections/{connection_id}", response_model=ConnectionResponse)
async def get_connection(connection_id: int):
    connection = await PersonBankDepositorConnection.filter(id=connection_id).first()
    if not connection:
        raise HTTPException(status_code=404, detail="Connection not found")
    return connection

# Update a specific connection by ID
@router.put("/connections/{connection_id}", response_model=ConnectionResponse)
async def update_connection(connection_id: int, data: ConnectionCreate):
    connection = await PersonBankDepositorConnection.filter(id=connection_id).first()
    if not connection:
        raise HTTPException(status_code=404, detail="Connection not found")
    await connection.update_from_dict(data.dict()).save()
    return connection

# Delete a specific connection by ID
@router.delete("/connections/{connection_id}")
async def delete_connection(connection_id: int):
    connection = await PersonBankDepositorConnection.filter(id=connection_id).first()
    if not connection:
        raise HTTPException(status_code=404, detail="Connection not found")
    await connection.delete()
    return {"message": "Connection deleted successfully"}
