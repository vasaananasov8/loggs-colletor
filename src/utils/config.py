import os
from typing import Final

from dotenv import load_dotenv

from src.utils.exeptions.configurate_exceptions import EnvDependNotFound

load_dotenv()


def get_env_var(var_name: str) -> str:
    """
    :raise EnvDependNotFound if value in None
    :param var_name: Env var name
    :return: Var value by name
    """
    value: str | None = os.getenv(var_name)
    if value is None:
        raise EnvDependNotFound(var_name)
    else:
        return value


APP_HOST: Final[str] = get_env_var("APP_HOST")
KAFKA_HOST: Final[str] = get_env_var("KAFKA_HOST")
APP_PORT: Final[int] = int(get_env_var("APP_PORT"))
KAFKA_PORT: Final[int] = int(get_env_var("KAFKA_PORT"))
KAFKA_TOPIC_NAME: Final[str] = get_env_var("KAFKA_TOPIC_NAME")
USERNAME_DB: Final[str] = get_env_var("USERNAME_DB")
HOST_DB: Final[str] = get_env_var("HOST_DB")
PASSWORD_DB: Final[str] = get_env_var("PASSWORD_DB")
DATABASE_NAME: Final[str] = get_env_var("DATABASE_NAME")
PORT_DB: Final[str] = get_env_var("PORT_DB")
