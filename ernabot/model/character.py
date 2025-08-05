import peewee

from ernabot.model import BaseModel
from ernabot.model.party import Party


class Character(BaseModel):
    id = peewee.IdentityField()
    party = peewee.ForeignKeyField(Party)
    name = peewee.CharField(unique=True)
    description = peewee.CharField()
    picture = peewee.BlobField()
    inventory = None
    discord_user_id = peewee.UUIDField()


class StatusEffect(BaseModel):
    id = peewee.IdentityField()
    character = peewee.ForeignKeyField(Character)
    description = peewee.CharField()
    applied_at = peewee.DateTimeField()
    extra = peewee.CharField()


class InventoryItem(BaseModel):
    id = peewee.IdentityField()
    character = peewee.ForeignKeyField(Character)
    name = peewee.CharField()
    amount = peewee.IntegerField(default=1)
