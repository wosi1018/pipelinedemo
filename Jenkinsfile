pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                echo 'python --version'
            }
        }
        stage('code pull') {
            steps {
                checkout scm
            }
        }
    }
}
