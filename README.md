# World of Games - Level 4

## Overview
This project is part of the World of Games assignment, Level 4. It features a Flask-based web service that reads a score from a file and serves it over an HTTP endpoint. 
The project is fully containerized using Docker and Docker Compose, and utilizes a Jenkins CI/CD pipeline to automate building, testing, and deploying the service.

## Project Structure
```
.
├── Dockerfile
├── docker-compose.yaml
├── Jenkinsfile
├── main_score.py
├── e2e.py
├── Scores.txt
├── requirements
└── utils.py
```

## 1. Set Up the Application

### main_score.py
- A Flask application that serves a web page displaying the score stored in `Scores.txt`.
- Endpoint: `/score`

### e2e.py
- A Selenium-based test script that automatically launches a browser and verifies that the `/score` endpoint returns a valid score.

### utils.py
- Contains utility variables like `SCORES_FILE_NAME` and a function to clear the screen.

### Scores.txt
- Holds the current score. It is read by the Flask app and validated by the test script.

## 2. Containerized the Application

### Dockerfile
- Builds a Docker image with:
  - Python 3.9
  - Flask
  - The Flask app and Scores.txt
- Exposes port 5000
- Uses CMD to run `main_score.py`

### Docker Compose
- Builds and runs the image
- Mounts `Scores.txt` as a volume to persist the score
- Maps port 5000 on the host to 5000 in the container

```yaml
services:
  flask-app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    volumes:
      - ./Scores.txt:/Scores.txt
    restart: always
    container_name: flask-app-container
```

## 3. Automated the Pipeline

### Jenkinsfile
Defines the full CI/CD pipeline with the following stages:

- **Checkout**: Clones the repository from GitHub.
- **Build**: Builds the Docker image using the Dockerfile.
- **Run**: Starts the Flask container, mounts `Scores.txt`, and maps ports.
- **Setup Test Environment**: Installs Python dependencies from the `requirements` file.
- **Test**: Executes `e2e.py` to ensure the web service works correctly.
- **Finalize**:
  - Stops and removes the Docker container
  - Pushes the Docker image to Docker Hub

## 4. Handled Edge Cases
- Pipeline cleans up Docker containers even if earlier stages fail.
- Scores.txt is mounted as a volume, so scores are preserved even when containers stop or are removed.

## 5. Pushed to Docker Hub
- Docker image is pushed to: [docker.io/fadi7ay/wog-app](https://hub.docker.com/r/fadi7ay/wog-app)
- Can be pulled and run on any Docker-enabled machine:

```bash
docker run -p 5000:5000 fadi7ay/wog-app:latest
```
![ChatGPT Image Apr 2, 2025, 01_54_36 PM](https://github.com/user-attachments/assets/a5a4d924-64a7-4f0e-aa34-f23bdf8b720d)



## How to Run Locally
```bash
git clone https://github.com/Fadi7AY/wog_3.0.git
cd wog_3.0
docker-compose up --build
```

Visit http://localhost:5000/score to see the score.


