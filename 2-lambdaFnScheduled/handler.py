import json
import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig()

def run(e, c):
    name = c.function_name
    body = f"Function {name} ran at {datetime.datetime.now().time()}"
    logger.info(body)
    return {"statusCode": 200, "body": json.dumps(body)}