pipeline {
    agent any
    stages {
        stage('code pull') {
            steps {
                checkout scm
            }
        }
        stage('Static code metrics') {
            steps {
                echo "PEP8 style check"
                sh  ''' source activate ${BUILD_TAG}
                        pylint --disable=C irisvmpy || true
                    '''
            }
        }
    }
}
