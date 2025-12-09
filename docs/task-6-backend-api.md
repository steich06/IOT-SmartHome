# Task 6 – Web Server with REST API (Backend)

This task implements a REST API for the Smart Plant Care System (SPCS).  
The backend exposes HTTP endpoints for telemetry data and watering commands.  
The API is deployed to Azure App Service using Python (FastAPI).

---

## 1. Backend Files

- backend/main.py — FastAPI web server (all API endpoints)
- backend/requirements.txt — Dependencies: FastAPI, Uvicorn, Gunicorn

---

## 2. API Endpoints

### GET /api/health
Checks if the API is running.

Example response:
{
  "status": "ok",
  "service": "spcs-backend",
  "timestamp": "2025-12-09T12:00:00Z"
}

---

### GET /api/telemetry/latest
Returns dummy telemetry data (later replaced with real IoT data).

Example response:
{
  "device_id": "spcs-simulator-1",
  "soil_moisture": 41.5,
  "light_level": 73.2,
  "temperature": 24.3,
  "timestamp": "2025-12-09T12:00:00Z"
}

---

### POST /api/water
Sends a watering command to the device (simulated).

Request:
{
  "duration_seconds": 5
}

Response:
{
  "device_id": "spcs-simulator-1",
  "command": "water",
  "duration_seconds": 5,
  "status": "accepted",
  "timestamp": "2025-12-09T12:00:00Z"
}

---

## 3. Deployment to Azure App Service

### Startup Command
To run FastAPI with Gunicorn:

gunicorn -k uvicorn.workers.UvicornWorker main:app

### Deployment Steps
1. Created backend folder and API files  
2. Added dependencies to requirements.txt  
3. Deployed using VS Code: “Azure App Service: Deploy to Web App”  
4. Selected backend folder  
5. Added Startup Command in Azure Portal  
6. Restarted App Service  
7. Verified API using:
   - /api/health
   - /api/telemetry/latest
   - /api/water
   - /docs (Swagger UI)

---

## 4. Result

The backend API is fully deployed and functional on Azure.  
Swagger documentation works, endpoints respond correctly, and the backend  
is ready for integration with IoT Hub (Task 7) and Storage (Task 5).
