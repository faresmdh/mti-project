from models.player import Player


class EventManager:
    def __init__(self,players):
        self.players = players

    def register_player(self, player:Player):
        self.players.append(player)

    def unregister_player(self, player:Player):
        if self.players.__contains__(player): self.players.remove(player)

