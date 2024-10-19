pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Clone the GitHub repository
                git 'https://github.com/your-username/fibonacci-jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Nincs külön dependency, de ha szükséges, itt lehetne pl. pip installt futtatni
                sh 'pip install -r requirements.txt || true'
            }
        }

        stage('Run Tests') {
            steps {
                // Futtatja a Python teszteket
                sh 'python -m unittest discover'
            }
        }
    }

    post {
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
