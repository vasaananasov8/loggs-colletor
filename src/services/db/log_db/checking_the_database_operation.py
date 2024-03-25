import asyncio

from sqlalchemy import URL

from src.services.db.log_db.PostgreAPI import SQLAlchemyDatabase, url_p


db = SQLAlchemyDatabase(url_p)
# Данные для вставки в базу данных
log_data = {
    "app_name": "my_app",
    "module": "my_module",
    "level": "DEBUG",
    "timestamp": "2024-03-20 12:00:00",
    "message": "This is a test log message."
}

# Вставляем запись в базу данных
asyncio.run(db.insert_log(log_data))

# Получаем все записи из базы данных для модуля "my_module"
logs = asyncio.run(db.get_log_by_model("my_module"))

# Выводим полученные записи
print(logs)
