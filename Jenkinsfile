pipeline {
    agent {label "agent1"}
    environment {
        DOCKER_IMAGE = "devopstraining1236/my-first-python-app:latest"
    }
    stages {
        stage('Build') {
            steps {
                script {
                    def customImage = docker.build(DOCKER_IMAGE)
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
                CONTAINER = "first-pipeline"
            }
            steps {
                script {
                    try {
                        sh 'docker run -t -d -u 1000:1000 --name $CONTAINER $DOCKER_IMAGE cat'
                        sh 'docker exec -t $CONTAINER pytest'
                    } catch (err) {
                        echo "Failed: ${err}"
                        sh 'docker rm -f $CONTAINER'
                        sh 'exit 1'
                    } finally {
                        echo "This is for docker container cleanup"
                    }
                    try {
                        echo "This is for docker push"
                        // sh 'docker login -u $DOCKER_USR -p $DOCKER_PWD'
                        // sh 'docker push $DOCKER_IMAGE'
                    }
                    finally {
                        echo "This is for docker image cleanup"
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
