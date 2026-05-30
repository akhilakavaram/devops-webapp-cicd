# DevOps Web App CI/CD Project

This is Project 1 in the DevOps learning path. It starts with a small web app and builds the habits every DevOps engineer needs: source control, containerization, repeatable local environments, automated tests, and CI/CD.

## What You Will Learn

- How a web service is structured
- How to use Git for a clean project workflow
- How to package an app with Docker
- How to run multi-command app environments with Docker Compose
- How health checks work
- How CI/CD validates code on every push
- How to prepare a repo for future deployment work

## Tech Stack

- Python standard library web server
- Docker
- Docker Compose
- GitHub Actions
- Linux container runtime

No local Python installation is required if you run the project with Docker.

## Project Structure

```text
devops-webapp-cicd/
├── app/
│   └── main.py
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
```

## Run Locally With Docker Compose

```bash
docker compose up --build
```

Open:

```text
http://localhost:8000
```

Useful endpoints:

```text
http://localhost:8000/health
http://localhost:8000/version
```

Stop the app:

```bash
docker compose down
```

## Run Tests In Docker

```bash
docker build -t devops-webapp-cicd:test .
docker run --rm --entrypoint python devops-webapp-cicd:test -m unittest discover -s tests
```

## CI/CD Pipeline

The GitHub Actions workflow has three jobs:

1. Run unit tests.
2. Build the Docker image.
3. Start the app with Docker Compose and test the `/health` endpoint.

This is the first production habit: every push should prove the app can be tested, built, and started.

## Beginner Tasks

- Run the app with Docker Compose.
- Change the app name using the `APP_NAME` environment variable.
- Visit `/health` and explain what each field means.
- Break one test on purpose, run CI, then fix it.

## Medium Tasks

- Add a `/ready` endpoint for readiness checks.
- Add a `Makefile` or task runner for common commands.
- Add image tagging with semantic versions.
- Push the image to Docker Hub or GitHub Container Registry.

## Advanced Tasks

- Add Trivy image scanning to CI.
- Add deployment to a cloud VM.
- Add Nginx as a reverse proxy.
- Add Kubernetes manifests for this app.

## Next Project Connection

Project 2 will use Terraform to create cloud infrastructure that can run this containerized app.
