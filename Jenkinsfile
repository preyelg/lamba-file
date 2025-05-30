pipeline {
    agent any

    environment {
        FUNCTION_NAME = 'file_processor'                         // ✅ fixed name
        ZIP_FILE       = 'lambda_function.zip'
        HANDLER_PATH   = 'lambda_function\\lambda_function.py'
        AWS_REGION     = 'us-east-2'
    }

    stages {
        stage('Prepare Workspace') {
            steps {
                echo "🧹 Cleaning previous zip"
                bat 'if exist lambda_function.zip del /F /Q lambda_function.zip'
            }
        }

        stage('Zip Lambda Function') {
            steps {
                echo "📦 Zipping lambda_function.py"
                bat "powershell -Command \"Compress-Archive -Path ${env.HANDLER_PATH} -DestinationPath ${env.ZIP_FILE} -Force\""
            }
        }

        stage('Deploy to AWS Lambda') {
            steps {
                echo "🚀 Deploying to Lambda"
                bat """
                    aws lambda update-function-code ^
                    --function-name ${env.FUNCTION_NAME} ^
                    --zip-file fileb://${env.ZIP_FILE} ^
                    --region ${env.AWS_REGION}
                """
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
