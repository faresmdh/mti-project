from player import Player
from abc import abstractmethod


class Event:
    def __init__(
            self,
            id: int,
            name: str="",
            date: str="",
            organizer: str="",
            players: list=[]
    ):
        self.id = id
        self.name = name
        self.date = date
        self.organizer = organizer
        self.type = type
        self.players = players

    def add_player(self, player:Player):
        self.players.append(player)

    def remove_player(self, player:Player):
        if self.players.__contains__(player): self.players.remove(player)

    @abstractmethod
    def display_event(self):
        pass

    @abstractmethod
    def update_event(
            self,
            name:str=None,
            date:str=None,
            organizer:str=None,
            players:[]=None,
            opponent:str=None,
            result:str=None
    ):
        pass