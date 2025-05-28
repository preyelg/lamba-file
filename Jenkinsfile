pipeline {
    agent any

    environment {
        FUNCTION_NAME = 's3-file-processor'
        ZIP_FILE = 'lambda_function.zip'
        HANDLER_PATH = 'lambda_function\\lambda_function.py'
        AWS_REGION = 'us-east-2'
    }

    stages {
        stage('Prepare Workspace') {
            steps {
                echo "Cleaning previous zip"
                bat 'if exist lambda_function.zip del /f /q lambda_function.zip'
            }
        }

        stage('Zip Lambda Function') {
            steps {
                echo "Zipping lambda_function.py"
                bat 'powershell -Command "Compress-Archive -Path lambda_function\\lambda_function.py -DestinationPath lambda_function.zip -Force"'
            }
        }

        stage('Deploy to AWS Lambda') {
            steps {
                echo "Deploying to Lambda"
                bat '''
                aws lambda update-function-code ^
                    --function-name s3-file-processor ^
                    --zip-file fileb://lambda_function.zip ^
                    --region us-east-2
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Lambda function deployed!"
        }
        failure {
            echo "❌ Deployment failed!"
        }
    }
}
