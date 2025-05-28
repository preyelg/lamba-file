
resource "aws_sns_topic" "lambda_notifications" {
  name = "MyTopic"
}

resource "aws_dynamodb_table" "processed_files" {
  name         = "ProcessedFiles"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "filename"

  attribute {
    name = "filename"
    type = "S"
  }

  tags = {
    Environment = "dev"
    Project     = "LambdaFileProcessor"
  }
}
