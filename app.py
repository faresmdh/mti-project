from flask import Flask, request, jsonify
from flask_cors import CORS

from controllers.dict_factory import DictFactory
from controllers.event_builder import EventBuilder
from controllers.event_controller import EventController
from controllers.member_payment_observer import MemberPaymentObserver
from controllers.name_adapter import NameAdapter
from controllers.player_builder import MemberBuilder
from controllers.players_controller import PlayersController
from controllers.subscription_builder import SubscriptionBuilder
from controllers.subscription_subject import SubscriptionSubject
from controllers.subscriptions_controller import SubscriptionController
from db.db_helper import SqLiteHelper

app = Flask(__name__)
CORS(app)
db_helper = SqLiteHelper()
db_helper.init_db()
players_controller = PlayersController(db_helper)
events_controller = EventController(db_helper)
subject = SubscriptionSubject()
observer = MemberPaymentObserver(db_helper)
subject.attach(observer)
sub_controller = SubscriptionController(db_helper,subject)
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
    name = NameAdapter(data.get("firstname", ""),data.get("lastname","")).get_name()
    p = (MemberBuilder().set_name(name)
                        .set_email(data.get("email",""))
                        .set_age(data.get("age",0))
                        .set_phone(data.get("phone",""))
                        .set_category(data.get("category", "Cadets"))
                        .set_address(data.get("address",""))
                        .set_join_date(data.get("join_date",""))
                        .set_positions(data.get("positions"))
                        .set_skills(data.get("skills",""))
                        .set_subscription_status(data.get("subscription_status", "Unpaid")))
    players_controller.insert_player(p)
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
    e = (EventBuilder().set_name(data.get("name", ""))
                        .set_date(data.get("date", ""))
                        .set_e_type(data.get("e_type", "Match"))
                        .set_organizer(data.get("organizer", ""))
                        .set_result(data.get("result", ""))
                        .set_opponent(data.get("opponent",""))
                        .set_duration(data.get("duration","")))
    events_controller.insert_event(e)
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