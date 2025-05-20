# 🚀 Simple Python Flask App with CI/CD on AWS

This repository demonstrates how to build, containerize, and deploy a simple Python Flask application using **Docker**, **AWS CodeBuild**, and **AWS CodeDeploy**, all managed through an automated CI/CD pipeline. This setup follows modern DevOps practices and uses **AWS Systems Manager Parameter Store** to securely manage secrets.

---

## 📦 Project Structure

```
.
├── appspec.yml               # Deployment configuration for CodeDeploy
├── buildspec.yml             # Build instructions for CodeBuild
├── Dockerfile                # Docker build file for Flask app
├── start_container.sh        # Script to start container
├── stop_container.sh         # Script to stop container
├── simple-python-app/        # Source code for Flask app
└── README.md                 # Project documentation
```

---

## 🧰 Prerequisites

* Docker installed locally
* AWS CLI configured
* AWS CodeBuild project
* AWS CodeDeploy application and deployment group
* IAM roles with permissions for CodeBuild and CodeDeploy

---

## 🚀 Clone the Repository

```sh
git clone <repository-url>
cd Python-Flask-application_AWS-CodeBuild/simple-python-app
```

---

## 🐳 Build and Run Locally with Docker

1. **Build the Docker image:**

   ```sh
   docker build -t simple-python-flask-app .
   ```

2. **Run the Docker container:**

   ```sh
   docker run -p 5000:5000 simple-python-flask-app
   ```

3. **Access the application:**

   * Open your browser at: `http://localhost:5000`

---

## ⚙️ AWS CodeBuild Configuration

CodeBuild is used to automate the process of building and pushing the Docker image.

### 🔐 Environment Variables

Stored securely using **AWS Parameter Store** (SecureString):

* `DOCKER_USER`: Docker Hub username
* `DOCKER_PASS`: Docker Hub password

Static:

* `DOCKER_URL`: Docker registry URL

### 🧱 Build Phases in `buildspec.yml`

1. **Install:** Install dependencies.
2. **Pre-build:** Authenticate with Docker Hub.
3. **Build:** Build and tag the Docker image.
4. **Post-build:** Push the image to Docker Hub.

### 🧾 Artifacts

Build artifacts are stored and deployed from the `../simple-python-app` directory.

---

## 🚀 Deployment with AWS CodeDeploy

Uses `appspec.yml` to manage the deployment lifecycle.

### 🪝 Lifecycle Hooks

* **ApplicationStop**: Stops the running container with `stop_container.sh`
* **AfterInstall**: Pulls and starts the latest Docker image with `start_container.sh`

### 🔧 Scripts

#### `stop_container.sh`

```bash
#!/bin/bash
set -e
echo "Stopping the running container..."
docker stop simple-python-flask-app || true
docker rm simple-python-flask-app || true
```

#### `start_container.sh`

```bash
#!/bin/bash
set -e
echo "Pulling the Docker image..."
docker pull $DOCKER_USER/simple-python-flask-app:latest

echo "Running the Docker container..."
docker run -d -p 5000:5000 --name simple-python-flask-app $DOCKER_USER/simple-python-flask-app:latest
```

---

## 🛡️ Security & Optimization

* Secrets like Docker credentials are stored securely using **AWS Systems Manager Parameter Store (SecureString)**.
* Follows AWS best practices for security and cost optimization.

---

## ✅ Summary

This project is a complete demonstration of how to:

* Build a Flask app
* Containerize with Docker
* Set up CI/CD with AWS CodeBuild and CodeDeploy
* Secure credentials using AWS Parameter Store
* Automate deployment with lifecycle hooks

---

