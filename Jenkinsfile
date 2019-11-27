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
        stage('unit test') {
            steps {
                sh 'python Test.py'
            }
        }
        stage('execution') {
            steps {
                sh 'python HelloPython.py'
            }
        }
    }
}
