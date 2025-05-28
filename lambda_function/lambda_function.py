import json

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    # Check if from API Gateway (HTTP POST)
    if "body" in event:
        try:
            body_data = json.loads(event["body"])
            print("Parsed API Gateway Body:", body_data)
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "message": "API POST successful",
                    "received": body_data
                })
            }
        except Exception as e:
            return {
                "statusCode": 400,
                "body": json.dumps({ "error": "Invalid JSON", "details": str(e) })
            }

    # Check if from S3
    elif "Records" in event and event["Records"][0].get("eventSource") == "aws:s3":
        print("S3 Event Triggered:", json.dumps(event))
        return {
            "statusCode": 200,
            "body": "S3 event processed."
        }

    return {
        "statusCode": 400,
        "body": "Unsupported event format."
    }
