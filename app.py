from flask import Flask, request, jsonify
from flask_cors import CORS


from controllers.event_controller import EventController
from controllers.players_controller import PlayersController
from db.db_helper import SqLiteHelper
from models.event import Event
from models.player import Player

app = Flask(__name__)
CORS(app)
db_helper = SqLiteHelper()
db_helper.init_db()
players_controller = PlayersController(db_helper)
events_controller = EventController(db_helper)


# Routes
@app.get("/players")
def list_players():
    result = players_controller.list_players()
    return result

@app.get("/players/<int:player_id>")
def get_player(player_id):
    result = players_controller.get_player(player_id)
    return jsonify(result.to_dict())

@app.post("/players")
def add_player():
    data = request.json
    player = Player(
        name=data.get("name", ""),
        email=data.get("email", ""),
        age=data.get("age", 0),
        phone=data.get("phone", ""),
        category=data.get("category", "Cadets"),
        address=data.get("address", ""),
        join_date=data.get("join_date", ""),
        positions=data.get("positions", []),
        skills=data.get("skills", []),
        subscription_status=data.get("subscription_status", "Unpaid")
    )
    result = players_controller.insert_player(player)
    return jsonify({"status": "ok"})

@app.delete("/players/<int:player_id>")
def delete_player(player_id):
    players_controller.delete_player(player_id)
    return jsonify({"status": "deleted"})

@app.get("/players/search/<query>")
def search_players(query):
    result = players_controller.search_player(query)
    return jsonify([p.to_dict() for p in result])

@app.get("/events")
def list_events():
    result = events_controller.list_events()
    return jsonify([e.to_dict() for e in result])

@app.post("/events")
def insert_event():
    data = request.json
    event = Event(
        id = 0,
        name=data.get("name", ""),
        date=data.get("date", ""),
        e_type=data.get("e_type", "Match"),
        organizer=data.get("organizer", ""),
        result=data.get("result", ""),
        opponent=data.get("opponent",""),
        duration=data.get("duration","")
    )
    events_controller.insert_event(event)
    return jsonify({"status": "ok"})


@app.post("/events/<int:event_id>/register/<int:player_id>")
def register_player(event_id, player_id):
    try:
        events_controller.register_player(event_id, player_id)
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": "Something went wrong"}), 500


@app.post("/events/<int:event_id>/unregister/<int:player_id>")
def unregister_player(event_id, player_id):
    try:
        events_controller.unregister_player(event_id, player_id)
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": "Something went wrong"}), 500

if __name__ == "__main__":
    app.run(debug=True)