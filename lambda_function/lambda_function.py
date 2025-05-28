import json

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    # Check if it's from API Gateway HTTP
    if "body" in event:
        try:
            data = json.loads(event["body"])
            print("Parsed body:", data)
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "message": "API POST successful",
                    "received": data
                })
            }
        except Exception as e:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Invalid JSON",
                    "details": str(e)
                })
            }

    # Handle S3 event (already working)
    elif "Records" in event and event["Records"][0].get("eventSource") == "aws:s3":
        print("S3 Event Triggered:", json.dumps(event))
        return {
            "statusCode": 200,
            "body": "S3 event processed."
        }

    # Unknown trigger
    return {
        "statusCode": 400,
        "body": "Unsupported event structure"
    }
