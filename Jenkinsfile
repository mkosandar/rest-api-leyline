
pipeline {
    agent any
    tools {
        //gradle "7.4.2"
        //jdk "JDK15"
        //maven "mvn 3.9.6"
        dockerTool "docker"
        //nodejs "nodejs"
    }
    environment {     
    DOCKERHUB_CREDENTIALS= credentials('dockerHub-login')
    }
    stages {
        stage("docker-publish") {
            steps {
                script{
                    sh """
                    docker build -t mayureshkosandar/rest-api-project_web:latest .
                    docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW}
                    docker push mayureshkosandar/rest-api-project_web:latest
                    """
                }
            }
        }
        stage("deploy-to-minikubecluster") {
            steps {
                script{
                    sh """
                    helm install rest-api ./home/mk/helm-charts/rest-api-chart
                    """
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
