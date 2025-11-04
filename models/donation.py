from models.basic_subscription import BasicSubscription


class Donation(BasicSubscription):
    def __init__(
            self,
            player_id:int,
            date: str,
            amount: float = 0,
            donator: str = ""
    ):
        super().__init__(player_id,date,"Paid",amount)
        self.donator = donator