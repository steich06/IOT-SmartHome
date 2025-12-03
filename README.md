Task 1 – Business Context Description
Project: Smart Plant Care System (SPCS)

Overview
SPCS is a Smart Home IoT solution that monitors soil moisture and light levels using an IoT Device Simulator connected to Azure IoT Hub (MQTT broker).
Users can view real time sensor data and send simulated watering commands through a Backend REST API and an API Client.
Historical sensor data is stored in Azure Blob Storage.

The goal is to help home users keep plants healthy with minimal effort while demonstrating a full cloud based IoT architecture.

Problem Statement
Home users often forget to water their plants or water them incorrectly.
SPCS provides real time insights and allows users to trigger watering actions remotely through cloud communication.

Target Users
Home Users – want simple monitoring and watering control

Developers – test or extend the REST API

Business Owners – analyze historical data and plant trends

Key Use Cases
View real time soil moisture and light data (via REST API)

Receive simulated low moisture notifications

Send watering commands to the IoT simulator via MQTT

Store & view historical sensor data (Azure Blob Storage)

Analyze long term plant health trends

User Stories
Home User Stories
As a home user, I want to see real time soil moisture so that I know when my plant needs water.

As a home user, I want to manually trigger simulated watering so that I can care for my plant remotely.

As a home user, I want feedback messages so that I know whether watering succeeded.

Developer Stories
As a developer, I want clear REST API documentation so I can easily integrate or test the system.

As a developer, I want the device simulator to send MQTT telemetry so I can test cloud logic without real hardware.

Business Owner Stories
As a business owner, I want to access historical plant data so I can analyze usage patterns and potential improvements.

Value Proposition
SPCS combines IoT telemetry, MQTT communication, and cloud automation to simplify plant care.
It uses:

Azure IoT Hub: reliable MQTT based device communication

Azure Blob Storage: cloud data storage for historical sensor data

Backend REST API: user interface for watering actions and data access

The system helps users make informed decisions, avoid under watering, and remotely monitor plant health while being scalable to thousands of devices.
