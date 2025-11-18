from models.event import Event
from models.player import Player
from models.subscription import Subscription


class ClubRepository:

    def __init__(
            self,
            controller
    ):
        self.controller = controller
        self.players = controller.list_players()
        self.events = controller.list_events()
        self.subscriptions = controller.list_subscriptions()

    def add_player(self, player: Player):
        self.controller.insert_player(player)

    def delete_player(self, player_id: int):
        self.controller.delete_player(player_id)

    def search_player(self, query: str):
        return self.controller.search_player(query)

    def add_event(self,event:Event):
        self.controller.insert_event(event)

    def add_subscription(self,subscription:Subscription):
        self.controller.insert_subscription(subscription)