from flask import Flask, request, jsonify
from controller.players_controller import PlayersController
from db.db_helper import SqLiteHelper
from models.player import Player

app = Flask(__name__)
db_helper = SqLiteHelper()
db_helper.init_db()
players_controller = PlayersController(db_helper)


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

@app.get("/players/search/<str:query>")
def search_players(query):
    result = players_controller.search_player(query)
    return jsonify([p.to_dict() for p in result])

if __name__ == "__main__":
    app.run(debug=True)