pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Install and Test') {
            steps {
                sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt && pytest -v'
            }
        }
        stage('Build Image') {
            steps { sh 'docker build -t fastapi-app:${BUILD_NUMBER} .' }
        }
        stage('Deploy') {
            steps {
                sh 'docker rm -f fastapi-app || true'
                sh 'docker run -d --name fastapi-app -p 8000:8000 fastapi-app:${BUILD_NUMBER}'
            }
        }
    }
    post {
        failure { echo 'Build failed - check the console output' }
    }
}