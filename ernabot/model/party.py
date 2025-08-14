from ernabot.model import BaseModel
import peewee


class Party(BaseModel):
    # One party per channel
    channel_id = peewee.UUIDField(primary_key=True)
    name = peewee.CharField()
    dungeon_master_id = peewee.UUIDField()
