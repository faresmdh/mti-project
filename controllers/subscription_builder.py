from models.subscription import Subscription


class SubscriptionBuilder:
    def __init__(self):
        self.player_id = None,
        self.date = None,
        self.status = "Unpaid",
        self.amount = None,
        self.duration = None

    def set_player_id(self, player_id):
        self.player_id = player_id
        return self

    def set_date(self, date):
        self.date = date
        return self

    def set_status(self, status):
        self.status = status
        return self

    def set_amount(self, amount):
        self.amount = amount
        return self

    def set_duration(self, duration):
        self.duration = duration
        return self

    def build(self):
        # Validate required fields
        if self.player_id is None:
            raise ValueError("player_id is required")
        if self.amount is None:
            raise ValueError("amount is required")
        if self.date is None:
            raise ValueError("date is required")
        if self.duration is None:
            raise ValueError("duration is required")

        return Subscription(
            id = 0,
            player_id=self.player_id,
            date=self.date,
            status=self.status,
            amount=self.amount,
            duration=self.duration
        )