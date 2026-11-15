
# Task Management REST API

## Project Description
A REST API developed using Python and Flask to manage tasks.

## Features
- Home page
- Health check endpoint
- View all tasks
- Add new tasks
- Retrieve individual tasks
- Delete tasks

## Technologies Used
- Python
- Flask
- Pytest
- Git
- Docker

## Testing
Automated tests are performed using Pytest.
## Docker

The application is containerized using Docker.

Build the Docker image:

```bash
docker build -t task-management-api .
```

Run the Docker container:

```bash
docker run -d --name task-management-container -p 5000:5000 task-management-api
```

Verify running containers:

```bash
docker ps
```

## Jenkins CI/CD Pipeline

Jenkins is used to automate the build and deployment process.

Pipeline steps:
1. Fetch source code from GitHub.
2. Install Python dependencies.
3. Run automated tests using Pytest.
4. Build the Docker image.
5. Start the Docker container.

## API Endpoints

| Endpoint | Description |
|---|---|
| `/` | Welcome message |
| `/health` | Application health check |

## Conclusion

This project demonstrates the use of Python Flask, GitHub, Pytest, Docker and Jenkins to develop, test and deploy a REST API using a basic CI/CD workflow.

## GitHub Repository

https://github.com/manasvi447/task-management-devops
