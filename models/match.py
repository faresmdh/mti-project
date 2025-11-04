from models.event import Event


class Match(Event):
    def __init__(
            self,
            id: int,
            name: str = "",
            date: str = "",
            organizer: str = "",
            players: list = [],
            opponent: str = "",
            result: str = ""
    ):
        super().__init__( id, name, date, organizer, players)
        self.opponent = opponent
        self.result = result

    def display_event(self):
        print(
            f"• ID : {self.id} \n• Name : {self.name} \n• Date : {self.date} \n• Organizer : {self.organizer} \n•Opponent : {self.opponent} \n•Result : {self.result}")
        print("• Registered players :")
        for p in self.players:
            print(f"    - {p.name} ({p.positions})")
        print("----------------------------------------------------------")