from models.event import Event


class Training(Event):
    def __init__(
            self,
            id: int,
            name: str = "",
            date: str = "",
            organizer: str = "",
            players: list = [],
            e_type:str = "",
            duration: str = ""
    ):
        super().__init__( id, name, date, organizer, players, e_type)
        self.duration = duration