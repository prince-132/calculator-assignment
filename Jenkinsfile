pipeline {
    agent any

    stages {
        stage('webhook') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'githubtoken', url: 'https://github.com/prince-132/calculator-assignment.git']])
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build('calculator')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def workspaceUnixPath = pwd().replaceAll('C:', '/c').replaceAll('\\\\', '/')
                    bat "docker run -v ${workspaceUnixPath}:${workspaceUnixPath} -w ${workspaceUnixPath} calculator pytest -v ./tests/test_calculator.py"
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    def workspaceUnixPath = pwd().replaceAll('C:', '/c').replaceAll('\\\\', '/')
                    bat "docker run -v ${workspaceUnixPath}:${workspaceUnixPath} -w ${workspaceUnixPath} calculator python calculator.py"
                }
            }
        }
    }
}
