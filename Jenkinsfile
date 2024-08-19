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
        stage('Deploy') {
            steps {
                script {
                    def workspaceUnixPath = pwd().replaceAll('C:', '/c').replaceAll('\\\\', '/')
                    sh "docker run -v ${workspaceUnixPath}:${workspaceUnixPath} -w ${workspaceUnixPath} simple-calculator python calculator.py"
                }
            }
        }
    }
}
