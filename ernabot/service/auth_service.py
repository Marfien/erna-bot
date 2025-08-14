from ernabot.exception import PartyNotFoundException
from ernabot.model.character import Character
from ernabot.model.party import Party


def is_member(channel_id: str, user_id: str) -> bool:
    party = Party.select().where(Party.channel_id == channel_id)

    if party is None:
        raise PartyNotFoundException(channel_id)

    return Character.select(Character.id).where(Character.party == party).exists()


def is_dungeon_master(channel_id: str, user_id: str) -> bool:
    party = Party.select(Party.dungeon_master_id).where(Party.channel_id == channel_id)

    if party is None:
        raise PartyNotFoundException(channel_id)

    return party.dungeon_master_id == user_id
