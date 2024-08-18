pipeline {
    agent any

    environment {
        JENKINS_IMAGE = 'jenkins-simulator'  // The custom Jenkins-like environment image
        APP_IMAGE = 'simple-calculator'      // The application image
    }

    stages {
        stage('Build Jenkins Environment') {
            steps {
                script {
                    // Build the Docker image for the Jenkins-like environment
                    docker.build("${JENKINS_IMAGE}", '.')
                }
            }
        }
        stage('Run Tests in Jenkins-like Environment') {
            steps {
                script {
                    // Run tests inside the Jenkins-like Docker environment
                    docker.image("${JENKINS_IMAGE}").inside("-v ${pwd()}:/workspace -w /workspace") {
                        sh '''
                        #!/bin/bash
                        set -e
                        
                        # Build the application Docker image
                        docker build -t ${APP_IMAGE} .
                        
                        # Run tests inside the application Docker container
                        docker run --rm -v "$(pwd)":/workspace -w /workspace ${APP_IMAGE} sh -c "pytest tests/test_calculator.py"
                        '''
                    }
                }
            }
        }
        stage('Deploy in Jenkins-like Environment') {
            steps {
                script {
                    // Run the application inside the Jenkins-like Docker environment
                    docker.image("${JENKINS_IMAGE}").inside("-v ${pwd()}:/workspace -w /workspace") {
                        sh '''
                        #!/bin/bash
                        set -e
                        
                        # Run the application inside the application Docker container
                        docker run --rm -v "$(pwd)":/workspace -w /workspace ${APP_IMAGE} sh -c "python calculator.py"
                        '''
                    }
                }
            }
        }
    }
}
