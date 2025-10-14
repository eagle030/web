pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Клонируем репозиторий..."
                git branch: 'master', url: 'https://github.com/eagle030/web'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Собираем Docker-образ..."
                sh 'docker build -t myapp:latest .'
            }
        }

        stage('Run Container') {
            steps {
                echo "Запускаем контейнер..."
                sh '''
                    docker stop myapp || true
                    docker rm myapp || true
                    docker run -d -p 5000:5000 --name myapp myapp:latest
                '''
            }
        }
    }
}
