# Usermanagement-GCP
This repository contains a FastAPI application that serves as a unified API for user management across three different projects. The API facilitates essential user operations.

- **Creating Users**: Add new users to the Firestore database with relevant details.
- **Retrieving User Details**: Fetch user information based on unique identifiers.
- **Updating User Information**: Modify existing user data to keep it current.
- **Deleting Users**: Remove users from the database when necessary.


## Features

- **CRUD Operations**: Implements full Create, Read, Update, and Delete functionality using Firestore, a scalable NoSQL database provided by Google Cloud Platform (GCP).
- **Swagger Documentation**: Automatically generated API documentation for testing and exploring endpoints, accessible at `/docs`.
- **GCP Integration**: The application is designed to work seamlessly with Google Cloud services, utilizing Firestore for data storage and Google Cloud Run (GCR) for hosting.


## Setup Instructions

### Clone the Repository

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   
2. Navigate to the project directory:
    ```bash
    cd Usermanagement-GCP/
    ```

3. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    env/script/activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```


## Running the Application
Start the application:
    ```bash
    python3 main.py
    ```



