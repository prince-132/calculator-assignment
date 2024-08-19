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
                    def absolutePath = "${env.WORKSPACE}/calculator"
                    docker.image('simple-calculator').inside("-v ${absolutePath}:${absolutePath}") {
                        sh 'python calculator.py'
                    }
                }
            }
        }
    }
}
