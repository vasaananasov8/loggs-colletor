#  docs: https://juby.atlassian.net/wiki/spaces/FTB/pages/26837024/Routers+models
from enum import Enum

from pydantic import BaseModel
from datetime import datetime


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class LogModel(BaseModel):
    """Data model for logs."""

    app_name: str
    module: str
    level: LogLevel
    timestamp: datetime
    message: str

    class Config:
        from_attributes = True  # This is necessary for from_orm to work
