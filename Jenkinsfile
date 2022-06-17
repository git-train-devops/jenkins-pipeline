pipeline {
    agent {label "agent1"}

    stages {
        stage('Build&Test') {
            steps {
                script {
                    def customImage = docker.build("my-first-python-app:latest")
                    // customImage.inside {
                    //     sh 'pytest'
                    // }
                    //push the image
                }
                sh 'docker run -t -d -u 1000:1000 --name first-pipeline my-first-python-app cat'
                sh 'docker exec -t first-pipeline pytest'
                sh 'docker rm -f first-pipeline'
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
