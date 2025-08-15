import requests

from ernabot.exception import (
    CharacterAlreadyExistsException,
    CharacterNotFoundException,
    CharacterUnsupportedContentTypeException,
    PartyNotFoundException,
    PartyNotPermittedException,
    UserHasAlreadyCharacterException,
)
from ernabot.model.character import Character
from ernabot.model.party import Party


def create_character(
    channel_id: str,
    executor_id: str,
    user_id: str,
    name: str,
    description: str,
    avatar_url: str,
    avatar_content_type: str,
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

    # None -> Allow not setting an avatar
    if avatar_content_type not in [None, "image/jpeg", "image/png"]:
        raise CharacterUnsupportedContentTypeException(avatar_content_type)

    avatar_data: bytes | None = None

    if avatar_url:
        response = requests.get(avatar_url)

        if response.status_code == 200:
            avatar_data = response.content

    character = Character.create(
        name=name,
        description=description,
        party=party,
        avatar=avatar_data,
        discord_user_id=user_id,
    )
    return character


def delete_character(
    channel_id: str,
    executor_id: str,
    name: str,
):
    party = Party.select(Party.dungeon_master_id).where(Party.channel_id == channel_id)

    if party is None:
        raise PartyNotFoundException(channel_id)

    character = Character.select(Character.discord_user_id).where(
        Character.name == name
    )

    if party.dungeon_master_id != executor_id and (
        character and character.user_id != executor_id
    ):
        raise PartyNotPermittedException(party.dungeon_master_id)

    if character is None:
        raise CharacterNotFoundException(name)

    character.delete_instance()
    return character
