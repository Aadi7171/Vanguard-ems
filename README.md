# Vanguard-EMS

A high-concurrency coordination engine that "patches" the chaotic reality of Indian traffic by transforming emergency response into a real-time distributed systems problem.

## System Flow
1. **Ingest (The Reality):** Captures real-time ambulance trajectories via GPS and processes environment snapshots through Google Gemini to identify physical roadblocks.
2. **Process (The Coordination):** Uses a SpacetimeDB-inspired shared state across all nodes, while ArmorIQ validates every proposed path against "Hard Rules".
3. **Output (The Patch):** Triggers dynamic green-waves at signal controllers and logs all performance metrics in MongoDB Atlas.

## How to Run
Run the `run.bat` file on Windows, or manually start the backend, simulator, and frontend dashboard individually.
