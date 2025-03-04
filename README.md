# Cloud Run App with OAuth2 and Firestore

## Overview
This project involves building a web application that implements authentication and authorization using OAuth2 with Google's Identity Platform. The backend is a FastAPI web server that serves HTML pages and interacts with Firestore as the datastore. The frontend will use vanilla JavaScript to send data to the backend API.

You will deploy the FastAPI server on **Google Cloud Run**, use **Google Cloud Identity Platform** for OAuth2 authentication, and **Firestore** for handling user data and application-related information.

### YOUR APPLICATION URL HERE!

## Addition Docs


## Technologies Used
- **FastAPI**: Python-based web framework for serving HTML and handling API requests
- **Google Cloud Identity Platform**: Manages OAuth2 authentication and user sign-ins
- **Firestore**: NoSQL database for storing application data and login information
- **Google Cloud Run**: Runs and deploys the FastAPI web server
- **Firestore Emulator**: Used for local development to simulate Firestore behavior
- **Vanilla JavaScript**: Handles client-side interactions and posts data to the API
- **Docker & Docker Compose**: Used for containerized local development

## Local Development Setup
The project is already set up to run with Docker Compose. The setup includes:
- A FastAPI web server running in a container (`vote` service)
- A Firestore emulator running in a container (`db` service)
- Authentication can be disabled in local mode by passing `auth=false` as a query parameter

### Running Locally
1. **Clone the repository**
   ```sh
   git clone <repository_url>
   cd <project_directory>
   ```

2. **Start the application using Docker Compose**
   ```sh
   docker compose up --build
   ```

3. **Access the application**
   - FastAPI Server: [http://localhost:9080](http://localhost:9080)
   - Firestore Emulator: [http://localhost:8080](http://localhost:8080)
   - Disable authentication by adding `?auth=false` to the query parameters

## Rubric (Total: 15 Points)
| Criteria | Points |
|----------|--------|
| OAuth2 login works using Google Identity Platform | 5 pts |
| Web server works with client-side JavaScript posting to backend | 5 pts |
| Firestore is correctly set up and used for data storage | 5 pts |

## Submission
1. **GitHub Repository:**
   - Ensure your project is in a **GitHub repository**.
   - The repository should include all necessary files (`main.py`, `Dockerfile`, `docker-compose.yml`, `index.html`, `requirements.txt`, etc.).

2. **Deployment:**
   - Deploy your FastAPI server to **Google Cloud Run**.
   - Ensure your **Firestore database** is properly configured and accessible by the application.

3. **README File:**
   - **Update this README with your application URL**
     - i.e. `https://tabs-vs-spaces-XXXXXX.us-central1.run.app/`

4. **Submit Application URL to Canvas:**
