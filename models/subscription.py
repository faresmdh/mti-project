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