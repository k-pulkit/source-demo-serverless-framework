import json
import os
import boto3
import datetime

def sqsInvoker(event, context):
    SQS_URL = os.environ.get("QUEUE_URL")
    client = boto3.client("sqs")
    
    assert SQS_URL is not None
    assert len(SQS_URL) > 0
    
    name = context.function_name
    body = f"Function {name} ran at {datetime.datetime.now().time()}"
    client.send_message(QueueUrl=SQS_URL, MessageBody=body)


def queueHandler(event, context):
    
    messages = []
    for record in event["Records"]:
        messages.append(record["body"])
        
    print(f"Messages received are - {messages}")
    
    body = {
        "message": messages,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
