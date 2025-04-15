# Simple Python Flask App

This project demonstrates how to create a Portfolio Python Flask application and deploy it using Docker and AWS CodeBuild and AWS CodeDeploy.

## Setup

### Prerequisites

- Docker
- AWS CLI
- AWS CodeBuild
- AWS Codedeploy

### Clone the Repository

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd Python-Flask-application_AWS-CodeBuild/simple-python-app
    ```

### Build and Run the Docker Container

1. Build the Docker image:
    ```sh
    docker build -t simple-python-flask-app .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 5000:5000 simple-python-flask-app
    ```

3. Access the application:
    Open your web browser and go to `http://localhost:5000`

## AWS CodeBuild

This project uses AWS CodeBuild for continuous integration and deployment.

### Build Specification

The build specification is defined in the `buildspec.yml` file.

### Environment Variables

The following environment variables are used in the build process:

- `DOCKER_USER`: Docker Hub username (stored in AWS Parameter Store)
- `DOCKER_PASS`: Docker Hub password (stored in AWS Parameter Store)
- `DOCKER_URL`: Docker registry URL (static variable)

### Build Phases

1. **Install**: Install dependencies.
2. **Pre-build**: Log in to Docker Hub.
3. **Build**: Build and push the Docker image.
4. **Post-build**: Finalize the build process.

### Artifacts

The build artifacts are stored in the `../simple-python-app` directory.

## Deployment

### AppSpec File

The deployment configuration is defined in the `appspec.yml` file.

### Hooks

The following hooks are defined in the `appspec.yml` file:

- **ApplicationStop**: Stops the running container (if any) using `stop_container.sh`.
- **AfterInstall**: Starts the container using `start_container.sh`.

## Scripts

### stop_container.sh

This script stops the running Docker container.

```bash
#!/bin/bash
set -e

# Stop the running container (if any)
echo "Stopping the running container..."
docker stop simple-python-flask-app || true
docker rm simple-python-flask-app || true
```

### start_container.sh

This script pulls the Docker image from Docker Hub and runs it as a container.

```bash
#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
echo "Pulling the Docker image..."
docker pull $DOCKER_USER/simple-python-flask-app:latest

# Run the Docker image as a container
echo "Running the Docker container..."
docker run -d -p 5000:5000 --name simple-python-flask-app $DOCKER_USER/simple-python-flask-app:latest
```
