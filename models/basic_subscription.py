from abc import ABC, abstractmethod

class BasicSubscription(ABC):
    def __init__(
            self,
            player_id: int,
            date: str,
            status: str = "Unpaid",
            amount: float = 0
    ):
        self.player_id = player_id
        self.date = date
        self.status = status
        self.amount = amount

    @abstractmethod
    def update_status(self,is_paid:bool):
        if is_paid: self.status = "Paid"
        else : self.status = "Unpaid"

    @abstractmethod
    def display_subscription(self):
        print(f"Player id : {self.player_id} - From : {self.date_from} - To : {self.date_to} - Status : {self.status} - Amount : {self.amount}")
