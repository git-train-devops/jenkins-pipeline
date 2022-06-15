pipeline {
    agent {label "agent1"}

    stages {
        stage('Build') {
            steps {
                echo 'This is build stage - trigger'
            }
        }
        stage('Test') {
            steps {
                echo 'This is test stage'
            }
        }
        stage('Deploy') {
            steps {
                echo 'This is deploy stage'
            }
        }
    }
}
