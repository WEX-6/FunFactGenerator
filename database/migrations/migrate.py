import sqlite3
import os

db_path = os.getenv("SQLITE_DB_PATH", "facts.db")
conn = sqlite3.connect(db_path)

# Made category nullable to avoid conflict in earlier tasks
with conn:
    cur = conn.cursor()
    cur.execute("""
        DROP TABLE IF EXISTS facts;
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS facts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fact TEXT NOT NULL,
            likes INTEGER DEFAULT 0,
            dislikes INTEGER DEFAULT 0,
            category TEXT
        );
    """)
    cur.execute("""
        INSERT INTO facts (fact, category) VALUES
        ('Honey never spoils.', 'food'),
        ('Bananas are berries.', 'food'),
        ('Octopuses have three hearts.', 'animal'),
        ('A group of flamingos is called a "flamboyance".', 'animal'),
        ('The Eiffel Tower can be 15 cm taller during hot days.', 'architecture');
    """)
    print("Migration complete: facts table created and sample data inserted.")

conn.close()
