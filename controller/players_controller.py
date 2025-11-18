import sqlite3
from json import loads, dumps

from flask import jsonify

from models.player import Player

class PlayersController:

    def __init__(self, db_helper):
        self.db = db_helper

    def get_player(self, player_id: int):
        conn = self.db.get_connection()
        cur = conn.cursor()

        row = cur.execute("SELECT * FROM players WHERE id = ?", (player_id,)).fetchone()
        conn.close()

        if row is None:
            return None

        player = Player(
            id=row["id"],
            name=row["name"],
            email=row["email"],
            age=row["age"],
            phone=row["phone"],
            category=row["category"],
            address=row["address"],
            join_date=row["join_date"],
            positions=loads(row["positions"]),
            skills=loads(row["skills"]),
            subscription_status=row["subscription_status"]
        )

        return player


    def insert_player(self, player: Player):
        conn = self.db.get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT OR REPLACE INTO players
            ( name, email, age, phone, category, address, join_date, positions, skills, subscription_status)
            VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            player.name,
            player.email,
            player.age,
            player.phone,
            player.category,
            player.address,
            player.join_date,
            dumps(player.positions),
            dumps(player.skills),
            player.subscription_status
        ))

        conn.commit()
        conn.close()

    def delete_player(self, player_id: int):
        conn = self.db.get_connection()
        cur = conn.cursor()

        cur.execute("DELETE FROM players WHERE id = ?", (player_id,))
        conn.commit()
        conn.close()

    def search_player(self, query: str):
        conn = self.db.get_connection()
        cur = conn.cursor()

        query_param = f"%{query}%"
        cur.execute("""
            SELECT * FROM players
            WHERE name LIKE ?
               OR positions LIKE ?
               OR skills LIKE ?
        """, (query_param, query_param, query_param))

        rows = cur.fetchall()
        conn.close()

        return [
            Player(
                id=r["id"],
                name=r["name"],
                email=r["email"],
                age=r["age"],
                phone=r["phone"],
                category=r["category"],
                address=r["address"],
                join_date=r["join_date"],
                positions=loads(r["positions"]),
                skills=loads(r["skills"]),
                subscription_status=r["subscription_status"]
            )
            for r in rows
        ]

    def list_players(self):
        conn = self.db.get_connection()
        cur = conn.cursor()

        rows = cur.execute("SELECT * FROM players ORDER BY id").fetchall()
        conn.close()

        players = [
            Player(
                id=r["id"],
                name=r["name"],
                email=r["email"],
                age=r["age"],
                phone=r["phone"],
                category=r["category"],
                address=r["address"],
                join_date=r["join_date"],
                positions=loads(r["positions"]),
                skills=loads(r["skills"]),
                subscription_status=r["subscription_status"]
            )
            for r in rows
        ]

        return jsonify([p.to_dict() for p in players])
