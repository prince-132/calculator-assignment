pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('simple-calculator')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def workspaceUnixPath = pwd().replaceAll('C:', '/c').replaceAll('\\\\', '/')
                    bat """
                    docker run -v ${workspaceUnixPath}:/app -w /app -e PYTHONPATH=/app simple-calculator /bin/bash -c "which pytest && pytest -v /app/tests/test_calculator.py"
                    """
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    def workspaceUnixPath = pwd().replaceAll('C:', '/c').replaceAll('\\\\', '/')
                    bat "docker run -v ${workspaceUnixPath}:${workspaceUnixPath} -w ${workspaceUnixPath} simple-calculator python calculator.py"
                }
            }
        }
    }
}
