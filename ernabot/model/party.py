from ernabot.model.character import Character


class Party:
    def __init__(self, name: str, channel_id: str, master: str) -> None:
        self.name = name
        self.channel_id = channel_id
        self.master = master
        self.characters = list[Character]
