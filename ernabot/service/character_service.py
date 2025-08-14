from ernabot.model.character import Character
from ernabot.model.party import Party
from ernabot.exception import (
    PartyNotFoundException,
    PartyNotPermittedException,
    CharacterAlreadyExistsException,
    CharacterUnsupportedContentTypeException,
    UserHasAlreadyCharacterException,
)


def create_character(
    channel_id: str,
    executor_id: str,
    user_id: str,
    name: str,
    description: str,
    picture_data: bytearray,
    picture_content_type: str,
) -> Character:
    party = Party.select(Party.dungeon_master_id).where(Party.channel_id == channel_id)

    if party is None:
        raise PartyNotFoundException(channel_id)

    if party.dungeon_master_id != executor_id:
        raise PartyNotPermittedException(party.dungeon_master_id)

    character = Character.select(Character.name).where(
        Character.party == party and Character.discord_user_id == user_id
    )
    if character is not None:
        raise UserHasAlreadyCharacterException(user_id, character.name)

    if (
        Character.select(Character.name)
        .where(Character.party == party and Character.name == name)
        .exists()
    ):
        raise CharacterAlreadyExistsException(name)

    # None -> Allow not setting a profile picture
    if picture_content_type not in [None, "image/jpeg", "image/png"]:
        raise CharacterUnsupportedContentTypeException(picture_content_type)

    character = Character.create(
        name=name,
        description=description,
        party=party,
        picture=picture_data,
        discord_user_id=user_id,
    )
    return character


def delete_character(
    channel_id: str,
    executor_id: str,
    name: str,
    user_id: str,
):
    pass
