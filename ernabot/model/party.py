from ernabot.model import BaseModel
import peewee


class Party(BaseModel):
    id = peewee.IdentityField()
    name = peewee.CharField()
    channel_id = peewee.UUIDField()
    dungeon_master_id = peewee.UUIDField()
