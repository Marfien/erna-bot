import discord

from ernabot import commands


def main():
    bot = discord.Bot()

    commands.register(bot)

    bot.run()  # TODO API key


if __name__ == "__main__":
    main()
