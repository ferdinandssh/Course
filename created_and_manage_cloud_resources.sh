# https://www.cloudskillsboost.google/focuses/10258?parent=catalog

# Setup region and zone
gcloud auth list
gcloud config set compute/region "us-west1"
gcloud config set compute/zone "us-west1-a"


# Task 1. Create a project jumphost instance
gcloud compute instances create nucleus-jumphost-390 --machine-type e2-micro --zone us-west1-a


# Task 2. Create a Kubernetes service cluster
## Create a GKE cluster
gcloud container clusters create --machine-type=e2-micro --zone=us-west1-a nucleus-jumphost-390-cluster

## Authenticate with the cluster:
gcloud container clusters get-credentials nucleus-jumphost-390-cluster

## Deploy an application to the cluster
kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:2.0
kubectl expose deployment hello-server --type=LoadBalancer --port 8081
kubectl get service # Wait until get the IP Address
# Testing by open http://[EXTERNAL-IP]:8080


# Task 3. Set up an HTTP load balancer
# Create an instance template


gcloud compute instance-templates create nginx-template \
  --metadata-from-file startup-script=startup.sh

# Create a target pool
gcloud compute target-pools create nginx-pool

# Create a managed instance group of 2 nginx web servers
gcloud compute instance-groups managed create nginx-group \
	--base-instance-name nginx \
	--size 2 \
	--template nginx-template \
	--target-pool nginx-pool

# Create a firewall rule
gcloud compute firewall-rules create permit-tcp-rule-602 --allow tcp:80

# Create a forwarding rule
gcloud compute forwarding-rules create nginx-lb \
	--region us-west1 \
	--ports=80 \
	--target-pool nginx-pool

# Create a health check
gcloud compute http-health-checks create http-basic-check

# Create a backend service and attach the managed instasnce group
gcloud compute instance-groups managed \
	set-named-ports nginx-group \
	--named-ports http:80

gcloud compute backend-services create nginx-backend \
	--protocol HTTP \
	--health-checks http-basic-check \
	--global

gcloud compute backend-services add-backend nginx-backend \
	--instance-group nginx-group \
	--instance-group-zone us-west1-a \
	--global

# Create a url map and target the HTTP proxy
gcloud compute url-maps create web-map \
	--default-service nginx-backend

gcloud compute target-http-proxies create http-lb-proxy \
	--url-map web-map

# Create a forwarding rule
gcloud compute forwarding-rules create http-content-rule \
	--global \
	--target-http-proxy http-lb-proxy \
	--ports 80










