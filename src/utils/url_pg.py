import src.utils.config as cfg


def get_url() -> str:
    """
    A function for generating the URL of the PostgreSQL database.

    :return: The URL string for connecting to the database.
    """
    url = f"postgresql+asyncpg://{cfg.USERNAME_DB}:{cfg.PASSWORD_DB}@{cfg.HOST_DB}:{cfg.PORT_DB}/{cfg.DATABASE_NAME}"
    return url
