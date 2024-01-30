import json
import numpy as np

def hello(event, context):
    print(np.array([1,2,3,4,5]))
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}

