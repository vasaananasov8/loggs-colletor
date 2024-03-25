import asyncio
import datetime

from src.services.db.log_db.PostgreAPI import SQLAlchemyDatabase
from src.utils.config import DB_URL


async def main():
    db = SQLAlchemyDatabase(DB_URL)

    # Данные для вставки в базу данных
    log_data = {
        "app_name": "my_app",
        "module": "new",
        "level": "INFO",
        "timestamp": datetime.datetime.strptime(
            "2024-03-20 12:00:00", "%Y-%m-%d %H:%M:%S"
        ),
        "message": "This is a test log message.",
    }

    # Вставляем запись в базу данных
    await db.insert_log(log_data)

    # Получаем все записи из базы данных для модуля "my_module"
    logs = await db.get_log_by_model("my_module")

    # Выводим полученные записи
    print(logs)


if __name__ == "__main__":
    asyncio.run(main())
