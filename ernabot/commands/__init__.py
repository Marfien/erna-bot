import discord
from ernabot.commands import game as game_command


def register(bot: discord.Bot):
    game_command.register(bot)
