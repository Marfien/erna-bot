import discord
from discord.ext import commands
from ernabot import util
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
            "The dungeon master, mostly for display reasons. Defaults to the command executor.",
            required=False,
        ),
    ):
        if not channel:
            channel = ctx.channel
        if not dungeon_master:
            dungeon_master = ctx.user

        party = service.create_party(name, channel.id, dungeon_master.id)

        await ctx.respond(
            f"Party `{party.name}` ({party.id}) with {util.mention_user(party.dungeon_master_id)} as dungeon master and bound to channel {util.mention_channel(party.channel_id)}"
        )

    @group.command()
    async def delete(
        ctx: discord.ApplicationContext,
        name: discord.Option(str, "The name of the party"),  # type: ignore
    ):
        pass

    @group.command()
    async def join(ctx: discord.ApplicationContext, other):
        pass
