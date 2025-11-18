from abc import ABC, abstractmethod


class Event(ABC):
    def __init__(
            self,
            id: int,
            name: str = "",
            date: str = "",
            organizer: str = "",
            players: list = [],
            opponent: str = "",
            result: str = "",
            e_type: str = "",
            duration: str = ""
    ):
        self.id = id
        self.name = name
        self.date = date
        self.e_type = e_type
        self.organizer = organizer
        self.opponent = opponent
        self.result = result
        self.players = players
        self.duration = duration

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "date":self.date,
            "e_type":self.e_type,
            "organizer":self.organizer,
            "oponent":self.opponent,
            "result":self.result,
            "players":self.players,
            "duration":self.duration
        }