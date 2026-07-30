Fake Job Detector

A full-stack web application designed to detect fraudulent job postings using a machine learning model. The application features a Spring Boot backend, a PostgreSQL database hosted on Neon, an HTML/CSS/JavaScript frontend, and a Python Flask backend serving the machine learning model.

Architecture
Frontend: HTML, CSS, JavaScript (Single-page user interface)

Backend API: Java Spring Boot (Containerized with Docker and deployed on Render)

Database: PostgreSQL (Hosted on Neon Tech)

Machine Learning Service: Python Flask API running a Logistic Regression and TF-IDF classification model (Hosted on Render)

Project Structure
Plaintext
fakejobdetector/
├── src/
│   ├── main/
│       ├── java/com/shyam/fakejobdetector/
│       │   ├── controller/
│       │   ├── model/
│       │   ├── repository/
│       │   └── service/
│       └── resources/
│           └── static/
│               └── index.html
├── Dockerfile
└── pom.xml
Setup and Installation
1. Database Configuration
Ensure your PostgreSQL database contains the necessary schema. To handle long job descriptions without character limitations, ensure the description column in the job_listings table is set to type TEXT:

SQL
ALTER TABLE job_listings ALTER COLUMN description TYPE TEXT;
2. Environment Variables
The Spring Boot application requires connection details for the database and the remote machine learning endpoint:

SPRING_DATASOURCE_URL: PostgreSQL JDBC connection string

SPRING_DATASOURCE_USERNAME: Database username

SPRING_DATASOURCE_PASSWORD: Database password

3. Running Locally via Docker
Build and run the container locally using Docker:

Bash
docker build -t fakejobdetector .
docker run -p 8080:8080 fakejobdetector
API Endpoints
Spring Boot Application
POST /api/job/analyze

Request Body: JSON object containing the job description text.

Response: JSON object containing the classification result (FAKE or REAL).

Python Flask ML Service
POST /predict

Request Body: Raw text or JSON payload containing the job description.

Response: Model prediction output.
