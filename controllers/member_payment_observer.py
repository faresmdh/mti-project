
from controllers.players_controller import PlayersController


class MemberPaymentObserver:
    def __init__(self,db_helper):
        self.db = db_helper
    def update(self, event):
        if event["type"] == "subscription_paid":
            member_id = event["member_id"]
            PlayersController(self.db).mark_player_sub_paid(member_id)