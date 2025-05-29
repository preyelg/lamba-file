import json
import boto3

s3 = boto3.client('s3')
BUCKET = "preye-lambda-upload-66ff1e89"

def lambda_handler(event, context):
    print("API Event received:", json.dumps(event))

    try:
        files = s3.list_objects_v2(Bucket=BUCKET)
        items = [obj['Key'] for obj in files.get('Contents', [])]

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "List of files",
                "files": items
            }),
            "headers": {
                "Content-Type": "application/json"
            }
        }
    except Exception as e:
        print("Error listing files:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({ "error": str(e) })
        }
