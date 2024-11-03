#!/bin/bash

# Define variables
IMAGE_NAME="Enter-the-image-name"
CONTAINER_NAME="Enter-the-Containername"
PROJECT_ID="Enter-the-project-id-gcp"
REGION="Region-to-be-deployed"
ENV_FILE="./dev.env"

# Build the Docker image
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

# Run the Docker container
echo "Running Docker container..."
docker run --name $CONTAINER_NAME --env-file $ENV_FILE -p 8080:8080 $IMAGE_NAME

# Set the Google Cloud project
echo "Setting Google Cloud project..."
gcloud config set project $PROJECT_ID

# Tag the Docker image for GCR
echo "Tagging Docker image..."
docker tag $IMAGE_NAME gcr.io/$PROJECT_ID/$IMAGE_NAME

# Push the Docker image to Google Container Registry
echo "Pushing Docker image to Google Container Registry..."
docker push gcr.io/$PROJECT_ID/$IMAGE_NAME

# Deploy to Google Cloud Run
echo "Deploying to Google Cloud Run..."
gcloud run deploy $CONTAINER_NAME \
  --image gcr.io/$PROJECT_ID/$IMAGE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated

echo "Deployment completed successfully!"
