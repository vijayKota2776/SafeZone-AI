from celery import Celery
from datetime import datetime, timedelta
import requests
import sqlite3

celery = Celery("tasks", broker="redis://localhost:6379/0")

@celery.task
def escalate_alert(user_id):
    conn = sqlite3.connect('safezone.db')
    cursor = conn.cursor()
    cursor.execute("SELECT alert_level, last_alert_time FROM alerts WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    if row:
        alert_level, last_alert_time = row
        if datetime.now() >= datetime.strptime(last_alert_time, '%Y-%m-%d %H:%M:%S') + timedelta(minutes=3):
            alert_level += 1
            send_alert(alert_level, user_id)
            cursor.execute("UPDATE alerts SET alert_level = ?, last_alert_time = ? WHERE user_id = ?", 
                           (alert_level, datetime.now(), user_id))
            conn.commit()
    conn.close()

def send_alert(level, user_id):
    # Replace with actual SMS/Call/Notification API
    if level == 1:
        print(f"Alert Level 1: Notify parents of user {user_id}.")
    elif level == 2:
        print(f"Alert Level 2: Notify user {user_id}.")
    elif level == 3:
        print(f"Alert Level 3: Notify police for user {user_id}.")