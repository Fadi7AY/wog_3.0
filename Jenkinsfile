pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "fadi7ay/wog-app:latest"
        CONTAINER_NAME = "flask-app-container"
        PYTHON_PATH = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" 
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
                echo 'Stopping and removing any existing container...'
                sh '''
                docker stop ${CONTAINER_NAME} || true
                docker rm ${CONTAINER_NAME} || true
                '''
                echo 'Running the Dockerized application...'
                sh '''
                docker run -d --name ${CONTAINER_NAME} -p 5000:5000 -v $(pwd)/Scores.txt:/Scores.txt ${DOCKER_IMAGE}
                '''
            }
        }

        stage('Setup Test Environment') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                ${PYTHON_PATH} --version || exit 1
                ${PYTHON_PATH} -m pip install -r requirements
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running e2e tests with Selenium...'
                script {
                    def result = sh(script: "${PYTHON_PATH} e2e.py", returnStatus: true)
                    if (result != 0) {
                        currentBuild.result = 'FAILURE'
                        error 'Tests failed'
                    }
                }
            }
        }

        stage('Finalize') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo 'Stopping and removing the container...'
                sh '''
                docker stop ${CONTAINER_NAME} || true
                docker rm ${CONTAINER_NAME} || true
                '''
                echo 'Pushing the Docker image to Docker Hub...'
                sh 'docker push ${DOCKER_IMAGE}'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up resources...'
            sh '''
            docker stop ${CONTAINER_NAME} || true
            docker rm ${CONTAINER_NAME} || true
            '''
        }
    }
}
