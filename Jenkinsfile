pipeline {
    agent {label "agent1"}
    environment {
        DOCKER_IMAGE = "devopstraining1236/my-first-python-app:latest"
        DOCKER = credentials('docker-hub-access-key')
        CONTAINER = "first-pipeline"
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
            steps {
                script {
                    try {
                        sh 'docker run -t -d -u 1000:1000 --name $CONTAINER $DOCKER_IMAGE cat'
                        sh 'docker exec -t $CONTAINER pytest'
                    } catch (err) {
                        echo "Failed: ${err}"
                        sh 'docker rm -f $CONTAINER'
                        sh 'exit 1'
                    }
                    sh "docker rm -f $CONTAINER"
                    try {
                        echo "Docker login ......"
                        sh 'docker login -u $DOCKER_USR -p $DOCKER_PSW'
                        echo "Docker push ......."
                        sh 'docker push $DOCKER_IMAGE'
                        echo "Docker logout ......."
                        sh 'docker logout'
                    }
                    catch (err) {
                        echo "Failed: ${err}"
                        sh 'exit 1'
                    }
                    finally {
                        echo "removing docker image ...... $DOCKER_IMAGE"
                        sh "docker rmi -f $DOCKER_IMAGE"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'ansible-playbook -i hosts -e DOCKER_IMAGE=$DOCKER_IMAGE -e CONTAINER=$CONTAINER -e DOCKER_USR=$DOCKER_USR -e DOCKER_PSW=$DOCKER_PSW playbook.yml'
            }
        }
    }
}
