import sqlite3

class SqLiteHelper:
    def __init__(self):
        self.conn = sqlite3.connect("app.db")
        self.conn.row_factory = sqlite3.Row

    def get_connection(self):
        conn = sqlite3.connect("app.db", check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                phone TEXT NOT NULL,
            
                category TEXT NOT NULL CHECK (
                    category IN ('Cadets', 'Juniors', 'Senior')
                ),
            
                address TEXT NOT NULL,
                join_date TEXT NOT NULL,       -- use 'YYYY-MM-DD'
            
                positions TEXT NOT NULL,       -- JSON array
                skills TEXT NOT NULL,          -- JSON array
            
                subscription_status TEXT NOT NULL CHECK (
                    subscription_status IN ('Unpaid', 'Paid')
                )
            );
        """)
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date TEXT NOT NULL,                     -- stored as YYYY-MM-DD
                organizer TEXT NOT NULL,
            
                players TEXT NOT NULL,                  -- JSON array: ["101","102",...], currently "[]"
            
                type TEXT NOT NULL CHECK (              -- only two types
                    type IN ('Match', 'Training')
                ),
            
                opponent TEXT,                          -- NULL for training
                result TEXT CHECK (                     -- match results only
                    result IN ('Win', 'Lose', 'Draw') OR result IS NULL
                ),
            
                duration TEXT                           -- "1 hour", "2 hours", etc., NULL for matches
            );
        """)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
            
                player_id INTEGER NOT NULL,
                date TEXT NOT NULL,              -- YYYY-MM-DD
            
                status TEXT NOT NULL CHECK (
                    status IN ('Paid', 'Unpaid')
                ),
            
                amount REAL NOT NULL,           -- subscription fee (0 for Unpaid)
                duration INTEGER NOT NULL,      -- days or months (you are using: 30)
            
                FOREIGN KEY (player_id) REFERENCES players(id)
            );
        """)
        self.conn.commit()