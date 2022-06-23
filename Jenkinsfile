pipeline {
    agent {label "agent1"}
    environment {
        DOCKER_IMAGE = "devopstraining1236/my-first-python-app:latest"
        DOCKER = credentials('docker-hub-access-key')
        SYS_CREDS = credentials('sys-user-pass')
        GITHUB_TOKEN = credentials('github-token')
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
                sh 'ansible-playbook -i hosts -e DOCKER_IMAGE=$DOCKER_IMAGE -e CONTAINER=$CONTAINER -e DOCKER_USR=$DOCKER_USR -e DOCKER_PSW=$DOCKER_PSW -e sys_usr=$SYS_CREDS_USR -e sys_pwd=$SYS_CREDS_PSW playbook.yml'
            }
        }
    }
    post { 
        success { 
            sh '''
            curl -XPOST -H "Accept: application/vnd.github.v3+json" -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/repos/git-train-devops/jenkins-pipeline/statuses/$(git rev-parse HEAD) -d '{"state": "success", "target_url": "${BUILD_URL}", "description": "The build has succeeded!", "context":"continuous-integration/jenkins"}'
            '''
        }
        failure { 
            sh '''
            curl -XPOST -H "Accept: application/vnd.github.v3+json" -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/repos/git-train-devops/jenkins-pipeline/statuses/$(git rev-parse HEAD) -d '{"state": "failure", "target_url": "${BUILD_URL}", "description": "The build has failed!", "context":"continuous-integration/jenkins"}'
            '''
        }
    }
}
