import sqlite3
from datetime import datetime

def save_to_vault(user_input, responses):
    conn = sqlite3.connect("chat_vault.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_input TEXT,
            agent_name TEXT,
            response TEXT
        )
    """)

    for agent, response in responses.items():
        # Convert list or dict response to string for storage
        if isinstance(response, (list, dict)):
            response = str(response)

        cursor.execute("""
            INSERT INTO chat_logs (timestamp, user_input, agent_name, response)
            VALUES (?, ?, ?, ?)
        """, (datetime.now(), user_input, agent, response))

    conn.commit()
    conn.close()
