pipeline {
    agent {label "agent1"}

    stages {
        stage('Build') {
            steps {
                script {
                    def customImage = docker.build("my-first-python-app:latest")
                    // customImage.inside {
                    //     sh 'pytest'
                    // }
                    //push the image
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        sh 'docker run -t -d -u 1000:1000 --name first-pipeline my-first-python-app cat'
                        sh 'docker exec -t first-pipeline pytest'
                    } catch (err) {
                        echo "Failed: ${err}"
                    } finally {
                        sh 'docker rm -f first-pipeline'
                        sh 'exit 1'
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
