# Task 4 – IoT Device Simulator

This task implements the IoT Device Simulator that sends telemetry data to Azure IoT Hub using MQTT.  
The simulator represents the Smart Plant Care System (SPCS) device that measures environmental values and communicates with the cloud.

---

## 1. Files & Cloud Resources Used

- **Simulator file:** `device/simple_mqtt_device_simulator.py`
- **IoT Hub:** `spcs-iot-hub-yunus-doruk`
- **Device ID:** `spcs-simulator-1`

Telemetry sent includes:
- temperature  
- humidity  
- pressure  
- timestamp  

---

## 2. How to Run the Simulator

### 1) Create and activate Python virtual environment

**Windows:**
```powershell
py -m venv .venv
.venv\Scripts\activate
