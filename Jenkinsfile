pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Caso Practico Paso 1...'
            }
        }
       stage('Test') {
        steps {
         bat '"C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe" install pytest'
         bat '"C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest --junitxml=report.xml'
         junit 'report.xml'
    }
}
        stage('Deploy') {
            steps {
                echo 'Desplegando aplicación...'
            }
        }
    }
}
