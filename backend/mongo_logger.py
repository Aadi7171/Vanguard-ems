from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import datetime

MONGO_URI = "mongodb://localhost:27017/"  # Change to Atlas URI for final deployment

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
    # Check if really connected
    client.admin.command('ping')
    db = client["vanguard_ems"]
    logs_collection = db["emergency_logs"]
    _mongo_connected = True
except Exception:
    _mongo_connected = False
    print("Warning: MongoDB not running locally. Logs will be stored in-memory for the demo.")

_fallback_logs = []

def log_event(event_type: str, data: dict):
    doc = {
        "event_type": event_type,
        "timestamp": datetime.datetime.utcnow(),
        "data": data
    }
    
    if _mongo_connected:
        try:
            logs_collection.insert_one(doc)
        except Exception:
            _fallback_logs.append(doc)
    else:
        _fallback_logs.append(doc)
        print(f"[MOCK MONGO] Logged: {event_type} - {data}")
