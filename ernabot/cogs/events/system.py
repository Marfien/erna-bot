import discord
from discord.ext import commands


class SystemEvents(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as '{self.bot.user.display_name}' (ID: {self.bot.user.id})")
