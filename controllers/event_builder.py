from models.event import Event
from models.subscription import Subscription


class EventBuilder:
    def __init__(self):
        self.name = None,
        self.date = None,
        self.e_type = "Match",
        self.organizer = None,
        self.result = None,
        self.opponent = None,
        self.duration = None,
        self.players = []

    def set_name(self, name):
        self.name = name
        return self

    def set_date(self, date):
        self.date = date
        return self

    def set_e_type(self, e_type):
        self.e_type = e_type
        return self

    def set_organizer(self, organizer):
        self.organizer = organizer
        return self

    def set_result(self, result):
        self.result = result
        return self

    def set_opponent(self, opponent):
        self.opponent = opponent
        return self

    def set_duration(self, duration):
        self.duration = duration
        return self

    def build(self):
        # Validate required fields
        if self.name is None:
            raise ValueError("name is required")
        if self.date is None:
            raise ValueError("amount is required")
        if self.organizer is None:
            raise ValueError("organizer is required")
        if self.e_type == "Match" and self.duration is None:
            raise ValueError("duration is required")
        if self.e_type == "Match" and self.opponent is None:
            raise ValueError("duration is required")

        return Event(
            id = 0,
            name=self.name,
            date=self.date,
            e_type=self.e_type,
            organizer=self.organizer,
            result=self.result,
            opponent=self.opponent,
            duration=self.duration,
            players=self.players
        )