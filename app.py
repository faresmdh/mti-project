from flask import Flask, request, jsonify
from flask_cors import CORS

from controllers.dict_factory import DictFactory
from controllers.event_controller import EventController
from controllers.players_controller import PlayersController
from controllers.subscription_builder import SubscriptionBuilder
from controllers.subscriptions_controller import SubscriptionController
from db.db_helper import SqLiteHelper
from models.event import Event
from models.player import Player
from models.subscription import Subscription

app = Flask(__name__)
CORS(app)
db_helper = SqLiteHelper()
db_helper.init_db()
players_controller = PlayersController(db_helper)
events_controller = EventController(db_helper)
sub_controller = SubscriptionController(db_helper)
dict_factory = DictFactory()


# Routes
@app.get("/players")
def list_players():
    result = players_controller.list_players()
    return jsonify([dict_factory.create_dict("member",p) for p in result])

@app.get("/players/<int:player_id>")
def get_player(player_id):
    result = players_controller.get_player(player_id)
    return jsonify(dict_factory.create_dict("member",result))

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
    players_controller.insert_player(player)
    return jsonify({"status": "ok"})

@app.delete("/players/<int:player_id>")
def delete_player(player_id):
    players_controller.delete_player(player_id)
    return jsonify({"status": "deleted"})

@app.get("/players/search/<query>")
def search_players(query):
    result = players_controller.search_player(query)
    return jsonify([dict_factory.create_dict("member",p) for p in result])

@app.get("/events")
def list_events():
    result = events_controller.list_events()
    return jsonify([dict_factory.create_dict("event",e) for e in result])

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

@app.delete("/events/<int:event_id>")
def delete_event(event_id):
    try:
        events_controller.delete_event(event_id)
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": "Something went wrong"}), 500

@app.get("/subscriptions")
def list_subscriptions():
    try:
        result = sub_controller.list_subscriptions()
        return jsonify([dict_factory.create_dict("subscription",s) for s in result])
    except Exception as e:
        return jsonify({"status": "error", "message": "Something went wrong"}), 500

@app.post("/subscriptions")
def add_subscription():
    try:
        data = request.json
        subscription = (SubscriptionBuilder()
                                .set_player_id(data.get("player_id", ""))
                                .set_date(data.get("date", ""))
                                .set_status(data.get("status", ""))
                                .set_amount(data.get("amount", ""))
                                .set_duration(data.get("duration", ""))
                                .build())
        sub_controller.insert_subscription(subscription)
        return jsonify({"status": "ok"})
    except Exception as e:
        print(e)
        return jsonify({"status": "error", "message": "Something went wrong"}), 500

if __name__ == "__main__":
    app.run(debug=True)