from abc import ABC, abstractmethod


class Event(ABC):
    def __init__(
            self,
            id,
            name,
            date,
            e_type:str,
            organizer,
            manager
    ):
        self.id = id
        self.name = name
        self.date = date
        self.e_type = e_type
        self.organizer = organizer
        self.type = type
        self.manager = manager

    @abstractmethod
    def display_event(self):
        pass