pipeline {

    agent any

    stages {

        stage('Git Checkout') {
            steps {
                git https://github.com/VijayaLaxmi474/employee-management-devops-project
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-app:v1 .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh 'docker images'
            }
        }

    }

}
