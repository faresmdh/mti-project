from db.db_helper import SqLiteHelper
from models.player import Player
from models.subscription import Subscription


class SubscriptionController:
    def __init__(self,db_helper:SqLiteHelper):
        self.db = db_helper

    def insert_subscription(self, s: Subscription):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("""
           INSERT INTO subscriptions (player_id, date, status, amount, duration)
           VALUES (?, ?, ?, ?, ?)
        """, (s.player_id, s.date, s.status, s.amount, s.duration))
        conn.commit()

    def list_subscriptions(self):
        conn = self.db.get_connection()
        cur = conn.cursor()

        rows = cur.execute("""
            SELECT s.id AS sub_id, s.player_id, s.date, s.status, s.amount, s.duration,
                   p.id AS p_id, p.name AS p_name, p.email AS p_email,
                   p.age AS p_age, p.phone AS p_phone, p.category AS p_category,
                   p.address AS p_address, p.join_date AS p_join_date,
                   p.subscription_status AS p_subscription_status
            FROM subscriptions s
            JOIN players p ON s.player_id = p.id
            ORDER BY s.id;
        """).fetchall()

        subscriptions = []

        for r in rows:
            player = Player(
                id=r["p_id"],
                name=r["p_name"],
                email=r["p_email"],
                age=r["p_age"],
                phone=r["p_phone"],
                category=r["p_category"],
                address=r["p_address"],
                join_date=r["p_join_date"],
                positions=[],
                skills=[],
                subscription_status=r["p_subscription_status"]
            )


            sub = Subscription(
                id=r["sub_id"],
                player_id=r["player_id"],
                date=r["date"],
                status=r["status"],
                amount=r["amount"],
                duration=r["duration"],
            )

            sub.player = player
            subscriptions.append(sub)

        return subscriptions
