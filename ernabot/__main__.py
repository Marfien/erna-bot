import discord

from ernabot import command, model
from ernabot.config import selected as config
from ernabot.model.character import InventoryItem, Character, StatusEffect
from ernabot.model.party import Party


def main():
    bot = discord.Bot()

    model.init([Party, Character, InventoryItem, StatusEffect])
    command.register(bot)

    bot.run(config.api_token)


if __name__ == "__main__":
    main()
