from abc import ABC, abstractmethod
from collections.abc import Callable
import os


class DatabaseConfig:
    username: str | None
    password: str | None
    host: str | None
    port: str | None
    database: str | None
    file: str | None


class Config(ABC):
    @property
    @abstractmethod
    def api_token(self) -> str:
        pass

    @property
    @abstractmethod
    def database(self) -> DatabaseConfig:
        pass


class EnvConfig(Config):
    def __init__(self) -> None:
        super().__init__()

        self._database = DatabaseConfig()
        self._database.username = os.getenv("ERNA_DB_USERNAME")
        self._database.password = os.getenv("ERNA_DB_PASSWORD")
        self._database.host = os.getenv("ERNA_DB_HOST")
        self._database.port = os.getenv("ERNA_DB_PORT")
        self._database.database = os.getenv("ERNA_DB_DATABASE")
        self._database.file = os.getenv("ERNA_DB_FILE")

    @property
    def api_token(self) -> str:
        token = os.getenv("ERNA_API_TOKEN")

        if token is None:
            raise Exception(
                "No API Token provided. Use ERNA_API_TOKEN environment variable to specify one."
            )

        return token

    @property
    def database(self) -> DatabaseConfig:
        return self._database


_config_types: dict[str, Callable[[], Config]] = {"environment": lambda: EnvConfig()}

selected: Config = _config_types[os.getenv("ERNA_CONFIG_TYPE", "environment")]()
