from player import Player


class Club:
    def __init__(
            self,
            name: str = "",
            abbreviation: str = "",
            players: list = []
    ):
        self.name = name
        self.abbreviation = abbreviation
        self.players = players

    def show_dashboard(self):
        print(f"{self.name} ({self.abbreviation})")
        print(f"{self.players.__len__()} players :")
        for p in self.players:
            print("=============================================")
            p.generate_player_card()


    def add_player(self, player: Player):
        self.players.append(player)

    def delete_player(self, player: Player):
        self.players.remove(player)

    def search_player(self, keyword: str):
        result = []
        for player in self.players:
            if player.name.__contains__(keyword) or player.positions.__contains__(keyword) or player.skills.__contains__(keyword):
                result.append(player)

        return result


if __name__ == "__main__":
    # creating a club
    c = Club("ABR Djebahia", "ABRD", [])

    # creating player 1
    p1 = Player(1, "Meddahi Fares", "fares.mdh1@gmail.com", 25, "0558015936", "Senior", "Djebahia", "13/12/2024",
                ["Middle", "Attack"], ["Left leg", "Shooter"])

    # creating player 2
    p2 = Player(2, "Dahmani Abdelhak", "dahmani@gmail.com", 23, "0777777777", "Senior", "Djebahia", "05/02/2025",
                ["Goal keeper"], ["Right leg", "Goal keeping"])

    # add players to club
    c.add_player(p1)
    c.add_player(p2)

    # show dashboard
    c.show_dashboard()

    # trying search
    searched_players = c.search_player("Left leg")
    for p in searched_players:
        p.generate_player_card()

    # deleting player
    c.delete_player(p1)

    # showing dashboard again
    c.show_dashboard()
