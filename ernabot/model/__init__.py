from peewee import Model
import peewee

from ernabot import config

# TODO different database types configurable
db = peewee.SqliteDatabase(config.selected.database.file)


class BaseModel(Model):
    class Meta:
        database = db
