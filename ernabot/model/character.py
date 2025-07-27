import datetime


class StatusEffect:
    def __init__(
        self,
        description: str,
        applied_at: datetime.datetime | None = None,
        extra: str | None = None,
    ) -> None:
        self.description = description
        self.extra = extra

        if applied_at is None:
            self.applied_at = datetime.datetime.now()
            self.applied_at = applied_at


class Character:
    def __init__(
        self,
        name: str,
        description: str,
        user_id: str,
        picture: bytearray | None = None,
    ) -> None:
        self.name = name
        self.description = description
        self.picture = picture
        self.inventory: dict[str, int] = {}
        self.status_effects: list[StatusEffect] = []
        self.user_id = user_id
