import csv

from event import Event
from match import Match
from player import Player
from subscription import Subscription
from training import Training
import json


class Club:
    def __init__(
            self,
            name: str = "",
            abbreviation: str = "",
            players: list = [],
            events: list = [],
            subscriptions: list = []
    ):
        self.name = name
        self.abbreviation = abbreviation
        self.players = players
        self.events = events
        self.subscriptions = subscriptions

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

    def init_players_from_csv(self,csv_file):
        with open(csv_file, encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter="\t")
            for row in reader:
                player = Player(
                    id = row['id'],
                    name= row['name'],
                    email= row['email'],
                    age= int(row['age']),
                    phone= row['phone'],
                    category= row['category'],
                    address= row['address'],
                    join_date= row['join_date'],
                    positions= [row['positions']],
                    skills= [row['skills']],
                    subscription_status= row['subscription_status'],
                )
                self.add_player(player)

    def add_event(self,event:Event):
        self.events.append(event)

    def add_subscription(self,subscription:Subscription):
        self.subscriptions.append(subscription)

    def init_events_from_csv(self,csv_file):
        with open(csv_file, encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=",")
            for row in reader:
                players_data = json.loads(row['players']) if row['players'] else []
                players = [
                    Player(
                        id=p['id'],
                        name=p.name,
                        email=p.email,
                        age=int(p.age),
                        phone=p.phone,
                        category=p.category,
                        address=p.address,
                        join_date=p.join_date,
                        positions=p.positions,
                        skills=p.skills,
                        subscription_status=p.subscription_status
                    )
                    for p in players_data
                ]

                # Create the correct event type
                if row['type'] == "Match":
                    event = Match(
                        id=int(row['id']),
                        name=row.get('name', ''),
                        date=row.get('date', ''),
                        organizer=row.get('organizer', ''),
                        players=players,
                        opponent=row.get('opponent', ''),
                        result=row.get('result', '')
                    )
                elif row['type'] == "Training":
                    event = Training(
                        id=int(row['id']),
                        name=row.get('name', ''),
                        date=row.get('date', ''),
                        organizer=row.get('organizer', ''),
                        players=players,
                        duration=row.get('duration', '')
                    )
                self.add_event(event)

    def init_subscriptions_from_csv(self, csv_file):
        with open(csv_file, encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=",")
            for row in reader:
                subscription = Subscription(
                    player_id=int(row['player_id']),
                    date_from=row['date_from'],
                    date_to=row['date_to'],
                    status=row.get('status', 'Unpaid'),
                    amount=float(row.get('amount', 0))
                )
                self.add_subscription(subscription)




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
