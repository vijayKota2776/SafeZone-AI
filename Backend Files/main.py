from fastapi import FastAPI
from pydantic import BaseModel
import requests
from database import init_db
from tasks import escalate_alert

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def startup():
    init_db()

class TrackingRequest(BaseModel):
    user_id: int
    start_location: tuple
    end_location: tuple
    battery_level: int

@app.post("/start_tracking")
async def start_tracking(request: TrackingRequest):
    # Calculate estimated time using Google Maps API
    travel_time = get_estimated_time(request.start_location, request.end_location);
    
    # Send battery level alert
    if request.battery_level < 20:
        send_notification("Battery is low", request.user_id)

    # Store travel details in the database (mocked function here)
    store_alert_data(request.user_id, travel_time)

    return {"travel_time": travel_time}

def get_estimated_time(start_location, end_location):
    # Replace with actual API key and URL
    response = requests.get("https://maps.googleapis.com/maps/api/directions/json", params={
        "origin": start_location,
        "destination": end_location,
        "mode": "walking",
        "key": "YOUR_GOOGLE_MAPS_API_KEY"
    })
    result = response.json()
    return result["routes"][0]["legs"][0]["duration"]["value"]  # ETA in seconds

def send_notification(message, user_id):
    # Implement notification sending (e.g., SMS or email)
    print(f"Notification to {user_id}: {message}")

def store_alert_data(user_id, travel_time):
    # Mock implementation for storing alert data
    print(f"Storing alert data for user {user_id} with travel time {travel_time} seconds.")