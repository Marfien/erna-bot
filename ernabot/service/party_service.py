from ernabot.model.party import Party


def create_party(name: str, channel_id: str, dungeon_master_id: str):
    party = Party(name=name, channel_id=channel_id, dungeon_master_id=dungeon_master_id)
