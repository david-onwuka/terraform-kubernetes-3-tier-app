# Terraform Kubernetes 3-Tier Application

## Project Overview

This project is a complete deployment of a containerized three-tier web application running on Kubernetes.

The application is separated into three main layers:

- Frontend layer: Handles the user interface
- Backend layer: Provides the application API and logic
- Database layer: Stores application data using PostgreSQL

The purpose of this project was to package an application into containers, deploy it into a Kubernetes environment, configure communication between services, and verify that every component works correctly.

---

## Architecture

The application follows a three-tier architecture:

Frontend
    |
    |
Backend API
    |
    |
PostgreSQL Database


Each component runs independently inside Kubernetes, allowing the application to be managed, updated, and scaled more easily.

---

## Frontend

The frontend is the user-facing part of the application.

It is deployed inside Kubernetes and exposed through a Kubernetes Service, allowing users to access the application through a browser.

The frontend communicates with the backend API to retrieve application data.

Frontend application running:

![Frontend Application](./screenshots/frontend-browser-ui.png.png)

The frontend access configuration was also verified through the terminal:

![Frontend URL Verification](frontend-url-terminal-proof.png.png)

---

## Backend API

The backend service is a Flask-based API that handles application requests.

It was containerized using Docker and deployed to Kubernetes with multiple replicas.

The backend is responsible for:

- Processing application requests
- Providing API endpoints
- Communicating with the database
- Returning application responses to the frontend

The backend runs internally inside Kubernetes and communicates with other services through Kubernetes networking.

---

## Database

The database layer uses PostgreSQL running inside Kubernetes.

The database is kept internal and accessed by the backend service through the Kubernetes service name.

The backend successfully connected to the database:

![Backend Database Connection](screenshots/backend-database-connected.png.png)

---

## Kubernetes Deployment

Kubernetes manages the complete application environment.

It handles:

- Running containers
- Maintaining replicas
- Service discovery
- Internal communication
- Restarting failed containers
- Keeping the application available

The deployment was verified by checking pods, deployments, and services:

![Kubernetes Status](screenshots/kubernetes-pods-deployments-services.png.png)

---

## Infrastructure

Terraform was used to manage the infrastructure configuration and make the deployment process repeatable.

The project uses:

- Docker for building container images
- Kubernetes for application orchestration
- Terraform for infrastructure management
- PostgreSQL for persistent data storage

---

## Project Structure

terraform-kubernetes-3-tier-app/

├── backend/

│   ├── app.py

│   ├── Dockerfile

│   └── requirements.txt


├── frontend/


├── kubernetes/

│   ├── deployment files

│   ├── service files

│   └── database configuration


├── terraform/


└── screenshots/

    ├── 01-frontend-browser-ui.png

    ├── 02-frontend-url-terminal-proof.png

    ├── 03-kubernetes-pods-deployments-services.png

    └── 04-backend-database-connected.png


---

## Final Result

The application was successfully deployed and tested.

The final deployment includes:

- A working frontend application
- A running backend API
- A connected PostgreSQL database
- Kubernetes-managed workloads
- Automated infrastructure configuration

This project demonstrates practical experience deploying a cloud-native application using Docker, Kubernetes, and Terraform.
