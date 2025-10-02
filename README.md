
# URL-CHECKER

This a python app which prompts two urls - one results with status code 200 and the other 503.






## Installation

I am using https://tools-httpstatus.pickup-services.com for the purpose. 
Checkout repo 

To start the app locally, install dependencies:

    python3 -m pip install prometheus_client httpx
    
Set virtual environment:

    python3 -m venv venv
    source venv/bin/activate




## Run Locally

Clone the project

Start the app locally:

    python main.py

From another terminal hit the locally deployed container:

    curl http://localhost:8000/




To start the app in docker build docker image:

    docker build -t url_checker_prometheus .

After building the image start the container:

    docker run -d -p 8000:8000 --name url_checker url_checker_prometheus

Hit: `curl http://localhost:8000`

## Deployment


After cloning the repo git@github.com:pechenikov/url_checker.git open url-checker-helm.
Set cluster context. Install chart:

    helm install -n $namespace url-checker ./url-checker-helm/

Check the internal ip of the service:

    kubectl get svc -n $namespace

The Deployment is ClusterIp. This means tha the service can be accessed only from inside the kubernetes cluster. 
For that purpose create test pod:


    kubectl run -it --rm curl-test --image=radial/busyboxplus:curl --restart=Never -- sh

From the test pod hit the endpoint:

    curl $ip:8000



If the service need to be accessed outside the cluster change the values.yaml snippet:


    service:
        type: ClusterIP
        port: 8000

to:

    service:
        type: LoadBalancer
        port: 8000



The endpoint required for the Loadbalancer should be configured seperatly according to the kind of Kubernetes cluster - onprem or cloud. For azure for example additional annotation is required:

    service.beta.kubernetes.io/azure-load-balancer-internal: "true"