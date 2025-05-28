
import json
import boto3

s3 = boto3.client('s3')
sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')

# Replace with your actual SNS topic ARN and DynamoDB table name
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-2:123456789012:MyTopic'
DYNAMO_TABLE_NAME = 'ProcessedFiles'

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    # Extract bucket and object key
    bucket = event['Records'][0]['s3']['bucket']['name']
    key    = event['Records'][0]['s3']['object']['key']

    # Read file content from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    print("File content:", content)

    # Send notification via SNS
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject='S3 Upload Processed',
        Message=f"File '{key}' was uploaded to bucket '{bucket}'.\n\nContent:\n{content}"
    )

    # Write summary to DynamoDB
    table = dynamodb.Table(DYNAMO_TABLE_NAME)
    table.put_item(Item={
        'filename': key,
        'bucket': bucket,
        'content': content,
        'status': 'processed'
    })

    return {"statusCode": 200, "body": "File processed, notified, and logged."}
