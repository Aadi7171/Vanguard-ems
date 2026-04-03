// Map Initialization
const map = L.map('map').setView([28.5670, 77.2100], 15);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

// Custom Icons
const ambulanceIcon = L.icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});

const redSignalIcon = L.icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});

const greenSignalIcon = L.icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});

const blockedSignalIcon = L.icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-violet.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});

// State
let ambulanceMarker = null;
let signalMarkers = {};

// DOM Elements
const wsStatus = document.getElementById('ws-status-badge');
const logList = document.getElementById('log-list');
const hudSignal = document.getElementById('hud-signal');

function addLog(message, type = 'normal') {
    const li = document.createElement('li');
    li.textContent = `[${new Date().toLocaleTimeString()}] ${message}`;
    if (type) li.classList.add(type);
    logList.prepend(li);
    
    // Keep only last 20 logs
    if (logList.children.length > 20) {
        logList.removeChild(logList.lastChild);
    }
}

// WebSocket Connection
function connectWebSocket() {
    const ws = new WebSocket('ws://localhost:8000/ws');

    ws.onopen = () => {
        wsStatus.textContent = 'CONNECTED';
        wsStatus.className = 'value success';
        addLog('SpacetimeDB Sync Established', 'normal');
    };

    ws.onclose = () => {
        wsStatus.textContent = 'DISCONNECTED';
        wsStatus.className = 'value warning';
        addLog('Connection lost. Retrying in 3s...', 'blocked');
        setTimeout(connectWebSocket, 3000);
    };

    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        
        if (data.type === 'world_state_update') {
            updateWorldState(data);
        }
    };
}

let lastSignalStates = {};

function updateWorldState(data) {
    // 1. Update Ambulance
    if (!ambulanceMarker) {
        ambulanceMarker = L.marker([data.ambulance.lat, data.ambulance.lng], {icon: ambulanceIcon}).addTo(map);
    } else {
        ambulanceMarker.setLatLng([data.ambulance.lat, data.ambulance.lng]);
    }
    
    // Auto pan to ambulance
    map.panTo([data.ambulance.lat, data.ambulance.lng], {animate: true, duration: 0.5});

    // 2. Update Signals
    data.signals.forEach(sig => {
        let iconToUse = redSignalIcon;
        
        if (sig.state === 'green') {
            iconToUse = greenSignalIcon;
            if (lastSignalStates[sig.id] !== 'green') {
                addLog(`GREEN WAVE trigged at ${sig.id}`, 'green-wave');
                hudSignal.textContent = `CLEARING ${sig.id} (GREEN-WAVE)`;
                hudSignal.style.color = '#22c55e';
            }
        } else if (sig.state === 'blocked_red') {
            iconToUse = blockedSignalIcon;
            if (lastSignalStates[sig.id] !== 'blocked_red') {
                addLog(`ARMOR-IQ BLOCK at ${sig.id}! Pedestrians detected.`, 'blocked');
                hudSignal.textContent = `AUTHORITY DENIED ON ${sig.id} (PEDESTRIANS)`;
                hudSignal.style.color = '#ef4444';
            }
        } else {
            // normal red
            if (lastSignalStates[sig.id] === 'green' || lastSignalStates[sig.id] === 'blocked_red') {
                hudSignal.textContent = `SCANNING AHEAD...`;
                hudSignal.style.color = '#f8fafc';
            }
        }
        
        lastSignalStates[sig.id] = sig.state;
        
        if (!signalMarkers[sig.id]) {
            signalMarkers[sig.id] = L.marker([sig.lat, sig.lng], {icon: iconToUse}).addTo(map);
            signalMarkers[sig.id].bindPopup(`<b>${sig.id}</b><br>State: ${sig.state}`);
        } else {
            signalMarkers[sig.id].setIcon(iconToUse);
            signalMarkers[sig.id].setPopupContent(`<b>${sig.id}</b><br>State: ${sig.state}`);
        }
    });
}

// Start
connectWebSocket();
