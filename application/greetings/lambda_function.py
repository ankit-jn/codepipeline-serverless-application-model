from get_time.time import get_time

def lambda_handler(event, context):
    now = get_time
    current_time = now.strftime("%H:%M:%S")
    return {
        "statusCode": 200,
        "body": {
            "message": "Hello Visitor!!!",
            "time": "You visited us at {0}".format(current_time)
        }
    }