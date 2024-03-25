import datetime

from sqlalchemy import ForeignKey, func, MetaData
from sqlalchemy.orm import mapped_column, Mapped, as_declarative, declared_attr

from src.models.log_model import LogLevel


@as_declarative()
class AbstractModul:
    metadata = MetaData()

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class LogDbModul(AbstractModul):
    __tablename__ = "log"
    app_name: Mapped[str]
    module: Mapped[str]
    level: Mapped[LogLevel]
    timestamp: Mapped[datetime.datetime] = mapped_column(insert_default=func.now)
    # timestamp: Mapped[datetime] = mapped_column(insert_default=text("TIMEZONE('utc', now())"))
    message: Mapped[str]
