"""Small, deliberately incomplete baseline for an isolated behavioral exercise."""

import sqlite3


class Inventory:
    def __init__(self, path):
        self.db = sqlite3.connect(path, timeout=5)
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id TEXT PRIMARY KEY,
                ordered INTEGER NOT NULL,
                received INTEGER NOT NULL DEFAULT 0
            );
            CREATE TABLE IF NOT EXISTS receipts (
                request_id TEXT PRIMARY KEY,
                order_id TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                result INTEGER NOT NULL
            );
        """)

    def create_order(self, order_id, ordered):
        with self.db:
            self.db.execute("INSERT INTO orders(order_id, ordered) VALUES (?, ?)",
                            (order_id, ordered))

    def received(self, order_id):
        row = self.db.execute("SELECT received FROM orders WHERE order_id = ?",
                              (order_id,)).fetchone()
        if row is None:
            raise KeyError(order_id)
        return row[0]

    def receive(self, order_id, quantity, request_id):
        with self.db:
            self.db.execute("UPDATE orders SET received = received + ? WHERE order_id = ?",
                            (quantity, order_id))
        return self.received(order_id)

    def close(self):
        self.db.close()
