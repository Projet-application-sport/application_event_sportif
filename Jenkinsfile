pipeline {
agent any
stages {
 stage('build'){
  steps{
  sh '/home/sana/maven3/bin/mvn clean install'
  }
 }
 stage('test'){
  steps{
  sh '/home/sana/maven3/bin/mvn test'
  }
 }
}
}
