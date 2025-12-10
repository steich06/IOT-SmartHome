# Task 8 – API Documentation (Swagger / OpenAPI)

For Task 8 I implemented API documentation for the Smart Plant Care System (SPCS)  
using **Swagger / OpenAPI** based on the FastAPI backend from Task 6.

The backend is deployed to Azure App Service and exposes a built-in Swagger UI and  
an OpenAPI JSON definition that can be used in tools like Swagger Editor or Postman.

---

## 1. Swagger UI

FastAPI automatically generates an interactive Swagger UI for the API.

Public URL:

- **Swagger UI:**  
  `https://spcs-backend-yunus-doruk-gafsc7h7fwa2g3em.switzerlandnorth-01.azurewebsites.net/docs`

Using this page it is possible to:

- See all available endpoints
- Check request/response models
- Test GET and POST requests directly from the browser

---

## 2. OpenAPI / Swagger JSON

FastAPI also exposes the OpenAPI (Swagger) definition as JSON.

- **OpenAPI JSON URL:**  
  `https://spcs-backend-yunus-doruk-gafsc7h7fwa2g3em.switzerlandnorth-01.azurewebsites.net/openapi.json`

This JSON file was downloaded and added to the project repository as:

- `docs/spcs-openapi.json`

This file can be used with:

- **Swagger Editor** (https://editor.swagger.io)  
  → Import URL or upload the JSON file  
- **Postman**  
  → Import the OpenAPI JSON to generate a collection  
- Other API tools that support OpenAPI / Swagger format

---

## 3. Endpoints documented

The Swagger / OpenAPI documentation includes the following endpoints:

- `GET /api/health` – health check of the backend
- `GET /api/telemetry/latest` – returns latest telemetry (dummy data for now)
- `POST /api/water` – sends a watering command (simulated)

All request and response models (e.g. `WateringRequest`) are described in the schema section of the Swagger UI.

---

## 4. How this satisfies Task 8

The project requirements for Task 8 were:

> “Create a Postman collection, or your own Frontend, or create a Swagger documentation.”

In this project, I chose the **Swagger documentation** option by:

1. Using FastAPI’s built-in Swagger UI at `/docs`
2. Exporting the OpenAPI JSON from `/openapi.json`
3. Storing the JSON file in the repository (`docs/spcs-openapi.json`)
4. Verifying it in Swagger Editor (compatible with https://petstore.swagger.io/ style documentation)

This provides a complete, machine-readable and human-friendly API documentation  
for the Smart Plant Care System backend.
