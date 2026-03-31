🖥️ Monitoring Dashboard

A real-time system monitoring dashboard built with Flask, Docker, and Chart.js, showing CPU, memory, disk usage, running Docker containers, and container logs dynamically.

Features
Real-time CPU, Memory, and Disk usage monitoring
Live updating charts using Chart.js
List of running Docker containers
Fetch logs from any container dynamically
Color-coded alerts for high CPU usage
Fully dockerized backend for easy deployment

Tech Stack
Backend: Flask, Python, PSUtil, Flask-CORS
Frontend: HTML, CSS, JavaScript, Chart.js
Containerization: Docker

Installation & Usage

1️⃣ Clone the repository
git clone https://github.com/yourusername/Monitoring-project.git
cd Monitoring-project/backend

2️⃣ Run with Docker
docker-compose up --build
Backend runs on http://localhost:5002
Frontend runs on your chosen server (e.g., http://localhost:3000)

3️⃣ Access the Dashboard
Open your browser and go to your frontend URL to see live metrics.

API Endpoints
GET /stats — Returns system metrics (CPU, memory, disk) and running containers
GET /logs/<container_name> — Returns logs of the specified Docker container

Notes
Uses Flask development server; not recommended for production
Requires Docker installed and running
Auto-refreshes every 2 seconds for live updates
