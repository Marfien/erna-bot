import discord
from discord.ext import commands
from ernabot import util
from ernabot.exception import handle_exception
import ernabot.service.party_service as service


class PartyCommand(commands.Cog):
    group = discord.SlashCommandGroup("party", "Manages DND parties")

    @group.command()
    async def create(
        ctx: discord.ApplicationContext,
        name: discord.Option(str, "The name of the party"),  # type: ignore
        channel: discord.Option(  # type: ignore
            discord.abc.GuildChannel,
            "The channel where commands from this party are mapped to. Defaults to the current channel.",
            required=False,
        ),
        dungeon_master: discord.Option(  # type: ignore
            discord.User,
            "The dungeon master. Defaults to the command executor.",
            required=False,
        ),
    ):
        if not channel:
            channel = ctx.channel
        if not dungeon_master:
            dungeon_master = ctx.user

        try:
            party = service.create(name, channel.id, dungeon_master.id)
            await ctx.respond(
                f"Behold, the `{party.name}` party was seighted with {util.mention_user(party.dungeon_master_id)} as their dungeon master"
            )
        except Exception as ex:
            await handle_exception(ex, ctx.respond)

    @group.command()
    async def delete(ctx: discord.ApplicationContext):
        channel_id = ctx.channel.id
        executer_id = ctx.user.id

        try:
            party = service.delete(executer_id, channel_id)
            await ctx.respond(
                f"There are no more adventures for {party.name} to go on. Farewell, my dear friends!"
            )
        except Exception as ex:
            await handle_exception(ex, ctx.respond)
