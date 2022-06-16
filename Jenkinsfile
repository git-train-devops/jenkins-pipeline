pipeline {
    agent {label "agent1"}

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t my-first-python-app .'
            }
        }
        stage('Test') {
            steps {
                echo 'This is test stage - trigger'
            }
        }
        stage('Deploy') {
            steps {
                echo 'This is deploy stage'
            }
        }
    }
}
