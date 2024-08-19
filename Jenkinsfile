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
                    def workspaceUnixPath = pwd().replaceAll('\\\\', '/').replaceAll('C:', '/c')
                    docker.image('simple-calculator').inside("-w ${workspaceUnixPath} -v ${workspaceUnixPath}:${workspaceUnixPath}") {
                        sh 'python calculator.py'
                    }
                }
            }
        }
    }
}
