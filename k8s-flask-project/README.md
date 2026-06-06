# Kubernetes Deployment of Flask Application

## Project Overview

This project demonstrates containerization and deployment of a Python Flask application using Docker and Kubernetes.

The application is deployed on a Kubernetes cluster using Minikube.

## Architecture

Developer
↓
Docker Image
↓
Kubernetes Deployment
↓
Pods
↓
Service
↓
Users

## Technologies Used

* Docker
* Kubernetes
* Minikube
* kubectl
* Python Flask
* Linux
* YAML

## Project Workflow

1. Create Flask Application
2. Containerize using Docker
3. Build Docker Image
4. Create Kubernetes Deployment
5. Create Kubernetes Service
6. Deploy Application
7. Access Application through Service

## Kubernetes Components

### Deployment

Manages application Pods and provides self-healing.

### ReplicaSet

Ensures desired number of Pods remain running.

### Service

Provides a stable endpoint to access the application.

## Setup Instructions

Clone Repository:

git clone https://github.com/VijayaLaxmi474/k8s-flask-project.git

Move into project:

cd k8s-flask-project

Start Minikube:

minikube start

Build Docker Image:

eval $(minikube docker-env)

docker build -t flask-k8s .

Deploy Application:

kubectl apply -f deployment.yaml

Create Service:

kubectl apply -f service.yaml

Verify:

kubectl get all

## Screenshots

### Pods Running

![Pods](screenshots/pods-running.png)

### Deployment Running

![Deployment](screenshots/deployment-running.png)

### Service Running

![Service](screenshots/service-running.png)

### Application Running

![Application](screenshots/app-running.png)

## Outcome

Successfully deployed a Dockerized Flask application on Kubernetes using Deployments, ReplicaSets, and Services while implementing self-healing and scalability concepts.
