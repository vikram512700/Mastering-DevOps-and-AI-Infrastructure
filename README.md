# Azure DevOps & AI Learning Platform 🚀

A comprehensive, end-to-end Learning Platform designed to teach Azure Fundamentals, Enterprise DevOps, Production Architecture, and AI. Built specifically for engineers looking to master the Hyderabad job market and transition into Senior Cloud/SRE roles.

## 🌟 Key Features
- **10 Enterprise DevOps Tracks**: From Fundamentals to Advanced Kubernetes (AKS).
- **Interactive Labs**: Step-by-step Sandbox Panel with mock terminal execution.
- **Dynamic Quiz Engine**: Test your knowledge and earn XP.
- **JD Analyzer (AI Mentor)**: Paste Job Descriptions and get a personalized learning plan using LangGraph & Azure OpenAI.
- **AI Interviewer**: Chat-based mock interviews to prepare for technical rounds.

## 🏗️ Architecture Stack
This application is built using a modern 3-tier microservice architecture:
- **Frontend**: Next.js 15 (App Router), TypeScript, TailwindCSS, ShadCN UI.
- **Backend**: NestJS, Prisma ORM, PostgreSQL (Stores XP, module progress, user profiles).
- **AI Microservice**: FastAPI, LangChain, LangGraph (Handles JD parsing and Interview bots).
- **Infrastructure**: Fully Dockerized for seamless local development (`docker-compose`).

## 🚀 How to Run the Application Locally

### Prerequisites
Make sure you have the following installed on your machine:
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Must be running in the background)
- Git

### 1. Start the Platform
The easiest way to launch the entire platform (Frontend, Backend, AI Server, Postgres DB, and Redis) is using Docker Compose.

Open your terminal in the root directory of this project and run:
```bash
docker-compose up --build
```

### 2. Access the Application
Once the Docker containers are successfully running, you can access the different services at the following URLs:

- **Frontend (Web App)**: [http://localhost:3000](http://localhost:3000)
- **NestJS Backend**: [http://localhost:4000](http://localhost:4000)
- **FastAPI AI Server**: [http://localhost:8000/docs](http://localhost:8000/docs) (Interactive Swagger UI)

### 3. Stopping the Application
To shut down all services gracefully, press `Ctrl + C` in the terminal where Docker is running, or run:
```bash
docker-compose down
```

## 📚 Environment Configuration
To use the AI Mentor features, you will eventually need to provide Azure OpenAI credentials. Create a `.env` file in the root or set them locally before running Docker:
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_KEY`
- `AZURE_OPENAI_DEPLOYMENT`

## 🤝 Roadmap
- Phase 1: Core MVP & UI Scaffold (✅ Completed)
- Phase 2: Quiz Engine & Interactive Labs (✅ Completed)
- Phase 3: AI Interviewer & JD Analyzer (✅ Completed)
- Phase 4: Market Intelligence Web Crawler (⏳ Upcoming)
