import sqlite3
def get_connection() -> sqlite3.Connection:
    return sqlite3.connect("todo.db")