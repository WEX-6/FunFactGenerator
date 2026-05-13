import os
import sqlite3

class SQLiteConnectionProvider:
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = os.getenv("SQLITE_DB_PATH", "facts.db")
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row  # Enable column access by name
    
    def cursor(self):
        return self.conn.cursor()
    
    def commit(self):
        self.conn.commit()
    
    def close(self):
        self.conn.close()
