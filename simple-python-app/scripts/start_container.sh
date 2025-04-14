#!/bin/bash

set -e

echo "Check if Docker is installed..."

if ! command -v docker &> /dev/null
then
    echo "Docker not found. Installing Docker..."
    sudo apt update
    sudo apt install docker.io -y
    sudo usermod -aG docker ubuntu 
    sudo systemctl restart docker
    echo "Docker installed successfully."
else
    echo "Docker is already installed."
fi

echo "Pulling Docker image shridhar71/simple-python-flask-app:latest..."
docker pull shridhar71/simple-python-flask-app:latest

echo "Running container as 'simple-python-flask-app'..."
docker run --name demoapp -p 8000:8000 -d shridhar71/simple-python-flask-app:latest || {
    echo "Container with name 'demoapp' may already exist. Attempting to restart..."
    docker start demoapp
}

echo "Success -> run"

simple-python-flask-app
