# Football Club Management System

This project is a **Football Club Management System** built using the **MVC (Model-View-Controller)** architecture. It provides a REST API for managing players only **(for now)** and allows interaction through a simple HTML dashboard.

## Dashboard
The dashboard is now separated into 03 HTML files and one CSS style file :
* `views/style.css` - defining dashboard style
* `views/members.html` – for members management

<img src="views/img.png"/>

* `views/events.html` – for events management

<img src="views/img2.png"/>

* `views/subscriptions.html` – for subscriptions management

<img src="views/img3.png"/>


---

## Technologies Used

* **Flask** – REST API backend for handling requests and routing
* **SQLite** – Lightweight database to store players, events and subscriptions data
* **MVC Architecture** – Separate layers for Models, Views, and Controllers
* **HTML ,CSS and JavaScript** – Simple dashboard for managing players

---

## Features

* List all players
* View detailed player information
* Add new players with customizable attributes
* Delete players
* Search players by name
* List all events
* Add new event
* Register player into event
* Unregister player from event
* Delete event
* List all subscriptions
* Add new subscription

---

## Getting Started

1. **Run the backend API**

   ```bash
   python app.py
   ```

   The API will start at `http://localhost:5000`.

2. **Open the dashboard**
   Open `members.html` in a web browser to manage players through a simple interface.

3. **Use the API directly (optional)**
   You can also interact with the API using tools like **Postman** or **curl**.

---

## Project Structure

* `models/` – Data models (Player, Event...)
* `controllers/` – Handles business logic and database operations
* `views/` – HTML dashboard for managing players, events and subscriptions
* `db/db_helper.py` – SQLite helper to init and create db if not exists
* `app.py` – Main Flask application and route definitions
* `app.db` – The SQLite database file (Delete it and you will lose your data)

---

## Notes

* The project follows **MVC design patterns** to separate concerns and improve maintainability.
* Default values are provided for optional fields to simplify adding new players.
* All API endpoints are working and fully tested with POSTMAN and the HTML dashboard.


## Applied design patterns
* **Factory method :** we have created a class named DictFactory to help create dictionaries for different classes such as member, event or subscription. This class contains a static method named create_dict that takes two parameter.The first one is the type of class we want to convert into dict ("member" or "event" or "subscription"). The second one is the object we want to convert. The function returns a dictionary of this class.
```python
import sys


class DictFactory:
    @staticmethod
    def create_dict(type,element):
        if type == "member":
            return {
                "id": element.id,
                "name": element.name,
                "email": element.email,
                "age": element.age,
                "phone": element.phone,
                "category": element.category,
                "address": element.address,
                "join_date": element.join_date,
                "positions": element.positions,
                "skills": element.skills,
                "subscription_status": element.subscription_status
            }
        elif type == "event":
            return {
                "id": element.id,
                "name": element.name,
                "date": element.date,
                "e_type": element.e_type,
                "organizer": element.organizer,
                "oponent": element.opponent,
                "result": element.result,
                "players": element.players,
                "duration": element.duration
            }
        elif type == "subscription":
            return {
                "id": element.id,
                "player_id": element.player_id,
                "date": element.date,
                "status": element.status,
                "amount": element.amount,
                "duration": element.duration,
                "player": DictFactory.create_dict("member",element.player) if element.player else None
            }
        else :
            print("Bad element : " + type)
            sys.exit()
```
applying this design pattern helped us convert objects into dict to send them as API response
```python
@app.get("/subscriptions")
def list_subscriptions():
    try:
        result = sub_controller.list_subscriptions()
        return jsonify([dict_factory.create_dict("subscription",s) for s in result])
    except Exception as e:
        return jsonify({"status": "error", "message": "Something went wrong"}), 500
```
* **Builder Pattern :**
We have created a class named SubscriptionBuilder to build a subscription object. The class contains a bunch of setter methods (set_player_id(), set_status()...) and a build method to build that class. The build method returns a Subscription object.
```python
from models.subscription import Subscription


class SubscriptionBuilder:
    def __init__(self):
        self.player_id = None,
        self.date = None,
        self.status = "Unpaid",
        self.amount = None,
        self.duration = None

    def set_player_id(self, player_id):
        self.player_id = player_id
        return self

    def set_date(self, date):
        self.date = date
        return self

    def set_status(self, status):
        self.status = status
        return self

    def set_amount(self, amount):
        self.amount = amount
        return self

    def set_duration(self, duration):
        self.duration = duration
        return self

    def build(self):
        # Validate required fields
        if self.player_id is None:
            raise ValueError("player_id is required")
        if self.amount is None:
            raise ValueError("amount is required")
        if self.date is None:
            raise ValueError("date is required")
        if self.duration is None:
            raise ValueError("duration is required")

        return Subscription(
            id = 0,
            player_id=self.player_id,
            date=self.date,
            status=self.status,
            amount=self.amount,
            duration=self.duration
        )
```
applying this design pattern helped us convert data from request body to a subscription object.
```python
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
```

# API Documentation
This API docs will explain each endpoint including endpoint url, request type (GET, POST or DELETE), request body and the response (case the http request success).
## Get all players

### Request
```http
GET http://127.0.0.1:5000/players
```

### Response
```json
    [
    {
        "address": "Djebahia",
        "age": 25,
        "category": "Senior",
        "email": "fares.mdhh@example.com",
        "id": 0,
        "join_date": "2025-11-18",
        "name": "Fares Meddahi",
        "phone": "+1234567890",
        "positions": [
            "Forward",
            "Midfielder"
        ],
        "skills": [
            "Dribbling",
            "Passing",
            "Speed"
        ],
        "subscription_status": "Paid"
    }
]
```

## Get player with id

### Request
```http
GET http://127.0.0.1:5000/players/<id>
```

### Response
```json
{
    "address": "Djebahia",
    "age": 25,
    "category": "Senior",
    "email": "fares.mdhh@example.com",
    "id": 1,
    "join_date": "2025-11-18",
    "name": "Fares Meddahi",
    "phone": "+1234567890",
    "positions": [
        "Forward",
        "Midfielder"
    ],
    "skills": [
        "Dribbling",
        "Passing",
        "Speed"
    ],
    "subscription_status": "Paid"
}
```

## Insert player

### Request
```http
POST http://127.0.0.1:5000/players
```

### Request body

```json
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 22,
    "phone": "+1234567890",
    "category": "Cadets",
    "address": "123 Main Street",
    "join_date": "2025-11-18",
    "positions": ["Forward", "Midfielder"],
    "skills": ["Dribbling", "Passing", "Shooting"],
    "subscription_status": "Paid"
}
```

### Response
```json
{
    "status": "ok"
}
```

## Delete player
### Request
```http
DELETE http://127.0.0.1:5000/players/<player_id>
```

### Response
```json
{
    "status": "ok"
}
```

## Search using name, skills and positions
### Request
```http
GET http://127.0.0.1:5000/players/search/<query>
```

### Response
```json
[
    {
        "address": "Djebahia",
        "age": 25,
        "category": "Senior",
        "email": "fares.mdhh@example.com",
        "id": 0,
        "join_date": "2025-11-18",
        "name": "Fares Meddahi",
        "phone": "+1234567890",
        "positions": [
            "Forward",
            "Midfielder"
        ],
        "skills": [
            "Dribbling",
            "Passing",
            "Speed"
        ],
        "subscription_status": "Paid"
    }
]
```

## Get all events
### Request
```http
GET http://127.0.0.1:5000/events
```

### Response
```json
[
    {
        "date": "2025-12-15",
        "duration": "90",
        "e_type": "Match",
        "id": 1,
        "name": "Match Seniors 01",
        "oponent": "ABRD",
        "organizer": "FAF",
        "players": [
            {
                "category": "Senior",
                "id": 2,
                "name": "Fares Meddahi"
            },
            {
                "category": "Coach",
                "id": 1,
                "name": "Coatch Yacine"
            },
            {
                "category": "Senior",
                "id": 3,
                "name": "Dahmani Abdelhak"
            }
        ],
        "result": null
    },
    {
        "date": "2025-12-14",
        "duration": "60",
        "e_type": "Training",
        "id": 2,
        "name": "Training Seniors",
        "oponent": "",
        "organizer": "Coatch Yacine",
        "players": [
            {
                "category": "Coach",
                "id": 1,
                "name": "Coatch Yacine"
            },
            {
                "category": "Senior",
                "id": 3,
                "name": "Dahmani Abdelhak"
            },
            {
                "category": "Senior",
                "id": 2,
                "name": "Fares Meddahi"
            }
        ],
        "result": null
    }
]
```

## Insert new event
### Request
```http
POST http://127.0.0.1:5000/events
```

### Request body
```json
{
    "name":"Event name",
    "date":"event date",
    "e_type":"Match",
    "organizer":"Organiser name",
    "result":"Win",
    "opponent":"Oponnent name",
    "duration":"90 min"
}
```

### Response
```json
{
    "status": "ok"
}
```

## Register player in event
### Request
```http
POST http://127.0.0.1:5000/events/<event_id>/register/<player_id>
```

### Response
```json
{
    "status": "ok"
}
```



## Unregister player in event
### Request
```http
POST http://127.0.0.1:5000/events/<event_id>/unregister/<player_id>
```

### Response
```json
{
    "status": "ok"
}
```




## Delete event
### Request
```http
DELETE http://127.0.0.1:5000/events/<event_id>
```

### Response
```json
{
    "status": "ok"
}
```

## Get all subscriptions
### Request
```http
GET http://127.0.0.1:5000/subscriptions
```

### Response
```json
[
    {
        "amount": 1000.0,
        "date": "2025-12-01",
        "duration": 30,
        "id": 1,
        "player": {
            "address": "Djebahia Bouira",
            "age": 35,
            "category": "Coach",
            "email": "yacine@email.dz",
            "id": 1,
            "join_date": "2025-01-12",
            "name": "Coatch Yacine",
            "phone": "0555555555",
            "positions": [],
            "skills": [],
            "subscription_status": "Paid"
        },
        "player_id": 1,
        "status": "Paid"
    },
    {
        "amount": 1200.0,
        "date": "2025-11-11",
        "duration": 30,
        "id": 2,
        "player": {
            "address": "Djebahi Bouira",
            "age": 25,
            "category": "Senior",
            "email": "fares.meddahi@univ-bouira.dz",
            "id": 2,
            "join_date": "2020-01-15",
            "name": "Fares Meddahi",
            "phone": "0558015936",
            "positions": [],
            "skills": [],
            "subscription_status": "Paid"
        },
        "player_id": 2,
        "status": "Paid"
    },
    {
        "amount": 1200.0,
        "date": "2025-12-12",
        "duration": 30,
        "id": 3,
        "player": {
            "address": "Ain Chriki Djebahia Bouira",
            "age": 22,
            "category": "Senior",
            "email": "dahmani.abdou@gmail.com",
            "id": 3,
            "join_date": "2021-03-21",
            "name": "Dahmani Abdelhak",
            "phone": "0555555555",
            "positions": [],
            "skills": [],
            "subscription_status": "Unpaid"
        },
        "player_id": 3,
        "status": "Paid"
    }
]
```

## Insert new subscription
### Request
```http
POST http://127.0.0.1:5000/subscriptions
```

### Request body
```json
{
    "player_id":"2",
    "date":"event date",
    "status":"Paid",
    "amount":"1000",
    "duration":"30"
}
```

### Response
```json
{
    "status": "ok"
}
```