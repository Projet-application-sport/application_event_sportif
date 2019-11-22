pipeline{
agent any
stages{
 stage('build'){
  step{
   sh '/home/sana/maven3/bin/mvn clean install'
  }
 }
 stage('test'){
  step{
   sh '/home/sana/maven3/bin/mvn test'
  }
 }
}
}
