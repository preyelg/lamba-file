pipeline {
    agent any

    environment {
        FUNCTION_NAME = 's3-file-processor'
        ZIP_FILE = 'lambda_function.zip'
        HANDLER_FILE = 'lambda_function.py'
        AWS_REGION = 'us-east-1'
    }

    stages {
        stage('Prepare Workspace') {
            steps {
                echo "Cleaning and preparing workspace"
                sh 'rm -f ${ZIP_FILE}'
            }
        }

        stage('Zip Lambda Function') {
            steps {
                echo "Zipping ${HANDLER_FILE} to ${ZIP_FILE}"
                sh 'zip -j ${ZIP_FILE} ${HANDLER_FILE}'
            }
        }

        stage('Deploy to AWS Lambda') {
            steps {
                echo "Updating AWS Lambda..."
                sh '''
                aws lambda update-function-code \
                    --function-name ${FUNCTION_NAME} \
                    --zip-file fileb://${ZIP_FILE} \
                    --region ${AWS_REGION}
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
