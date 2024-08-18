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
                    // Convert Windows path to Unix style for Docker
                    def workspaceUnix = "${env.WORKSPACE}".replaceAll('C:', '/c').replaceAll('\\\\', '/')
                    
                    // Run tests inside the Docker container
                    docker.image('simple-calculator').inside("-v ${workspaceUnix}:/workspace -w /workspace") {
                        sh 'pytest tests/test_calculator.py'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Convert Windows path to Unix style for Docker
                    def workspaceUnix = "${env.WORKSPACE}".replaceAll('C:', '/c').replaceAll('\\\\', '/')
                    
                    // Run the calculator inside the Docker container
                    docker.image('simple-calculator').inside("-v ${workspaceUnix}:/workspace -w /workspace") {
                        sh 'python calculator.py'
                    }
                }
            }
        }
    }
}
