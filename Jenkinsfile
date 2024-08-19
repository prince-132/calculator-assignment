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
        // stage('Test') {
        //     steps {
        //         script {
                    
        //         }
        //     }
        // }
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
