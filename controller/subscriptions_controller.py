from db.db_helper import SqLiteHelper
from models.subscription import Subscription


class SubscriptionController:
    def __init__(self,db_helper:SqLiteHelper):
        self.conn = db_helper.conn

    def insert_subscription(self, s: Subscription):
        cur = self.conn.cursor()
        cur.execute("""
           INSERT INTO subscriptions (player_id, date, status, amount, duration)
           VALUES (?, ?, ?, ?, ?)
        """, (s.player_id, s.date, s.status, s.amount, s.duration))
        self.conn.commit()
        self.conn.close()

    def list_subscriptions(self):
        """
        Returns all subscriptions as a list of Subscription objects.
        """
        cur = self.conn.cursor()
        rows = cur.execute("SELECT * FROM subscriptions ORDER BY id").fetchall()

        subscriptions = []
        for r in rows:
            sub = Subscription(
                id=r.id,
                player_id=r.player_id,
                date=r.date,
                status=r.status,
                amount=r.amount,
                duration=r.duration
            )
            subscriptions.append(sub)

        return subscriptions