## Automates Kubernetes deployments, scaling, and monitoring for DevOps workflows.

## Technologies Used
- **Python**: For automation scripts (e.g., `deploy.py`).
- **Bash**: For workflow automation (e.g., `deploy.sh`).
- **YAML**: For Kubernetes configurations (e.g., `nginx-deployment.yaml`).
- **Linux**: For hosting and managing the Kubernetes environment (via WSL2 and Minikube).


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
## Results
### Nginx Service Access
After exposing the Nginx service using `minikube service nginx-service -n default`, the service was accessible at `http://127.0.0.1:43985`, displaying the "Welcome to nginx!" page.

### Pod Status After Scaling
Scaled down to 1 replica using `kubectl scale deployment my-nginx-deployment --replicas=1`. Verified with `kubectl get pods -n default`:
