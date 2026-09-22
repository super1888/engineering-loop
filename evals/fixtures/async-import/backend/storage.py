from contextlib import closing
import sqlite3


def connect(path):
    connection = sqlite3.connect(path, timeout=10)
    connection.row_factory = sqlite3.Row
    connection.execute('PRAGMA foreign_keys = ON')
    return connection


def initialize(path):
    with closing(connect(path)) as connection, connection:
        connection.executescript('''
            CREATE TABLE IF NOT EXISTS batches (
                id TEXT PRIMARY KEY, request_id TEXT UNIQUE NOT NULL,
                payload TEXT NOT NULL, status TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS items (
                batch_id TEXT NOT NULL REFERENCES batches(id), row_id TEXT NOT NULL,
                name TEXT NOT NULL, status TEXT NOT NULL, attempts INTEGER NOT NULL DEFAULT 0,
                error TEXT, output TEXT, PRIMARY KEY (batch_id, row_id)
            );
            CREATE TABLE IF NOT EXISTS records (
                batch_id TEXT NOT NULL, row_id TEXT NOT NULL, name TEXT NOT NULL,
                PRIMARY KEY (batch_id, row_id)
            );
            CREATE TABLE IF NOT EXISTS retry_requests (
                batch_id TEXT NOT NULL, request_id TEXT NOT NULL,
                PRIMARY KEY (batch_id, request_id)
            );
        ''')
