pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    docker.build('simple-calculator')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests inside the Docker container
                    docker.image('simple-calculator').inside("-v ${pwd()}:/workspace -w /workspace") {
                        sh 'pytest tests/test_calculator.py'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Run the calculator inside the Docker container
                    docker.image('simple-calculator').inside("-v ${pwd()}:/workspace -w /workspace") {
                        sh 'python calculator.py'
                    }
                }
            }
        }
    }
}
