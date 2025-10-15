pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                // Клонируем репозиторий
                git branch: 'practice', url: 'https://github.com/eagle030/web.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    # Сборка Docker образа
                    docker build -t myapp .
                '''
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh '''
                    # Сохраняем Docker образ в tar-файл
                    docker save myapp -o myapp.tar

                    # Запускаем Ansible playbook для деплоя
                    ansible-playbook -i inventory.ini playbook.yml --extra-vars "docker_image_tar=myapp.tar"
                '''
            }
        }
    }
}
