pipeline {
    agent any

    environment {
        FUNCTION_NAME = 's3-file-processor'
        ZIP_FILE = 'lambda_function.zip'
        HANDLER_FILE = 'lambda_function.py'
        AWS_REGION = 'us-east-2'
    }

    stages {
        stage('Prepare Workspace') {
            steps {
                echo "Cleaning and preparing workspace"
                bat 'del /f /q lambda_function.zip'
            }
        }

        stage('Zip Lambda Function') {
            steps {
                echo "Zipping lambda_function.py"
                bat 'powershell -Command "Compress-Archive -Path lambda_function.py -DestinationPath lambda_function.zip -Force"'
            }
        }

        stage('Deploy to AWS Lambda') {
            steps {
                echo "Deploying to Lambda"
                bat '''
                aws lambda update-function-code ^
                    --function-name %FUNCTION_NAME% ^
                    --zip-file fileb://lambda_function.zip ^
                    --region %AWS_REGION%
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Lambda function deployed successfully!"
        }
        failure {
            echo "❌ Lambda deployment failed!"
        }
    }
}
