String dockerRun = 'docker run -d --restart always --name'
String imageName = 'portal.kickerliga-bochum.de'

pipeline {
    agent {
        label 'jenkins'
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
                        // sh 'npm run e2e-test' TODO
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
                            sh "${dockerRun} ${imageName} -p 0.0.0.0:8001:8001 ${imageName}:latest -p ${password} --mail-user ${mailUser} --mail-pass ${mailPass}"
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