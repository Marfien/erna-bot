from ernabot.exception import (
    PartyAlreadyExistsException,
    PartyNotFoundException,
    PartyNotPermittedException,
)
from ernabot.model.party import Party


def create(name: str, channel_id: str, dungeon_master_id: str) -> Party:
    if Party.select(Party.channel_id).where(Party.channel_id == channel_id).exists():
        raise PartyAlreadyExistsException(channel_id)

    party = Party.create(
        name=name, channel_id=channel_id, dungeon_master_id=dungeon_master_id
    )
    return party


def delete(executor_id: str, channel_id: str) -> Party:
    party = Party.select(Party.dungeon_master_id, Party.name).where(
        Party.channel_id == channel_id
    )

    if not party:
        raise PartyNotFoundException(channel_id)

    if party.dungeon_master_id != executor_id:
        raise PartyNotPermittedException(party.dungeon_master_id)

    party.delete_instance()
    return party
