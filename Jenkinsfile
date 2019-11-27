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
            }
        }
        stage('execution') {
            steps {
                sh 'python HelloPython.py'
            }
        }
    }
}
