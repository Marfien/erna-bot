import discord
from discord.ext import commands

from ernabot.exception import handle_exception
from ernabot.service import character_service as service


class CharacterCommand(commands.Cog):
    group = discord.SlashCommandGroup("character", "Manage characters in DND parties")

    @group.command()
    async def delete(
        ctx: discord.ApplicationContext,
        name: discord.Option(str, "The name of the character to remove."),  # pyright: ignore
    ):
        try:
            service.delete_character(ctx.channel_id, ctx.user.id, name)
            await ctx.respond(
                f"{name} will not be seen around anymore. May his soul rest in peace and watch over the remaining party."
            )
        except Exception as e:
            await handle_exception(e, ctx.respond)

    @group.command()
    async def create(
        ctx: discord.ApplicationContext,
        user: discord.Option(  # pyright: ignore
            discord.User,
            "The master of this character. Defaults to your user.",
            required=False,
        ),
        name: discord.Option(str, "The name of the character"),  # pyright: ignore
        description: discord.Option(  # pyright: ignore
            str,
            "The characters description/lore",
            default="Once, a big pile of smoke appeared. That's when I started my existance.",
        ),
        avatar: discord.Option(  # pyright: ignore
            discord.Attachment, "The avatar of this character.", required=False
        ),
    ):
        if user is None:
            user = ctx.user

        try:
            service.create_character(
                ctx.channel_id,
                ctx.user.id,
                user.id,
                name,
                description,
                avatar.url,
                avatar.content_type,
            )
            await ctx.respond(
                f"There was some time when {name} was not around. But the bigger a party the better adventures."
            )
        except Exception as e:
            await handle_exception(e, ctx.respond)
