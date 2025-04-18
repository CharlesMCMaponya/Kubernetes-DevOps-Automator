from kubernetes import client, config, utils
import sys

# Load kube config
config.load_kube_config()

# Create API clients
api_instance = client.AppsV1Api()
core_api = client.CoreV1Api()

# Delete existing my-nginx-deployment if it exists
try:
    api_instance.delete_namespaced_deployment(name="my-nginx-deployment", namespace="default")
    print("Existing my-nginx-deployment deleted")
except:
    pass

# Delete existing nginx-deployment if it exists (cleanup for old resources)
try:
    api_instance.delete_namespaced_deployment(name="nginx-deployment", namespace="default")
    print("Existing nginx-deployment deleted")
except:
    pass

# Delete existing service if it exists
try:
    core_api.delete_namespaced_service(name="nginx-service", namespace="default")
    print("Existing nginx-service deleted")
except:
    pass

# Create deployment
try:
    utils.create_from_yaml(client.ApiClient(), "nginx-deployment.yaml", namespace="default")
    print("My Nginx deployment created!")
except Exception as e:
    print(f"Failed to create deployment: {str(e)}")
    sys.exit(1)

# Create service
try:
    utils.create_from_yaml(client.ApiClient(), "nginx-service.yaml", namespace="default")
    print("My Nginx service created!")
except Exception as e:
    print(f"Failed to create service: {str(e)}")
    sys.exit(1)

def deploy():
    print("Deploying My Nginx application...")

if __name__ == "__main__":
    deploy()
