import discord

from ernabot import model
from ernabot.config import selected as config
from ernabot.model.character import InventoryItem, Character, StatusEffect
from ernabot.model.party import Party


def main():
    model.init([Party, Character, InventoryItem, StatusEffect])

    bot = discord.Bot()
    bot.load_extensions("ernabot.cogs.commands", "ernabot.cogs.events")

    bot.run(config.api_token)


if __name__ == "__main__":
    main()
