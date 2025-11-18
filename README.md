# Football Club Management System

This project is a **Football Club Management System** built using the **MVC (Model-View-Controller)** architecture. It provides a REST API for managing players only **(for now)** and allows interaction through a simple HTML dashboard.

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

---

## Getting Started

1. **Run the backend API**

   ```bash
   python app.py
   ```

   The API will start at `http://localhost:5000`.

2. **Open the dashboard**
   Open `index.html` in a web browser to manage players through a simple interface.

3. **Use the API directly (optional)**
   You can also interact with the API using tools like **Postman** or **curl**.

---

## Project Structure

* `models/` – Data models (Player, Event...)
* `controllers/` – Handles business logic and database operations
* `views/` – HTML dashboard for managing players
* `db/db_helper.py` – SQLite helper to init and create db if not exists
* `app.py` – Main Flask application and route definitions
* `app.db` – The SQLite database file (Delete it and you will lose your data)

---

## Notes

* The project follows **MVC design patterns** to separate concerns and improve maintainability.
* Default values are provided for optional fields to simplify adding new players.
* We will add new API routes later and upgrade the dashboard to test all the API endpoints.


# API Documentation
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