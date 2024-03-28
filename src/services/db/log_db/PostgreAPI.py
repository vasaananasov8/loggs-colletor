import json
from abc import ABC, abstractmethod

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.services.db.log_db.tables import LogDbModul
from src.models.log_model import LogModel


class LogDBInterface(ABC):
    @abstractmethod
    async def insert_log(self, data):
        pass

    @abstractmethod
    async def get_logs(self, field_name, field_value):
        pass


class SQLAlchemyDatabase(LogDBInterface):
    def __init__(self, db_url: str):
        self.engine = create_async_engine(db_url)
        self.Session = sessionmaker(bind=self.engine, class_=AsyncSession)

    async def insert_log(self, data):
        async with self.Session() as session:
            async with session.begin():
                new_log = LogDbModul(**data)
                session.add(new_log)

    async def get_logs(self, field_name: str, field_value: str) -> str:
        async with self.Session() as session:
            async with session.begin():
                query = await session.execute(
                    select(LogDbModul).filter(
                        getattr(LogDbModul, field_name) == field_value
                    )
                )
                logs = query.scalars().all()
                log_models = [LogModel.from_orm(log) for log in logs]
                return json.dumps([log.json() for log in log_models])
