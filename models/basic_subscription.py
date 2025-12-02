from abc import ABC, abstractmethod

class BasicSubscription(ABC):
    def __init__(
            self,
            id: int,
            player_id: int,
            date: str,
            status: str = "Unpaid",
            amount: float = 0
    ):
        self.id = id
        self.player_id = player_id
        self.date = date
        self.status = status
        self.amount = amount