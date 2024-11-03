# Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

# Set the working directory
WORKDIR /app

# Copy the FastAPI application code to the container
COPY ./app /app

# Copy the service account JSON file
COPY secret.json /app/secret.json

# Copy the environment file
COPY dev.env /app/dev.env

# Install any additional dependencies if needed
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8080

# Run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
