import time
import math

class SpacetimeState:
    def __init__(self):
        # Starting point near AIIMS New Delhi for realism
        self.ambulance_state = {
            "lat": 28.5670, 
            "lng": 77.2100,
            "id": "AMB-01"
        }
        
        # Mucking up some static traffic lights along a dummy route in Delhi
        self.traffic_signals = {
            "SIG-1": {"id": "SIG-1", "lat": 28.5680, "lng": 77.2110, "state": "red", "distance": None, "pedestrian_blocked": False},
            "SIG-2": {"id": "SIG-2", "lat": 28.5700, "lng": 77.2120, "state": "red", "distance": None, "pedestrian_blocked": False},
            "SIG-3": {"id": "SIG-3", "lat": 28.5730, "lng": 77.2140, "state": "red", "distance": None, "pedestrian_blocked": True}, # Simulating a block
        }
        
    def update_ambulance_location(self, lat, lng):
        self.ambulance_state["lat"] = lat
        self.ambulance_state["lng"] = lng
        
        # Calculate distances to all signals
        for sig_id, sig in self.traffic_signals.items():
            dist = math.sqrt((sig["lat"] - lat)**2 + (sig["lng"] - lng)**2)
            sig["distance"] = dist
            
            # If the ambulance passed the light, turn it back to red
            if dist > 0.005 and sig["state"] == "green":
                sig["state"] = "red"
                
    def get_upcoming_signals(self):
        # Return signals that are close (e.g. within 0.003 coordinate degrees)
        upcoming = []
        for sig_id, sig in self.traffic_signals.items():
            if sig["distance"] is not None and sig["distance"] < 0.003 and sig["state"] != "green":
                upcoming.append(sig)
        return upcoming
        
    def set_signal_green(self, sig_id):
        if sig_id in self.traffic_signals:
            self.traffic_signals[sig_id]["state"] = "green"
            
    def set_signal_blocked(self, sig_id):
        if sig_id in self.traffic_signals:
            self.traffic_signals[sig_id]["state"] = "blocked_red"
            
    def get_world_state(self):
        return {
            "type": "world_state_update",
            "ambulance": self.ambulance_state,
            "signals": list(self.traffic_signals.values()),
            "timestamp": time.time()
        }
