# Task 5 – Data Storage (Azure Blob Storage)

For this task we created a **data storage layer** for the Smart Plant Care System (SPCS) using **Azure Blob Storage**.  
This storage is used to store historical sensor data sent by the IoT Device Simulator (soil moisture, light level, etc.).

---

## 1. Chosen Option

According to the assignment we could choose between:

- VM-based database (e.g. PostgreSQL)
- Docker-based database (e.g. PostgreSQL)
- Azure Blob Storage
- Azure Cosmos DB

In this project we chose: **Azure Blob Storage**, because:

- it is simple and cheap for time-series IoT data,
- it is fully managed (no need to maintain a VM),
- it matches the reference lab: `8-storage-blob` from the course repository.

---

## 2. Storage Account Configuration

The following Azure resources were created:

- **Resource Group:** `rg-smart-plant-iot`
- **Storage Account Name:** `spcsstorageyunusdoruk`
- **Region:** `Switzerland North`
- **Performance:** Standard
- **Redundancy:** LRS (Locally-redundant storage)
- **Account kind:** StorageV2 (general purpose v2, default)

This storage account will be used as the main data lake for SPCS telemetry.

---

## 3. Blob Container for Telemetry

Inside the storage account we created a **Blob Container**:

- **Container name:** `spcs-telemetry`
- **Access level:** `Private (no anonymous access)`

This container will store **historical sensor data** coming from the IoT Device Simulator, for example JSON or CSV files with measurements.

Example blob naming convention (virtual folders):

```text
spcs-telemetry/
  spcs-simulator-1/
    2025/12/09/telemetry_2025-12-09T13-30-00.json
