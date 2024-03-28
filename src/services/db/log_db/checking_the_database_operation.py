import asyncio
import datetime

from src.services.db.log_db.PostgreAPI import SQLAlchemyDatabase
from src.utils.url_pg import get_url


async def main():
    # PostgreSQL url
    url = get_url()
    db = SQLAlchemyDatabase(url)

    # Data to insert into the database
    log_data = {
        "app_name": "my_app",
        "module": "new",
        "level": "INFO",
        "timestamp": datetime.datetime.now(),
        "message": "This is a test log message.",
    }

    # Insert log's into the database
    await db.insert_log(log_data)

    # Getting all log's from the database for the "new" module
    logs = await db.get_logs("module", "new")

    # Printing the log's
    print(logs)


if __name__ == "__main__":
    asyncio.run(main())
