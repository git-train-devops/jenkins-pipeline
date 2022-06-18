pipeline {
    agent {label "agent1"}

    stages {
        stage('Build') {
            steps {
                script {
                    def customImage = docker.build("devopstraining1236/my-first-python-app:latest")
                    // customImage.inside {
                    //     sh 'pytest'
                    // }
                    //push the image
                }
            }
        }
        stage('Test&push') {
            environment {
                DOCKER = credentials('docker-hub-access-key')
            }
            steps {
                script {
                    try {
                        sh 'docker run -t -d -u 1000:1000 --name first-pipeline my-first-python-app cat'
                        sh 'docker exec -t first-pipeline pytest'
                    } catch (err) {
                        echo "Failed: ${err}"
                        sh 'docker rm -f first-pipeline'
                        sh 'exit 1'
                    } finally {
                        echo "This is for docker container cleanup"
                    }
                    try {
                        echo "This is for docker push"
                        // sh 'docker login -u $DOCKER_USR -p $DOCKER_PWD'
                        // sh 'docker push devopstraining1236/my-first-python-app:latest'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'This is deploy stage'
            }
        }
    }
}
