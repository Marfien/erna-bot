import discord
from ernabot.command import party_command


def register(bot: discord.Bot):
    party_command.register(bot)
