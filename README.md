# aws_flask_app

This project demonstrates how to create a Python application using AWS CI/CD.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd aws_flask_app
    ```

2. Build the Docker image:
    ```sh
    docker build -t aws_flask_app .
    ```

3. Run the Docker container:
    ```sh
    docker run -p 5000:5000 aws_flask_app
    ```

4. Access the application:
    Open your web browser and go to `http://localhost:5000`

## AWS CodeBuild

This project uses AWS CodeBuild for continuous integration and deployment.

### Build Specification

The build specification is defined in the `build.yml` file.

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
