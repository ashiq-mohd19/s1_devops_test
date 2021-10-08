pipeline {
    environment{
        // env variables of docker image name and gke cluster properties
        dockerImage = ''
        PROJECT_ID = 'notional-plasma-327916'
        CLUSTER_NAME = 'bits-devops-assignment'
        LOCATION = 'us-west4-b'
        CREDENTIALS_ID = 'My First Project'
    }
    agent {
        label 'docker-instance'
    }
    stages {
        stage('CodeCheckout') {
            steps {
                // Get some code from a GitHub repository
                cleanWs()
                checkout changelog: false, poll: false, scm: [$class: 'GitSCM', branches: [[name: '*/betadeploy']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ashiq-mohd19/s1_devops_test.git']]]

            }
        }
        stage('Build') {
            steps {
                //Compiling the python code
                sh 'cd $WORKSPACE'
                sh 'python3 -m compileall application.py test_hello.py'
            }
        } 
        
        stage('Test') {
            steps {
                //Running unit tests
                sh 'cd $WORKSPACE'
                sh 'python3 -m pytest'
                sh 'rm -rf __pycache__ .pytest_cache'
                
            }
        }
        
        stage('Build-Docker-Image') {
            steps{
                script{
                        // Building and pushing the docker image to repo
                        withCredentials([usernamePassword( credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) 
                        {
                                sh 'sudo docker login --username $USERNAME --password $PASSWORD'
                                dockerImage = 'sudo docker.build("srinijakammari/devops")'
                                sudo docker.withRegistry('', 'dockerhub') {
                                    sh 'sudo docker login -u $USERNAME -p $PASSWORD'
                                    sudo dockerImage.push("$BUILD_NUMBER")
                                    sudo dockerImage.push("latest")
                                }
                        }
                    }
            }
        }
        
        stage('Deploy_NonProd'){
            steps{
                    //Running container in local env
                    sh 'docker run --name helloapp$BUILD_NUMBER -d srinijakammari/devops:latest'
            }
           
        }
        
        stage('App_health_check'){
            steps{
                    //Validating the deployment of container
                    //bat 'dos2unix app_function_test.sh'
                    sh 'docker cp app_function_test.sh  helloapp$BUILD_NUMBER:./app_function_test.sh'
                    sh 'docker exec helloapp$BUILD_NUMBER /bin/bash -c "bash /app_function_test.sh"'
            }
        }
        
        stage('Deploy_Production'){
            steps{
                //Deploying the container in GKE cluster
                step([
                $class: 'KubernetesEngineBuilder',
                projectId: env.PROJECT_ID,
                clusterName: env.CLUSTER_NAME,
                location: env.LOCATION,
                manifestPattern: 'manifest.yaml',
                credentialsId: env.CREDENTIALS_ID,
                verifyDeployments: true])
            }
        }
    }
}

