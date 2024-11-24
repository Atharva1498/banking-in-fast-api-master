from enum import Enum

class ConnectionType(str, Enum):
    PRIMARY = "primary"  # Primary connection
    SECONDARY = "secondary"  # Secondary connection
    JOINT = "joint"  # Joint account connection

class ConnectionStatus(str, Enum):
    ACTIVE = "active"  # Active connection
    INACTIVE = "inactive"  # Inactive connection
    PENDING = "pending"  # Pending approval
    TERMINATED = "terminated"  # Connection has been terminated


