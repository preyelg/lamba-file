import json

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    # Check for API Gateway HTTP POST event
    if "body" in event:
        try:
            data = json.loads(event["body"])
            print("Parsed body:", data)
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "API POST successful", "data": data})
            }
        except Exception as e:
            print("Error parsing body:", str(e))
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Invalid JSON"})
            }

    # If it's an S3 event
    elif "Records" in event and event["Records"][0]["eventSource"] == "aws:s3":
        print("S3 Event:", json.dumps(event))
        return {
            "statusCode": 200,
            "body": "S3 event handled"
        }

    # Unknown event
    return {
        "statusCode": 400,
        "body": "Unsupported event type"
    }
