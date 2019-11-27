pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                echo 'version'
                sh 'python --version'
            }
        }
        stage('code pull') {
            steps {
                checkout scm
            }
        }
    }
}
