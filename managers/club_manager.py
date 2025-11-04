import csv
import json

from models.event import Event
from models.match import Match
from models.player import Player
from models.subscription import Subscription
from models.training import Training


class ClubRepository:

    def __init__(
            self,
    ):
        self.players = []
        self.events = []
        self.subscriptions = []


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
                self.players.append(player)

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
                self.events.append(event)

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
                self.subscriptions.append(subscription)
                
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

    def add_event(self,event:Event):
        self.events.append(event)

    def add_subscription(self,subscription:Subscription):
        self.subscriptions.append(subscription)