import discord

from ernabot.cogs.events import system


def setup(bot: discord.Bot):
    bot.add_cog(system.SystemEvents(bot=bot))
