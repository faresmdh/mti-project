from abc import ABC, abstractmethod


class Event(ABC):
    def __init__(
            self,
            id,
            name,
            date,
            organizer,
            manager
    ):
        self.id = id
        self.name = name
        self.date = date
        self.organizer = organizer
        self.type = type
        self.manager = manager

    @abstractmethod
    def display_event(self):
        pass