# Fake Job Detector

A full-stack web application that detects fraudulent job postings using machine learning. Paste a job description, and the app tells you whether it's **REAL** or **FAKE** — powered by a Logistic Regression + TF-IDF classification model served via a dedicated Python Flask API.

🔗 **Live Demo** → [fakejobdetector2.onrender.com](https://fakejobdetector2.onrender.com/)

---

## How It Works

1. User pastes a job description into the frontend
2. The Spring Boot backend receives the input and forwards it to the Flask ML service
3. The Flask API runs it through a trained **Logistic Regression + TF-IDF** pipeline
4. The prediction (`FAKE` or `REAL`) is returned to Spring Boot, stored in PostgreSQL, and sent back to the UI

---

## Architecture

```
┌─────────────────────┐
│   HTML/CSS/JS UI    │  ← Single-page frontend
└────────┬────────────┘
         │ POST /api/job/analyze
┌────────▼────────────┐
│  Spring Boot API    │  ← Main backend (Java)
│  + PostgreSQL       │  ← Job listings stored on Neon
└────────┬────────────┘
         │ POST /predict
┌────────▼────────────┐
│  Python Flask API   │  ← ML service
│  Logistic Regression│
│  + TF-IDF           │
└─────────────────────┘
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Java, Spring Boot, Spring Data JPA |
| ML Service | Python, Flask, Logistic Regression, TF-IDF |
| Database | PostgreSQL (Neon) |
| Containerisation | Docker |
| Deployment | Render |

---

## API Reference

### Spring Boot — `POST /api/job/analyze`

**Request**
```json
{
  "description": "We are hiring a remote data entry officer. No experience required. Earn $5000/week."
}
```

**Response**
```json
{
  "result": "FAKE"
}
```

---

### Flask ML Service — `POST /predict`

**Request**
```json
{
  "text": "We are hiring a remote data entry officer..."
}
```

**Response**
```json
{
  "prediction": "FAKE"
}
```

---

## Running Locally

### Prerequisites
- Java 17+
- Python 3.9+
- PostgreSQL (or a [Neon](https://neon.tech) connection string)
- Docker (optional)

---

### 1. Flask ML Service

```bash
cd ml-service
pip install -r requirements.txt
python app.py
# Runs on http://localhost:5000
```

---

### 2. Spring Boot Backend

Set the following environment variables:

```
SPRING_DATASOURCE_URL=jdbc:postgresql://<your-neon-host>/neondb
SPRING_DATASOURCE_USERNAME=your_username
SPRING_DATASOURCE_PASSWORD=your_password
```

> **Note:** If your `description` column hits character limits, run this once:
> ```sql
> ALTER TABLE job_listings ALTER COLUMN description TYPE TEXT;
> ```

Then run the app from VS Code or IntelliJ by starting `FakejobdetectorApplication.java`.

The API starts on `http://localhost:8080`.

---

### 3. Running via Docker

```bash
docker build -t fakejobdetector .
docker run -p 8080:8080 fakejobdetector
```

---

## Project Structure

```
fakejobdetector/
├── src/
│   └── main/
│       ├── java/com/shyam/fakejobdetector/
│       │   ├── controller/
│       │   ├── model/
│       │   ├── repository/
│       │   └── service/
│       └── resources/
│           └── static/
│               └── index.html
├── ml-service/
│   ├── app.py
│   ├── model.pkl
│   └── requirements.txt
├── Dockerfile
└── pom.xml
```

---

## Author

**Shyam A** — [github.com/shyam6767](https://github.com/shyam6767) · [LinkedIn](https://www.linkedin.com/in/shyam6712/)
