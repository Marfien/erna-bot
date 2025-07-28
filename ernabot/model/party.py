from ernabot.model.character import Character


class Party:
    def __init__(self, name: str, guild_id: str, master: str) -> None:
        self.name = name
        self.guild_id = guild_id
        self.master = master
        self.characters = list[Character]
