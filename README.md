# Task Management REST API – DevOps Project

## Project Overview

A Task Management REST API developed using Python and Flask, demonstrating DevOps automation through GitHub Actions, Maven, Ansible, Jenkins, Docker, and automated testing.

## Features

- Home page
- Health check endpoint
- View all tasks
- Add new tasks
- Retrieve individual tasks
- Delete tasks

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Flask | REST API framework |
| Pytest | Automated testing |
| Git and GitHub | Version control |
| GitHub Actions | CI workflow |
| Maven | Build automation |
| Ansible | Configuration and test automation |
| Jenkins | CI/CD automation |
| Docker | Application containerization |

## Project Structure

```text
applications/
├── .github/
│   └── workflows/
├── ansible/
│   ├── inventory.ini
│   └── site.yml
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── pom.xml
├── README.md
└── .gitignore
```

## Automated Testing

The project uses Pytest to execute automated tests.

Run tests:

```bash
python -m pytest -v
```

**Testing result:** 7 tests passed.

## GitHub Actions

GitHub Actions automates the CI workflow whenever changes are pushed to the repository.

The workflow automates project testing and validation.

## Maven Build Automation

Maven is included for build automation through the project's `pom.xml` configuration.

## Ansible Automation

Ansible automates the following tasks:

1. Check Python installation.
2. Create a Python virtual environment.
3. Install project dependencies.
4. Execute automated Pytest tests.
5. Display test results.

Run the Ansible playbook:

```bash
ansible-playbook -i ansible/inventory.ini ansible/site.yml
```

**Ansible testing result:** 7 tests passed and 0 failed tasks.

## Docker

The Flask application is containerized using Docker.

Build the image:

```bash
docker build -t task-management-api .
```

Run the container:

```bash
docker run -d --name task-management-container -p 5000:5000 task-management-api
```

Verify running containers:

```bash
docker ps
```

Application URL:

http://localhost:5000

## Jenkins CI/CD Pipeline

Jenkins automates the application's build and deployment process.

### Pipeline steps

1. Fetch source code from GitHub.
2. Check Python installation.
3. Install project dependencies.
4. Run automated Pytest tests.
5. Build the Docker image.
6. Start the Docker container.

**Jenkins result:** Build completed successfully (`Finished: SUCCESS`).

**Docker result:** Container successfully started and application accessible on port 5000.

## API Endpoints

| Endpoint | Description |
|---|---|
| `/` | Welcome message |
| `/health` | Application health check |

## Project Results

- 7 automated Python tests passed.
- Ansible automation executed successfully.
- Jenkins build completed successfully.
- Docker image built successfully.
- Docker container started successfully.
- Flask REST API responded successfully.

## Conclusion

This project demonstrates a basic DevOps workflow integrating application development, version control, automated testing, configuration automation, continuous integration, and containerized deployment.

## GitHub Repository

https://github.com/manasvi447/task-management-devops
