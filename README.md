# 🚑 Vanguard-EMS

> A high-concurrency emergency coordination engine that transforms ambulance response in Indian traffic into a real-time distributed systems problem.

<div align="center">

[![Live Demo](https://img.shields.io/badge/🌐_Website-Live_Demo-e63a2e?style=for-the-badge)](https://aadi7171.github.io/Vanguard-ems)
[![GitHub Stars](https://img.shields.io/github/stars/Aadi7171/Vanguard-ems?style=for-the-badge&color=1de9b6)](https://github.com/Aadi7171/Vanguard-ems/stargazers)
[![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb)](https://www.mongodb.com/atlas)

**[🌐 Live Demo & Website](https://aadi7171.github.io/Vanguard-ems)** · **[📋 Report Bug](https://github.com/Aadi7171/Vanguard-ems/issues)** · **[✨ Request Feature](https://github.com/Aadi7171/Vanguard-ems/issues)**

</div>

---

## 🌐 Website & Live Demo

The project website with an interactive live demo is available at:

**👉 [https://aadi7171.github.io/Vanguard-ems](https://aadi7171.github.io/Vanguard-ems)**

The website includes:
- **Animated live demo** — simulated dashboard showing ambulance routing, green-wave signals, and real-time log output
- **Feature overview** — breakdown of all system capabilities
- **Architecture diagram** — the 3-layer system explained visually
- **Tech stack table** — full list of technologies used
- **Quickstart guide** — get running in 4 steps

> To deploy the website yourself, place `index.html` in the `docs/` folder of your repo and enable GitHub Pages in the repository settings.

---

## 🧠 Overview

Vanguard-EMS is a real-time Emergency Management System (EMS) designed to tackle the chaotic nature of Indian urban traffic. It coordinates ambulance routing and traffic signal management through a combination of AI-powered environment analysis, distributed state synchronization, and rule-validated path planning — all working together to reduce emergency response times.

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
- Logs all performance metrics and routing decisions to **MongoDB Atlas** for observability and post-analysis.

---

## 🗂️ Project Structure

```
Vanguard-ems/
├── backend/              # Core coordination engine (Python/FastAPI)
├── frontend/             # Real-time dashboard (HTML/CSS/JavaScript)
├── simulator/            # Ambulance GPS simulator
│   └── ambulance_driver.py
├── docs/                 # ← GitHub Pages website (add index.html here)
│   └── index.html
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.bat
└── .gitignore
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.10, FastAPI |
| Frontend | HTML, CSS, JavaScript |
| AI / Vision | Google Gemini API |
| Database | MongoDB (Atlas / local) |
| Containerization | Docker, Docker Compose |
| Simulation | Custom Python ambulance driver |

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

## 🚀 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) and Docker Compose installed
- A **Google Gemini API key**
- (Optional) A MongoDB Atlas URI, or use the local MongoDB container

### 1. Clone the Repository

```bash
git clone https://github.com/Aadi7171/Vanguard-ems.git
cd Vanguard-ems
```

### 2. Set Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
MONGO_URI=mongodb://mongo:27017/   # or your Atlas URI
```

### 3. Run with Docker Compose

```bash
docker-compose up --build
```

This will start three services:

| Service | Description | Port |
|---|---|---|
| `backend` | FastAPI coordination server | `8000` |
| `mongo` | MongoDB instance | `27017` |
| `simulator` | Ambulance GPS driver | — |

### 4. Run on Windows (Quick Start)

Simply double-click or run:

```bat
run.bat
```

### 5. Access the Dashboard

Open your browser and navigate to:

```
http://localhost:8000
```

---

## 🧩 Manual Service Startup

If you prefer running services individually:

```bash
# Start the backend
python -m backend.main

# Start the simulator
python simulator/ambulance_driver.py

# Open the frontend
# Open frontend/index.html in your browser
```

---

## 🔒 Environment Variables

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Google Gemini API key for vision/AI processing |
| `MONGO_URI` | MongoDB connection string |

---

## 🐳 Docker Services

| Service | Image | Port |
|---|---|---|
| backend | Custom Python 3.10 | 8000 |
| mongo | `mongo:latest` | 27017 |
| simulator | Custom Python 3.10 | — |

---

## 🌐 Deploy the Website

To host the project website using GitHub Pages:

1. Copy `index.html` into a `docs/` folder at the root of the repository.
2. Go to **Settings → Pages** in your GitHub repository.
3. Under *Source*, select **Deploy from a branch**.
4. Choose `main` branch and `/docs` folder. Click **Save**.
5. Your site will be live at `https://aadi7171.github.io/Vanguard-ems`.

---

## 📄 License

This project does not currently specify a license. Please contact the author for usage permissions.

---

## 👤 Author

**Aadi7171** — [GitHub Profile](https://github.com/Aadi7171)

---

<div align="center">
  <sub>Built to patch the chaotic reality of Indian emergency response.</sub>
</div>
