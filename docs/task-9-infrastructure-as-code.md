# Bonus Task 9 – Infrastructure as Code (Bicep)

For the bonus task I defined the cloud infrastructure of the Smart Plant Care System (SPCS)  
using **Azure Bicep**. The goal is to describe the resources from previous tasks in code and  
deploy them in a repeatable way.

---

## 1. Resources defined in Bicep

The following Azure resources are defined in `infra/main.bicep`:

- **Azure IoT Hub** – for device connectivity and telemetry (Task 3)
- **Azure Storage Account (Blob Storage)** – for storing telemetry data (Task 5)
- **Azure App Service Plan (Linux)** – hosting plan for the web API (Task 6)
- **Azure Web App** – the FastAPI backend from Task 6

The Bicep file uses parameters for:

- `location` (default: `switzerlandnorth`)
- `iotHubName`
- `storageAccountName`
- `webAppName`
- `appServicePlanName`
- `appServiceSku` (Free F1 or Basic B1)

---

## 2. main.bicep file

The infrastructure as code definition is stored in:

- `infra/main.bicep`

It defines:

- Storage Account (`Microsoft.Storage/storageAccounts`)
- IoT Hub (`Microsoft.Devices/IotHubs`)
- App Service Plan (`Microsoft.Web/serverfarms`)
- Web App (`Microsoft.Web/sites`)

The file also defines outputs:

- `iotHubHostname`
- `storageAccountId`
- `webAppUrl`

---

## 3. Deployment using Azure CLI

To deploy the infrastructure I used the Azure CLI:

1. Resource group (already created in previous tasks):

```bash
az group create -n rg-smart-plant-iot -l switzerlandnorth
