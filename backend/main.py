from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import json
import asyncio
from backend.spacetime_sync import SpacetimeState
from backend.armor_iq_validator import validate_safety_rules
from backend.mongo_logger import log_event

app = FastAPI(title="Vanguard-EMS Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

state = SpacetimeState()

connected_clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            payload = json.loads(data)
            
            # Simulated GPS ping from ambulance simulator
            if payload.get("type") == "ambulance_telemetry":
                lat = payload["lat"]
                lng = payload["lng"]
                
                # Update Spacetime mock state
                state.update_ambulance_location(lat, lng)
                
                # Check for signals ahead and try to clear them
                upcoming_signals = state.get_upcoming_signals()
                
                for signal in upcoming_signals:
                    # ArmorIQ Safety Validation
                    is_safe = validate_safety_rules(signal, payload.get("sensors", {}))
                    
                    if is_safe:
                        state.set_signal_green(signal["id"])
                        log_event("green_wave_triggered", {"signal_id": signal["id"], "ambulance": payload["id"]})
                    else:
                        state.set_signal_blocked(signal["id"])
                        log_event("green_wave_blocked", {"signal_id": signal["id"], "reason": "ArmorIQ Safety Violation"})

            # Broadcast updated state to all clients (the frontend dashboard)
            current_state = state.get_world_state()
            for client in connected_clients:
                await client.send_text(json.dumps(current_state))
                
    except WebSocketDisconnect:
        connected_clients.remove(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
