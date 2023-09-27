pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build and Push to GCR') {
            steps {
                // Build your Docker image with the appropriate Dockerfile
                sh 'docker build -t gcr.io/my-pro-400108/my_pro-flask-app:latest .'

                // Authenticate with Google Container Registry (GCR)
                withCredentials([[
                    $class: 'UsernamePasswordMultiBinding',
                    credentialsId: 'gcr-credentials',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD'
                ]]) {
                    sh "docker login -u $USERNAME -p $PASSWORD https://gcr.io"
                }

                // Push the Docker image to GCR
                sh "docker push gcr.io/my-pro-400108/my_pro-flask-app:latest"
            }
        }
        stage('Deploy to GKE') {
            steps {
                // Authenticate with Google Kubernetes Engine (GKE)
                withCredentials([usernamePassword(credentialsId: 'gke-credentials', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    // Set the kubectl context to your GKE cluster
                    sh "kubectl config use-context my-cluster"
                    
                    // Apply your Kubernetes deployment configuration (YAML)
                    sh "kubectl apply -f https://raw.githubusercontent.com/Antony313/my_pro/main/deployment.yaml"
                }
            }
        }
    }
}
