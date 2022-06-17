pipeline {
    agent {label "agent1"}

    stages {
        stage('Build&Test') {
            steps {
                script {
                    def customImage = docker.build("my-first-python-app:latest")
                    customImage.inside {
                        sh 'pytest'
                    }
                    //push the image
                }
                // sh 'docker build -t my-first-python-app .'
            }
        }
        stage('Push') {
            steps {
                sh 'push image'
            }
        }
        stage('Deploy') {
            steps {
                echo 'This is deploy stage'
            }
        }
    }
}
