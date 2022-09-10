pipeline {
    environment { 
        registry = "25112021/jenkinsdocker0910"
        registryCredential = '25112021' 
        dockerImage = ''
    }
   agent any
   stages {
        // stage('Checkout to project2 branch') {
        //     steps {
        //         checkout([$class: 'GitSCM', branches: [[name: '*/project2']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'unknown12734', url: 'https://github.com/unknown12734/database.git']]])
        //         sh "ls -lart ./*"
        //     }
        // }
        stage('restarting docker') {
            steps {
                sh "sudo service docker restart"
            }
        }
        stage('fetch code complete') {
            steps {
                echo 'fecthing the code from git is complete.'
            }
        }
        stage('Building image') { 
            steps { 
                script { 
                dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            } 
        }
        stage('pushing image to dockerhub') { 
            steps { 
                script { 
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() 
                    }
                } 
            }

        }
        stage('running the docker container') { 
            steps { 
                script { 
                    echo registry
                    echo "$registry"
                    sh "docker container run -p 5000:5000 -d $registry" + ":$BUILD_NUMBER"
                } 
            }   

        }
        
    }
}
