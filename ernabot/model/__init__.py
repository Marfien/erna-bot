from collections.abc import Callable
from peewee import Database, Model
import peewee

from ernabot import config
from ernabot.model.character import Character, InventoryItem, StatusEffect
from ernabot.model.party import Party

# TODO different database types configurable
db = peewee.SqliteDatabase(config.selected.database.file)

# TODO init tables


class BaseModel(Model):
    class Meta:
        database = db
