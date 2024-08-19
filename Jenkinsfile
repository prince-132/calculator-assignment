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
                    // docker.image('simple-calculator').inside {
                    //     sh 'pytest ./tests/test_calculator.py'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    docker.image('simple-calculator').inside {
                        sh 'python calculator.py'
                    }
                }
            }
        }
    }
}