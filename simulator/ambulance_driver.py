import asyncio
import websockets
import json

async def drive_ambulance():
    uri = "ws://localhost:8000/ws"
    
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected to Vanguard-EMS Engine")
            
            # Start position
            lat = 28.5670
            lng = 77.2100
            
            while True:
                # Move towards destination slightly every second
                lat += 0.0002
                lng += 0.0001
                
                payload = {
                    "type": "ambulance_telemetry",
                    "id": "AMB-01",
                    "lat": lat,
                    "lng": lng,
                    "sensors": {
                        # We could randomly inject pedestrian_detected here if we wanted to dynamically trigger ArmorIQ
                        "pedestrian_detected": False,
                        "intersection_clearance": 0.9
                    }
                }
                
                await websocket.send(json.dumps(payload))
                print(f"[Simulated GPS] Pushed coords: {lat:.5f}, {lng:.5f}")
                
                await asyncio.sleep(1)  # Drive tick
                
                # Reset if it goes too far to loop the demo
                if lat > 28.5800:
                    lat = 28.5670
                    lng = 77.2100
                    
    except ConnectionRefusedError:
        print("Backend not running. Please start the FastAPI server on port 8000 first.")
        
if __name__ == "__main__":
    asyncio.run(drive_ambulance())
