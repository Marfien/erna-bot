import peewee

from ernabot.model import BaseModel
from ernabot.model.party import Party


class Character(BaseModel):
    id = peewee.AutoField()
    party = peewee.ForeignKeyField(Party, on_delete="CASCADE")
    name = peewee.CharField()
    description = peewee.CharField()
    picture = peewee.BlobField(null=True)
    discord_user_id = peewee.UUIDField()

    class Meta(BaseModel.Meta):
        constraints = [
            peewee.SQL("UNIQUE(party,name)"),
            peewee.SQL("UNIQUE(party,discord_user_id)"),
        ]


class StatusEffect(BaseModel):
    id = peewee.AutoField()
    character = peewee.ForeignKeyField(model=Character, on_delete="CASCADE")
    description = peewee.CharField()
    applied_at = peewee.DateTimeField()
    extra = peewee.CharField()

    class Meta(BaseModel.Meta):
        constraints = [
            peewee.SQL("UNIQUE(character,description)"),
        ]


class InventoryItem(BaseModel):
    id = peewee.AutoField()
    character = peewee.ForeignKeyField(Character, on_delete="CASCADE")
    name = peewee.CharField()
    amount = peewee.IntegerField(default=1)

    class Meta(BaseModel.Meta):
        constraints = [peewee.SQL("UNIQUE(character,name)")]
