from event import Event
from player import Player


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

if __name__ == "__main__":
    # creating match
    m = Match(1,"Training science 1","27/10/2025","ABRD",[],"DRBK","2-1")

    # creating player 1
    p1 = Player(1, "Meddahi Fares", "fares.mdh1@gmail.com", 25, "0558015936", "Senior", "Djebahia", "13/12/2024",
                ["Middle", "Attack"], ["Left leg", "Shooter"])

    # creating player 2
    p2 = Player(2, "Dahmani Abdelhak", "dahmani@gmail.com", 23, "0777777777", "Senior", "Djebahia", "05/02/2025",
                ["Goal keeper"], ["Right leg", "Goal keeping"])

    # add players to event
    m.register_player(p1)
    m.register_player(p2)

    m.display_event()