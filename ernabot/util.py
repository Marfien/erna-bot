from typing import Any

from discord.abc import GuildChannel
from discord.channel import _TextChannel
from discord.user import BaseUser


def mention_user(user: Any) -> str:
    if isinstance(user, str):
        return f"<@{user}>"
    elif isinstance(user, BaseUser):
        return user.mention
    else:
        raise TypeError(f"Cannot create mention for type {type(user)}")


def mention_channel(channel: Any) -> str:
    if isinstance(channel, str):
        return f"<#{channel}>"
    elif isinstance(channel, GuildChannel):
        return channel.mention
    else:
        raise TypeError(f"Cannot create mention for type {type(channel)}")
