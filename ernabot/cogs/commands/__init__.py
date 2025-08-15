import discord

from ernabot.cogs.commands.charcter_command import CharacterCommand
from ernabot.cogs.commands.party_command import PartyCommand


def setup(bot: discord.Bot):
    bot.add_cog(PartyCommand(bot))
    bot.add_cog(CharacterCommand(bot))
