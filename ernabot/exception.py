from collections.abc import Awaitable, Callable
from ernabot.util import mention_channel, mention_user


async def handle_exception(ex: Exception, respond: Callable[[str], Awaitable]):
    if isinstance(ex, ErnaException):
        await respond(ex.user_message)
    else:
        await respond(
            "I think I had one to much @.@ - There is something wrong here...\n"
            + "Please try again later or talk to my master if it does not get better!"
        )
        print(ex)


class ErnaException(Exception):
    user_message: str


class PartyAlreadyExistsException(ErnaException):
    def __init__(self, channel_id: str) -> None:
        self.user_message = (
            f"There is only place for one party in {mention_channel(channel_id)}."
        )


class PartyNotFoundException(ErnaException):
    def __init__(self, channel_id: str) -> None:
        self.user_message = f"This is a peacful place. No party arond here in {mention_channel(channel_id)}."


class PartyNotPermittedException(ErnaException):
    def __init__(self, dungeon_master_id: str) -> None:
        self.user_message = (
            f"Pesant! That's a job for the mighty {mention_user(dungeon_master_id)}."
        )
