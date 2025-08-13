import discord

from ernabot.cogs.commands.party_command import PartyCommand


def setup(bot: discord.Bot):
    bot.add_cog(PartyCommand(bot))
