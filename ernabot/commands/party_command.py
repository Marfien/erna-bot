import discord

group = discord.SlashCommandGroup("party", "Manages DND parties")


@group.command()
async def create(
    ctx: discord.ApplicationContext, name: discord.Option(str, "The name of the party")
):
    pass


@group.command()
async def delete(
    ctx: discord.ApplicationContext, name: discord.Option(str, "The name of the party")
):
    pass


@group.command()
async def join(
    ctx: discord.ApplicationContext,
):
    pass


def register(bot: discord.Bot):
    bot.add_application_command(group)
