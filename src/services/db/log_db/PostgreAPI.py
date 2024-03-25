from abc import ABC, abstractmethod

from sqlalchemy import select, URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.services.db.log_db.tables import LogDbModul
from src.utils import config


class LogDBInterface(ABC):
    @abstractmethod
    async def insert_log(self, data):
        pass

    @abstractmethod
    async def get_log_by_model(self, module):
        pass


class SQLAlchemyDatabase(LogDBInterface):
    def __init__(self, db_url):
        self.engine = create_async_engine(db_url)
        self.Session = sessionmaker(bind=self.engine, class_=AsyncSession)

    async def insert_log(self, data):
        async with self.Session() as session:
            async with session.begin():
                new_log = LogDbModul(**data)
                session.add(new_log)

    async def get_log_by_model(self, module):
        async with self.Session() as session:
            async with session.begin():
                query = select(LogDbModul).where(LogDbModul.module == module)
                result = await session.execute(query)
                logs = []
                for row in result.fetchall():
                    log = row[0]
                    log_str = f"Log id: {log.id} -> {log.app_name}, {log.module}, {log.level}, {log.timestamp}, {log.message}"
                    logs.append(log_str)
                return logs
