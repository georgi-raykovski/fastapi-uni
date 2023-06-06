# fastapi-uni
   This project provides a REST API for deploying a machine learning model using FastAPI.  


## Docker

To run the application using Docker, follow these steps:

1. Build the Docker image:

   ```shell
   docker build -t fastapi-uni .
   ```

2. Run the Docker container

   ```shell
   docker run -p 8000:8000 fastapi-uni
   ```


The FastAPI server will be accessible at http://localhost:8000.
  

## Kubernetes


To deploy the application to Kubernetes using the provided manifest files, follow these steps:

1. Ensure you have a Kubernetes cluster up and running (e.g., Minikube).

2. If using minikube load the local image.
   ```shell
   minikube image load fastapi-uni
   ```
   If using a local registry just push the image into it with `docker push`
   

3. Apply the Kubernetes manifests:

   ```shell
    kubectl apply -f app-deployment.yaml
    ```

4.  Run the container

    ```shell
    kubectl port-forward deployment/fastapi-app 8000:8000
    ```

The FastAPI server will be accessible at http://localhost:8000.

## Usage

1. Once the server is running, navigate to http://localhost:8000/docs to access the automatically generated API documentation. Here, you can explore the available endpoints, view request/response examples, and interact with the API.

2. Train the ML model from the "/fit" endpoint. 

3. From here you can choose either "/predict_single" or "/metrics" to play around with the REST api. The "/predict_single" endpoint has prefilled parameters, try to leave some of them out.

4. You can restart the service and see the error that pops up if the user tries to use any of the endpoints form the above point without training the model first.
