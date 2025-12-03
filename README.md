Task 1 – Business Context Description
Project: Smart Plant Care System (SPCS)

Overview

SPCS is a Smart Home IoT solution that monitors soil moisture and light levels using an IoT Device Simulator connected to Azure IoT Hub (MQTT broker).
Users can view real-time sensor data and send simulated watering commands through a Backend REST API and API Client (e.g., Postman or a simple frontend).
Historical data is stored in Azure Blob Storage for later analysis.

The goal is to help home users keep plants healthy with minimal effort while demonstrating a complete cloud‑based IoT architecture.

--
Problem Statement

Home users often forget to water their plants or water them incorrectly.
This system provides real-time data insights and lets users trigger watering actions remotely through cloud communication.

--
Target Users

Home Users – want simple plant monitoring and watering control
Developers – integrate the REST API or extend the system
Business Owners – explore data trends and plan product improvements

--
Key Use Cases

-View real-time soil moisture & light data (via REST API)

-Receive notifications/status about low moisture (simulated)

-Send watering commands to the IoT device simulator via MQTT

-Store & view historical sensor data using Azure Blob Storage

-Analyze plant health trends over time

--
User Stories

Home User Stories
As a home user, I want to see real-time soil moisture so that I know when my plant needs water.
As a home user, I want to manually trigger simulated watering so that I can care for my plant remotely.
As a home user, I want simple feedback messages so that I know if watering succeeded.

Developer Stories
As a developer, I want clear REST API documentation so that I can easily integrate or test the system.
As a developer, I want the device simulator to send MQTT telemetry so that I can test cloud logic without real hardware.

Business Owner Stories
As a business owner, I want to access historical plant data so that I can analyze usage patterns and improvements.

--
Value Proposition

SPCS combines real-time IoT telemetry with cloud automation to simplify plant care for users.
It provides reliable MQTT‑based device communication through Azure IoT Hub, cloud storage via Azure Blob Storage, and a simple REST API for user control.
The system helps users make informed decisions, prevent underwatering/overwatering, and remotely monitor plant health—while being easy to scale to thousands of devices.
