String imageName = 'portal.kickerliga-bochum.de'
String testImageName = 'e2e-kickerliga:test'
String testContainerName = 'e2e-test-kickerliga'

pipeline {
    agent {
        label 'jenkins'
    }
    environment {
        NO_COLOR=1
        TERM='xterm-256color'
    }
    stages {
        stage ('Test') {
            steps {
                script {
                    dir ('backend') {
                        sh 'pip install -r requirements.txt'
                        sh 'python -m pylint .'
                        sh 'python -m pytest --cov=models --cov=modules'
                    }
                    dir ('frontend') {
                        sh 'npm install'
                        sh 'npm run unit-test'
                        sh "docker build --tag ${testImageName} ."
                        sh "docker run -d --rm --name ${testContainerName} -p 5173:5173 ${testImageName}"
                        sh 'npm run e2e-test'
                        sh "docker stop ${testContainerName}"
                    }
                }
            }
        }
        stage ('Build') {
            steps {
                script {
                    dir ('backend') {
                        sh "docker build --tag ${imageName}:latest ."
                    }
                    dir ('frontend') {
                        sh 'npm run build'
                    }
                }
            }
        }
        stage ('Deploy') {
            steps {
                script {
                    try {
                        sh "docker stop ${imageName} && docker rm ${imageName}"
                    }
                    catch (ignored) {
                        println("${imageName} has not been running!")
                    }
                    withCredentials([string(credentialsId: 'kickerliga-bochum.de-password', variable: 'password')]) {
                        withCredentials([usernamePassword(credentialsId: 'marciland.net-mailtoken', usernameVariable: 'mailUser', passwordVariable: 'mailPass')]) {
                            sh "docker run -d --restart always --name ${imageName} -p 0.0.0.0:8001:8001 ${imageName}:latest -p ${password} --mail-user ${mailUser} --mail-pass ${mailPass}"
                        }
                    }
                    sh 'docker image prune -f'
                    // TODO deploy frontend aswell?
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}