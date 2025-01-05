pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "fadi7ay/wog-app:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the repository...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the Docker image...'
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }

        stage('Run') {
            steps {
                echo 'Running the Dockerized application...'
                sh 'docker run -d --name flask-app-container -p 5000:5000 -v $(pwd)/Scores.txt:/Scores.txt ${DOCKER_IMAGE}'
            }
        }

        stage('Test') {
            steps {
                echo 'Running e2e tests with Selenium...'
                script {
                    def result = sh(script: 'python3 e2e.py', returnStatus: true)
                    if (result != 0) {
                        error 'Tests failed'
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                echo 'Finalizing the pipeline...'
                sh 'docker stop flask-app-container || true'
                sh 'docker rm flask-app-container || true'
                sh 'docker push ${DOCKER_IMAGE}'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up resources...'
            sh 'docker stop flask-app-container || true'
            sh 'docker rm flask-app-container || true'
        }
    }
}
