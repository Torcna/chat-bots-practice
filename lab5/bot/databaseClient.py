import json
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()


def recreate_db() -> None:
    connection = sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH"))
    with connection:
        connection.execute("DROP TABLE IF EXISTS telegram_updates")
        connection.execute(
            """
                           CREATE TABLE IF NOT EXISTS telegram_updates
                           (
                                id INTEGER PRIMARY KEY,
                                payload TEXT NOT NULL
                           )
                           """
        )
        connection.execute(
                """
                CREATE TABLE IF NOT EXISTS users
                (
                    id INTEGER PRIMARY KEY,
                    telegram_id INTEGER NOT NULL UNIQUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    state TEXT DEFAULT NULL,
                    ordet_json TEXT DEFAULT NULL
                )
                """,
            )
    connection.close()


def persistUpdate(update: dict) -> None:
    payload = json.dumps(update, ensure_ascii=False, indent=2)
    with sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH")) as connection:
        with connection:
            connection.execute(
                "INSERT INTO telegram_updates (payload) VALUES (?)", (payload,)
            )

def ensure_user_exists(telegram_id: int) -> None:
    """Ensure a user with the given telegram_id exists in the users table.
    If the user doesn't exist, create them. All operations happen in a single transaction."""
    with sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH")) as connection:
        with connection:
            # Check if user exists
            cursor = connection.execute(
                "SELECT 1 FROM users WHERE telegram_id = ?", (telegram_id,)
            )

            # If user doesn't exist, create them
            if cursor.fetchone() is None:
                connection.execute(
                    "INSERT INTO users (telegram_id) VALUES (?)", (telegram_id,)
                )