pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t wog-app .'
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    sh 'docker run -d -p 8777:8777 --name wog-container wog-app'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def result = sh(script: 'python e2e.py', returnStatus: true)
                    if (result != 0) {
                        error 'Tests failed'
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    sh 'docker stop wog-container'
                    sh 'docker rm wog-container'
                    sh 'docker tag wog-app your-dockerhub-username/wog-app:latest'
                    sh 'docker push your-dockerhub-username/wog-app:latest'
                }
            }
        }
    }
}



