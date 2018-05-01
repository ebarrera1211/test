pipeline {
  agent {
    node {
      label 'master'
    }

  }
  stages {
    stage('test') {
      steps {
        bat(script: 'whoami', returnStatus: true)
      }
    }
  }
}