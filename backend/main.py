from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(
    title="Smart Plant Care System API",
    description="REST API for SPCS – telemetry & watering commands",
    version="1.0.0",
)


class WateringRequest(BaseModel):
    duration_seconds: int


@app.get("/api/health")
def health_check():
    """
    Basit health endpoint – API ayakta mı?
    """
    return {"status": "ok", "service": "spcs-backend", "timestamp": datetime.utcnow().isoformat()}


@app.get("/api/telemetry/latest")
def get_latest_telemetry():
    """
    Şimdilik dummy veri döndürüyoruz.
    Sonraki tasklerde Blob Storage / IoT Hub'dan gerçek veri alacağız.
    """
    return {
        "device_id": "spcs-simulator-1",
        "soil_moisture": 41.5,
        "light_level": 73.2,
        "temperature": 24.3,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }


@app.post("/api/water")
def send_watering_command(body: WateringRequest):
    """
    Sulama komutu simülasyonu.
    Gerçekte burada IoT Hub üzerinden cihaza C2D mesajı göndereceğiz.
    """
    return {
        "device_id": "spcs-simulator-1",
        "command": "water",
        "duration_seconds": body.duration_seconds,
        "status": "accepted",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
