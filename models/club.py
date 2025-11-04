class Club:
    def __init__(
            self,
            name,
            abbreviation,
            clubRepo
    ):
        self.name = name
        self.abbreviation = abbreviation
        self.clubRepo = clubRepo

    def show_dashboard(self):
        print(f"{self.name} ({self.abbreviation})")
        print(f"{self.clubRepo.players.__len__()} players :")
        for p in self.clubRepo.players:
            print("=============================================")
            p.generate_player_card()