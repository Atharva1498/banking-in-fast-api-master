from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application configuration settings."""
    # General app settings
    APP_NAME: str = "FastAPI App"
    ENV: str = "development"  # Can be 'development', 'staging', or 'production'
    DEBUG: bool = True  # Enable or disable debug mode

    # Database configuration
    DATABASE_URL: str = "postgres://admin:admin@postgres:5432/bank_db"  # Default for Docker
    DB_ECHO: bool = False  # Enable SQL query logging if True
    DB_CONNECTION_LIMIT: int = 10  # Optional: Limit connection pool size

    # You can add other configuration fields as needed

    class Config:
        """Meta-configuration for BaseSettings."""
        env_file = ".env"  # Automatically loads variables from .env file
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings():
    """Return the cached settings instance."""
    return Settings()

# Global settings instance
settings = get_settings()
