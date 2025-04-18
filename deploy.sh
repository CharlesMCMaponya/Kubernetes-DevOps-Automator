#!/bin/bash
# Deploy and manage Nginx on Kubernetes
echo "Starting Minikube..."
minikube start --driver=docker
echo "Deploying Nginx..."
kubectl apply -f nginx-deployment.yaml
echo "Exposing Nginx service..."
kubectl apply -f nginx-service.yaml
echo "Scaling to 3 replicas..."
kubectl scale deployment my-nginx-deployment --replicas=3
echo "Accessing the service..."
minikube service nginx-service -n default --url
