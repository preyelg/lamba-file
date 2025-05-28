import json

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    # Handle HTTP API Gateway event
    if "body" in event:
        try:
            data = json.loads(event["body"])
            print("Parsed API body:", data)
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "message": "API POST successful",
                    "received": data
                })
            }
        except Exception as e:
            print("API body parsing failed:", str(e))
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Invalid JSON",
                    "details": str(e)
                })
            }

    # Handle S3 event
    elif "Records" in event and event["Records"][0].get("eventSource") == "aws:s3":
        print("S3 Event:", json.dumps(event))
        return {
            "statusCode": 200,
            "body": "S3 event processed"
        }

    return {
        "statusCode": 400,
        "body": "Unsupported event structure"
    }
