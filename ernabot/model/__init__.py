from typing import Type
import peewee

from ernabot.config import selected as config

database_proxy = peewee.DatabaseProxy()


class BaseModel(peewee.Model):
    class Meta:
        legacy_table_names = False
        database = database_proxy


def init(models: list[Type[BaseModel]]):
    db_config = config.database
    if (
        db_config.database
        and db_config.host
        and db_config.port
        and db_config.username
        and db_config.password
    ):
        database_proxy.initialize(
            peewee.PostgresqlDatabase(
                db_config.database,
                user=db_config.username,
                password=db_config.password,
                host=db_config.host,
                port=db_config.port,
            )
        )
    else:
        database_proxy.initialize(
            peewee.SqliteDatabase(
                db_config.file or "database.sqlite", pragmas=[("foreign_keys", "on")]
            )
        )

    with database_proxy.obj as db:
        if db.is_closed():
            print("Somethings wrong! Database connection could not be established.")
        else:
            print("Successfully connected to database.")
            db.create_tables(models)
            print(
                "Created tables:",
                ", ".join(map(lambda model: model._meta.table_name, models)),  # pyright: ignore
            )
