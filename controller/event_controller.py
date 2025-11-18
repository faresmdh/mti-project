from db.db_helper import SqLiteHelper
from json import loads, dumps

from models.event import Event
from models.match import Match
from models.training import Training


class EventController:
    def __init__(self,db_helper:SqLiteHelper):
        self.conn = db_helper.conn

    def insert_event(self,e: Event):
        cur = self.conn.cursor()
        cur.execute("""
          INSERT OR REPLACE INTO events
          (id, name, date, organizer, players, type, opponent, result, duration)
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            e.id,
            e.name,
            e.date,
            e.organizer,
            dumps(e.players),
            e.type,
            e.opponent,
            e.result,
            e.duration
        ))
        self.conn.commit()
        self.conn.close()

    def list_events(self):
        """
        Returns all events as a list of Event objects, ordered by date descending.
        """
        cur = self.conn.cursor()
        rows = cur.execute("SELECT * FROM events ORDER BY date DESC").fetchall()

        events = []
        for r in rows:
            if r.type == 'Match':
                event = Match(
                    id=r.id,
                    name=r.name,
                    date=r.date,
                    organizer=r.organizer,
                    players=loads(r.players),
                    e_type=r.type,
                    opponent=r.opponent,
                    result=r.result
                )
            else:
                event = Training(
                    id=r.id,
                    name=r.name,
                    date=r.date,
                    organizer=r.organizer,
                    players=loads(r.players),
                    e_type=r.type,
                    duration=r.duration
                )
            events.append(event)

        return events

    def register_player(self, event_id: int, player_id: int):
        cur = self.conn.cursor()
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
            self.conn.commit()

    def unregister_player(self, event_id: int, player_id: int):
        cur = self.conn.cursor()
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
            self.conn.commit()