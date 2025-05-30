import json
import boto3

s3 = boto3.client('s3')
BUCKET = "preye-lambda-upload-daa1df51"

def lambda_handler(event, context):
    print("API Event received:", json.dumps(event))

    try:
        files = s3.list_objects_v2(Bucket=BUCKET)
        items = [obj['Key'] for obj in files.get('Contents', [])]

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "List of files",
                "files": items
            })
        }

    except Exception as e:
        print("Error listing files:", str(e))
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps({ "error": str(e) })
        }
