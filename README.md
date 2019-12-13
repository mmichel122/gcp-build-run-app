# Simple Python Flask Dockerized Application #

Build the image using the following command

```bash
docker build -t flask-app:latest .
```

Run the Docker container using the command shown below.

```bash
docker run -d -p 8080:8080 flask-app
```

Build the Cloud Run container using the command below

```bash
gcloud builds submit --config cloudbuild.yaml
```

That will build the docker image from the Dockerfile, push the image on GCP registry and build the Cloud Run container.
