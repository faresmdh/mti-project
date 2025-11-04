from models.basic_subscription import BasicSubscription


class Subscription(BasicSubscription):
    def __init__(
            self,
            player_id:int,
            date: str,
            status: str = "Unpaid",
            amount: float = 0,
            duration: int = 0
    ):
        super().__init__(player_id,date,status,amount)
        self.duration = duration

    def update_status(self,is_paid:bool):
        super()


    def display_subscription(self):
        super()