import json
import base64

def hello(event, context):
    
    i = 0
    for record in event["Records"]:
        data = base64.b64decode(record["kinesis"]["data"])
        deserialized_data = json.loads(data)
        print(f"Received data is {deserialized_data}")
        i += 1
    
    body = {
        "message": f"Processed {i} messages",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
