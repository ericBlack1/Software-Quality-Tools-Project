
pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.13.0'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: '*/main']], 
                    extensions: [[$class: 'CleanCheckout']], 
                    userRemoteConfigs: [[credentialsId: '80e791a9-4e0c-4910-ba40-01c280f2be70', url: 'https://github.com/GinaBlack/Software-Quality-Tools-Project.git']]
                ])
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    sh """
                        python${PYTHON_VERSION} -m pip install --user \
                            bcrypt==4.2.1 \
                            blinker==1.9.0 \
                            click==8.1.7 \
                            coverage==7.6.8 \
                            dnspython==2.7.0 \
                            flake8==7.1.1 \
                            Flask==3.1.0 \
                            Flask-Bcrypt==1.0.1 \
                            Flask-Login==0.6.3 \
                            Flask-PyMongo==2.3.0 \
                            Flask-SQLAlchemy==3.1.1 \
                            greenlet==3.1.1 \
                            iniconfig==2.0.0 \
                            itsdangerous==2.2.0 \
                            Jinja2==3.1.4 \
                            MarkupSafe==3.0.2 \
                            mccabe==0.7.0 \
                            packaging==24.2 \
                            pluggy==1.5.0 \
                            pycodestyle==2.12.1 \
                            pyflakes==3.2.0 \
                            pymongo==4.10.1 \
                            pytest==8.3.4 \
                            pytest-cov==6.0.0 \
                            python-dotenv==1.0.1 \
                            SQLAlchemy==2.0.36 \
                            typing_extensions==4.12.2 \
                            Werkzeug==3.1.3
                    """
                }
            }
        }
        
        stage('Code Quality Check') {
            steps {
                script {
                    sh """
                        python${PYTHON_VERSION} -m flake8 . --max-line-length=120
                    """
                }
            }
        }
        
        stage('Run Integration Tests') {
            steps {
                script {
                    sh """
                        # Create directories for test results
                        mkdir -p test-results coverage-reports
                        
                        # Run tests with coverage
                        python${PYTHON_VERSION} -m pytest tests/ \
                            --verbose \
                            --junitxml=test-results/junit.xml \
                            --cov=. \
                            --cov-report=xml:coverage-reports/coverage.xml \
                            --cov-report=html:coverage-reports/html
                    """
                }
            }
        }
        
        stage('Generate Requirements') {
            steps {
                script {
                    sh """
                        python${PYTHON_VERSION} -m pip freeze > requirements.txt
                    """
                }
            }
        }
    }
    
    post {
        always {
            junit 'test-results/junit.xml'
            recordIssues enabledForFailure: true, tool: flake8()
            publishCoverage adapters: [coberturaAdapter('coverage-reports/coverage.xml')]
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'coverage-reports/html',
                reportFiles: 'index.html',
                reportName: 'Coverage Report',
                reportTitles: ''
            ])
        }
        success {
            echo 'Integration tests completed successfully!'
            archiveArtifacts artifacts: 'requirements.txt', fingerprint: true
        }
        failure {
            echo 'Integration tests failed!'
        }
        cleanup {
            cleanWs()
        }
    }
}
