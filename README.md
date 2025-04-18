# Kubernetes Automation Tool
Automates Kubernetes deployments, scaling, and monitoring for DevOps workflows.

## Setup
- Start Minikube: `minikube start --driver=docker`
- Install dependencies: `pip install kubernetes`

## Usage
- Deploy Nginx: `python3 deploy.py deploy`
- Expose service: `kubectl apply -f nginx-service.yaml` (NodePort YAML) or `minikube service nginx-service -n default`
- Scale deployment: `kubectl scale deployment my-nginx-deployment --replicas=3`
- Test: Use `minikube service nginx-service -n default` to access the service

## Features
- Automated deployment of Nginx on Kubernetes.
- Service exposure via NodePort or Minikube service.
- Scaling and monitoring capabilities.

## Notes
- WSL2 users may need to use `minikube service` due to networking limitations with Minikube’s Docker driver.
- Ensure `minikube` and `kubectl` are installed.
