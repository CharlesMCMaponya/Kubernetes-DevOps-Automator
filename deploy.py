import argparse
from kubernetes import client, config

def deploy():
    config.load_kube_config()
    try:
        with open("nginx-deployment.yaml") as f:
            dep = client.V1Deployment.from_yaml(f)
        api = client.AppsV1Api()
        api.create_namespaced_deployment(namespace="default", body=dep)
        print("Nginx deployment created!")
    except FileNotFoundError:
        print("Error: nginx-deployment.yaml not found!")
        return
    try:
        with open("nginx-service.yaml") as f:
            svc = client.V1Service.from_yaml(f)
        api = client.CoreV1Api()
        api.create_namespaced_service(namespace="default", body=svc)
        print("Nginx service created!")
    except FileNotFoundError:
        print("Error: nginx-service.yaml not found!")
        return

def delete():
    config.load_kube_config()
    api = client.CoreV1Api()
    try:
        api.delete_namespaced_service(name="nginx-service", namespace="default")
        print("Nginx service deleted!")
    except client.ApiException as e:
        if e.status != 404:
            raise
        print("Nginx service already deleted!")
    api = client.AppsV1Api()
    try:
        api.delete_namespaced_deployment(name="nginx-deployment", namespace="default")
        print("Nginx deployment deleted!")
    except client.ApiException as e:
        if e.status != 404:
            raise
        print("Nginx deployment already deleted!")

def main():
    parser = argparse.ArgumentParser(description="Kubernetes Automation Tool")
    parser.add_argument("command", choices=["deploy", "delete"], help="Command to run")
    args = parser.parse_args()

    if args.command == "deploy":
        deploy()
    elif args.command == "delete":
        delete()

if __name__ == "__main__":
    main()