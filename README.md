🔧 Automation & Analytics Platform

A full-stack web application built to streamline operations, automate workflows, and provide real-time insights for multi-department teams. Originally designed to replace daily Google Sheets usage, the platform improves efficiency, data organization, and customer communication.

🚀 Features

Workflow Automation: Replaced manual Google Sheets processes with structured Django + PostgreSQL workflows.

Real-Time Dashboards: Built with Streamlit, tracking 50+ productivity metrics for management insights.

Background Tasks & Notifications: Powered by Celery + Redis for real-time communication and task queues.

REST APIs: Django APIs to support scalable, multi-department operations.

Authentication & Access Control: Role-based workflows with Django Workflows.

Video Automation Pipeline: Built with FastAPI to watermark customer videos, upload them to YouTube, and handle metadata.

LLM Integration: Automatically generates YouTube descriptions and content summaries.

Containerized Deployment: Dockerized for reproducibility and scalability.

🛠️ Tech Stack

Backend: Django, FastAPI, Celery, Redis

Frontend: HTML, CSS, HTMX (future: React/TypeScript)

Database: PostgreSQL

Dashboards: Streamlit

DevOps: Docker, Git

AI Integration: LLM APIs (for automated video descriptions)

📊 Architecture Overview
graph TD
    A[Frontend (HTMX/Streamlit)] --> B[Django API]
    B --> C[PostgreSQL Database]
    B --> D[Celery + Redis]
    D --> B
    E[FastAPI Pipeline] --> B
    E --> F[LLM API + YouTube API]

📈 Impact

Improved operational efficiency by 15% across three departments.

Reduced manual data entry errors and streamlined communication between technicians and customer service.

Provided real-time visibility into operations, enabling faster decision-making.

▶️ Getting Started
Prerequisites

Python 3.11+

Docker & Docker Compose

Installation
git clone https://github.com/arsham909/repair_shop.git
cd repair_shop
docker-compose up --build

Run Migrations
docker-compose exec web python manage.py migrate

Create Superuser
docker-compose exec web python manage.py createsuperuser

📚 Future Improvements

Replace Streamlit dashboard with React + TypeScript frontend for scalability.

Add unit tests and GitHub Actions CI/CD.

Implement role-based analytics dashboards for different departments.

Expand LLM integrations to cover email automation and report generation.

👤 Author

Arsham Ardeshirian

GitHub: @arsham909

Email: Arsham202@gmail.com
