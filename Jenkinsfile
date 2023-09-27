pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Build your application (e.g., using Maven, Gradle, etc.)
                sh 'mvn clean package'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                // Use kubectl to apply Kubernetes manifests
                script {
                    def kubeconfig = readKubeconfig()
                    sh "kubectl apply --kubeconfig=\$kubeconfig -f deployment.yaml"
                }
            }
        }
    }
}
