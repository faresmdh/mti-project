from models.event import Event


class Training(Event):
    def __init__(
            self,
            id: int,
            name: str = "",
            date: str = "",
            organizer: str = "",
            players: list = [],
            duration: str = ""
    ):
        super().__init__( id, name, date, organizer, players)
        self.duration = duration

    def display_event(self):
        print(
            f"• ID : {self.id} \n• Name : {self.name} \n• Date : {self.date} \n• Organizer : {self.organizer} \n• Duration : {self.duration}")
        print("• Registered players :")
        for p in self.players:
            print(f"    - {p.name} ({p.positions})")
        print("----------------------------------------------------------")