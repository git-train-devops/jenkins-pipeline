pipeline {
    agent {label "agent1"}

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'docker:dind'
                    // Run the container on the node specified at the
                    // top-level of the Pipeline, in the same workspace,
                    // rather than on a new node entirely:
                    reuseNode true
                }
            }
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
