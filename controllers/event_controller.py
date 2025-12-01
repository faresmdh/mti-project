from db.db_helper import SqLiteHelper
from json import loads, dumps, JSONDecodeError

from models.event import Event


class EventController:
    def __init__(self, db_helper):
        self.db = db_helper

    def insert_event(self,e: Event):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("""
          INSERT OR REPLACE INTO events
          ( name, date, organizer, players, type, opponent, result, duration)
          VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            e.name,
            e.date,
            e.organizer,
            dumps(e.players),
            e.e_type,
            e.opponent,
            e.result,
            e.duration
        ))
        conn.commit()
        conn.close()

    def list_events(self):
        """
        Returns all events as a list of Event objects, ordered by date descending.
        """
        conn = self.db.get_connection()
        cur = conn.cursor()

        # Simply get all events - players are stored as JSON in the players column
        rows = cur.execute("SELECT * FROM events ORDER BY date DESC").fetchall()

        events = []
        for r in rows:
            # Parse the JSON player data directly from the players column
            players_json = r["players"]
            try:
                # Parse the JSON array of player IDs
                player_ids = loads(players_json) if players_json else []

                # Convert to list of player objects with id and name
                players = []
                for player_id in player_ids:
                    # Get player details from players table
                    player_row = cur.execute("SELECT id, name, category FROM players WHERE id = ?", (player_id,)).fetchone()
                    if player_row:
                        players.append({
                            "id": player_row["id"],
                            "name": player_row["name"],
                            "category": player_row["category"]
                        })
            except JSONDecodeError:
                players = []

            event = Event(
                id=r["id"],
                name=r["name"],
                date=r["date"],
                organizer=r["organizer"],
                players=players,  # Now contains list of player objects with id and name
                e_type=r["type"],
                opponent=r["opponent"],
                result=r["result"],
                duration=r["duration"]
            )
            events.append(event)

        return events

    def register_player(self, event_id: int, player_id: int):
        conn = self.db.get_connection()
        cur = conn.cursor()
        row = cur.execute("SELECT players FROM events WHERE id = ?", (event_id,)).fetchone()
        if row is None:
            raise ValueError(f"Event {event_id} does not exist")

        players_list = loads(row["players"])
        if player_id not in players_list:
            players_list.append(player_id)
            cur.execute(
                "UPDATE events SET players = ? WHERE id = ?",
                (dumps(players_list), event_id)
            )
            conn.commit()

    def unregister_player(self, event_id: int, player_id: int):
        conn = self.db.get_connection()
        cur = conn.cursor()
        row = cur.execute("SELECT players FROM events WHERE id = ?", (event_id,)).fetchone()
        if row is None:
            raise ValueError(f"Event {event_id} does not exist")

        players_list = loads(row["players"])
        if player_id in players_list:
            players_list.remove(player_id)
            cur.execute(
                "UPDATE events SET players = ? WHERE id = ?",
                (dumps(players_list), event_id)
            )
            conn.commit()

    def delete_event(self, event_id: int):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM events WHERE id = ?", (event_id,))
        conn.commit()