properties([githubProjectProperty(displayName: '', projectUrlStr: 'https://github.com/pzukovski/WorldOfGamesProject.git/')])

pipeline {
    agent any

    stages {
        
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/pzukovski/WorldOfGamesProject.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        
        stage('Run') {
            steps {
                sh '/usr/local/bin/docker-compose up -d'
            }
        }

        stage('Test') {
            steps {
                catchError(message: 'Failed e2e Test') {
                    script {
                        try{
                            sh '''pip install -r ./requirements.txt
                            cd utils/
                            python3 e2e.py'''
                        }                
                        catch (e) {
                            echo "Failed e2e Test"
                        }
                    }                
                }
            }
        }

        stage('Finalize') {
            steps {
                sh '''docker-compose down
                docker login -u polik1999 -p 123456789
                docker tag world_of_games_web polik1999/devops:latest
                docker image push polik1999/devops:latest
                docker logout'''
            }
        }
    }
}
