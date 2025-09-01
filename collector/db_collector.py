# collector/db_collector.py

import sqlite3
from storage import db
from .base_collector import BaseCollector

class DBCollector(BaseCollector):
    def __init__(self, db_path: str):
        super().__init__("DBCollector")
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def execute(self, query: str, params: tuple = ()):
        query_type = query.strip().split()[0].upper()

        if query_type == "SELECT":
            db.insert_event("database", "read", query)
        elif query_type in ("INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER"):
            db.insert_event("database", "write", query)

        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor

    def start(self):
        print("[DBCollector] Ready to intercept queries.")

    def stop(self):
        print("[DBCollector] Closing DB connection.")
        self.conn.close()
