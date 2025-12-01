from models.basic_subscription import BasicSubscription


class Subscription(BasicSubscription):
    def __init__(
            self,
            id: int,
            player_id:int,
            date: str,
            status: str = "Unpaid",
            amount: float = 0,
            duration: int = 0
    ):
        super().__init__(id,player_id,date,status,amount)
        self.duration = duration

    def update_status(self,is_paid:bool):
        super()


    def display_subscription(self):
        super()

    def to_dict(self):
        return {
            "id": self.id,
            "player_id": self.player_id,
            "date": self.date,
            "status": self.status,
            "amount": self.amount,
            "duration": self.duration,
            "player": self.player.to_dict() if self.player else None
        }