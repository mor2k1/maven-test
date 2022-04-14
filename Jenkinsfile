pipeline {
  agent any
  stages {
    stage('BlueOcean Python File Test') {
      steps {
        git(url: 'https://github.com/mor2k1/maven-test.git', branch: 'main')
        emailext(subject: 'Done', body: 'test', attachLog: true, from: 'Jenkins', to: 'yuvi.mor@gmail.com')
      }
    }

  }
}