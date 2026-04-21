# 🚑 Vanguard-EMS

> A high-concurrency emergency coordination engine that transforms ambulance response in Indian traffic into a real-time distributed systems problem.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688.svg)](https://fastapi.tiangolo.com)

---

## 🧠 Overview

Vanguard-EMS is a real-time Emergency Management System designed to tackle the chaotic nature of Indian urban traffic. It coordinates ambulance routing and traffic signal management through a combination of AI-powered environment analysis, distributed state synchronization, and rule-validated path planning — all working together to reduce emergency response times.

---

## ⚙️ System Architecture

The system is composed of three major layers:

### 1. Ingest — *The Reality*
- Captures live ambulance GPS trajectories in real time.
- Processes environment snapshots using **Google Gemini** to detect physical roadblocks, congestion, and obstacles.

### 2. Process — *The Coordination*
- Maintains a **SpacetimeDB-inspired shared state** across all system nodes, ensuring every service has a consistent world view.
- **ArmorIQ** validates every proposed route against a set of "Hard Rules" — safety constraints that cannot be overridden.

### 3. Output — *The Patch*
- Triggers **dynamic green-waves** at traffic signal controllers along the ambulance's path.
- Logs all performance metrics and routing decisions to **MongoDB** for observability and post-analysis.

---

## 🗂️ Project Structure

```
Vanguard-ems/
├── backend/                  # Core coordination engine (Python/FastAPI)
├── frontend/                 # Real-time dashboard (HTML/CSS/JavaScript)
├── simulator/                # Ambulance GPS simulator
│   └── ambulance_driver.py
├── tests/                    # Automated test suite
│   └── test_backend.py
├── Dockerfile                # Backend image
├── Dockerfile.simulator      # Lightweight simulator image
├── docker-compose.yml
├── requirements.txt          # Backend dependencies (pinned)
├── requirements.simulator.txt
├── pytest.ini
├── .env.example              # Template for environment variables
├── .gitignore
├── run.bat                   # Quick start — Windows
├── run.sh                    # Quick start — Linux/macOS
├── LICENSE
└── CONTRIBUTING.md
```

---

## 🛠️ Tech Stack

| Layer          | Technology                   |
|----------------|------------------------------|
| Backend        | Python 3.10, FastAPI 0.111   |
| Frontend       | HTML, CSS, JavaScript        |
| AI / Vision    | Google Gemini API            |
| Database       | MongoDB 7.0                  |
| Containerisation | Docker, Docker Compose     |
| Simulation     | Custom Python ambulance driver |

---

## 🚀 Getting Started

### Prerequisites
- [Docker](https://www.docker.com/) and Docker Compose
- A **Google Gemini API key** — get one at [aistudio.google.com](https://aistudio.google.com/app/apikey)

### 1. Clone the Repository

```bash
git clone https://github.com/Aadi7171/Vanguard-ems.git
cd Vanguard-ems
```

### 2. Set Environment Variables

```bash
cp .env.example .env
# Open .env in your editor and fill in GEMINI_API_KEY
```

### 3. Run with Docker Compose

```bash
docker compose up --build
```

This starts three services:
- **backend** — FastAPI server on port `8000`
- **mongo** — MongoDB 7.0 on port `27017`
- **simulator** — Ambulance GPS driver feeding live position data to the backend

The simulator automatically waits for the backend to be healthy before starting.

### 4. Quick Start Scripts

**Windows:**
```
run.bat
```

**Linux / macOS:**
```bash
chmod +x run.sh
./run.sh
```

### 5. Access the Dashboard

```
http://localhost:8000
```

---

## 🧩 Manual Service Startup (without Docker)

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\activate       # Windows

pip install -r requirements.txt

# Start the backend
python -m backend.main

# In a second terminal — start the simulator
python simulator/ambulance_driver.py

# Open frontend/index.html in your browser
```

---

## 🔒 Environment Variables

| Variable       | Description                                        |
|----------------|----------------------------------------------------|
| `GEMINI_API_KEY` | Google Gemini API key for AI/vision processing   |
| `MONGO_URI`    | MongoDB connection string (local or Atlas)         |

See `.env.example` for the full template.

---

## 🧪 Running Tests

```bash
pip install pytest pytest-asyncio httpx
pytest tests/ -v
```

---

## 📊 Features

- **Real-time GPS ingestion** from ambulance units
- **AI-powered roadblock detection** via Google Gemini
- **Distributed shared state** across all coordination nodes
- **Rule-validated path planning** with ArmorIQ hard constraints
- **Dynamic green-wave signaling** for traffic lights along the route
- **Performance metrics logging** to MongoDB
- **Live dashboard** for monitoring active emergencies

---

## 🐳 Docker Services

| Service   | Image               | Port  |
|-----------|---------------------|-------|
| backend   | Custom Python 3.10  | 8000  |
| mongo     | `mongo:7.0`         | 27017 |
| simulator | Custom Python 3.10  | —     |

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup instructions, coding style, and how to submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Aadi7171** — [GitHub Profile](https://github.com/Aadi7171)
