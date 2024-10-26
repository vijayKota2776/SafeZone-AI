from pydantic import BaseModel

class Alert(BaseModel):
    user_id: int
    alert_level: int
    last_alert_time: str