class Subscription:
    def __init__(
            self,
            player_id:int,
            date_from: str,
            date_to: str,
            status: str = "Unpaid",
            amount: float = 0
    ):
        self.player_id = player_id
        self.date_from = date_from
        self.date_to = date_to
        self.status = status
        self.amount = amount

    def update_status(self,is_paid:bool):
        if is_paid: self.status = "Paid"
        else : self.status = "Unpaid"