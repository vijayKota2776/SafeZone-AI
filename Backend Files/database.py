import sqlite3

def init_db():
    conn = sqlite3.connect('safezone.db')
    cursor = conn.cursor()
    cursor.execute(
        import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('safezone.db')
cursor = conn.cursor()

# Create the alerts table if it doesn't exist
cursor.execute(
    CREATE TABLE IF NOT EXISTS alerts (
        user_id INTEGER,
        alert_level INTEGER,
        last_alert_time TEXT
    )
)

# Commit changes and close the connection
conn.commit()
conn.close()
        )
    conn.commit()
    conn.close()

import sqlite3

def init_db():
    conn = sqlite3.connect('safezone.db')
    cursor = conn.cursor()
    cursor.execute(
        CREATE TABLE IF NOT EXISTS alerts (
            user_id INTEGER,
            alert_level INTEGER,
            last_alert_time TEXT
        )
    )
    conn.commit()
    conn.close()