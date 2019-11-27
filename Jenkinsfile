pipeline {
    agent any
    stages {
        stage('python version') {
            steps {
                echo 'python version'
                sh 'python --version'
            }
        }
        stage('code pull') {
            steps {
                checkout scm
            }
        }
        stage('Unit tests') {
            steps {
                sh  'source activate ${BUILD_TAG}'
                sh  'python -m pytest --verbose --junit-xml test-reports/results.xml'
            }
        }
    }
}
